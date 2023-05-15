from flask import (Blueprint, render_template, url_for, flash,
                   redirect, request, abort)
from flask_login import current_user, login_required
from website import db
from website.models import Restaurant, RestaurantReview
from website.users.utils import save_picture
from website.restaurants.forms import PostForm, UpdateForm
from website import foods

restaurants = Blueprint('restaurants', __name__)


@restaurants.route("/restaurant/new", methods=['GET', 'POST'])
@login_required
def new_restaurant():
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)

        else:
            picture_file = 'default.jpg'

        restaurant = Restaurant(name=form.name.data,
                                description=form.description.data, owner=current_user, location=form.location.data, detail_location=form.detail_location.data, rating=0, image_file=picture_file)
        # print(form.name.data, form.description.data, current_user,
        #   form.location.data, form.detail_location.data)
        db.session.add(restaurant)
        db.session.commit()
        flash('Restaurant has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_restaurant.html', title='New Restaurant',
                           form=form, legend='Create New Restaurant')


@restaurants.route("/restaurant/<int:restaurant_id>")
def restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    foods = restaurant.foods

    foods = sorted(
        foods,
        key=lambda x: (x.total_rating /
                       x.rating_count) if x.rating_count != 0 else 0,
        reverse=True
    )

    # print(restaurant.foods)
    return render_template('restaurant.html', title=restaurant.name, foods=foods, restaurant=restaurant)


@restaurants.route("/restaurant/<int:restaurant_id>/update", methods=['GET', 'POST'])
@login_required
def update_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    if restaurant.owner != current_user:
        abort(403)
    form = UpdateForm()
    if form.validate_on_submit():
        restaurant.name = form.name.data
        restaurant.description = form.description.data
        restaurant.location = form.location.data
        restaurant.detail_location = form.detail_location.data

        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            restaurant.image_file = picture_file

        db.session.commit()
        flash('Info has been updated!', 'success')
        return redirect(url_for('restaurants.restaurant', restaurant_id=restaurant.id))
    elif request.method == 'GET':
        form.name.data = restaurant.name
        form.description.data = restaurant.description
        form.location.data = restaurant.location
        form.detail_location.data = restaurant.detail_location
    return render_template('create_restaurant.html', title='Update restaurant',
                           form=form, legend='Update restaurant information')


# @restaurants.route("/post/<int:post_id>/delete", methods=['POST'])
# @login_required
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     db.session.delete(post)
#     db.session.commit()
#     flash('Your post has been deleted!', 'success')
#     return redirect(url_for('main.home'))


@restaurants.route("/review/<int:restaurant_id>")
def review_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    reviews = RestaurantReview.query.filter_by(restaurant_id=restaurant_id).order_by(
        RestaurantReview.date_posted.desc()).all()
    return render_template('review2.html', restaurant=restaurant, reviews=reviews)


@restaurants.route('/add-restaurant-review', methods=['GET', 'POST'])
def add_restaurant_review():
    if request.method == 'POST':
        review_text = request.form.get('review-text')
        restaurant_id = request.form.get('restaurant_id')
        reviewer_id = request.form.get('reviewer_id')

        print(review_text, reviewer_id)

        reviews = RestaurantReview.query.filter_by(restaurant_id=restaurant_id).order_by(
            RestaurantReview.date_posted.desc()).all()
        # print(review_text, reviewer_id)
        rating = request.form.get('rating')
        print(review_text, rating)

        new_review = RestaurantReview(
            restaurant_id=restaurant_id, reviewer_id=reviewer_id, description=review_text, rating=(6 - int(rating)))
        db.session.add(new_review)
        db.session.commit()
        restaurant = Restaurant.query.get(restaurant_id)

        restaurant.total_rating = restaurant.total_rating - float(rating) + 6.0
        restaurant.rating_count = restaurant.rating_count + 1

        if restaurant.rating_count > 0:
            restaurant.rating = (restaurant.total_rating /
                                 restaurant.rating_count)

        # print(food.name, food.total_rating, food.rating_count)
        db.session.commit()

        flash('Your review has been added. Thank You!', 'success')
        return redirect(url_for('restaurants.review_restaurant', restaurant_id=restaurant_id))

    else:
        review_text = request.form.get('review-text')
        restaurant_id = request.form.get('restaurant_id')
        reviewer_id = request.form.get('reviewer_id')
        reviews = RestaurantReview.query.filter_by(restaurant_id=restaurant_id).order_by(
            RestaurantReview.date_posted.desc()).all()
        restaurant = Restaurant.query.get(restaurant_id)
        return redirect(url_for('restaurants.review_restaurant', restaurant_id=restaurant_id))
