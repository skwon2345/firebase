#flask
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request

#database
import db as conn
from firebase_admin import firestore

#dotenv
import os
from os.path import join, dirname
from dotenv import load_dotenv

#stock
import FinanceDataReader as fdr

#mnist image
import base64
import cv2
from PIL import Image
import joblib
import io

import datetime
import numpy as np

app = Flask(__name__)

# Settings
CORS(app)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# def sendEmail(name, emailAddress, content):
#     email_user = 'josephonsk@gmail.com'     
#     email_password = os.environ.get("MAIL_PASSWORD")
# ##    email_send = 'joohyeong1211@gmail.com'
# ##    email_send = '69ij@naver.com'
#     email_send = 'sklass2345@gmail.com'
# ##    email_send = 'onyoung@chol.com'
#     # email_send = 'hwjiyoon@naver.com'
#     # 제목
#     subject = 'Contact from ' + name 

#     msg = MIMEMultipart('mixed')
#     msg['From'] = email_user
#     msg['To'] = email_send
#     msg['Subject'] = subject

#     # 본문 내용
#     body = 'Email to reply: '+emailAddress+'\n\n'+content
#     msg.attach(MIMEText(body,'plain'))

#     text = msg.as_string()
#     server = smtplib.SMTP_SSL('smtp.gmail.com',465)

#     server.login(email_user,email_password)

#     server.sendmail(email_user,email_send,text)
#     server.quit()

def img_to_array(img, data_format='channels_last', dtype='float32'):
    """Converts a PIL Image instance to a Numpy array.
    # Arguments
        img: PIL Image instance.
        data_format: Image data format,
            either "channels_first" or "channels_last".
        dtype: Dtype to use for the returned array.
    # Returns
        A 3D Numpy array.
    # Raises
        ValueError: if invalid `img` or `data_format` is passed.
    """
    if data_format not in {'channels_first', 'channels_last'}:
        raise ValueError('Unknown data_format: %s' % data_format)
    # Numpy array x has format (height, width, channel)
    # or (channel, height, width)
    # but original PIL image has format (width, height, channel)
    x = np.asarray(img, dtype=dtype)
    if len(x.shape) == 3:
        if data_format == 'channels_first':
            x = x.transpose(2, 0, 1)
    elif len(x.shape) == 2:
        if data_format == 'channels_first':
            x = x.reshape((1, x.shape[0], x.shape[1]))
        else:
            x = x.reshape((x.shape[0], x.shape[1], 1))
    else:
        raise ValueError('Unsupported image shape: %s' % (x.shape,))
    return x

def calcSMA (values, window):
	weights = np.repeat(1.0, window)/ window
	smas = np.convolve(values, weights, 'valid')
	return smas


@app.route('/')
def hello():
    try:
        doc_ref_overall = conn.db.collection(u'test11').document('aaa')
        doc_ref_overall.set({
           'name':'los angefles'
})

        return jsonify({"success":True}), 200
    except Exception as e:
        print("Error")
        print(e)
        return f"An Error Occured: {e}"
    return 'Hello World!'

@app.route('/users', methods=['POST'])
def createUser():
    try:
        reqData = request.json
        doc_ref_overall = conn.db.collection(u'test11').document('fe')
        doc_ref_overall.set(reqData)

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
        urls = conn.db.collection(u'files').order_by(u'date', direction=firestore.Query.DESCENDING).limit(10).stream()

        my_dict = [url.to_dict() for url in urls]
        return jsonify(my_dict), 200
    except Exception as e:
        return f"An Error occured: {e}"

    
@app.route('/contact', methods=['POST'])
def contactToMe():
    try:
        reqData = request.json
        today = str(datetime.date.today())
        docName = today+'_'+reqData['_name']
        doc_ref_overall = conn.db.collection(u'contact').document(docName)
        doc_ref_overall.set(reqData)

        return jsonify({"success":True}), 200

    except Exception as e:
        print("Error")
        print(e)
        return f"An Error Occured: {e}"

@app.route('/api/digit-classification', methods=['POST'])
def uploadImageBASE64():
    try:
        reqData = request.json
        data = reqData['image']
        _format, str_img = data.split(';base64')
        decoded_file = base64.b64decode(str_img)
        
        img = Image.open(io.BytesIO(decoded_file))
        img_array = img_to_array(img)

        new_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        # dim = (8,8) # sklearn.dataset has to shrink img to 8*8
        dim = (28,28) # keras.dataset has to shrink img to 28*28
        resized = cv2.resize(new_img, dim, interpolation = cv2.INTER_AREA)

        print(resized.shape) # (8,8) for sklearn (28,28) for keras

        result = resized.flatten()

        print(result.shape) # (64,0) for sklearn (784,0) for keras

        # model = joblib.load('./models/keras_random_forest_joblib') # model trained with keras.dataset using random forest algorithm
        model = joblib.load('./models/keras_svm_model_joblib') # model trained with keras using Support Vector Machine
        # model = joblib.load('./models/sklearn_svm_model_joblib') # model trained with sklearn.dataset using Support Vector Machine
        # model = joblib.load('./models/sklearn_model_joblib') # model trained with sklearn.dataset using Logistic Regression
        # model = joblib.load('./models/keras_model_joblib') # model trained with kears.dataset
        ans = model.predict([result])
        print(model.predict([result]))

        return jsonify({"success":int(ans[0])}), 200

    except Exception as e:
        print(e)
        return f"An Error Occured: {e}"

@app.route('/buySignal', methods=['GET'])
def getBuySignals():
    try:
        bSignals = conn.db.collection(u'history').where(u'recommended', u'==', False).order_by(u'date', direction=firestore.Query.DESCENDING).limit(10).stream()
        my_dict = []
        today = str(datetime.date.today())
        for s in bSignals:
            tmp = s.to_dict()
            df_reverse = fdr.DataReader(tmp['code'], today)
            df = df_reverse.iloc[::-1]
            tmp['_id'] = s.id
            tmp['current_price'] = int(df['Close'][0])
            tmp['profit'] = "{:.2f}".format((tmp['current_price']-tmp['bPrice'])/tmp['bPrice']*100)
            my_dict.append(tmp)
 
        return jsonify(my_dict), 200
    except Exception as e:
        return f"An Error Occured; {e}"

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8088, debug=True) # deploy host; 0.0.0.0 , development host: 127.0.0.2


