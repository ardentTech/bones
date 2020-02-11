import logging

from flask import Flask, jsonify, request

from adapters.config import bus, todo_list_view
from app.messages import NewTodoCommand
from domain.exceptions import ValidationError

app = Flask(__name__)
logger = logging.getLogger(__name__)


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
        return jsonify(todo_list_view())
    else:
        # @todo request level validation
        cmd = NewTodoCommand(**request.get_json())
        try:
            bus.handle(cmd)
        except ValidationError as e:
            return jsonify(e.errors), 400
        else:
            return "", 201
