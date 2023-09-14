#! /usr/bin/env python3

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/sendData")
async def read_item(request: Request):
    data = await request.json()
    print(data)
    return {"status": "ok"}



""" from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sendData', methods=['POST'])
def send_data():
    data = request.json
    print(data)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=5000)
 """