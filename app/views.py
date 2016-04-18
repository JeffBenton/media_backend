from flask import jsonify
from . import mod, mysql


@mod.route('/')
def index():
    data = mysql.fetch("SELECT * FROM users")
    return jsonify({"res": data})
