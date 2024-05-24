import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iotdemo-a28a8-default-rtdb.firebaseio.com/"
})