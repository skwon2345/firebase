#flask
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request

#database 
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

#dotenv
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

key = os.environ.get("DB_KEY")

cred = credentials.Certificate(key)
default_app = initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# Settings
CORS(app)

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

@app.route('/users', methods=['POST'])
def createUser():
    print(request.json)
    try:
        doc_ref_overall = db.collection(u'test11').document('fe')
        doc_ref_overall.set(request.json)
        print("efe")

        return jsonify({"success":True}), 200
    except Exception as e:
        print("fesf")
        print(e)
        return f"An Error Occured: {e}"
        

@app.route('/users', methods=['GET'])
def getUsers():
    try:
        todo = db.collection(u'test11').document('fe').get()
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        return f"An Error Occured; {e}"

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8088, debug=True)
