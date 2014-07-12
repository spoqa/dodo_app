from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config.from_object('config')

from testapp.database import db_session
from testapp.models import LMS, SMS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/messages', methods=['GET'])
def messages():
    title = request.args['title']
    msg = request.args['msg']
    phone_from = request.args['phone_from']
    phone = request.args['phone']
    try:
        if len(msg) < 1:
            resp = 'Message is Null'
            raise Exception(ValueError)
        else:
            int(phone_from)
            int(phone)
            resp = 'Success'
    except ValueError:
        resp = 'form phone_from or phone Value Error. numbers only & Not Null'
    else:
        if len(msg.encode('euc-kr')) >= 80:
            db_msg = LMS(title, msg, phone_from, phone)
        else:
            db_msg = SMS(msg, phone_from, phone)
        db_session.add(db_msg)
        db_session.commit()
    finally:
        return jsonify(result=resp)
