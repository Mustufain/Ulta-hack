#!/usr/bin/env python

##############################
# Main app
##############################
#
# Starts the webserver to 0.0.0.0:5000 (0r 127.0.0.1:5000 in windows).
# Creates binds the python camera streams to html page using flask.
#

from flask import Flask, render_template, Response
from camera2 import VideoCamera2
from camera1 import VideoCamera1

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

# read data from camera 2 and yield it in correct format
def gen2(camera2):
    """Video streaming generator function."""
    while True:
        frame = camera2.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# read data from camera 1 and yield it in correct format
def gen1(camera1):
    """Video streaming generator function."""
    while True:
        frame = camera1.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# wrap camera 2 frames to a stream
@app.route('/video_feed_2')
def video_feed_2():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen2(VideoCamera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# wrap camera 1 frames to a stream
@app.route('/video_feed_1')
def video_feed_1():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen1(VideoCamera1()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
