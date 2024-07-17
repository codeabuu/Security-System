import cv2 as cv
import numpy as np
import threading
import datetime
from storage import handle_detection

class Camera:
    net = cv.dnn.readNetFromCaffe('models/config.txt', 'models/mobilenet_iter_73000.caffemodel')
    cap = cv.VideoCapture(0)
    out = None

    def __init__(self):
        self.armed = False
        self.camera_thread = None

    def arm(self):
        pass