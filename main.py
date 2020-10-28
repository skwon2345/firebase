#flask
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request

#database
# import db as conn
from firebase_admin import firestore

app = Flask(__name__)

# Settings
CORS(app)

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

# @app.route('/users', methods=['POST'])
# def createUser():
#     try:
#         reqData = request.json
#         doc_ref_overall = conn.db.collection(u'test11').document('fe')
#         doc_ref_overall.set(reqData)

#         return jsonify({"success":True}), 200

#     except Exception as e:
#         print("Error")
#         print(e)
#         return f"An Error Occured: {e}"
        

# @app.route('/users', methods=['GET'])
# def getUsers():
#     try:
#         todo = conn.db.collection(u'test11').document('fe').get()
#         return jsonify(todo.to_dict()), 200
#     except Exception as e:
#         return f"An Error Occured; {e}"


# @app.route('/storage',methods=['GET'])
# def getStorageFile():
#     try:
#         urls = conn.db.collection(u'files').order_by(u'date', direction=firestore.Query.ASCENDING).limit(3).stream()

#         my_dict = [url.to_dict() for url in urls]
#         return jsonify(my_dict), 200
#     except Exception as e:
#         return f"An Error occured: {e}"

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8088, debug=True) # deploy host; 0.0.0.0 , development host: 127.0.0.2


