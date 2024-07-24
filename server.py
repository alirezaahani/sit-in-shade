from flask import Flask, request, jsonify, render_template
import requests
import base64
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bus-routing')
def bus_routing():
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    response = requests.get('https://neshan.org/maps/pwa-api/bus-routing/', params=dict(request.args), headers=headers)

    t = base64.b64decode(response.json()['data'])
    i = list(bytearray("https://rajman.org".encode('utf-8')))
    n = len(t)
    o = [0] * n

    for r in range(n):
        o[r] = t[r] ^ i[r % len(i)]

    data = bytearray(o).decode('utf-8')
    data = json.loads(data)

    return jsonify(data)