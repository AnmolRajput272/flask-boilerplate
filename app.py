from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def hello():
    return "this is custom flask app"

if __name__ == "__main__":
    app.run()