import eel
import time

from pypresence import Presence

rpc = None
discord_img = 'https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png'


@eel.expose
def start_app():
    eel.init('interface')
    eel.start('/main.html', size=(600, 600), position=(400, 100))


@eel.expose
def connect_rpc(client_id):
    global rpc
    try:
        rpc = Presence(client_id)
        rpc.connect()
    except Exception as err:
        print(err)


@eel.expose
def update(deliver):
    try:
        empty_keys = [key for key, value in deliver.items() if not value]
        for e in empty_keys:
            match e:
                case 'details':
                    deliver['details'] = 'Test'
                case 'state':
                    deliver['state'] = None
                case 'img_url':
                    deliver['img_url'] = discord_img
                case 'little_img':
                    deliver['little_img'] = discord_img

        print(deliver)
        rpc.update(
            state=deliver['state'],
            details=deliver['details'],
            large_image=deliver['img_url'],
            small_image=deliver['little_img'],
            start=int(time.time())
        )
    except Exception as err:
        print(err)


@eel.expose
def disconnect_rpc():
    try:
        rpc.close()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    start_app()
