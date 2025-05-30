from aiohttp import ClientSession
from openai import OpenaiClient


class DiscordClient:
    def __init__(self, token, proxy, settings: dict):
        self.token = token
        self.proxy = proxy
        self.settings = settings
        self.session = ClientSession()