from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Web App_2"

app.run(host='0.0.0.0', port=5002, threaded=True, debug=True)