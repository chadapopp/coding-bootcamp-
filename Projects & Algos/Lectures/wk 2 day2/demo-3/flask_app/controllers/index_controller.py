from flask import redirect, render_template, request, send_from_directory, abort, jsonify, url_for
from flask_app import app
import os
import uuid

@app.route("/")
def index():
    return "<h1>This is / route.<br/> <a href='/my-gallery'>Goto Gallery</a>"