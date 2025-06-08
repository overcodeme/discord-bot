import asyncio
import logging
from data.settings import ACCOUNTS_SETTINGS
from core.discord import DiscordClient
from colorama import Fore, Style
import os


logging.getLogger('asyncio').setLevel(logging.ERROR)

async def handle_account(account_idx, account_settings, proxy):
    try:
        dc = DiscordClient(account_idx=account_idx, settings=account_settings, proxy=proxy)
        while True:
            await dc.send_message()
    except Exception as e:
        print(Fore.RED + f'An error occurred: {e}' + Style.RESET_ALL)


async def main():
    os.system('cls')
    tasks = []
    proxies = []

    with open('data/proxies.txt', 'r') as file:
        proxies = [pr.split()[0] for pr in file.readlines()]

    if not proxies:
        print(Fore.RED + 'No proxies found' + Style.RESET_ALL)

    for idx, (acc, pr) in enumerate(zip(ACCOUNTS_SETTINGS, proxies), start=1):
        tasks.append(handle_account(idx, acc, pr))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())