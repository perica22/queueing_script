# importing the queue module
#import queue
import time

import redis
from flask import Flask, request
from rq import Queue


APP = Flask(__name__)
r = redis.Redis()
q = Queue(connection=r)
#q = queue.Queue()


def background_task(n):
    """
    Function that returns len(n) and simulates a delay
    """
    delay = 2

    print("Task running")
    print(f"Simulating a {delay} second delay")

    time.sleep(delay)

    print(len(n))
    print("Task complete")

    return len(n)

@APP.route("/task", methods=["POST"])
def index():
    request_json = request.get_json()
    if request_json:

        job = q.enqueue(background_task, request_json)
        q_len = len(q)
        return f"Task ({job.id}) added to queue at {job.enqueued_at}, queue size is {q_len}"

    return "No value for count provided"


if __name__ == "__main__":
    APP.run()
