from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security
from application.models import db, User, Role
from config import DevelopmentConfig
from application.resources import api
from application.sec import datastore
from application.worker import celery_init_app
import flask_excel as excel
from celery.schedules import crontab
from application.tasks import daily_reminder,monthly_report_mail
from application.instances import cache


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    api.init_app(app)
    excel.init_excel(app)
    app.security = Security(app, datastore)
    cache.init_app(app)
    with app.app_context():
        import application.views

    return app


app = create_app()
celery_app = celery_init_app(app)


@celery_app.on_after_configure.connect
def send_email(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=15, minute=29),
        daily_reminder.s('ceo@growcery.com', 'Daily Reminder'),
    )
    sender.add_periodic_task(
        crontab(hour=15, minute=29,day_of_month=31),
        monthly_report_mail.s('ceo@growcery.com', 'Monthly Sales Report'),
    )

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask
# from application.models import db,User,Role
# from config import DevelopmentConfig
# from application.resources import api
# from flask_security import SQLAlchemyUserDatastore,Security


# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(DevelopmentConfig)
#     db.init_app(app)
#     api.init_app(app)
#     datastore=SQLAlchemyUserDatastore(db,User,Role)
#     app.security=Security(app,datastore)
#     with app.app_context():
#         import application.views

#     return app,datastore

# app,datastore  = create_app()  

# if __name__ == '__main__':
#     app.run(debug=True)