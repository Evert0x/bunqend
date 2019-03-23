from bunq.sdk.context import ApiContext, BunqContext
from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated.object_ import Pointer, Amount, NotificationFilter
from flask import Flask
from flask import request
import json
from flask_cors import CORS
from flask import jsonify
app = Flask(__name__)
CORS(app)

def make_request(amount_string, description, recipient):
    """
    :type amount_string: str
    :type description: str
    :type recipient: str
    """

    endpoint.RequestInquiry.create(
        amount_inquired=Amount(amount_string, "EUR"),
        counterparty_alias=Pointer("PHONE_NUMBER", recipient),
        description=description,
        allow_bunqme=True
    )

#   curl -X POST \
#   https://82d8fd4a.ngrok.io \
#   -H 'Content-Type: application/json' \
#   -d '{
#       "+31658578688": 12.00
#   }'

@app.route('/', methods=["POST"])
def hello_world():
    data = json.loads(request.data)
    for k,v in data.items():
        money = str(round(float(v), 2))
        phone = str(k).replace(" ", "")
        make_request(money, "Sugar Split", phone)
    return 'Hello World!'

@app.route('/image', methods=["POST"])
def image():
    print("Do machine learning stuff")
    return jsonify({
        "Zwarte bonen": 2.68,
        "Knoflook": 7.00,
        "Donuts": 3.32
    })


if __name__ == '__main__':
    with open('bunq.conf', 'r') as content_file:
        content = content_file.read()
        api = ApiContext.from_json(content)

    BunqContext.load_api_context(api)
    app.run()
