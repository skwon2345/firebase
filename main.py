#flask
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request

#database
import db as conn
from firebase_admin import firestore

#stock data
import FinanceDataReader as fdr
import numpy as np

# import time

app = Flask(__name__)

# Settings
CORS(app)


tickers = fdr.StockListing('KOSPI')['Symbol'].values
stckListing = fdr.StockListing('KOSPI')


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

@app.route('/api/data',methods=['GET'])
def testStockAPI():
    dataToSend = []
    # start = time.time()
    for ticker in tickers:
        print(ticker)
        try:
            if len(ticker) <= 6:
                df_reverse = fdr.DataReader(ticker)
                df = df_reverse.iloc[::-1]
                if len(df) < 200:
                        continue
            else:
                continue
##  df, meta_data = ts.get_intraday(symbol=ticker,interval='60min', outputsize='full')
        except Exception as e:
            return f"An Error occured: {e}"

        selectedStck = stckListing.loc[stckListing['Symbol']==str(ticker)]
        stckMarket = str(selectedStck['Market'].values[0])

        if stckMarket == "KONEX":
                continue
        sma_df = df['Close']
        sma_5 = calcSMA(sma_df, 5)
        sma_10 = calcSMA(sma_df, 10)
        sma_20 = calcSMA(sma_df, 20)
        sma_60 = calcSMA(sma_df, 60)
        sma_120 = calcSMA(sma_df, 120)
        sma_200 = calcSMA(sma_df, 200)
        if sma_5[1] < sma_10[1] and sma_5[0] > sma_10[0]:
            dataToSend.append(ticker)

    a = df.head(5).to_dict('index')
    a = {str(k)[:10]:v for k,v in a.items()}
    # timeTaken = time.time() - start
    # dataToSend.insert(0, str(timeTaken))
    print(dataToSend)
    # print(timeTaken)
    return jsonify(dataToSend), 200

    

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8088, debug=True) # deploy host; 0.0.0.0 , development host: 127.0.0.2


