import eel, time, asyncio
from pypresence import Presence

RPC = None

@eel.expose
def connect_rpc(client_id):  
    global RPC   
    RPC = Presence(client_id)
    RPC.connect()
    
@eel.expose
def update(client_id, state, img_url):    

     RPC.update(
            state= state,
            large_image= img_url,
            # small_image= data["IMG_NAME"],
            start = int(time.time())
        )

@eel.expose
def disconnect_rpc(client_id): 
    RPC.close()

eel.init('interface')
eel.start('/main.html',size = (400,600), position = (400, 100))