from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from website import db
from website.models import Restaurant, Food
from website.foods.forms import PostForm

foods = Blueprint('foods', __name__)


@foods.route("/food/<int:restaurant_id>/new", methods=['GET', 'POST'])
@login_required
def new_food(restaurant_id):
    form = PostForm()
    if form.validate_on_submit():
        food = Food(name=form.name.data,
                    description=form.description.data, restaurant_id=restaurant_id)
        # print(form.name.data, form.description.data, current_user,
        #   form.location.data, form.detail_location.data)
        db.session.add(food)
        db.session.commit()
        flash('Food item has been added!', 'success')
        return redirect(url_for('restaurants.restaurant', restaurant_id=restaurant_id))
    return render_template('add_item.html', title='Add Item',
                           form=form, legend='Add New Item')


@foods.route("/post/<int:post_id>")
def food(post_id):
    restaurant = Restaurant.query.get_or_404(post_id)
    return render_template('post.html', title=food.name, restaurant=restaurant)
