from flask import render_template

def init_app(app):
    @app.route("/")
    def index():
        universo = "marvel"
        heroi = "capitao"
        return render_template("index.html", **locals())