#!python3
"""
Python 3 wrapper for identifying objects in images with yolo.tiny and OpenCV
"""
import cvlib as cv
from cvlib.object_detection import YOLO
import cv2
import sys

weights = sys.argv[1]
config = sys.argv[2]
labels = sys.argv[3]
GSTREAMER_PIPELINE = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=21/1 ! nvvidconv flip-method=0 ! video/x-raw, width=960, height=616, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink'
# open webcam
webcam = cv2.VideoCapture(GSTREAMER_PIPELINE, cv2.CAP_GSTREAMER)
if not webcam.isOpened():
    print("Could not open webcam")
    exit()
yolo = YOLO(weights, config, labels)
# loop through frames
while webcam.isOpened():
    # read frame from webcam 
    status, frame = webcam.read()
    if not status:
        print("Could not read frame")
        exit()
    # apply object detection
    bbox, label, conf = yolo.detect_objects(frame)
    print(bbox, label, conf)
    # draw bounding box over detected objects
    yolo.draw_bbox(frame, bbox, label, conf, write_conf=True)
    # display output
    cv2.imshow("Real-time object detection", frame)
    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# release resources
webcam.release()
cv2.destroyAllWindows()  
