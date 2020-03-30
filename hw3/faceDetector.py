import numpy as np
import cv2 
import paho.mqtt.client as mqtt
import os
import time

MQTT_HOST="169.54.0.2" # docker ip address of the broker
MQTT_PORT=1883
MQTT_TOPIC="hw3"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc))) 
    client.subscribe(LOCAL_MQTT_TOPIC)

mqttclient=mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(MQTT_HOST,MQTT_PORT,60)

face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)

while(True):

    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        face = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
        print("face detected ",face.shape,face.dtype)
        rc,png = cv2.imencode(".png",face)
        msg = png.tobytes()
        mqttclient.publish(MQTT_TOPIC,payload=msg,qos=2,retain=False)
    
# release the capture
cap.release()
cv2.destroyAllWindows()
mqttclient.disconnect()