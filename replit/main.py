from flask import Flask, jsonify, request
from threading import Thread

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "replit", "message": "Halo dari ux-suprema-final"})

@app.route("/api/halo")
def halo():
    return jsonify({"pesan": "Halo dari Replit - ux-suprema-final!"})

@app.route("/api/data", methods=["POST"])
def data():
    return jsonify({"data_dikirim": request.get_json()})

def run():
    app.run(host="0.0.0.0", port=3000)

Thread(target=run).start()
