import eel, time, asyncio
from pypresence import Presence

RPC = None

@eel.expose
def connect_rpc(client_id):  
    global RPC   
    RPC = Presence(client_id)
    RPC.connect()
    
@eel.expose
def update(details, state, img_url, little_img):    

     RPC.update(
            state= state,
            details= details,
            large_image= img_url,
            small_image= little_img,
            start = int(time.time())
        )

@eel.expose
def disconnect_rpc(client_id): 
    RPC.close()

eel.init('interface')
eel.start('/main.html',size = (400,600), position = (400, 100))