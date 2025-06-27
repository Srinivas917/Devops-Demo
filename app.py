from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello, {os.getenv('NAME','WORLD')}.<br>{os.getenv('NAME','WORLD')}, Everything is working fine. You can go on..."
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 80)
