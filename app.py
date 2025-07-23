from flask import Flask
import redis
import socket

app = Flask(__name__)
redis_client = redis.Redis("redis", 6379, 0, decode_responses=True)
container_id = socket.gethostname()


@app.route("/")
def hello():
    visit_count = redis_client.incr("visit_count")
    return (
        "Hello world!<br>"
        f"This page has been visited {visit_count} times. <br>"
        f"Handled by container {container_id}"
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')