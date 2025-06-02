from curl_cffi.requests import AsyncSession
from .openai import get_openai_response
from utils.requests_headers_utils import calculate_nonce, create_x_super_properties
from data.settings import ATTEMPTS
import random
import asyncio
from utils.logger import logger


class DiscordClient:
    def __init__(self, proxy, settings: dict):
        self.server_id = settings['server_id']
        self.channel_id = settings['channel_id']
        self.sleep_duration = settings['sleep_duration']
        self.proxy = proxy
        self.settings = settings
        self.session = AsyncSession()
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,zh-TW;q=0.6,zh;q=0.5',
            'authorization': settings['discord_token'],
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'priority': 'u=1, i',
            'referer': f'https://discord.com/channels/{self.server_id}/{self.channel_id}',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Etc/GMT-2',
            'x-super-properties': create_x_super_properties(),
        }


    async def get_chat_messages(self):
        url = f'https://discord.com/api/v9/channels/{self.channel_id}/messages?limit=50'


    async def send_message(self, message):
        for retry in range(ATTEMPTS):
            try:
                url = f'https://discord.com/api/v9/channels/{self.channel_id}/messages'

                data = {
                    'content': message, 
                    'flags': 0,
                    'mobile_network_type': 'unknown',
                    'nonce': calculate_nonce(),
                    'tts': False
                }

            except Exception as e:
                random_sleep = random.randint(self.sleep_duration[0], self.sleep_duration[1])


    async def reply_message(self):
        pass


    async def request_to_openai(self):
        pass