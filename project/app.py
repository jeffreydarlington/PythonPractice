from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/message", methods=["POST"])
def message():
    data = request.get_json()
    user_text = data.get("text", "")
    return jsonify({"reply": f"You said: {user_text}"})

if __name__ == "__main__":
    app.run(debug=True)
