import os
from flask import Flask, render_template, request, send_file
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from rembg import remove
from PIL import Image
from io import BytesIO

from dotenv import load_dotenv
load_dotenv()

USER = os.getenv('APP_USER')
PASSWORD = os.getenv('APP_PASSWORD')

app = Flask(__name__, static_folder='static', static_url_path='')
auth = HTTPBasicAuth()

users = {
    USER: generate_password_hash(PASSWORD)
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        background = request.form.get('background')
        if file.filename == '':
            return 'No file selected', 400
        if file:
            input_image = Image.open(file.stream)
            output_image = remove(input_image, post_process_mask=True)
            img_io = BytesIO()
            if background == '':
                output_image.save(img_io, 'PNG')
            else:
                background_image = Image.open('static' + background)
                transparent_image = Image.new('RGBA', background_image.size, (0, 0, 0, 0))
                x = (transparent_image.width - output_image.width) // 2
                y = (transparent_image.height - output_image.height) // 2

                transparent_image.paste(output_image, (x, y), output_image)
                transparent_image = transparent_image.resize(background_image.size)
                merged_image = Image.alpha_composite(background_image.convert('RGBA'), transparent_image)
                merged_image.save(img_io, 'PNG')
            img_io.seek(0)
            # return send_file(img_io, mimetype='image/png')  # Change download in separatre browser tab
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='_rmbg.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)