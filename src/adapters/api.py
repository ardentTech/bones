import logging
from uuid import uuid4

from flask import Flask, jsonify, request

from adapters.config import bus, todo_view_factory
from app.exceptions import TodoNotFoundError
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


@app.route("/v1/todos/<todo_id>", methods=["GET"])
def todo(todo_id):
    try:
        return jsonify(todo_view_factory(todo_id))
    except TodoNotFoundError as e:
        return not_found(e)


@app.route("/v1/todos", methods=["GET", "POST"])
def todos():
    if request.method == "GET":
        return jsonify(todo_view_factory())
    else:
        # @todo request level validation
        cmd = NewTodoCommand(uid=str(uuid4()), **request.get_json())
        try:
            bus.handle(cmd)
        except ValidationError as e:
            return jsonify(e.errors), 400
        else:
            return "", 201, {"Location": "/v1/todos/" + str(cmd.uid)}
