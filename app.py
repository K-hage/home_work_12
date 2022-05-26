import logging
from flask import Flask, send_from_directory
from loader.views import loader_blueprint
from main.views import main_blueprint
from config import UPLOAD_FOLDER

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

logging.basicConfig(filename="basic.log", format='%(asctime)s: %(message)s', level=logging.INFO, encoding="utf-8")
console_log = logging.getLogger()
console_log.addHandler(logging.StreamHandler())

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>/")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run(debug=True)
