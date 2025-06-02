import openai
from data.settings import OPENAI_KEY, PROXY_FOR_GPT_ASKING
import httpx
from utils.logger import logger
from colorama import Fore, Style


def get_openai_response(account_idx, system_prompt, prompt=None, replying_message=None):
    http_client = httpx.Client(proxy=PROXY_FOR_GPT_ASKING) 
    openai_client = openai.OpenAI(OPENAI_KEY, http_client=http_client)

    try:
        response = openai_client.completions.create(
            model='gpt-4o',
            messages = [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': replying_message if replying_message else prompt}
            ]
        )
        response_text = response['choices'][0]['message']['content']

        if 'Rate limit reached' in response_text:
            raise Exception('GPT rate limit reached, please try again later.')
        
        if 'You exceeded your current quota' in response_text:
            raise Exception('Your ChatGPT API key has no balance.')

        logger.info(account_idx, response_text)
        return response_text

    except Exception as e:
        if 'Rate limit reached' in str(e):
            return Fore.RED + 'GPT rate limit reached, please try again later.' + Style.RESET_ALL
        
        if "You exceeded your current quota" in str(e):
            return Fore.RED + 'Your ChatGPT API key has no balance.' + Style.RESET_ALL
        
        return Fore.RED + f'GPT Error occurred: {str(e)}' + Style.RESET_ALL

    