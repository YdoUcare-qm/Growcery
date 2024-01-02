from flask_restful import Resource, Api, reqparse, marshal_with, fields, request
from datetime import datetime
from flask_security import auth_required, roles_required, current_user
from application.models import *
from application.tasks import *
from application.instances import cache
from flask import jsonify



api = Api(prefix='/api')


product_fields = {
    'id':fields.String,
    'p_name':   fields.String,
    'category':  fields.String,
    'rem_units': fields.Integer,
    'added_date': fields.String,
    'expiry_date': fields.String,
    'rate': fields.Integer,
    'unit_SI': fields.String,
    'store_name': fields.String
}



class Products(Resource):

    
    @marshal_with(product_fields)
    def get(self):
        all_products = AllProducts.query.all()
        return (all_products)

    



api.add_resource(Products, '/user')

class Product(fields.Raw):
    def format(self, product):
        return {
            
            'p_name':  product.p_name,
            'category':  product.category,
            'added_date': str(product.added_date),
            'expiry_date': str(product.expiry_date),
            'unit_SI': product.unit_SI,
            'store_name': product.store_name,
        }

history_fields = {
    
    'order_date':  fields.String,
    'quantity': fields.Integer,
    'price': fields.Integer,
    'details': Product
}

parser2 = reqparse.RequestParser()
parser2.add_argument("data", type=list, location="json")
# parser3 = reqparse.RequestParser()
# parser3.add_argument("user_id", type=int)

class Orders(Resource):
    @marshal_with(history_fields)
    @auth_required("token")
    @roles_required("user")
    # @cache.cached(timeout=50)
    def get(self):
        all_history = FetchHistory(current_user.id)
        if all_history:
            return (all_history)
        else:
            return {"message":"No Orders So Far"},400
    
    @auth_required("token")
    @roles_required("user")
    def post(self):
        args = parser2.parse_args()
        json_data = args["data"]
        b=BuyProduct(current_user.id,json_data)
        if b == 1:
            return {"message": "Order Placed Successfully"}, 201
        if b==0:
            return {"message": "No Such product"}, 400
        if b==2:
            return {"message": "Exceeded inventory"}, 400
    
    #def patch(self):
        
api.add_resource(Orders, '/user/order')   


#---------------------------STORE MANAGER -----------------------------#

store_inventory= {
    'id': fields.String,
    'p_name':   fields.String,
    'category':  fields.String,
    'rem_units': fields.Integer,
    'added_date': fields.String,
    'expiry_date': fields.String,
    'rate': fields.Integer,
    'unit_SI': fields.String,
    'store_name': fields.String,
    'img': fields.String
}

# parser4 = reqparse.RequestParser()
# parser4.add_argument("category", type=str)

parser5 = reqparse.RequestParser()
parser5.add_argument("data", type=list, location="json")
# parser5.add_argument('p_name', type=str, help=' is required should be a string', required=True)
# parser5.add_argument('category', type=str, help=' is required and should be a string', required=True)
# parser5.add_argument('rem_units', type=str, help=' is required and should be a string', required=True)
# parser5.add_argument('added_date', type=str, help=' is required should be a string', required=True)
# parser5.add_argument('expiry_date', type=str, help=' is required and should be a string', required=True)
# parser5.add_argument('rate', type=int, help=' is required and should be a string', required=True)
# parser5.add_argument('unit_SI', type=str, help='is required should be a string', required=True)
# parser5.add_argument('store_name', type=str, help=' is required and should be a string', required=True)

parser6 = reqparse.RequestParser()
parser6.add_argument("data", type=list, location="json")

parser7 = reqparse.RequestParser()
parser7.add_argument("p_id", type=int)




class StoreOps(Resource):
    # Get Store Details

    @auth_required("token")
    @roles_required("sm")
    @marshal_with(store_inventory)
    def get(self):
        # args = parser4.parse_args()
        category = request.args.get('category')
        inventory = FetchCatProduct(current_user.sname,category)
        return inventory
        
    # Add New Product
    @auth_required("token")
    @roles_required("sm")
    def post(self):
        args = parser5.parse_args()
        json_data = args["data"]
        e = AddNewProduct(json_data,current_user.sname)
        if e==1:
            return {"message": "Product Added"},201
        else:
            return {"message": "Fill All Fields"},400
        

    # Edit Product
    @auth_required("token")
    @roles_required("sm")
    def patch(self):
        #json data with p_id 
        args = parser6.parse_args()
        json_data = args["data"]
        e = EditProduct(json_data)
        if e == 1:
            return {"message":"Product Edited"},201
        else:
            return {"message":"Fill All Fields"},400

    
    # Delete Product
    @auth_required("token")
    @roles_required("sm")
    def delete(self):
        args = parser7.parse_args()
        p_id = args["p_id"]
        d = DeleteProduct(p_id)
        if d == 1:
            return {"message":"Product Deleted"},201
        else:
            return {"message":"No Such Product"},400
        
