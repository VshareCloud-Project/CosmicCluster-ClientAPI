import requests
from tools import request,calculate
import json
import configloader
c = configloader.config()
handler = request.request_handler()

source = c.getkey("client_id")
message = calculate.base64_encode("Hello World!")
message_id = calculate.genuuid()
destination = "3ed05db5-ea6c-4bd2-90f4-5160e5d27777"
data = {
    "message_id":message_id,
    "message":message,
    "source":source,
    "destination":destination,
}
ret = handler.post_request("/v0/west/addmessage",data)
data = {
    "message_id":message_id,
    "message":message,
    "source":source,
    "destination":destination,
}
ret = handler.post_request("/v0/west/getstatus",data)
print(ret)

data = {
    "messages":[
        {
            "message_id":calculate.genuuid(),
            "message":"test",
            "source":source,
            "destination":destination,
        },
        {
            "message_id":calculate.genuuid(),
            "message":"test",
            "source":source,
            "destination":destination,
        },
        {
            "message_id":calculate.genuuid(),
            "message":"test",
            "source":source,
            "destination":destination,
        },
        {
            "message_id":calculate.genuuid(),
            "message":"test",
            "source":source,
            "destination":destination,
        },
        {
            "message_id":calculate.genuuid(),
            "message":"test",
            "source":source,
            "destination":destination,
        }
    ]
}
ret = handler.post_request("/v0/west/addmessages",data)
print(ret)
ret = handler.post_request("/v0/west/getmultistatus",data)
print(ret)

