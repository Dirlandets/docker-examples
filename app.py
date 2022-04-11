from flask import Flask, render_template, request

from database import migrate, get_session
from crud import get_product, create_product
from dotenv import load_dotenv
load_dotenv()


def create_app(create_db=True):
    app = Flask(__name__)
    if create_db:
        migrate()
    return app


app = create_app()

@app.route('/', methods=['GET'])
def get_prod():
    session = get_session()
    products = get_product(session)
    return render_template('products_page.html', products=products)


@app.route('/', methods=['post'])
def create_prod():
    form = request.form
    session = get_session()
    create_product(session, form['name'])
    products = get_product(session)
    return render_template('products_page.html', context={}, products=products)
