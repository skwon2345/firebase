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