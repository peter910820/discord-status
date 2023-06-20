from pypresence import Presence
import time

client_id = "1120361058729738250"
RPC = Presence(client_id)

RPC.connect()

RPC.update(
        state= f"正在玩迷霧列車",
        large_image= "cover",
        small_image = "cover",
        start = int(time.time())
    )


while True:
    time.sleep(60)