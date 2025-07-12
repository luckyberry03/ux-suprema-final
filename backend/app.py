from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "running", "message": "Welcome to ux-suprema-final"})

@app.route('/api/halo')
def halo():
    return jsonify({"pesan": "Halo dari ux-suprema-final!"})

@app.route('/api/data', methods=['POST'])
def data():
    return jsonify({"data_dikirim": request.get_json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
