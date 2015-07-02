import redis

from flask import Flask, jsonify


MAIN_KEY="main"
app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return jsonify(counter=r.incr(MAIN_KEY))


if __name__ == "__main__":
    r = redis.StrictRedis(host='192.168.59.103', port=6379, db=0)
    app.run()
