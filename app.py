from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Containerized Application Running Successfully"

@app.route("/health")
def health():
    return "healthy"

@app.route("/version")
def version():
    return "1.0"
 
def calculate():
    return 10 + 20

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
