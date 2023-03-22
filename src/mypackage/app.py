from flask import Flask

app = Flask(__name__)

print("Runing Python script")
@app.route("/")
def home():
    return "Hello, World! CWT"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
