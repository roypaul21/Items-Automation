from flask import Blueprint, render_template, request,  redirect, url_for
from website.models.model import Item

homeBP = Blueprint("home", __name__)

@homeBP.route("/", methods=["POST", "GET"])
def homePage():
    item_list = Item.allItems()
    for item_tuple in item_list:
        for item in item_tuple:
            print(item)
   
    return render_template("home.html", item_list = item_list)


@homeBP.route("/addItem", methods=["POST", "GET"])
def addItem():
    if request.method == "POST":
        itemName = request.form["item"]
        Item.insertItem(itemName)
        return render_template("home.html")
    

@homeBP.route("/itemList", methods=["POST", "GET"])
def itemList():
    if request.method == "POST":
        itemcheck = request.form.getlist("mycheckbox")

        #automate the following items
        if request.form['action'] == "automate":
            print(f"Start Automate {itemcheck}")
        
        #remove the following items
        elif request.form['action'] == "remove":
             print(f" Remove {itemcheck}")

        return render_template("home.html")

