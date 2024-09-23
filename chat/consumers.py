import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from django.utils import timezone
from .models import ChatMessage
from courses.models import Course
from django.shortcuts import render, get_object_or_404

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # accept connection
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.id
        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # load previous messages
        previous_messages = await self.get_previous_messages()

        for message in previous_messages:
            await self.send(text_data=json.dumps(message))

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        # # send message to WebSocket
        # self.send(text_data=json.dumps({'message': message}))
        # send message to room group
        await self.save_message(message, now)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username, 
                'datetime': now.isoformat(),

            }
        )


    # receive message from room group
    async def chat_message(self, event):
        # send message to WebSocket
        await self.send(text_data=json.dumps(event))

    @sync_to_async
    def save_message(self, message, timestamp):
        course = Course.objects.get(id=self.id)
        ChatMessage.objects.create(
            sender= self.user,
            content= message,
            course = course,
            timestamp=timestamp
        )


    @sync_to_async
    def get_previous_messages(self):
        messages = ChatMessage.objects.filter(course=self.id).order_by('-timestamp')[:50][::-1]
        return [{'message':msg.content,'user':msg.sender.username, 'datetime':msg.timestamp.isoformat()} for msg in messages]
    
    
    async def message_to_json(message):
        return {
        'message': message.content,  # Accessing the 'message' attribute
        'user': message.sender.username,  # Accessing sender's username
        'datetime': message.timestamp.isoformat(),  # Accessing created_at attribute
    }