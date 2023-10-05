import suspengine as sgn
import json

iden = 0

def verify_id(client, _id):
    assert sgn.callvariable('id', client) == _id, f"No client with id {_id}"



@sgn.channel("connect")
def connect(c, addr):
    global iden
    sgn.savevariable('id', iden, c)
    sgn.emit("connect", {'id': int(iden)}, c)

    iden += 1


@sgn.channel("disconnect")
def disconnect(c, addr):
    print("Client with id :", sgn.callvariable('id', c), "disconnected from the server")


@sgn.channel("block")
def block(c, addr, data):
    print(f"Received block data {data}")
    headSetClientList = sgn.callvariablelist("role", "headset")
    for headSetClient in headSetClientList:
        sgn.emit("block", data, headSetClient)


@sgn.channel("user")
def user(c, addr, data):
    print(f"Received user data {data}")
    headSetClientList = sgn.callvariablelist("role", "headset")
    for headSetClient in headSetClientList:
        sgn.emit("user", data, headSetClient)



@sgn.channel("client_info")
def clientInfo(c, addr, data):
    print(f"Received client_info data {data}")

    if "role" not in data and "name" not in data:
        print("Invalid client_info data received")
    else:
        sgn.savevariable("role", data["role"], c)
        sgn.savevariable("name", data["name"], c)


@sgn.channel("message")
def message(c, addr, data):
    pass
