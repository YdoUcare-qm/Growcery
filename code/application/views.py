from flask import current_app as app, jsonify, request, render_template, send_file
from flask_security import auth_required, roles_required,current_user
from werkzeug.security import check_password_hash,generate_password_hash
from flask_restful import marshal, fields
import flask_excel as excel
from celery.result import AsyncResult
from .tasks import create_monthlyreport_csv,create_monthly_sales_report_csv,daily_reminder
from .models import User, db, RegistrationRequest,CategoryAllowed
from .sec import datastore


@app.get('/')
def home():
    return render_template("index.html")

@auth_required('token')
@roles_required('admin')
@app.get('/admin')
def adminhome():
    return render_template("admin.html")

@auth_required('token')
@roles_required('sm')
@app.get('/storemanager')
def smhome():
    return render_template("storemanager.html")

@auth_required('token')
@roles_required('user')
@app.get('/user')
def userhome():
    return render_template("user.html")

@app.post('/user-login')
def user_login():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({"message": "email not provided"}), 400

    user = datastore.find_user(email=email)

    if not user:
        return jsonify({"message": "User Not Found"}), 404
    if user.active==False:
        return jsonify({"message": "Store Management not Approved Yet"}), 404

    if check_password_hash(user.password, data.get("password")):
        return jsonify({"token": user.get_auth_token(), "email": user.email, "role": user.roles[0].name})
    else:
        return jsonify({"message": "Wrong Password"}), 400



@app.post('/user-register')   
def user_register():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    if not email or not username or not password:
        return jsonify({"message": "Email, username, and password are required"}), 400

    existing_user = datastore.find_user(email=email) or datastore.find_user(username=username)
    if existing_user:
        return jsonify({"message": "User with this email or username already exists"}), 400

    hashed_password = generate_password_hash(password)

    datastore.create_user(
            email=email ,
            username=username,
            password=hashed_password, 
            roles=["user"])
    db.session.commit()

    user = datastore.find_user(email=email)
    return jsonify({"token": user.get_auth_token(), "email": user.email, "role": user.roles[0].name})
    


@app.post('/sm-register')   
def sm_register():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    storename = data.get('storename')

    if not email or not username or not password or not storename:
        return jsonify({"message": "Email, username, and password are required"}), 400

    existing_user = datastore.find_user(email=email)
    if existing_user:
        return jsonify({"message": "User with this email already exists"}), 400
    existing_user = datastore.find_user(username=username)
    if existing_user:
        return jsonify({"message": "User with this username already exists"}), 400
    existing_user = datastore.find_user(sname=storename)
    if existing_user:
        return jsonify({"message": "Store with this name already exists"}), 400

    hashed_password = generate_password_hash(password)

    datastore.create_user(
            email=email ,
            username=username,
            password=hashed_password,
            sname=storename, 
            active=False,
            roles=["sm"])
    rr=RegistrationRequest(username=username,
                           email=email,
                           sname=storename,
                           password=hashed_password
                           )
    db.session.add(rr)
    db.session.commit()

    return jsonify({"message": "Request for Store Management Placed"}), 201

category={
    'category':fields.String
}


@auth_required('token')
@roles_required('sm')
@app.get('/get-category')
def get_category():
    storename=current_user.sname
    c=CategoryAllowed.query.filter_by(sname=storename).all()
    if c:
        return marshal(c,category)
    else:
        return jsonify({"message": "No Categories Allotted So Far"}), 400



#############_____________________________________________#############


@app.get('/download-csv')
@auth_required('token')
@roles_required('user')
def download_csv():
    f,status = create_monthlyreport_csv(current_user.id)
    if status==1:
        return send_file(f, as_attachment=True)
    else:
        return jsonify({"message":"No orders so far"}),400
    # task = create_resource_csv.delay()
    # return jsonify({"task-id": task.id})


@app.get('/download-sales-csv')
@auth_required('token')
@roles_required('sm')
def download_sales_csv():
    f,status = create_monthly_sales_report_csv(current_user.sname)
    if status==1:
        return send_file(f, as_attachment=True)
    else:
        return jsonify({"message":"No orders so far"}),400




# @app.get('/get-csv/<task_id>')
# def get_csv(task_id):
#     res = AsyncResult(task_id)
#     if res.ready():
#         filename = res.result
#         return send_file(filename, as_attachment=True)
#     else:
#         return jsonify({"message": "Task Pending"}), 404
    