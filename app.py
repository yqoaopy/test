from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, this is a demo with a vulnerable Flask version!123"

if __name__ == '__main__':
    app.run(debug=True)
