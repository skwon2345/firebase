#database 
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
<<<<<<< HEAD
=======
import json
>>>>>>> f33ebed06667d0661e62c459baae246f86d3b2d8

#dotenv
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

<<<<<<< HEAD
key = os.environ.get("DB_KEY")
=======
key = {
  "type": "service_account",
  "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
  "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCX2I1O6HuCs8pJ\nkw21fuf81qPo3ZduxsIV+fB04noig+ubmYMVD+2VDNg8ISk+P2tze0HcJNL3OemP\nT2qT0fIL+pALfO/PaoC8yCB/13S0a55ESkrBS509IzCupEpA7ONrw4DK1yuNOVIL\nYr9dAhHUavTpMuf01iUCrCTAWklfJDct/eIKVA0udXnJAm8EqJzPZqXxt0BNw506\nzHbDtnaktkjanLKQdB1NuXH11j1BRUEko3EAjeumyImOrST8x9H0qXNJDAuNf2DW\n5vf8VQrGUqbYVxfB2n0cjAUfIAxTwACZnOu9PmrU6u3CAcuOsOE1CChE/N3uXNU2\nTj9lGpCjAgMBAAECggEAJU2JyWzLitxoQZLit0ep7i88rSRi40/otkVkkRJiNsB5\nzQv1a+Mx1oAFTyBGZYhm+UO6dj6FpT6Q5if4YsAc2lx/rpLOxwG/BqGTelSP0xLt\nGpG1s67DvhU7DGxH4ZNQe1TX+vzJMjR2t11W7Z5oiuqLqA5ddYR2KyXnEWocxEZc\nbmZyJrDD/mTZqd3IegJrQxW/GwSTEP1IWflaGeyCE08IbVUe8alRTyknionhCzOw\nAyFcm1HVkASB74oxQJq3UhiJ6vhBxOukyAfGg8gV5nmtXgamK+oxi986+xea2Vbv\nLrJqOYM+5e3SiygJkrS9Bgw+KvES47u2wM01Tor5QQKBgQDK76sIc4yWE6QJbmD5\naBbcJNIV4p4CkTdRAHRreEBE97HECwPCs6IuJv5vsN4g43hEOgH+HmA1Izu8c21t\njmFdUkTeluPUkPUjfRN0YvPdIXi011RPhrVUjY9LS47vlR4+qqnFMIvs3BLrrWW1\nYv7ybLBBnsBtR7VuhaJh3NINSQKBgQC/jPRDqOxP4Bl/5LhyPnSJ8bxHijzz3oGX\nWrDEtSCmEkFTtDlGQQ2sXG94QcQ3wwtUtO2mEprXPV0RenWz0zXtl+aVh9Os4wNP\nzQBgf2Nw9VCxlFBfwUboel4emXTnz/eMi4ODeVa1CHqBRRjtOwzTMss1dz70fHGu\nXKcwWMSKiwKBgFezD3TNirnorwEsZFgkNYzZlLjEgIiXfRJSYf13sD6d1ILmR6/C\ntZnAXECkbLpF01mYv/ez5NvR6CTetTGdUFJmFUEkcD0Sj/3QNbIceUrdBi8Qx2y+\nyGpL6tsdQh4jkTh/xHJlMnMgAEU9YDDtIURe2CTjmEEhtjSXJ7+nEFeRAoGAfuDM\nwyxXKylTeqVzjyjTZLPcdL6aVSajTC/kOseHErmwz9LmxSQ9/FdV9qAJaq4lCTy2\n1XQpYDzjMrqc0Dos1G3zbESF71SHUwqFH2YB5kZ35shI3MRXRZIYWchn6UyVumCH\nAkUTK+Kr0oiEVE7y1colVArihmsPmeEBVULXHLUCgYB9JNmzgFVVggefW11AO0IJ\nR9I8LUf+QJ9mLFLuCc6199VEqrYZ5q7m3G1SKrPKpGzTpCxA9A+qXQCe/6zZzFUl\nH9LQA+sQfYYF19CYt/IosRVK18mxWFXEaW3To2dMBHtWr4qMPfxUDzLhWK6W/unS\n7mApIn+M74cg6cUiiCh+rg==\n-----END PRIVATE KEY-----\n",
  "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
  "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
  "auth_uri": os.environ.get("FIREBASE_AUTH_URI"),
  "token_uri": os.environ.get("FIREBASE_TOKEN_URI"),
  "auth_provider_x509_cert_url": os.environ.get("FIREBASE_AUTH_CERT_URL"),
  "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_CERT_URL")
}
>>>>>>> f33ebed06667d0661e62c459baae246f86d3b2d8

cred = credentials.Certificate(key)
default_app = initialize_app(cred)
db = firestore.client()