from flask import Flask, render_template, jsonify, request
#database 
import firebase_admin
from firebase_admin import credentials, firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\Administrator\Desktop\stock\stocktrading-14119-2c743d2f58b4.json" # r converts normal string to raw string. (raw string is necessary for file path) 

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'stocktrading-14119',
})

db = firestore.client()

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        doc_ref_overall = db.collection(u'test11').document('aaa')
        doc_ref_overall.set({
           'name':'los angefles'
        })

        return jsonify({"success":True}), 200
    except Exception as e:
        print("fesf")
        print(e)
        return f"An Error Occured: {e}"
    return 'Hello World!'

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8088, debug=True)
