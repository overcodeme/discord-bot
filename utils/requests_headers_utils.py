import base64
import json
import time


def calculate_nonce():
    return str((int(time.time()) * 1000 - 1420070400000) * 4194304)


def create_x_super_properties():
    return base64.b64encode(json.dumps({
   "os":"Windows",
   "browser":"Chrome",
   "device":"",
   "system_locale":"ru",
   "browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
   "browser_version":"133.0.0.0",
   "os_version":"10",
   "referrer":"https://discord.com/",
   "referring_domain":"discord.com",
   "referrer_current":"",
   "referring_domain_current":"",
   "release_channel":"stable",
   "client_build_number":370533,
   "client_event_source":None,
   "has_client_mods":False
}, separators=(',', ':')).encode('utf-8')).decode('utf-8')