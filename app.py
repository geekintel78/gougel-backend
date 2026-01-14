from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Gougel backend is running"

@app.route("/search")
def search():
    q = request.args.get("q", "").lower()

    data = [
        {"title": "The Beatles - Hey Jude", "score": 1.42},
        {"title": "The Beatles - Yesterday", "score": 1.31},
        {"title": "The Rolling Stones - Satisfaction", "score": 1.10},
    ]

    results = [d for d in data if q in d["title"].lower()]
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

