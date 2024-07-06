import requests
from bs4 import BeautifulSoup
import os
import requests
import platform
from datetime import datetime

url = 'https://2ip.ru/'

def get_ip():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            div_ip = soup.find('div', class_='ip')
            ip_address = div_ip.find('span').text.strip()
            return ip_address
        else:
            print(f"Ошибка при запросе: {response.status_code}")
            return None
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return None

def get_user_os():
    return platform.system()

def get_info_by_ip(ip):
    try:
        responce = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        return responce
    except requests.exceptions.ConnectionError:
        print("проверь подключения")
