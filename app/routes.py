import json

from app import APP
from app import R
from app import Q

from flask import request, jsonify, make_response

from app.tasks import background_task
from app.register_service import RegisterService


@APP.route("/register", methods=["POST"])
def register():
    request_json = request.get_json()

    register_service = RegisterService(payload=request_json)

    errors = register_service.validate_user()
    if errors:
        return jsonify({"errors": errors}), 400

    user = register_service.create()

    result = register_service.create_response()
    job = Q.enqueue(background_task, result)
    print(f"Task ({job.id}) added to queue at {job.enqueued_at}, queue size is {len(Q)}")

    response = make_response(json.dumps(result), 200)
    response.mimetype = "application/json"

    return response
