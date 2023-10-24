from flask import Blueprint, render_template, request, flash

homeBP = Blueprint("home", __name__)

@homeBP.route("/", methods=["POST", "GET"])
def homePage():
    if request.method == "POST":
        item = request.form["item"]
        print(item)
        return render_template("home.html")
    
    else:
        return render_template("home.html")


