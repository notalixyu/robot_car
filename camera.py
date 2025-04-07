import cv2

#camera capture area
camera = cv2.VideoCapture(0, cv2.CAP_V4L)

#while true if camera not read, it will fail to capture
while True:
    ret, frame = camera.read()
    if not ret:
        print(" Failed to capture image")
        break
#if true, will display camera test
    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()