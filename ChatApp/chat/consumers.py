
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from pymongo import MongoClient

class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mongo_client = MongoClient('localhost', 27017)
        self.db = self.mongo_client.vijaydb
        self.collection = self.db.vijay

    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()
        
        #previous_messages = self.collection.find().sort("_id", -1).limit(10)
        previous_messages = self.collection.find().sort("_id", 1)
        for message in previous_messages:
            await self.send(text_data=json.dumps({
                "message":message["message"],
                "username":message["username"]
            }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        # Save message and username to MongoDB
        self.collection.insert_one({'message': message, 'username': username})

        # Broadcast the message to the group
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
            }  
        )

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_data=json.dumps({"message": message, "username": username}))

  
        