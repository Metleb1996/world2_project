from flask import Blueprint, render_template


bp_ankets = Blueprint("__bp_ankets__", __name__, template_folder="../templates", static_folder='../static/', static_url_path="/")

@bp_ankets.route("")
def index():
    cntx = {
        "title":"Ankets"
    }
    return render_template("ankets/index.html", cnt=cntx)