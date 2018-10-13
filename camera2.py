import cv2

# change 0 to 2
# 0 is for debugging purposes


class VideoCamera2(object):
    '''This is the feed from external camera.'''
    def __init__(self):
        # Using OpenCV to capture from device 2. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(1)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret2, frame2 = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        # return frame2

        gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        ret, jpeg = cv2.imencode('.jpg', gray)

        # gray = cv2.cvtColor(jpeg, cv2.COLOR_BGR2GRAY)

        return jpeg.tobytes()
