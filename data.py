from flask import Flask, jsonify
import json
import pandas as pd

url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_malaysia.csv"
df = pd.read_csv(url, usecols=[0, 1, 2, 4])
df2 = df.iloc[[-1]]
df3 = df2.to_json('df.json',orient='records')
buttom = df.tail(1)
concatenated = pd.concat([buttom])

app = Flask(__name__)
with open('df.json') as json_file:
    data = json.load(json_file)
resulte = data


@app.route('/', methods=['get'])
def home():
    return jsonify({'covid data': resulte})


if __name__ == '__main__':
    app.run(debug=True)