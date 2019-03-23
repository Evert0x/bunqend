from bunq.sdk.context import ApiContext, BunqContext
from bunq.sdk.context import ApiEnvironmentType
import socket

apiContext = ApiContext(ApiEnvironmentType.SANDBOX, "sandbox_ae9afa8798dc521804bd1d8900167457243b9fd323e6799a9d42d75d",
                        socket.gethostname());
apiContext.save("bunq.conf")
BunqContext.load_api_context(apiContext)
