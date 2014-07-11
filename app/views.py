from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config.from_object('config')

from app.database import db_session
from app.models import LMS, SMS


@app.route('/')
def index():
    cur = db_session.query(LMS)
    cur2 = db_session.query(SMS)
    List = [dict(id=lms.mt_pr, subject=lms.subject,
                 content=lms.content, callback=lms.callback,
                 recipent_num=lms.recipent_num) for lms in cur]
    List2 = [dict(id=sms.mt_pr, content=sms.content,
                  callback=sms.callback,
                  recipent_num=sms.recipent_num) for sms in cur2]
    return render_template('index.html', List=List, List2=List2)


@app.route('/messages', methods=['GET'])
def messages():
    title = request.args['title']
    msg = request.args['msg']
    phone_from = request.args['phone_from']
    phone = request.args['phone']
    try:
        int(phone_from)
        int(phone)
        resp = 'Success'
        if len(msg) < 1:
            resp = 'Message is Null'
            raise Exception(ValueError)
    except ValueError:
        resp = 'form phone_from or phone is not integer'
    else:
        if len(msg.encode('euc-kr')) >= 80:
            db_msg = LMS(title, msg, phone_from, phone)
        else:
            db_msg = SMS(msg, phone_from, phone)
        db_session.add(db_msg)
        db_session.commit()
    finally:
        return jsonify(result=resp)


