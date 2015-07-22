import extract
from flask import Flask, request, render_template

orbit= Flask (__name__)

temp = extract.extract_labels()
@orbit.route("/", methods=["POST", "GET"])

def census_taker():
    if request.method == "GET":
        return render_template("base.html", galaxy= "Nothing yet", label= temp)
    elif request.method == "POST":
        tracking= request.form["Select_galaxies"]
        d= extract.select_galax(tracking)
        return render_template("answer.html", galaxy= "Galaxies", answer= float(d), label= temp)

if __name__ == "__main__":

    orbit.debug= True
    orbit.run(host= '0.0.0.0', port= 12345)

