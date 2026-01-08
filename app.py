from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Gougel Python backend is running 🚀"

@app.route("/search")
def search():
    query = request.args.get("q", "")
    return jsonify({
        "query": query,
        "results": [
            {"title": "The Beatles - Yesterday"},
            {"title": "The Beatles - Hey Jude"}
        ]
    })

if __name__ == "__main__":
    app.run()
