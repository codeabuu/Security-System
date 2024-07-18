import cv2 as cv
import numpy as np
import threading
import datetime
from storage import handle_detection

class Camera:
    '''Load pre-trained model'''
    net = cv.dnn.readNetFromCaffe('models/config.txt', 'models/mobilenet_iter_73000.caffemodel')
    
    cap = cv.VideoCapture(0)
    out = None

    def __init__(self):
        self.armed = False
        self.camera_thread = None

    def arm(self):
        '''Start the camera thread if it is not already armed and not running
        '''
        if not self.armed and not self.camera_thread:
            self.camera_thread = threading.Thread(target=self.run)
        
        self.camera_thread.start()
        self.armed = True
        print("Camera is armed!!")

    def disarm(self):
        self.armed = False
        self.camera_thread = None

    def run(self):
        person_detected = False
        non_detected_counter = 0
        current_recording_name = None

        # Reinitialize the video capture object to ensure it's ready
        Camera.cap = cv.VideoCapture(0)
        print("Camera Succefully Started..")

        while self.armed:
            # Capture frame-by-frame
            _, frame = self.cap.read()

            # Convert the frame to a blob suitable for neural network input
            blob = cv.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
            self.net.setInput(blob)
            detections = self.net.forward()
            person_detected = False

            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]

                idx = int(detections[0, 0, i, 1])

                #check if detections is of a person and it's confidence is greater than the minimum confidence
                if idx == 15 and confidence > 0.5:
                    box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                    (startX, startY, endX, endY) = box.astype("int")
                    cv.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    person_detected = True


                if person_detected:
                    non_detected_counter = 0
                    if self.out is None:
                        now = datetime.datetime.now()
                        formatted_now = now.strftime("%d-%m-%y-%H-%M-%S")
                        print("Person motion detected at", formatted_now)
                        current_recording_name = f'{formatted_now}.mp4'
                        fourcc = cv.VideoWriter_fourcc(*'mp4')
                        self.out = cv.VideoWriter(current_recording_name, fourcc, 20.0, (frame.shape[1], frame.shape[0]))

                    self.out.write(frame)

                else:
                    non_detected_counter += 1
                    if non_detected_counter >= 50:
                        if self.out is not None:
                            self.out.release()
                            self.out = None
                            handle_detection(current_recording_name)
                            current_recording_name = None

        if self.out is not None:
            self.out.release()  # Release the video writer object
            self.out = None
            handle_detection(current_recording_name)
            current_recording_name = None

        self.cap.release()
        print('Camera released..')

    def _del_(self):
        self.cap.release()
        if self.out is not None:
            self.out.release()