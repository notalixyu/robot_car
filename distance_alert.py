import RPi.GPIO as GPIO
import time

# Define GPIO pins
TRIG = 23
ECHO = 24

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#measure distance with GPIO outputs
def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
#pulses echo statement
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    duration = pulse_end - pulse_start
    distance = (duration * 34300) / 2  #convert to cm

    return distance


try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance:.2f} cm")

#if distance detected will print something is detected
        if distance < 15:
            print("Object detected! Triggering alert...")
            #can trigger an alert via flask

        time.sleep(1)

#after system sleeps will stop
except KeyboardInterrupt:
    print("Measurement stopped.")
    GPIO.cleanup()
