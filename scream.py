import requests
import winreg
import os

def get_download_path():
    if os.name == 'nt':
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


url = 'https://cdn.discordapp.com/attachments/811646112163168327/878010354586759188/naike.mp4'
filename = 'Wtf.mp4'
r = requests.get(url)

with open(f'{get_download_path()}/{filename}', 'wb') as f:
    f.write(r.content)

os.startfile(f'{get_download_path()}/{filename}')
