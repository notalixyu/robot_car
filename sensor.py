import RPi.GPIO as GPIO
import time

#GPIO pins for ultrasonic Sensor
TRIG = 17  #GPIO 17 (Pin 11)
ECHO = 27  #Pin 27 (Reserved, to ensure it's usable)

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    #measures the distance using HC-SR04 ultrasonic sensor
    #send 10 pulse to trigger pin
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    #wait for echo to start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    #wait for echo to end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
