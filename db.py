#database 
import firebase_admin
from firebase_admin import storage, credentials, firestore, initialize_app

#dotenv
import os
from os.path import join, dirname
from dotenv import load_dotenv

import urllib.request
import datetime 
import requests


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

key = {
  "type": "service_account",
  "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
  "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDE5v7L4cJmg4JT\nAnhjxSjR0cvqesK1ed4HmyqAaCvKzIwhjP8DznMgPWl9CiJaiLkCCzJn4Eu5wZ6T\n9fAhjWmwLeNJAvklruxOgPpEnB68yqYiKRakJvg6sVVurDXG5hHRc2ckSGDbg8Jf\nuZ+JiJzOACQaGihBFps2HHnNDod+f6eNfW4b7zV6VGpSPHYdSFsQD+p5JRTNeOuv\n/4nC8XiBkxl8MNlQ2obydpKiTvQ50UdAKC0vAFtat5a/g365IAoqK9sF2nq9WChb\nx/ilKSI9+fRtXfwBlcLFURTcvYA2HBzOL5/2/6Hko/JbidtpV70EYrbEh7vVa/Gl\n5hV5mkNVAgMBAAECggEAAeppMd5/CKKgk7CBhMoWNr9888mraZ55FCP6DH3hoWmk\nKH1n2flZ8iq95reWIoha/4yXj5ApBx0hLwCPRSNor2+62ty3CwzedVv1Gn0AzKoy\nEQg8+OA1vX3G90i9FBdBtsoDle7zAPURYMZ8YkHjnDcGP1aKz5tNa5xoiPUjSRxf\n6Kb33kng5tcrRKS9Wy8fH8eQOZYAXHc20KhnvSmdYjOhbaCEFmoK8P8AbKNgIkxW\nCtXqiX8+C7o3pd6S2AwMI/dQgf0Szfp5Eo80lBmvDfAXhW8iFhynkjr7SSacq9zw\nnBzW+0aowe/GlNQXU6bsd3mohYk0kdxqi17mq++bEQKBgQDlu98Z+6SrlK+eXIBy\ntEzpD5PureTK/xnNOa8bCpoLZ/DFBxChW5Mtne87HeOmSEpoLXYB0ZQlYy5JiADh\niQcEGGBBlZs+/HbPXlT+4XQSLNQ7nuA89gU6tT7MsDpLKxA7zb2p/8lT3wd4bLBI\ndA8SvITlBERu2Q/ZM1UI8A5lnQKBgQDbaiugJtEZHy+PYvYTGWIEGQ578iZ1HUIT\neOy5TgDLozVnmo328YBaUX7l0I+qJsgzhQGEOF9j5/Nen/eQsWbRHGLdA5B8cNkp\n0sGi5U43ix8z7CPeiAWKGBo9DqRV15wjrI1b1TqeWZ9kHvuYMQdlcSX6lM9WMZBf\ndupurg+DGQKBgCPkUTve++Aur61fKFZDYwy6eVM96dPpPR+6Fmh0JJMJny05KFj9\nVKY42Ypz5gAxpSZXi+tG0g1xTGcCj5is7uKt6EP22rVhfjJxu3fCw36fcF0MOl5r\n1W9Rp8kU81aRGM0vHKW1p7+pxaID4RrAvyYfO+gH3aUv1nEJuwxVbPplAoGAUjt+\nUi16HII1nvWl6A6RT5vcc9OTWj028HlXrzNu1OM8NrIUFsL4KeF1P8hkr46NZdGp\nedZu2dCqw4IMlKwILsMGwnJ9ikX4/dXBQL3UDLkVXq5X2yT7fn/+BXghWxLNsAkR\niaNmrsZEGJAMF0P406oOY9W1x0YYJ883mXee1LECgYEAm3t91ZN1oJ/9gLwILOAS\n9c/pXzaqpIuQRETlRas19rLH9FMFzwfj1XkbtqqUbv1GmPoWvqRr3HdaNJQV2QyT\n7i4bLMI0iWf5Dt/aOUhkeusgNsS8BXzjBWNmq2sBIQq65OfxWdb+VT0Yrz/CjuCi\nqnxx8fwvnx4wHm0mHCbol3M=\n-----END PRIVATE KEY-----\n",
  "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
  "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
  "auth_uri": os.environ.get("FIREBASE_AUTH_URI"),
  "token_uri": os.environ.get("FIREBASE_TOKEN_URI"),
  "auth_provider_x509_cert_url": os.environ.get("FIREBASE_AUTH_CERT_URL"),
  "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_CERT_URL")
}

cred = credentials.Certificate(key)
default_app = initialize_app(cred, {'storageBucket':'stocktrading-14119.appspot.com'})
bucket = storage.bucket()
db = firestore.client()

# fileName = './report.docx'
# blob = bucket.blob('files/report.docx')
# blob.upload_from_filename(fileName)

# blob.make_public()

# print("your file url:", blob.public_url)



