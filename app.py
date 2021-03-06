from flask import Flask, render_template
from imageresizer import bp_imgrsz
from ankets import bp_ankets


app = Flask(__name__)
app.register_blueprint(bp_imgrsz, url_prefix="/image/resizer")
app.register_blueprint(bp_ankets, url_prefix="/ankets")


@app.route("/")
def index():
    cntx = {
        "title":"W2Project"
    }
    return render_template("index.html", cnt=cntx)

@app.route("/ua")
def user_actions():
    cntx = {
        "title":"Login or Register"
    }
    return render_template("ua.html", cnt=cntx)

@app.route("/ma")
def manage_applications():
    cntx = {
        "title":"Manage Applications"
    }
    return render_template("ma.html", cnt=cntx)


if __name__ == "__main__":
    app.run(debug=False)