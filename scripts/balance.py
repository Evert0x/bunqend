from bunq.sdk.context import ApiContext, BunqContext

with open('bunq.conf', 'r') as content_file:
    content = content_file.read()
    api = ApiContext.from_json(content)

BunqContext.load_api_context(api)


print(BunqContext.user_context().primary_monetary_account.balance.value)