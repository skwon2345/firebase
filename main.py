#flask
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request

#database
import db as conn
from firebase_admin import firestore

#Email
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime

app = Flask(__name__)

# Settings
CORS(app)

def sendEmail(email_receiver):
    email_user = 'josephonsk@gmail.com'     
    email_password = 'dhstjrrn00'
    email_send = email_receiver
    today = str(datetime.date.today())
    # 제목
    subject = today + ' 분석 결과' 

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    # 본문 내용
    body = "온석권"
    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)

    server.login(email_user,email_password)

    server.sendmail(email_user,email_send,text)
    server.quit()

@app.route('/')
def hello():
    # try:
    #     doc_ref_overall = conn.db.collection(u'test11').document('aaa')
    #     doc_ref_overall.set({
    #        'name':'los angefles'
    #     })

    #     return jsonify({"success":True}), 200
    # except Exception as e:
    #     print("Error")
    #     print(e)
    #     return f"An Error Occured: {e}"
    return 'Hello World!'

@app.route('/users', methods=['POST'])
def createUser():
    try:
        reqData = request.json
        doc_ref_overall = conn.db.collection(u'test11').document('fe')
        doc_ref_overall.set(reqData)
        sendEmail(reqData['email'])

        return jsonify({"success":True}), 200

    except Exception as e:
        print("Error")
        print(e)
        return f"An Error Occured: {e}"
        

@app.route('/users', methods=['GET'])
def getUsers():
    try:
        todo = conn.db.collection(u'test11').document('fe').get()
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        return f"An Error Occured; {e}"


@app.route('/storage',methods=['GET'])
def getStorageFile():
    try:
        urls = conn.db.collection(u'files').order_by(u'date', direction=firestore.Query.ASCENDING).limit(3).stream()

        my_dict = [url.to_dict() for url in urls]
        return jsonify(my_dict), 200
    except Exception as e:
        return f"An Error occured: {e}"

# if __name__=='__main__':
#     app.run(host='127.0.0.1', port=8088, debug=True) # deploy host; 0.0.0.0 , development host: 127.0.0.2


