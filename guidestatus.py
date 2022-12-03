from pypresence import Presence
import time

#in terminal write pip install pypresence
#go to the discord developer portal and create bot, than go to the "Rich Presence" in it go to the "Art Assets" and add images
#you can also go to the "Visualizer" and see what the status can be

RPC = Presence('bot id')
RPC.connect()#connecting
print('connected')

#buttons
buttons = [
    {
        'label': 'your label',
        'url': 'your url'
    },
    {
        'label': 'your label',
        'url': 'your url'
    }
]

#status
RPC.update(
    state='your state',
    details='your details',
    start=time.time(),#it's time
    large_image='your name of image in discord developer portal',
    large_text='your text',
    small_image='your name of image in discord developer portal',
    small_text='your text',
    buttons='buttons'
)

while True:
    time.sleep(15)