from main import app,datastore
from datetime import datetime
from application.models import *
from flask_security import hash_password
from werkzeug.security import generate_password_hash



with app.app_context():
    db.drop_all()
    db.create_all()
    datastore.find_or_create_role(name="admin", description="User is an Admin")
    datastore.find_or_create_role(
        name="sm", description="User is a Store Manager")
    datastore.find_or_create_role(name="user", description="User is a Customer")
    db.session.commit()
    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(
            email="admin@email.com",username="admin" ,password=generate_password_hash("admin"), roles=["admin"])
    if not datastore.find_user(email="sm1@email.com"):
        datastore.create_user(
            email="sm1@email.com" ,username="store manager 1", password=generate_password_hash("sm"), roles=["sm"])
    if not datastore.find_user(email="user1@email.com"):
        datastore.create_user(
            email="user1@email.com" ,username="Customer 1", password=generate_password_hash("user"), roles=["user"])
    if not datastore.find_user(email="user2@email.com"):
        datastore.create_user(
            email="user2@email.com" ,username="Customer 2", password=generate_password_hash("user"), roles=["user"])



    db.session.commit()