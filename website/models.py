from datetime import datetime
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from flask import current_app
from website import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    restaurants = db.relationship('Restaurant', backref='owner', lazy=True)
    restaurant_reviews = db.relationship(
        'RestaurantReview', backref='reviewer', lazy=True)
    food_reviews = db.relationship('FoodReview', backref='reviewer', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False, default='No description')
    detail_location = db.Column(db.Text)
    rating = db.Column(db.Float, default=0.0)
    foods = db.relationship('Food', backref='belong_to', lazy=True)
    reviews = db.relationship(
        'RestaurantReview', backref='review_for', lazy=True)
    rating_count = db.Column(db.Float, nullable=False, default=0.0)
    total_rating = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"Restaurant('{self.name}', '{self.owner_id}', '{self.location}', '{self.image_file}')"


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(
        'restaurant.id'), nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    rating = db.Column(db.Float, default=0.0)
    description = db.Column(db.Text, nullable=False, default='No description')
    reviews = db.relationship('FoodReview', backref='review_for', lazy=True)
    rating_count = db.Column(db.Float, nullable=False, default=0.0)
    total_rating = db.Column(db.Float, nullable=False, default=0.0)
    price = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"Food('{self.name}', '{self.restaurant_id}')"


class RestaurantReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(
        'restaurant.id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)
    description = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    rating = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"RestaurantReview('{self.restaurant_id}', '{self.reviewer_id}')"


class FoodReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey(
        'food.id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)
    description = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    rating = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"FoodReview('{self.food_id}', '{self.reviewer_id}')"
