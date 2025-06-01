from curl_cffi.requests import AsyncSession
from .openai import get_openai_response
import random
import asyncio


class DiscordClient:
    def __init__(self, proxy, settings: dict):
        self.channel_id = settings['channel_id']
        self.chat_id = settings['chat_id']
        self.sleep_duration = settings['sleep_duration']
        self.proxy = proxy
        self.settings = settings
        self.session = AsyncSession()
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,zh-TW;q=0.6,zh;q=0.5',
            'authorization': settings['token'],
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'priority': 'u=1, i',
            'referer': f'https://discord.com/channels/{self.channel_id}',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
        }


    async def get_message_details(self, message):
        pass


    async def get_chat_messages(self):
        url = f'https://discord.com/api/v9/channels/{self.chat_id}/messages?limit=50'


    async def send_message(self):
        url = f'https://discord.com/api/v9/channels/{self.chat_id}/messages'
        content = ''

        data = {
            'content': content, 
            'flags': 0,
            'mobile_network_type': 'unknown',
            'nonce': '',
            'tts': False
        }


    async def reply_message(self):
        pass


    async def request_to_openai(self):
        pass