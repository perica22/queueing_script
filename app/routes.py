from app import APP
from app import R
from app import Q

from flask import request

from app.tasks import background_task


@APP.route("/task", methods=["POST"])
def add_task():
    request_json = request.get_json()
    if request_json:

        job = Q.enqueue(background_task, request_json)
        q_len = len(Q)
        return f"Task ({job.id}) added to queue at {job.enqueued_at}, queue size is {q_len}"

    return "No value for count provided"
