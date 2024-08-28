from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio

class StatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Simulate a long-running task and send status updates
        for i in range(10):
            await asyncio.sleep(1)
            await self.send(text_data=json.dumps({
                'status': f'Running {i+1}/10'
            }))
