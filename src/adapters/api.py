from flask import Flask, jsonify, request

from adapters.config import bus
from adapters.views import TodoListView
from app.messages import NewTodoCommand

app = Flask(__name__)


@app.errorhandler(404)
def not_found(e):
    return "", 404


@app.route("/v1/health-check")
def health_check():
    resp = jsonify({"status": "available"})
    resp.headers["Cache-Control"] = "no-cache"
    return resp


@app.route("/v1/todos", methods=["GET", "POST"])
def todos():
    if request.method == "GET":
        return jsonify(TodoListView()())
    else:
        cmd = NewTodoCommand(**request.get_json())
        bus.handle(cmd)
        return "", 201
