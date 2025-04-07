import motor_control as motor
import sensor  #import HC-SR04 sensor

def main():
    try:
        #get distance in cm
        while True:
            distance = sensor.get_distance()
            print(f"Distance: {distance} cm")

#detectes obstacle
            if distance < 15:
                print("Obstacle detected! Stopping car.")
                motor.stop()

#if no obstacle detected car keeps moving
            else:
                print("No obstacle. Moving forward.")
                motor.move_forward(5)

            time.sleep(1)

    except KeyboardInterrupt:
        print("Program interrupted.")

#after finishing cleans up GPIO
    finally:
        print("Cleaning up GPIO...")
        motor.cleanup()
        GPIO.cleanup()

if __name__ == "__main__":
    main()