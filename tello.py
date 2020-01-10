# 「Tello SDK1.3」を利用して、Telloを操作するクラス 
# 参考: https://terra-1-g.djicdn.com/2d4dce68897a46b19fc717f3576b7c6a/Tello%20%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/For%20Tello/Tello%20SDK%20Documentation%20EN_1.3_1122.pdf

import threading
import socket
import time

class TelloController():

    def __init__(self, local_address=('', 9000), tello_address=('192.168.10.1', 8889), interval_sec=0.01):
        self.__local_address = local_address
        self.__tello_address = tello_address
        self.__interval_sec = interval_sec

    def __wait_interval(self):
        time.sleep(self.__interval_sec)

    def send_command(self, command):
        encoded_command = command.encode(encoding='utf-8')
        self.__sock.sendto(encoded_command, self.__tello_address)
        self.__wait_interval()

    def connect(self):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.bind(self.__local_address)
        self.send_command('command')

    def disconnect(self):
        self.__sock.close()

    def print_streaming_receive_data(self):
        def target():
            while True:
                try:
                    data, server = self.__sock.recvfrom(1518)
                    print(data.decode(encoding="utf-8"))
                except Exception:
                    print('\nデータの受信でエラーが発生しました。\n')
                    print(Exception)

        thread = threading.Thread(target=target, daemon=True)
        thread.start()
