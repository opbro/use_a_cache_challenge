from flask import Flask, request, jsonify
import os
import logging
import time
import json

app = Flask(__name__)

with open('decoder.json') as _file:
    decoder = json.load(_file)

with open('encoded.txt') as _file:
    encoded_text = _file.read()

@app.route("/")
def index():
    app.logger.info(vars(request))
    return jsonify("Example Flask App")

@app.route("/tasking", methods=["GET"])
def tasking():
    d = dict()
    for key, value in request.args.items():
        app.logger.info("{}, {}".format(key, value))
        d[key] = value
    return jsonify(d)

@app.route('/challenge', methods=['GET'])
def challenge():
    return encoded_text

@app.route('/decode', methods=['GET'])
def decode():
    value = request.args.get('value')
    time.sleep(1)
    if value is None:
        return 'Error can\'t decode', 400
    answer = decoder.get(str(value))
    if answer is None:
        return 'Value [{}] doesn\'t exsist in decoder map'.format(value) , 400
    return answer, 200

if __name__ == "__main__":
    ip = os.environ.get('LISTEN_HOST', '0.0.0.0')
    port = os.environ.get('LISTEN_PORT', 8200)
    debug = os.environ.get('DEBUG', True)
    app.run(host=ip, port=port, debug=debug)