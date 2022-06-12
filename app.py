from distutils.log import debug
from urllib import response
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    source_amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    target_amount = fetch_conversion_amount(source_currency, source_amount, target_currency)
    # print(target_amount)

    response = {
            'fulfillmentText':"{} {} is {} {}".format(source_amount, source_currency, target_amount, target_currency)
    }
    return jsonify(response)

def fetch_conversion_amount(source_currency, source_amount, target_currency):
    url = "https://api.apilayer.com/currency_data/convert?to={}&from={}&amount={}".format(target_currency, 
            source_currency, source_amount)

    payload = {}
    headers= {
        "apikey": "RW7X9K13uyemQVh6L2nBqbxiqtC4I753"
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    result = response.json()
    return result['result']

if __name__ == "__main__":
    app.run(debug=True)

