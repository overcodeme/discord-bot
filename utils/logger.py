from colorama import Fore, Style
from datetime import datetime, timezone


class Logger:

    def _log(self, message, color=Fore.WHITE, level='INFO'):
        time = f'{datetime.now(timezone.utc).strftime('%d.%m.%Y %H:%M:%S')}'
        print(f'{f'{Fore.BLUE}{time}{Style.RESET_ALL}'} | {color}{level} | {message} {Style.RESET_ALL}')


    def error(self, message):
        self._log(message, Fore.RED, 'ERROR')

    def success(self, message):
        self._log (message, Fore.GREEN, 'SUCCESS')

    def info(self, message):
        self._log(message)


logger = Logger()