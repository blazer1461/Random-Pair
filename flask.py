import API 
from flask import Flask, request, render_template

census= Flask (__name__)

@census.route("/", methods=["POST", "GET"])

def census_taker():
    if request.method == "GET":
        return render_template("base.html", galaxy= "Nothing yet", label= label)
    elif request.method == "POST":
        tracking= request.form["Select_galaxies"]
        d= API.extract(tracking)
        return render_template("base.html", galaxy= label, answer= d)




