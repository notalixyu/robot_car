import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self, pinForward, pinBackward, pinControl):
        #initialise the motor with its GPIO pins and start pulse-width
        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.pinControl = pinControl

        GPIO.setup(self.pinForward, GPIO.OUT)
        GPIO.setup(self.pinBackward, GPIO.OUT)
        GPIO.setup(self.pinControl, GPIO.OUT)

        self.pwm_forward = GPIO.PWM(self.pinForward, 50)  #50Hz frequency
        self.pwm_backward = GPIO.PWM(self.pinBackward, 50)

        self.pwm_forward.start(0)  #start with 0% cycle
        self.pwm_backward.start(0)

        GPIO.output(self.pinControl, GPIO.HIGH)  #to enable motor

    def forward(self, pwm):
        #moves motor forward with set speed
        self.pwm_backward.ChangeDutyCycle(0)
        self.pwm_forward.ChangeDutyCycle(pwm)

    def backward(self, pwm):
        #moves motor backward with set speed
        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(pwm)

    def stop(self):
        #stops motor and clean up
        self.pwm_forward.stop()
        self.pwm_backward.stop()
        GPIO.output(self.pinForward, GPIO.LOW)
        GPIO.output(self.pinBackward, GPIO.LOW)

class motor_control:
    def __init__(self,
                 m1_pinForward=22, m1_pinBackward=24, m1_pinControl=4,
                 m2_pinForward=17, m2_pinBackward=27, m2_pinControl=23):
        self.motor_right = Motor(m1_pinForward, m1_pinBackward, m1_pinControl)
        self.motor_left = Motor(m2_pinForward, m2_pinBackward, m2_pinControl)

    def set_speed_direction(self, speed, direction):
        #sets speed and direction for both motors
        if direction >= 0:
            pwm_left = round(1 * speed * 100)
            pwm_right = round((1 - direction) * speed * 100)
        else:
            pwm_left = round((1 + direction) * speed * 100)
            pwm_right = round(1 * speed * 100)

        if speed >= 0:
            self.motor_left.forward(pwm_left)
            self.motor_right.forward(pwm_right)
        else:
            self.motor_left.backward(-1 * pwm_left)
            self.motor_right.backward(-1 * pwm_right)

    def stop(self):
        self.motor_left.stop()
        self.motor_right.stop()

if __name__ == "__main__":
    try:
        car_motor_control = motor_control()
        car_motor_control.set_speed_direction(1, 0)      #moves forward
        time.sleep(2)                                    #delay wait 2 seconds
        car_motor_control.set_speed_direction(1, -0.5)   #turns left
        time.sleep(2)
        car_motor_control.set_speed_direction(1, 0.5)    #turn rights
        time.sleep(2)
        car_motor_control.stop()                         #stops the motors
    finally:
        GPIO.cleanup()  #GPIO cleanup even if an error occurs