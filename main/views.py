import logging
from flask import Blueprint, render_template, request
from functions import *

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_text = request.args.get('s')
    search_data = search_post(search_text)
    logging.info(f"Страница поиска запрошена по тексту: {search_text}")
    return render_template('post_list.html',
                           search_data=search_data,
                           search_text=search_text)
