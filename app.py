import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "localhost")

r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def index():
    count = r.incr("hits")

    return jsonify({
        "message": "Hello from Docker Compose",
        "visits": count
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)