from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin,RoleMixin


db = SQLAlchemy()

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    sname = db.Column(db.String)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    
    roles = db.relationship('Role',secondary='roles_users',
                           backref=db.backref('users',lazy='dynamic'))
    customer = db.relationship('AllOrders', backref='buyer')
   
    
class Role(db.Model,RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class AllProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    rem_units = db.Column(db.Integer, nullable=False)
    added_date = db.Column(db.Date , nullable=False)
    expiry_date = db.Column(db.Date , nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    unit_SI = db.Column(db.String, nullable=False)
    store_name = db.Column(db.String, nullable=False)
    img = db.Column(db.String)
    product_det = db.relationship('AllOrders', backref='details')


class AllOrders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    p_id = db.Column(db.Integer, db.ForeignKey('all_products.id'), nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
#   A relationship to Allproducts needs to be built

class RequestQueue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String, nullable=False)
    operation = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    name2 = db.Column(db.String)

class ReplyQueue(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    r_id = db.Column(db.Integer,nullable=False)
    sname = db.Column(db.String, nullable=False)
    operation = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    name2 = db.Column(db.String)
    status = db.Column(db.Integer, nullable=False)
    

class RegistrationRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    sname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    allowed = db.Column(db.Integer)

class CategoryAllowed(db.Model):
    sname = db.Column(db.String, primary_key=True)
    category = db.Column(db.String, primary_key=True) 
    
