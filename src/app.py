from flask import Flask, render_template, jsonify
from system_info import get_system_info

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/stats")
def api_stats():
    return jsonify(get_system_info())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
