from flask import Flask, send_file, request
from PIL import ImageGrab
from io import BytesIO
import ctypes

app = Flask(__name__)
user32 = ctypes.windll.user32

MOUSEEVENTF_LEFTDOWN = 2
MOUSEEVENTF_LEFTUP = 4

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/desktop.jpeg')
def desktop():
    screen = ImageGrab.grab()
    buf = BytesIO()
    screen.save(buf, 'JPEG', quality=90)
    buf.seek(0)
    return send_file(buf, mimetype='image/jpeg')


@app.route('/click')
def click():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
    except TypeError:
        return 'error: expecting 2 ints x and y'

    user32.SetCursorPos(x,y)
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    return 'done'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7080, debug=True)