from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iotdemo-a28a8-default-rtdb.firebaseio.com/"
})

ref = db.reference()  # Reference to the root of your Firebase database

def sensor_insert(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        sensor_ref = ref.child('SENSOR')  # Reference to 'SENSOR' node in Firebase
        sensor_ref.update({key: value})
        return render(request, 'iot/success.html')  # Redirect to success page
    return render(request, 'iot/insert_sensor.html')

def user_insert(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        user_ref = ref.child('USER')  # Reference to 'USER' node in Firebase
        user_ref.update({key: value})
        return render(request, 'iot/success.html')  # Redirect to success page
    return render(request, 'iot/insert_user.html')


