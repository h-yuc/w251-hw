import cv2
import sys
import os
import time
import urllib
import paho.mqtt.client as mqtt
import tensorflow.contrib.tensorrt as trt
import tensorflow as tf
import numpy as np

cap = cv2.VideoCapture(1)
fps = int(cap.get(cv2.CAP_PROP_FPS))

FROZEN_GRAPH_NAME = 'data/frozen_inference_graph_face.pb'
INPUT_NAME = 'image_tensor'
BOXES_NAME = 'detection_boxes'
CLASSES_NAME = 'detection_classes'
SCORES_NAME = 'detection_scores'
MASKS_NAME = 'detection_masks'
NUM_DETECTIONS_NAME = 'num_detections'
DETECTION_THRESHOLD = 0


input_names = [INPUT_NAME]
output_names = [BOXES_NAME, CLASSES_NAME, SCORES_NAME, NUM_DETECTIONS_NAME]

# Load the frozen graph
output_dir = ''
frozen_graph = tf.GraphDef()
with open(os.path.join(output_dir, FROZEN_GRAPH_NAME), 'rb') as f:
    frozen_graph.ParseFromString(f.read())

# Optimize the frozen graph using TensorRT
trt_graph = trt.create_inference_graph(
    input_graph_def=frozen_graph,
    outputs=output_names,
    max_batch_size=1,
    max_workspace_size_bytes=1 << 25,
    precision_mode='FP16',
    minimum_segment_size=50
)

# Create session and load graph
tf_config = tf.ConfigProto()
tf_config.gpu_options.allow_growth = True
tf_sess = tf.Session(config=tf_config)

tf.import_graph_def(frozen_graph, name='')
tf_input = tf_sess.graph.get_tensor_by_name(input_names[0] + ':0')
tf_scores = tf_sess.graph.get_tensor_by_name('detection_scores:0')
tf_boxes = tf_sess.graph.get_tensor_by_name('detection_boxes:0')
tf_classes = tf_sess.graph.get_tensor_by_name('detection_classes:0')
tf_num_detections = tf_sess.graph.get_tensor_by_name('num_detections:0')

# OpenCV CascadeClassifier
# Downloaded from 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
is_load = face_cascade.load('haarcascade_frontalface_default.xml')

if is_load:
    print('Load haarcascades successfully')
else:
    print('Fail to load haarcascades')

LOCAL_MQTT_BROKER = "mqtt_broker"
LOCAL_MQTT_TOPIC = "hw3/topic"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connect to broker")
    else:
        print("Failed to connect to broker")

# Connect to broker
client = mqtt.Client()
client.connect(LOCAL_MQTT_BROKER, 1883, 60)
client.on_connect = on_connect
client.loop_start()

count = 0
while 1:
    ret, frame = cap.read()

    t = time.time()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    print('Face detection %f sec' % float(time.time() - t))

    # Resize image
    t1 = time.time()
    img = cv2.resize(frame, (300, 300), interpolation=cv2.INTER_AREA)
    img = np.array(img)
    print('Image resize %f sec' % float(time.time() - t1))

    # Run network on image
    t2 = time.time()
    scores, boxes, classes, num_detections = tf_sess.run([tf_scores, tf_boxes, tf_classes, tf_num_detections],
                                                         feed_dict={tf_input: img[None, ...]
                                                         })

    boxes = boxes[0]  
    scores = scores[0]
    classes = classes[0]
    num_detections = num_detections[0]
    print('Face detection  %f sec' % float(time.time() - t2)

    for i in range(int(num_detections)):
        if scores[i] >= DETECTION_THRESHOLD:
            box = boxes[i] * np.array([frame.shape[0], frame.shape[1], frame.shape[0], frame.shape[1]])
            cv2.rectangle(frame, (int(box[1]), int(box[0])), (int(box[3]), int(box[2])), (255, 0, 0), 2)
            face_detected = frame[int(box[0]):int(box[2]), int(box[1]):int(box[3])]
            rc, png = cv2.imencode('.png', face_detected)

            # Publish message
            try:
                client.publish(LOCAL_MQTT_TOPIC, png.tobytes())
            except:
                print('No connection')

    count += 1
    # Waits for a user input to quit the application
    if cv2.waitKey(30) & 0xFF == 27:
        break

client.disconnect()
tf_sess.close()

# Release capture
cap.release()
cv2.destroyAllWindows()