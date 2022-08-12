from flask import Flask, jsonify
import requests

from csv2json import csv2json

app = Flask(__name__)
url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_malaysia.csv"

@app.route('/', methods=['get'])
def home():
    return jsonify({
        'ok': True,
        'status': 200,
        'result': csv2json(requests.get(url).text)
    })


if __name__ == '__main__':
    app.run(debug=True)