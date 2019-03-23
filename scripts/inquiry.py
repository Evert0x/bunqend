from bunq.sdk.context import ApiContext, BunqContext
from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated.object_ import Pointer, Amount, NotificationFilter

with open('bunq.conf', 'r') as content_file:
    content = content_file.read()
    api = ApiContext.from_json(content)

BunqContext.load_api_context(api)


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

def make_bulk_request():
    endpoint.RequestInquiryBatch.create(

    )

make_request("500", "hehe", "+31641677353")