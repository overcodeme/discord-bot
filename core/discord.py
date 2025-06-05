import aiohttp
from .gpt import get_openai_response
from utils.requests_headers_utils import calculate_nonce, create_x_super_properties
from data.settings import ATTEMPTS
import random
import asyncio
from utils.logger import logger


class DiscordClient:
    def __init__(self, account_idx, proxy, settings: dict):
        self.account_idx = account_idx
        self.system_prompt = settings['system_prompt']
        self.prompt = settings['prompt']
        self.server_id = settings['server_id']
        self.channel_id = settings['channel_id']
        self.delay_between_actions = settings['delay_between_actions']
        self.delay_between_messages = settings['delay_between_messages']
        self.reply_chance = settings['reply_chance']
        self.proxy = proxy
        self.settings = settings
        self.session = aiohttp.ClientSession()
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


    async def get_channel_messages(self):
        url = f'https://discord.com/api/v9/channels/{self.channel_id}/messages?limit=50'

        for retry in range(ATTEMPTS):
            try:
                async with self.session.get(url=url, headers=self.headers, proxy=self.proxy) as response:
                    if response.status == 200:
                        logger.success(self.account_idx, 'Successfully got channel messages')
                        data = await response.json()
                        return data
                    else:
                        raise Exception(response.text)
            except Exception as e:
                random_sleep = random.randint(self.delay_between_actions[0], self.delay_between_actions[1])
                logger.error(self.account_idx, f'Error while getting channel messages: {e}. Retrying in {random_sleep} sec...')
                await asyncio.sleep(random_sleep)


    async def send_message(self):
        is_reply = (random.random() * 100) >= self.reply_chance
        message = ''
        data = {}

        if is_reply:
            channel_messages = await self.get_channel_messages()
            random_message = channel_messages[random.randint(0, 49)]
            prompt, message_id = random_message['content'], random_message['id']
            message = get_openai_response(self.account_idx, system_prompt=self.system_prompt, prompt=prompt)

            data = {
                'content': message,
                'flags': 0,
                'message_reference': {
                    'channel_id': self.channel_id,
                    'guild_id': self.server_id,
                    'message_id': message_id
                },
                'mobile_network_type': 'unknown',
                'nonce': calculate_nonce(),
                'tts': False
            }

        else:
            message = get_openai_response(account_idx=self.account_idx, system_prompt=self.system_prompt, prompt=self.prompt)
            data = {
                'content': message,
                'flags': 0,
                'mobile_network_type': 'unknown',
                'nonce': calculate_nonce(),
                'tts': False
            }

        for retry in range(ATTEMPTS):
            try:
                url = f'https://discord.com/api/v9/channels/{self.channel_id}/messages'

                print(type(self.proxy))

                async with self.session.post(url=url, headers=self.headers, json=data, proxy=self.proxy) as response:
                    if response.status == 200:
                        logger.success(self.account_idx, f'Message "{message}" sent successfully.')
                        random_sleep = random.randint(self.delay_between_messages[0], self.delay_between_messages[1])
                        logger.info(self.account_idx, f'Sleeping for {random_sleep} before next message...')
                        await asyncio.sleep(random_sleep)
                    else:
                        raise Exception(response.text)

            except Exception as e:
                random_sleep = random.randint(self.delay_between_actions[0], self.delay_between_actions[1])
                logger.error(self.account_idx, f'Error while sending message: {e}. Retrying in {random_sleep} seconds...')
                await asyncio.sleep(random_sleep)
