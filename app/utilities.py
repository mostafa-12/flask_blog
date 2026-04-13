from flask import current_app
from werkzeug.utils import secure_filename
import os
def save_pic_secure(form_picture):
    ABS_PICS_PATH = os.path.join(current_app.config['UPLOAD_FOLDER'], "pics")

    filename = secure_filename(form_picture.filename)
    picture_path = os.path.join(ABS_PICS_PATH, filename)
    form_picture.save(picture_path)
    return filename