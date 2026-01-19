from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from rules import chatbot_reply

app = Flask(__name__)
CORS(app)  # Fix server errors due to cross-origin

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    message = data.get("message", "")
    reply = chatbot_reply(message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
