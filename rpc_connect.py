from pypresence import Presence
import json, os
import time

print([file_name for file_name in os.listdir("./config")])

use = input("choose a config file: ")

with open(f"./config/{use}.json",'r', encoding='utf8')  as f:
    data = json.loads(f.read())

client_id = data["CLIENT_ID"]
RPC = Presence(client_id)

RPC.connect()

RPC.update(
        state= data["STATE"],
        large_image= data["IMG_NAME"],
        small_image= data["IMG_NAME"],
        start = int(time.time())
    )

while True:
    time.sleep(60)