import os
import random
import requests
import threading
from time import strftime, gmtime, time, sleep    



class TikTok:
    def __init__(self):

        print(" [40;36m╔═╗┬ ┬┌─┐┬─┐┌─┐  ╔╗ ┌─┐┌┬┐ ")
        print(" [40;36m╚═╗├─┤├─┤├┬┘├┤   ╠╩╗│ │ │ ")
        print(" [40;36m╚═╝┴ ┴┴ ┴┴└─└─┘  ╚═╝└─┘ ┴ ")
        print("                           ")
        print("                           ")

        self.added = 0
        self.lock = threading.Lock()

        try:
            print('[40;37m╔═════Enter the Amount of shares desired:')
            self.amount = int(input('[40;37m╚══> '))
        except ValueError:
            self.close('[40;31mValue error, expected an integer')

        try:
            print("[40;37m╔═════TikTok Video URL:"https://vm.tiktok.com/ZMLbc7pff/





)
            self.video_id = input('[40;37m╚══>').split('/')[5]
            
        except IndexError:
            self.close(
                '[40;31mInvalid TikTok URL format.\nFormat expected: https://www.tiktok.com/@username/vide'
                'o/1234567891234567891'
            )
        else:
            if not self.video_id.isdigit():
                self.close(
                    '[40;31mInvalid TikTok URL format.\nFormat expected: https://www.tiktok.com/@username/'
                    'video/1234567891234567891'
                )
            else:
                print()

    def close(self, message):
        print(f'\n{message}')
        os.system("title Xeldra.EU TikTok SharesBot - Restart required")
        os.system('pause >NUL')
        os.system("title Xeldra.EU TikTok SharesBot - Closing...")
        sleep(5)
        os._exit(0)

    def status(self, code, intention):
        if code == 200:
            self.added += 1
        else:
            self.lock.acquire()
            print(f'Error: {intention} | Status Code: {code}')
            self.lock.release()
            self.bot()

    def update_title(self):
        # Avoid ZeroDivisionError
        while self.added == 0:
            sleep(0.2)

        while self.added < self.amount:
            # Elapsed Time / Added * Remaining
            time_remaining = strftime(
                '%H:%M:%S', gmtime(
                    (time() - self.start_time) / self.added * (self.amount - self.added)
                )
            )
            os.system(
                f"title Xeldra.EU TikTok SharesBot - Added: {self.added} Shares/{self.amount} Shares "
                f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                f'{threading.active_count()} ^| Time Remaining: {time_remaining}'
            )
            sleep(0.2)
        os.system(
            f"title Xeldra.EU TikTok SharesBot - Added: {self.added}/{self.amount} "
            f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
            f'{threading.active_count()} ^| Time Remaining: 00:00:00'
        )

    def bot(self):
        
        if self.added > 0:
            print(f"{self.added} [40;32mShares have been added!")
            
        action_time = round(time())
        device_id = ''.join(random.choice('0123456789') for _ in range(19))

        data = (
            f'action_time={action_time}&item_id={self.video_id}&item_type=1&share_delta=1&stats_channel=copy'
        )
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-common-params-v2': 'version_code=16.6.5&app_name=musical_ly&channel=App%20Store&devi'
                                  f'ce_id={device_id}&aid=1233&os_version=13.5.1&device_platform=ip'
                                  'hone&device_type=iPhone10,5',
            'User-Agent': 'TikTok 16.6.5 rv:166515 (iPhone; iOS 13.6; en_US) Cronet',
        }

        try:
            response = requests.post(
                'https://api16-core-c-useast1a.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region='
                'SE&app_skin=white&', data=data, headers=headers
            )
        except Exception as e:
            print(f'Error: {e}')
            self.bot()
        else:
            if all(i not in response.text for i in ['Service Unavailable', 'Gateway Timeout']):
                self.status(response.status_code, response.text)
            else:
                self.bot()

    def start(self):
        self.start_time = time()
        threading.Thread(target=self.update_title).start()

        for _ in range(self.amount):
            while True:
                if threading.active_count() <= 300:
                    threading.Thread(target=self.bot).start()
                    break

        os.system('pause >NUL')
        os.system("title Xeldra.EU TikTok SharesBot - Closing...")
        sleep(3)


if __name__ == '__main__':
    os.system("cls && title Create By Xeldra.EU ~ TikTok SharesBot")
    main = TikTok()
    main.start()
