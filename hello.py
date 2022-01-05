from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/numpy')
def randMatrix():
    x = np.random.rand(5,5)
    return np.array2string(x, precision=2, separator=',', suppress_small=True)

if __name__ == '__main__':
    app.run()
