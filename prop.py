import requests
import json
import time
import keyboard
import signal
import os

url = 'https://propiy.com/api/nowruz/coupons'

running = True

def stop_program(e):
    global running
    running = False

def signal_handler(sig, frame):
    pass

signal.signal(signal.SIGINT, signal_handler)

keyboard.add_hotkey('q', stop_program)
print('hwiehasan@ To stop the program Click On Screen')
while running:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for item in data:
            code = item.get('code')
            initBalance = item['challenge_types'][0]['init_balance']
            print(f'Code: {code}' + '   '+ f'initBalance: {initBalance}' )
        print('===========================')
        time.sleep(2)  # انتظار 2 ثانیه قبل از ارسال درخواست بعدی
    else:
        print('خطا در دریافت اطلاعات. وضعیت درخواست:', response.status_code)