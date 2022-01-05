from flask import Flask
import numpu as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/numpy')
def randMatrix():
    return np.random.rand(5,5)

if __name__ == '__main__':
    app.run()
