import os
import requests

class YD:

    def __init__(self, TokenYandexPoligon):
        self.Token = TokenYandexPoligon

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(self.Token)
        }

    def disk_file_path(self, path):  # Создаем папку на яндекс диске
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        res = requests.put(f"{url}?path={path}", headers=headers).status_code
        print(f"Создана папка '{path}' на Яндекс диске")
        print(res)
        return res

TokenYandexPoligon = "*******"

if __name__ == '__main__':
    ya = YD(TokenYandexPoligon)
    ya.disk_file_path('test123')
