from flask import Blueprint, render_template, request
from functions import *
from config import *

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post/")
def loader_page():
    return render_template('post_form.html')


@loader_blueprint.route("/post/", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    content = request.form['content']
    filename = picture.filename

    error = check_errors(picture, content)
    match error:
        case "allowed":
            logger.info(f"Попытка загрузки файла формата '{filename.split('.')[-1]}'")
        case "not_load_picture":
            logger.error(f"Не удалось загрузить файл: {filename}")

    return render_template('post_uploaded.html',
                           error=error,
                           pic=picture.filename,
                           content=content,
                           )
