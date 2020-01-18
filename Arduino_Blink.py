import serial
import time

ser = serial.Serial('COM3', 9600)
from sklearn import svm

import speech_recognition as sr
r=sr.Recognizer()
from monkeylearn import MonkeyLearn
 
ml = MonkeyLearn('31bfede74537bd6c0d8b5d73f01ad4beaa1369d4')
model_id = 'cl_pi3C7JiL'
def led_on_off():
    
    print("How are you feeling today? ")
    """
    with sr.Microphone() as source:
        audio=r.listen(source)  
    try:
        ip=str(r.recognize_google(audio))
    except Exception:
        ip='-1'
    """
    ip=str(raw_input())
    if ip=='-1' or ip.lower()=='bye':
        print("Program Exiting")
        time.sleep(0.1)
        ser.write(b'L')
        ser.close()
    else:
        print(ip)
        json=ml.classifiers.classify(model_id, [ip]).body
        user_input=json[0]['classifications'][0]['tag_name']
        if user_input =='Positive':
            print("Positive!\n")
            time.sleep(0.1) 
            ser.write(b'H') 
            led_on_off()
        elif user_input =='Neutral':
            print("Neutral!\n")
            time.sleep(0.1) 
            ser.write(b'H') 
            led_on_off()
        elif user_input =='Negative':
            print("Negative!\n")
            time.sleep(0.1)
            ser.write(b'L')
            led_on_off()

time.sleep(2)

led_on_off()
        
