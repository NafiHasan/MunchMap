from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website import db, create_app
from website.models import Food, Restaurant, User

app = create_app()


def view_table(table_name):
    with app.app_context():
        print(User.query.all())


if __name__ == '__main__':
    view_table('hello')
