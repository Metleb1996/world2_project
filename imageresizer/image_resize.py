from flask import Blueprint, render_template


bp_imgrsz = Blueprint("__bp_imgrsz__", __name__, template_folder="../templates", static_folder='../static/', static_url_path="/")

@bp_imgrsz.route("")
def index():
    return render_template("imageresizer/index.html")