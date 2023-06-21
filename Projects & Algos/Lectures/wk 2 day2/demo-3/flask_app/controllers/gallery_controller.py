from flask import redirect, render_template, request, send_from_directory, abort, jsonify, url_for, session
from flask_app import app
from flask_app.models.file import File
import os
import uuid

@app.route("/my-gallery")
def my_gallery():
    user_files = File.get_all(session["user_id"])
    return render_template("gallery/my-gallery.html", files = user_files)