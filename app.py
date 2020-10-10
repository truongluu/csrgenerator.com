#!/usr/bin/env python

import os

from flask import Flask, request, Response, render_template, jsonify

from csr import CsrGenerator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/security')
def security():
    return render_template('security.html')


@app.route('/generate', methods=['POST'])
def generate_csr():
    csr = CsrGenerator(request.form)
    return jsonify({"csr": csr.csr.decode('utf-8'), "private_key": csr.private_key.decode('utf-8')})


if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5555))
    app.run(host='0.0.0.0', port=port)
