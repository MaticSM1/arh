from flask import Flask, render_template_string
import requests
import base64
import threading
import time

app = Flask(__name__)
slika_base64 = None 


def osvezi_sliko():
    global slika_base64
    while True:
        try:
            response = requests.get('http://streznik:3000/slika')
            if response.status_code == 200:
                slika_base64 = base64.b64encode(response.content).decode('utf-8')
        except Exception as e:
            print(f"Napaka! ni slike: {e}")
        
        time.sleep(10)


@app.route('/')
def prikazi_sliko():
    if slika_base64:
        return render_template_string(f'''
            <h2>Slika:</h2>
            <img src="data:image/jpeg;base64,{slika_base64}" width="600">
        ''')
    return "Slike nini"


if __name__ == '__main__':
    threading.Thread(target=osvezi_sliko, daemon=True).start()  # asyinc
    app.run(host='0.0.0.0', port=3001)
