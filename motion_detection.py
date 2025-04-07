import cv2
import numpy as np
import time
from flask import Flask, Response

app = Flask(__name__)

#initialise the camera
camera = cv2.VideoCapture(0)  #0 for pi camera

#initialise variables for motion detection
first_frame = None

#capture current frame from camera
def detect_motion():
    global first_frame
    while True:
        ret, frame = camera.read()
        if not ret:
            continue
#will skipp iteration if not detected
#converts frame to grayscale for simplifying process
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if first_frame is None:
#stores first frame as reference for motion detection
            first_frame = gray

#to flag if motion detected in this frame
        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) < 1000:  #ignores small movements
                continue

        if motion_detected:
            print("Motion Detected!")
            trigger_alert("Motion detected!")  #send alert to website

#trigger alerts
#function to handle alerts
#just prints alert messages to console
def trigger_alert(message):
    print(f"[ALERT] {message}")

#video feed when detected
#streams video when motion is detected
@app.route('/video_feed')
def video_feed():


#home route to confirm server is live
@app.route('/')
def index():
    return "Raspberry Pi Motion Detection Running..."

