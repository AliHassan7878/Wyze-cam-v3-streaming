import cv2
import os
#connect through rtsp
cap = cv2.VideoCapture('rtsp://USERNAME:PASSWORD@CAM_IP/live')

if not cap.isOpened():
    print('Cannot open RTSP stream, check camera again')
    exit(-1)

while True:
    _, frame = cap.read()
    cv2.imshow('RTSP stream', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

