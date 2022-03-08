import logging
import json
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from raw_data import ORDERS_JSON
from data import Test_JSON

FORMAT = "%Y%m%d_%H:%M:%S"

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")
app = Flask(__name__)
auth = HTTPBasicAuth()
users = {"bpi": generate_password_hash("coe"), }


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@app.route("/secret")
@auth.login_required
def secret():
    return f"Hello {auth.current_user()}"


@app.route("/")
def main():
    return "Welcome 💻"


@app.route("/orders")
@auth.login_required
def orders():
    return jsonify(ORDERS_JSON)

@app.route("/test")
@auth.login_required
def test():
    return jsonify(Test_JSON)

if __name__ == '__main__':
    app.run(debug=True)
