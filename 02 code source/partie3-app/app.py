from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Bienvenue dans notre application Cloud Computing !",
        "status": "Application is running"
    })

@app.route("/about")
def about():
    return jsonify({
        "project": "Mini Projet Cloud Computing",
        "technology": "Python Flask",
        "service": "API REST"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)