from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Web App_3"

app.run(host='0.0.0.0', port=5003, threaded=True, debug=True)
