#flask
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request

#database
import db as conn
from firebase_admin import firestore

#stock data
# import FinanceDataReader as fdr
import numpy as np

# # E-mail
# import os
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders

#dotenv
import os
from os.path import join, dirname
from dotenv import load_dotenv

#mnist image
import base64
import uuid
import cv2
from PIL import Image
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import joblib


import datetime

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

# @app.route('/api/data',methods=['GET'])
# def testStockAPI():
#     tickers = fdr.StockListing('KOSPI')['Symbol'].values
#     stckListing = fdr.StockListing('KOSPI')
#     dataToSend = []
#     count = 0 
#     # start = time.time()
#     for ticker in tickers:
#         if count > 10:
#             break
#         print(ticker)
#         try:
#             if len(ticker) <= 6:
#                 df_reverse = fdr.DataReader(ticker)
#                 df = df_reverse.iloc[::-1]
#                 if len(df) < 200:
#                         continue
#             else:
#                 continue
# ##  df, meta_data = ts.get_intraday(symbol=ticker,interval='60min', outputsize='full')
#         except Exception as e:
#             return f"An Error occured: {e}"

#         selectedStck = stckListing.loc[stckListing['Symbol']==str(ticker)]
#         stckMarket = str(selectedStck['Market'].values[0])

#         if stckMarket == "KONEX":
#                 continue
#         sma_df = df['Close']
#         sma_5 = calcSMA(sma_df, 5)
#         sma_10 = calcSMA(sma_df, 10)
#         sma_20 = calcSMA(sma_df, 20)
#         sma_60 = calcSMA(sma_df, 60)
#         sma_120 = calcSMA(sma_df, 120)
#         sma_200 = calcSMA(sma_df, 200)
#         if sma_5[1] < sma_10[1] and sma_5[0] > sma_10[0]:
#             dataToSend.append(ticker)
#         count = count + 1

#     a = df.head(5).to_dict('index')
#     a = {str(k)[:10]:v for k,v in a.items()}
#     # timeTaken = time.time() - start
#     # dataToSend.insert(0, str(timeTaken))
#     print(dataToSend)
#     # print(timeTaken)
#     return jsonify(dataToSend), 200

    
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

@app.route('/api/mnist', methods=['POST'])
def uploadImageBASE64():
    try:
        reqData = request.json
        data = reqData['image']
        _format, str_img = data.split(';base64')
        decoded_file = base64.b64decode(str_img)
        fname = f"{str(uuid.uuid4())[:10]}.png"
        path = './images/'+ fname
        with open(path,'wb') as f:
            f.write(decoded_file)
        
        img = Image.open(path)
        img_array = image.img_to_array(img)
        print(img_array)
        print(img_array.shape) #(800, 798, 4)


        new_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        dim = (8,8) #have to shrink img to 28*28
        resized = cv2.resize(new_img, dim, interpolation = cv2.INTER_AREA)
        print(resized.shape) # (8,8)

        result = resized.flatten()

        model = joblib.load('./mnist_model_joblib')
        ans = model.predict([result])
        print(model.predict([result]))


        return jsonify({"success":int(ans[0])}), 200

    except Exception as e:
        print(e)
        return f"An Error Occured: {e}"



if __name__=='__main__':
    app.run(host='127.0.0.1', port=8088, debug=True) # deploy host; 0.0.0.0 , development host: 127.0.0.2


