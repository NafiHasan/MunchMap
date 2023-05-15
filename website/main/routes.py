from flask import render_template, request, Blueprint
from website.models import Restaurant, Food

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    restaurants = Restaurant.query.order_by(
        Restaurant.rating.desc()).paginate(page=page, per_page=12)
    return render_template('home.html', restaurants=restaurants)


@main.route("/home2")
def home2():
    page = request.args.get('page', 1, type=int)
    foods = Food.query.order_by(
        Food.rating.desc()).paginate(page=page, per_page=12)
    # foods = sorted(
    #     foods,
    #     key=lambda x: (x.total_rating /
    #                    x.rating_count) if x.rating_count != 0 else 0,
    #     reverse=True
    # )
    return render_template('home2.html', foods=foods)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        print(request.form.get('search'), 'he')

    else:
        search_query = request.args.get('search')
        print(search_query)
        if search_query:
            page = request.args.get('page', 1, type=int)
            restaurants = Restaurant.query.filter(
                Restaurant.name.like(f'%{search_query}%')).paginate(page=page, per_page=12)
            return render_template('home.html', restaurants=restaurants)
    page = request.args.get('page', 1, type=int)
    restaurants = Restaurant.query.order_by(
        Restaurant.name).paginate(page=page, per_page=12)
    return render_template('home.html', restaurants=restaurants)


@main.route("/search_food", methods=['GET', 'POST'])
def search_food():
    if request.method == 'POST':
        print(request.form.get('search'), 'he')

    else:
        search_query = request.args.get('search')
        print(search_query)
        if search_query:
            page = request.args.get('page', 1, type=int)
            foods = Food.query.filter(
                Food.name.like(f'%{search_query}%')).paginate(page=page, per_page=12)
            return render_template('home2.html', foods=foods)
    page = request.args.get('page', 1, type=int)
    foods = Food.query.order_by(
        Food.name).paginate(page=page, per_page=12)
    return render_template('home2.html', foods=foods)
