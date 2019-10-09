import cv2
import numpy as np

class TrafficLight():
    def __init__(self):
        self.counter = 0
        self.state = True
    def turnRed(self, time):
        """

        :param time:
        :return:
        """
        self.state = False
        self.counter = time

    def turnGreen(self, time):
        self.state = True
        self.counter = time




class CountVehiclesInFrame():
    def __init__(self, detector_path = "cars.xml"):
        ## load vehicle detection classifier
        self.detector = cv2.CascadeClassifier(detector_path)

    def vehiclePositions(self, frame):
        """
        To find the position of all cars in image
        :param frame: a 3-channel image
        :return: positions of cars denoted by 4-tuple
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = self.detector.detectMultiScale(gray, 1.1, 1)
        return cars

    def showVideo(self, video_path = "video.mp4"):
        """
        streams a video and counts the number of cars in image
        :param video_path:
        :return: None
        """
        cap = cv2.VideoCapture(video_path)
        while True:
            ret, frames = cap.read()
            cars = self.vehiclePositions(frames)
            for (x, y, w, h) in cars:
                cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imshow('video2', frames)
            if cv2.waitKey(33) == 27:
                break
        cv2.destroyAllWindows()

def main():
    testing = CountVehiclesInFrame()
    testing.showVideo()

if  __name__ == "__main__":
    main()