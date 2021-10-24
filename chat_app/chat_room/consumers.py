import json
from channels.generic.websocket import AsyncWebsocketConsumer
#from .models import ChatModel
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Layer is to be created
        self.email = self.scope['url_route']['kwargs']['email']
        self.email_name = 'chat_' + str(self.email)
        await self.channel_layer.group_add(self.email_name, self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(self.email_name, self.channel_name)

    @database_sync_to_async
    def save_to_db(self, message):
        ChatModel(room_no=self.email, message=message).save()

    async def receive(self, text_data):
        test_data_json = json.loads(text_data)
        message = test_data_json['message']
        # await sync_to_async(ChatModel(room_no=self.room_name, message=message).save())
        # await self.save_to_db(message)
        await self.channel_layer.group_send(self.email_name, {
            'type' : 'send_back',
            'message': message
        })
    
    async def send_back(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
    