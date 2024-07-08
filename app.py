from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return "this is custom flask app"

if __name__ == "__main__":
    app.run()