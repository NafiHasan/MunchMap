from flask import render_template, request, Blueprint
from website.models import Restaurant

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    restaurants = Restaurant.query.order_by(
        Restaurant.name).paginate(page=page, per_page=9)
    return render_template('home.html', restaurants=restaurants)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