api.add_resource(StoreOps, '/store') 

inbox_fields = {
    'sname':   fields.String,
    'operation':  fields.Integer,
    'name': fields.String,
    'name2': fields.String,
    'status': fields.Integer,
}


# parser8 = reqparse.RequestParser()
# parser8.add_argument("store_name", type=str)

parser9 = reqparse.RequestParser()

parser9.add_argument('operation', type=int, help='#1 for new cat,#2 for edit cat,#3 for delete cat', required=True)
parser9.add_argument('name', type=str, help='is required should be a string', required=True)
parser9.add_argument('name2', type=str, help=' is required only when editing')

class Requests(Resource):
    # Check Inbox
    @auth_required("token")
    @roles_required("sm")
    @marshal_with(inbox_fields)
    def get(self):
        # args = parser8.parse_args()
        store_name = current_user.sname
        #check if storename is valid in user table
        inbox = CheckInbox(store_name)
        return inbox
      
        
    # Request for Category related stuff but with flags 
    @auth_required("token")
    @roles_required("sm")
    def post(self):
        args = parser9.parse_args()
        sname = current_user.sname
        operation = args["operation"]
        name = args["name"]
        name2 = args["name2"]
        rm = RequestManager(sname,operation,name,name2)
        if rm==0:
            return {"message":"No such storename"},400
        elif rm==1:
            return {"message":"Invalid Operation"},400
        elif rm==2:
            return {"message":"Category is already allotted"},400
        elif rm==3:
            return {"message":"Request for new Category placed"},201
        elif rm==4:
            return {"message":"name2 not specified"},400
        elif rm==5:
            return {"message":"How can you edit a category which you don't own"},400
        elif rm==6:
            return {"message":"Request for editing category placed"},201
        elif rm==7:
            return {"message":"How can you delete a category which you don't own"},400
        elif rm==8:
            return {"message":"Request for category deletion placed"},201
        elif rm==100:
            return {"message":"Fill the blank fields first"},400
        else:
            return {"message":"Request already exists"},400
               
api.add_resource(Requests, '/store/request')


all_requests = {
    'id': fields.Integer,
    'sname':   fields.String,
    'operation':  fields.Integer,
    'name': fields.String,
    'name2': fields.String
}

reg_requests = {
    'id':fields.Integer,
    'username': fields.String,
    'email':  fields.String,
    'sname':   fields.String,
    
}

request_fields = {
    'category': fields.List(fields.Nested(all_requests)),
    'registration': fields.List(fields.Nested(reg_requests)),
}



parser10 = reqparse.RequestParser()
parser10.add_argument('id', type=int, help=' is required', required=True)
parser10.add_argument('status', type=int, help=' is required',required=True)

parser11 = reqparse.RequestParser()
parser11.add_argument('id', type=int, help=' is required', required=True)
parser11.add_argument('status', type=int, help=' is required',required=True)

class Decision(Resource):
    # Aprove or reject requests
    @auth_required("token")
    @roles_required("admin")
    @marshal_with(request_fields)
    def get(self):
        all_requests=RequestQueue.query.all()
        #add registration requests too
        all_reg_requests=RegistrationRequest.query.filter(RegistrationRequest.allowed.is_(None)).all()
        response_data = {
            'category': all_requests,
            'registration': all_reg_requests
        }

        return response_data
      
        
    # Request for Category related stuff but with flags 
    @auth_required("token")
    @roles_required("admin")
    def post(self):
        args = parser10.parse_args()
        r_id = int(args["id"])
        status=int(args["status"])
        print(r_id,status)

        d = Decide(r_id,status,current_user.sname)
        if d==0:
            return jsonify({"message":"No such Request Found"}),400
        elif d==1:
            return {"message":"Already has that category"},400
        elif d==2:
            return {"message":"No such Category for that store"},400
        elif d==3:
            return {"message":"Cant delete non-existent category"},201
        else:
            return {"message":"Request Handled"},201
        
    @auth_required("token")
    @roles_required("admin")
    def put(self):
        args=parser11.parse_args()
        rr_id = int(args["id"])
        status=int(args["status"])

        asm=ApproveSM(rr_id,status)
        if asm==0:
            return {"message":"No Such Request"},400
        elif asm==1:
            return {"message":" Registration Request declined"},201
        elif asm==2:
            return {"message":"Registration Request accepted"},201  
        else:
            return{"message":"Invalid Operation"}   

api.add_resource(Decision, '/admin')