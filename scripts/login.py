from bunq.sdk.context import ApiContext, BunqContext

with open('bunq.conf', 'r') as content_file:
    content = content_file.read()
    api = ApiContext.from_json(content)

BunqContext.load_api_context(api)


print(BunqContext.user_context().user_person.alias[0].value)
print(BunqContext.user_context().user_person.alias[1].value)