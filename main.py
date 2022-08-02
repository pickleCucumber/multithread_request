import requests
import time

from threading import Thread



class Parser(object):
    def __init__(self):

        input_file = open("input.txt", "r")
        proxies_file = open('proxies.txt', 'r')

        wallets = input_file.readlines()
        self.proxies = proxies_file.readlines()


        for i, additionally in enumerate("обозначение input_file"):
            start_time = time.time()
            additionally = additionally.strip()
            url = f'http://url{additionally}'
            #прокси крутятся по кругу как кукурузник
            index = i % len(self.proxies)
            proxy = self.proxies[index].strip()
            # Создаем поток и запускаем его
            Thread(target=self.request, args=(url, proxy)).run()

        time.sleep(3)
        end_time = time.time()
        print(end_time-start_time)

    def request(self, url, proxy):
        start_time = time.time()
        proxies = {
            'http': proxy
        }
        try:
            res = requests.get(url, proxies=proxies)

            if res.status_code != 200:
                # Поднимаем свою ошибку с указанием кода ответа
                raise Exception(f"Request status code: {res.status_code}")
            p = res.json()
            response = str(p['need path to response'])
            response = response.rjust(9, '0')
        #условие нужное в проекте
            if response >= number:
                with open("output.txt", "r+") as f:
                    f.seek(0,2)
                    f.write(response)
                    f.write("\n")
               # output_file.writeLine(wallet)
        except Exception as e:
            print(f"Error: {e}")
        end_time = time.time()
        print(end_time-start_time)


if __name__ == "__main__":
    Parser()
