from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
app.config.from_object('config')

from app.database import db_session
from app.models import LMS, SMS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/messages', methods=['GET', 'POST'])
def messages():
    msg_length = len(request.form['msg'].encode('euc-kr'))
    if msg_length >= 80:
        msg = LMS(request.form['title'], request.form['msg'],
                  request.form['phone_from'], request.form['phone'])
    else:
        msg = SMS(request.form['msg'],
                  request.form['phone_from'], request.form['phone'])
    import pdb; pdb.set_trace()
    db_session.add(msg)
    db_session.commit()
    return msg

