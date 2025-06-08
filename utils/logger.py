from colorama import Fore, Style
from datetime import datetime


class Logger:

    def _log(self, account_idx, message, color=Fore.WHITE, level='INFO'):
        time = f'{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}'
        print(f'{f'{Fore.BLUE}{time}{Style.RESET_ALL}'} | {color}{level} | [{account_idx}] {message} {Style.RESET_ALL}')


    def error(self, account_idx, message):
        self._log(account_idx, message, Fore.RED, 'ERROR')

    def success(self, account_idx, message):
        self._log (account_idx, message, Fore.GREEN, 'SUCCESS')

    def info(self, account_idx, message):
        self._log(account_idx, message)


logger = Logger()