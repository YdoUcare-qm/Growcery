from main import app,datastore
from datetime import datetime
from application.models import *
from werkzeug.security import generate_password_hash

with app.app_context():
    

    
    products=[
    {
      "id": 1,
      "p_name": "Apples",
      "category": "Fruits",
      "rem_units": 20,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-01",
      "rate": 2.50,
      "unit_SI": "kg",
      "store_name": "Fresh Mart"
    },
    {
      "id": 2,
      "p_name": "Milk",
      "category": "Dairy",
      "rem_units": 15,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-30",
      "rate": 1.75,
      "unit_SI": "liter",
      "store_name": "Dairy Delight"
    },
    {
      "id": 3,
      "p_name": "Bread",
      "category": "Bakery",
      "rem_units": 25,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-28",
      "rate": 2.00,
      "unit_SI": "piece",
      "store_name": "Bakery Haven"
    },
    {
      "id": 4,
      "p_name": "Chicken Breast",
      "category": "Meat",
      "rem_units": 10,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-03",
      "rate": 5.50,
      "unit_SI": "kg",
      "store_name": "Meat Master"
    },
    {
      "id": 5,
      "p_name": "Rice",
      "category": "Grains",
      "rem_units": 30,
      "added_date": "2023-11-25",
      "expiry_date": "2024-01-15",
      "rate": 3.75,
      "unit_SI": "kg",
      "store_name": "Grains Galore"
    },
    {
      "id": 6,
      "p_name": "Bananas",
      "category": "Fruits",
      "rem_units": 22,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-05",
      "rate": 1.80,
      "unit_SI": "kg",
      "store_name": "Fresh Mart"
    },
    {
      "id": 7,
      "p_name": "Yogurt",
      "category": "Dairy",
      "rem_units": 18,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-27",
      "rate": 2.25,
      "unit_SI": "kg",
      "store_name": "Dairy Delight"
    },
    {
      "id": 8,
      "p_name": "Baguette",
      "category": "Bakery",
      "rem_units": 20,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-30",
      "rate": 1.50,
      "unit_SI": "piece",
      "store_name": "Bakery Haven"
    },
    {
      "id": 9,
      "p_name": "Pork Chops",
      "category": "Meat",
      "rem_units": 12,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-07",
      "rate": 6.75,
      "unit_SI": "kg",
      "store_name": "Meat Master"
    },
    {
      "id": 10,
      "p_name": "Pasta",
      "category": "Grains",
      "rem_units": 28,
      "added_date": "2023-11-25",
      "expiry_date": "2024-01-10",
      "rate": 2.25,
      "unit_SI": "kg",
      "store_name": "Grains Galore"
    },
    {
      "id": 11,
      "p_name": "Oranges",
      "category": "Fruits",
      "rem_units": 25,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-03",
      "rate": 3.00,
      "unit_SI": "kg",
      "store_name": "Fresh Mart"
    },
    {
      "id": 12,
      "p_name": "Cheese",
      "category": "Dairy",
      "rem_units": 15,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-29",
      "rate": 3.50,
      "unit_SI": "kg",
      "store_name": "Dairy Delight"
    },
    {
      "id": 13,
      "p_name": "Croissants",
      "category": "Bakery",
      "rem_units": 18,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-28",
      "rate": 2.20,
      "unit_SI": "piece",
      "store_name": "Bakery Haven"
    },
    {
      "id": 14,
      "p_name": "Ground Beef",
      "category": "Meat",
      "rem_units": 10,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-05",
      "rate": 7.50,
      "unit_SI": "kg",
      "store_name": "Meat Master"
    },
    {
      "id": 15,
      "p_name": "Quinoa",
      "category": "Grains",
      "rem_units": 25,
      "added_date": "2023-11-25",
      "expiry_date": "2024-01-12",
      "rate": 4.00,
      "unit_SI": "kg",
      "store_name": "Grains Galore"
    },
    {
      "id": 16,
      "p_name": "Grapes",
      "category": "Fruits",
      "rem_units": 20,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-02",
      "rate": 2.75,
      "unit_SI": "kg",
      "store_name": "Fresh Mart"
    },
    {
      "id": 17,
      "p_name": "Butter",
      "category": "Dairy",
      "rem_units": 17,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-28",
      "rate": 2.00,
      "unit_SI": "kg",
      "store_name": "Dairy Delight"
    },
    {
      "id": 18,
      "p_name": "Cinnamon Roll",
      "category": "Bakery",
      "rem_units": 22,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-30",
      "rate": 2.50,
      "unit_SI": "piece",
      "store_name": "Bakery Haven"
    },
    {
      "id": 19,
      "p_name": "Salmon Fillet",
      "category": "Meat",
      "rem_units": 8,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-10",
      "rate": 9.00,
      "unit_SI": "kg",
      "store_name": "Meat Master"
    },
    {
      "id": 20,
      "p_name": "Couscous",
      "category": "Grains",
      "rem_units": 30,
      "added_date": "2023-11-25",
      "expiry_date": "2024-01-18",
      "rate": 3.25,
      "unit_SI": "kg",
      "store_name": "Grains Galore"
    },
    {
      "id": 21,
      "p_name": "Pineapple",
      "category": "Fruits",
      "rem_units": 23,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-04",
      "rate": 2.80,
      "unit_SI": "piece",
      "store_name": "Fresh Mart"
    },
    {
      "id": 22,
      "p_name": "Sour Cream",
      "category": "Dairy",
      "rem_units": 15,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-29",
      "rate": 2.30,
      "unit_SI": "kg",
      "store_name": "Dairy Delight"
    },
    {
      "id": 23,
      "p_name": "Ciabatta",
      "category": "Bakery",
      "rem_units": 18,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-29",
      "rate": 1.80,
      "unit_SI": "piece",
      "store_name": "Bakery Haven"
    },
    {
      "id": 24,
      "p_name": "Lamb Chops",
      "category": "Meat",
      "rem_units": 10,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-08",
      "rate": 8.50,
      "unit_SI": "kg",
      "store_name": "Meat Master"
    },
    {
      "id": 25,
      "p_name": "Brown Rice",
      "category": "Grains",
      "rem_units": 28,
      "added_date": "2023-11-25",
      "expiry_date": "2024-01-14",
      "rate": 3.50,
      "unit_SI": "kg",
      "store_name": "Grains Galore"
    },
    {
      "id": 26,
      "p_name": "Strawberries",
      "category": "Fruits",
      "rem_units": 20,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-02",
      "rate": 3.20,
      "unit_SI": "kg",
      "store_name": "Fresh Mart"
    },
    {
      "id": 27,
      "p_name": "Eggs",
      "category": "Dairy",
      "rem_units": 25,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-30",
      "rate": 1.50,
      "unit_SI": "dozen",
      "store_name": "Dairy Delight"
    },
    {
      "id": 28,
      "p_name": "Bagels",
      "category": "Bakery",
      "rem_units": 22,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-28",
      "rate": 1.90,
      "unit_SI": "piece",
      "store_name": "Bakery Haven"
    },
    {
      "id": 29,
      "p_name": "Turkey Breast",
      "category": "Meat",
      "rem_units": 12,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-06",
      "rate": 6.00,
      "unit_SI": "kg",
      "store_name": "Meat Master"
    },
    {
      "id": 30,
      "p_name": "Barley",
      "category": "Grains",
      "rem_units": 30,
      "added_date": "2023-11-25",
      "expiry_date": "2024-01-16",
      "rate": 2.75,
      "unit_SI": "kg",
      "store_name": "Grains Galore"
    },
    {
      "id": 31,
      "p_name": "Watermelon",
      "category": "Fruits",
      "rem_units": 15,
      "added_date": "2023-11-25",
      "expiry_date": "2023-12-05",
      "rate": 4.00,
      "unit_SI": "piece",
      "store_name": "Fresh Mart"
    },
    {
      "id": 32,
      "p_name": "Cheddar Cheese",
      "category": "Dairy",
      "rem_units": 18,
      "added_date": "2023-11-25",
      "expiry_date": "2023-11-29",
      "rate": 3.75,
      "unit_SI": "kg",
      "store_name": "Dairy Delight"
    }
  ] 
    i=1
    for data in products:
        product = AllProducts(
            p_name=data["p_name"],
            category=data["category"],
            rem_units=data["rem_units"],
            added_date=datetime.strptime(data["added_date"], "%Y-%m-%d").date(),             #datetime.now(),
            expiry_date=datetime.strptime(data["expiry_date"], "%Y-%m-%d").date(),            #datetime.now() + timedelta(days=30),
            rate=data["rate"],
            unit_SI=data["unit_SI"],
            store_name=data["store_name"])
        db.session.add(product)
        db.session.commit()

        store_name=data["store_name"]
        if not datastore.find_user(sname=store_name):
          i=i+1
          datastore.create_user(
            email="sm"+str(i)+"@email.com" ,username="store manager"+str(i), password=generate_password_hash("sm"), roles=["sm"],sname=store_name)
          
        category=data["category"]
        if not CategoryAllowed.query.filter_by(sname=store_name,category=category).first():
           ca = CategoryAllowed(sname=store_name,category=category)
           db.session.add(ca)
           db.session.commit()
           
        
    db.session.commit()

    # nr = CategoryAllowed(sname="Jeevan Butchery",category="Meat")
    # db.session.add(nr)
    # db.session.commit()

    # nr = CategoryAllowed(sname="Grains Galore",category="Rotten Meat")
    # db.session.add(nr)
    # db.session.commit()

    # nr = CategoryAllowed(sname="Jeevan Butchery",category="Grains")
    # db.session.add(nr)
    # db.session.commit()

    # nr = CategoryAllowed(sname="Jeevan Butchery",category="Dairy")
    # db.session.add(nr)
    # db.session.commit()

    