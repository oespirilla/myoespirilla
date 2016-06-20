from flask import Flask, send_file, request, make_response, redirect
import logging

# Utility libaries
import os

app = Flask(__name__)

@app.route('/')
# @cross_origin()
def index():
    return send_file("index.html")
