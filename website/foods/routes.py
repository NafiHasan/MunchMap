from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from website import db
from website.models import Restaurant, Food, FoodReview
from website.users.utils import save_picture
from website.foods.forms import PostForm

foods = Blueprint('foods', __name__)


@foods.route("/food/<int:restaurant_id>/new", methods=['GET', 'POST'])
@login_required
def new_food(restaurant_id):
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
        else:
            picture_file = 'default.jpg'

        food = Food(name=form.name.data,
                    description=form.description.data, restaurant_id=restaurant_id, image_file=picture_file)
        # print(form.name.data, form.description.data, current_user,
        #   form.location.data, form.detail_location.data)
        db.session.add(food)
        db.session.commit()
        flash('Food item has been added!', 'success')
        return redirect(url_for('restaurants.restaurant', restaurant_id=restaurant_id))
    return render_template('add_item.html', title='Add Item',
                           form=form, legend='Add New Item')


@foods.route("/food/<int:food_id>")
def food(food_id):
    food = Food.query.get_or_404(food_id)
    reviews = FoodReview.query.filter_by(food_id=food_id).order_by(
        FoodReview.date_posted.desc()).all()
    return render_template('review.html', food=food, reviews=reviews)


# @foods.route("/<int:food_id>/post_review", methods=['GET', 'POST'])
# def search(food_id):
#     if request.method == 'POST':
#         print(request.form.get('search'), 'he')

#     else:
#         review = request.args.get('review')
#         print(review)
#         if review:
#             page = request.args.get('page', 1, type=int)
#             foods = Food.query.get(food_id)
#             return render_template('review.html', foods=foods)
#     page = request.args.get('page', 1, type=int)
#     foods = Food.query.order_by(
#         Food.name).paginate(page=page, per_page=12)
#     return render_template('review.html', foods=foods)


@foods.route('/add-food-review', methods=['GET', 'POST'])
def add_food_review():
    if request.method == 'POST':
        review_text = request.form.get('review-text')
        food_id = request.form.get('food_id')
        reviewer_id = request.form.get('reviewer_id')
        reviews = FoodReview.query.filter_by(food_id=food_id).order_by(
            FoodReview.date_posted.desc()).all()
        print(review_text, reviewer_id)
        new_review = FoodReview(
            food_id=food_id, reviewer_id=reviewer_id, description=review_text)
        db.session.add(new_review)
        db.session.commit()
        food = Food.query.get(food_id)
        flash('Your review has been added. Thank You!', 'success')
        return redirect(url_for('foods.food', food_id=food_id))

    else:
        review_text = request.form.get('review-text')
        food_id = request.form.get('food_id')
        reviewer_id = request.form.get('reviewer_id')
        reviews = FoodReview.query.filter_by(food_id=food_id).order_by(
            FoodReview.date_posted.desc()).all()
        food = Food.query.get(food_id)
        return redirect(url_for('foods.food', reviews=reviews, food=food))
