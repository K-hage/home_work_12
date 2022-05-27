import logging
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

logger = logging.getLogger("log")
logger.setLevel(logging.INFO)
filehandler_logger = logging.FileHandler("basic.log", encoding="utf-8")

logger.addHandler(filehandler_logger)
