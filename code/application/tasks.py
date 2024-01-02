from .models import *
from celery import shared_task
import flask_excel as excel
from .mail_service import send_message,send_monthly_report
from datetime import datetime
from jinja2 import Template
from .sec import datastore


###############USER#################################################
def FetchProducts():
    return AllProducts.query.all()

def FetchHistory(user_id):
    return AllOrders.query.filter_by(user_id=user_id).all()



def BuyProduct(user_id,json_data):

    for item in json_data:
        p_id = item["p_id"]
        quantity = item["quantity"]
        p = AllProducts.query.filter_by(id=p_id).first()
        if (not p): 
            return 0
        print(p)
        print(quantity)
        print(p.rem_units)
        if(quantity > p.rem_units):
            return 2
    
    for item in json_data:
        # user_id = item["user_id"]
        p_id = int(item["p_id"])
        quantity = item["quantity"]
        order_date = datetime.strptime(item["order_date"], "%Y-%m-%d").date()
        price = item["price"]

        p = AllProducts.query.filter_by(id=p_id).first()

        # Update remaining units and add an order
        p.rem_units -= quantity
        q = AllOrders(user_id=user_id, p_id=p_id, quantity=quantity, order_date=order_date, price=price)
        db.session.add(q)
        db.session.commit()
    return 1

    
# ################STORE##MANAGER############################################

def FetchCatProduct(store_name,category):
    return AllProducts.query.filter_by(store_name=store_name,category=category).all()



def AddNewProduct(json_data,store_name):
    for item in json_data:
        p_name = item["p_name"]
        category = item["category"]
        rem_units = int(item["rem_units"])
        added_date = datetime.strptime(item['added_date'], "%Y-%m-%d").date()
        expiry_date = datetime.strptime(item['expiry_date'], "%Y-%m-%d").date()
        rate = int(item["rate"])
        unit_SI = item["unit_SI"]
        img=item["img"]

        if p_name=="" or category=="" or rem_units=="" or added_date=="" or expiry_date=="" or rate=="" or unit_SI=="":
                return 2

        ap=AllProducts(
            p_name=p_name,
            category=category,
            rem_units=rem_units,
            added_date=added_date,
            expiry_date=expiry_date,
            rate=rate,
            unit_SI=unit_SI,
            store_name=store_name,
            img=img
        )
        db.session.add(ap)
        db.session.commit()
        return 1



def EditProduct(json_data):
    for item in json_data:
        p_id = int(item["p_id"])
        pe = AllProducts.query.filter_by(id=p_id).first()
        if pe:
            p_name = item["p_name"]
            category = item["category"]
            rem_units = item["rem_units"]
            added_date = datetime.strptime(item['added_date'], "%Y-%m-%d").date()
            expiry_date = datetime.strptime(item['expiry_date'], "%Y-%m-%d").date()
            rate = item["rate"]
            unit_SI = item["unit_SI"]
            img=item["img"]

            if p_name=="" or category=="" or rem_units=="" or added_date=="" or expiry_date=="" or rate=="" or unit_SI=="":
                return 2

            pe.p_name=p_name
            pe.category=category
            pe.rem_units=rem_units
            pe.added_date=added_date
            pe.expiry_date=expiry_date
            pe.rate=rate
            pe.unit_SI=unit_SI
            pe.img=img

            db.session.commit()
            return 1
        else:
            return 0





def DeleteProduct(p_id):
    product_to_be_deleted = AllProducts.query.filter_by(id=p_id).first()
    if product_to_be_deleted:
        db.session.delete(product_to_be_deleted)
        db.session.commit()
        return 1
    else:
        return 0


def CheckInbox(store_name):
    return ReplyQueue.query.filter_by(sname=store_name).all()
    
#1 for new category
#2 for editing category
#3 for deleting category
def RequestManager(sname,operation,name,name2):
    #check if storename is valid in user table
    if 1 > operation or operation > 3:
        return 1
    sc = RequestQueue.query.filter_by(sname=sname,operation=operation,name=name,name2=name2).first()
    if sc:
        return 9
    else:
        if operation==1:
            if name=="":
                return 100
            sc = CategoryAllowed.query.filter_by(sname=sname,category=name).first()
            if sc:
                return 2
            else:
                r=RequestQueue(sname=sname,operation=operation,name=name)
                db.session.add(r)
                db.session.commit()
                return 3

        if operation==2:
            if name2=="":
                return 100
            if not name2:
                return 4
            sc = CategoryAllowed.query.filter_by(sname=sname,category=name).first()
            if not sc:
                return 5
            else:
                r=RequestQueue(sname=sname,operation=operation,name=name,name2=name2)
                db.session.add(r)
                db.session.commit()
                return 6
        
        if operation == 3:
            if name=="":
                return 100
            sc = CategoryAllowed.query.filter_by(sname=sname,category=name).first()
            if not sc:
                return 7
            else:
                r=RequestQueue(sname=sname,operation=operation,name=name)
                db.session.add(r)
                db.session.commit()
                return 8
    

