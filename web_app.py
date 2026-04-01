from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Smart Talent Selection Engine</h1><p>Project Running Successfully 🚀</p>"

if __name__ == "__main__":
    app.run(debug=True)