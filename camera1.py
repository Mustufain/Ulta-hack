import cv2
import numpy as np


class VideoCamera1(object):
    def __init__(self):
        # Using OpenCV to capture from device 1. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(1)
        self.threshold = 40
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
            ret, frame = self.video.read()
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

            # Our operations on the frame come here
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # # color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #
            # b_channel, g_channel, r_channel = cv2.split(frame)
            #
            # # creating a dummy alpha channel image.
            # alpha_channel = np.ones(
            #     b_channel.shape, dtype=b_channel.dtype) * 50
            #
            # img_BGRA = cv2.merge(
            #     (b_channel, g_channel, r_channel, alpha_channel))
            # # gray[gray < 200]
            # img_BGRA[gray > self.threshold, 0] = 0
            # # gray[gray < 200]
            # img_BGRA[gray > self.threshold, 1] = 0
            # # gray[gray < 200]
            # img_BGRA[gray > self.threshold, 2] = 255
            # # img_BGRA[gray < 240, 0] = gray[gray < 240]
            # return img_BGRA
