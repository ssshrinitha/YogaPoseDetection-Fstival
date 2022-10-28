import mimetypes
from flask import Flask, render_template, Response
# from prometheus_client import CONTENT_TYPE_LATEST
from camera import Video
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')   

def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'

@app.route('/video')
def video():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Video()),
                    mimetype ='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
   app.run(debug=True)