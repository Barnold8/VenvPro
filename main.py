import setup
from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "<h1> VenvPro helped build this app! </h1>"

if __name__ == "__main__":
    app.run()