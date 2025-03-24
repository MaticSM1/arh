from flask import Flask, Response
import cv2

app = Flask(__name__)

@app.route('/slika')
def slika():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        _, img_encoded = cv2.imencode('.jpg', frame)
        return Response(img_encoded.tobytes(), mimetype='image/jpeg')
    
    return "Napaka! zajemu slike neuspeh", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
