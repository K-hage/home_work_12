import json
from classes.post import Post
from config import POST_PATH


def load_data(path=POST_PATH):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return "Файл не открывается"
    except json.JSONDecoder:
        return "Не удается преобразовать файл"
    else:
        return data


def dump_json(pic, content, path=POST_PATH):
    data = load_data()
    post = {
        "pic": f"/uploads/images/{pic}",
        "content": content
    }
    data.append(post)
    with open(path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_posts():
    database = []
    for data in load_data():
        database.append(Post(data["pic"], data['content']))
    return database


def is_filename_allowed(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    extension = filename.lower().split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True


def download_error(picture):
    if picture:
        return True


def search_post(text):
    data = get_posts()
    search_content = []
    for content in data:
        if text.lower().strip() in content.content.lower():
            search_content.append(content)
    return search_content


def check_errors(picture, content):
    filename = picture.filename

    if not content:
        return "content_none"
    if not picture:
        return "picture_none"
    if is_filename_allowed(filename) is None:
        return "allowed"

    try:
        picture.save(f"./uploads/images/{filename}")
    except:
        return "not_load_picture"

    try:
        dump_json(filename, content)
    except:
        return "not_load_post"
