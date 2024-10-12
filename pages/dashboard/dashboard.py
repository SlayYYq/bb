from flask import Blueprint, render_template
from util import auth

Dashboard = Blueprint("dashboard", __name__, template_folder="pages")

@Dashboard.route("/dashboard", methods=["GET"])
@auth.authenticated_required
def dashboard():
    return render_template("dashboard/dashboard.html")