import redis
from flask import Flask
from rq import Queue


APP = Flask(__name__)
R = redis.Redis()
Q = Queue(connection=R)

from app import routes
from app import tasks
