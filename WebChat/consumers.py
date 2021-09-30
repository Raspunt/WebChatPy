import json
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer



class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        print("За конектился")

        await self.send(text_data=json.dumps({
            'message': "update text aga"
        }))


    async def disconnect(self, code):
        print("вышел")

    async def receive(self, text_data=None):
        
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))


    async def send_message(self,text):

        await self.send(text_data=json.dumps({
            'message': text
        }))

    

    