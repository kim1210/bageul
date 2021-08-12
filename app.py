from flask import Flask, render_template, request, send_file, flash, url_for
from flask.wrappers import Request
from werkzeug.utils import redirect
app = Flask(__name__)

import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import os
import config

# app.secret_key = 'the random string'
app.config.from_object(config)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    note_1 = list(str(request.form['note_1']))
    note_2 = list(str(request.form['note_2']))
    note_3 = list(str(request.form['note_3']))
    note_4 = list(str(request.form['note_4']))

    form_img = os.path.dirname(__file__) +"\static\\note.png"
    img = cv2.imread(form_img)

    image = Image.open(form_img)
    font = ImageFont.truetype(os.path.dirname(__file__)+"\\static\\fonts\\NanumMyeongjo.ttf", 88)
    draw = ImageDraw.Draw(image)

    def make_form(note_n, y1):
        x1 = 105
        for v in note_n :
            if v == ' ':
                x1 = x1+115
                draw.text((x1, y1), v, font=font, fill=(0,0,0))
            else :
                x1 = x1+100
                draw.text((x1,y1), v, font=font, fill=(0,0,0))

    if len(note_1) > 14 or len(note_2) > 14 or len(note_3) > 14 or len(note_4) > 14:
        flash('글자 수를 초과하였습니다.')
        return redirect(url_for('index'))

    make_form(note_1, 210)
    make_form(note_2, 417)
    make_form(note_3, 627)
    make_form(note_4, 839)

    nd_image = np.array(image)

    load = os.path.dirname(__file__) + "\static\kew.png"
    new_img = Image.fromarray(nd_image)
    new_img.save(load)

    return send_file(load, attachment_filename='form.png', mimetype='image/png')
