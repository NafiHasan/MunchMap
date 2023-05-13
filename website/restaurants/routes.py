from flask import (Blueprint, render_template, url_for, flash,
                   redirect, request, abort)
from flask_login import current_user, login_required
from website import db
from website.models import Restaurant
from website.restaurants.forms import PostForm
from website import foods

restaurants = Blueprint('restaurants', __name__)


@restaurants.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        restaurant = Restaurant(name=form.name.data,
                                description=form.description.data, owner=current_user, location=form.location.data, detail_location=form.detail_location.data, rating=0)
        print(form.name.data, form.description.data, current_user,
              form.location.data, form.detail_location.data)
        db.session.add(restaurant)
        db.session.commit()
        flash('Restaurant has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_restaurant.html', title='New Restaurant',
                           form=form, legend='Create New Restaurant')


@restaurants.route("/restaurant/<int:restaurant_id>")
def restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    # print(restaurant.foods)
    return render_template('restaurant.html', title=restaurant.name, foods=restaurant.foods, restaurant=restaurant)


@restaurants.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    restaurant = Restaurant.query.get_or_404(post_id)
    if restaurant.owner != current_user:
        abort(403)
    form = PostForm()
    # if form.validate_on_submit():
    #     post.title = form.title.data
    #     post.content = form.content.data
    #     db.session.commit()
    #     flash('Your post has been updated!', 'success')
    #     return redirect(url_for('restaurants.post', post_id=post.id))
    # elif request.method == 'GET':
    #     form.title.data = post.title
    #     form.content.data = post.content
    # return render_template('create_restaurant.html', title='Update Post',
    #                        form=form, legend='Update Post')


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
