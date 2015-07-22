import API 
from flask import Flask, request, render_template

census= Flask (__name__)

@census.route("/", methods=["POST", "GET"])

def census_taker():

    d= API.extract(tracking)




