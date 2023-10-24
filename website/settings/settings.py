from flask import Blueprint, render_template, request, flash

settingsBP = Blueprint("settings", __name__)

@settingsBP.route("/settings")
def settingsPage():
    return render_template("settings.html")