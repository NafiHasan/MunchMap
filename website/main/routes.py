from flask import render_template, request, Blueprint
from website.models import Restaurant

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    restaurants = Restaurant.query.order_by(
        Restaurant.name).paginate(page=page, per_page=12)
    return render_template('home.html', restaurants=restaurants)


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
                Restaurant.name.like(f'%{search_query}%')).paginate(page=page, per_page=9)
            return render_template('home.html', restaurants=restaurants)
    page = request.args.get('page', 1, type=int)
    restaurants = Restaurant.query.order_by(
        Restaurant.name).paginate(page=page, per_page=9)
    return render_template('home.html', restaurants=restaurants)