# ##############ADMIN#########################################

def Decide(r_id,status,sname):
    r=RequestQueue.query.filter_by(id=r_id).first()
    if not r:
        return 0
    else:
        if status==0:
            pass 
        elif status==1:
            if r.operation==1:
                c=CategoryAllowed.query.filter_by(sname=r.sname,category=r.name).first()
                if c:
                    return 1
                nc=CategoryAllowed(sname=r.sname,category=r.name)
                db.session.add(nc)
                db.session.commit()
                
            elif r.operation==2:
                c=CategoryAllowed.query.filter_by(sname=r.sname,category=r.name).first()
                if not c:
                    return 2
                c.category=r.name2
                
                aps=AllProducts.query.filter_by(store_name=sname,category=r.name).all()
                for p in aps:
                    p.category=r.name2
                    

                db.session.commit()
                
            elif r.operation==3:
                c=CategoryAllowed.query.filter_by(sname=r.sname,category=r.name).first()
                if not c:
                    return 3
                db.session.delete(c)
                
                aps=AllProducts.query.filter_by(store_name=sname,category=r.name).all()
                for p in aps:
                    db.session.delete(p)
                db.session.commit()
                
                

    s=ReplyQueue(r_id=r.id,sname=r.sname,operation=r.operation,name=r.name,name2=r.name2,status=status)
    db.session.add(s)
    db.session.delete(r)
    db.session.commit()   
    return 4

            




def ApproveSM(rr_id,status):
    rr=RegistrationRequest.query.filter_by(id=rr_id).first()
    if not rr:
        return 0
    else:
        if status==0:
            rr.allowed=status
            db.session.commit()
            with open('registrationstatus.html', 'r') as f:
                template = Template(f.read())
                send_message(rr.email, "Request Rejected",
                         template.render(username=rr.username,status='rejected'))
            return 1

        elif status ==1:
            rr.allowed=status
            sm=datastore.find_user(email=rr.email)
            sm.active=True
            db.session.commit()
            with open('registrationstatus.html', 'r') as f:
                template = Template(f.read())
                send_message(rr.email, "Request Accepted",
                         template.render(username=rr.username,status='accepted'))
            return 2
        else:
            return 3


#@shared_task(ignore_result=False)
def create_monthlyreport_csv(user_id):
  
    user_past_orders = (
    db.session.query(
        AllProducts.p_name, AllProducts.expiry_date, AllProducts.unit_SI, AllProducts.store_name,
        AllOrders.order_date, AllOrders.quantity, AllOrders.price
    )
    .join(AllOrders, AllProducts.id == AllOrders.p_id)
    .filter(AllOrders.user_id == user_id) 
    .all()
    )
    if user_past_orders:
        csv_output = excel.make_response_from_query_sets(
            user_past_orders,["p_name","expiry_date","unit_SI","store_name",
                              "order_date","quantity","price"], "csv")
        filename = "yourhistory.csv"

        with open(filename, 'wb') as f:
            f.write(csv_output.data)

        return filename,1
    else:
        filename = "yourhistory.csv"

        with open(filename, 'wb') as f:
            f.write("You haven't placed any orders so far")

        return filename,0
    


#@shared_task(ignore_result=False)
def create_monthly_sales_report_csv(store_name):
  
    store_sales = (
    db.session.query(
        AllOrders.user_id,AllProducts.p_name,
        AllOrders.order_date, AllOrders.quantity, AllOrders.price
    )
    .join(AllOrders, AllProducts.id == AllOrders.p_id)
    .filter(AllProducts.store_name == store_name) 
    .all()
    )
    if store_sales:
        csv_output = excel.make_response_from_query_sets(
            store_sales,["user_id","p_name",
                              "order_date","quantity","price"], "csv")
        filename = "monthlyreport.csv"

        with open(filename, 'wb') as f:
            f.write(csv_output.data)

        return filename,1
    else:
        filename = "monthlyreport.csv"
        with open(filename, 'wb') as f:
            f.write(b"no sales data for the month")

        return filename,0



@shared_task(ignore_result=True)
def daily_reminder(to, subject):
    users = User.query.filter(User.roles.any(Role.name == 'user')).all()
    for user in users:
        with open('dailyreminder.html', 'r') as f:
            template = Template(f.read())
            send_message(user.email, subject,
                         template.render(username=user.username))
    return "OK"


@shared_task(ignore_result=True)
def monthly_report_mail(to, subject):
    users = User.query.filter(User.roles.any(Role.name == 'sm')).all()
    for user in users:
        filename,status=create_monthly_sales_report_csv(user.sname)
       
        with open('monthlyreport.html', 'r') as f:
            template = Template(f.read())
            send_monthly_report(user.email, subject,
                            template.render(storename=user.sname),filename)
              
    return "OK"