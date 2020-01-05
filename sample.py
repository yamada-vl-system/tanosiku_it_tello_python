"""
このプログラムは、予め決めた順序で、Telloを飛ばすためのPython3プログラムです。
プログラミング初心者の方に、どのプログラミング言語でも共通するプログラミングの基本
（「プログラムの実行順序」、「コメント文」、「標準出力」、「変数」、
「モジュール」、「演算子」、「データ型」、「リスト」、「辞書」、
「条件分岐」、「ループ」、「関数」）
を説明することを目的として書いています。
そのため、Python固有の機能に関しては、出来る限り使用しないようにしています。
また、プログラムをシンプルにするためにTelloからのデータ受信処理を除いています。
"""

import socket
import time

print('\nドローンを飛ばす場合は、キーボードの「a」を入力して「Enter」を押してください。\n中止する場合は、キーボードの「a」以外を入力して「Enter」を押してください。\n')
answer = input('入力: ')

if answer == 'a':

    settings_dict = {
        'tello_ip_address': '192.168.10.1',
        'speed': 10,
        'interval_sec': 5,
    }

    # Telloへコマンドを送信するための関数
    def send_command(sock, command):
        tello_address = (settings_dict['tello_ip_address'], 8889) 
        encoded_command = command.encode(encoding='utf-8')

        sock.sendto(encoded_command, tello_address)

    # Telloと通信するためのソケットを作成する
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Telloとの通信を開始する
    send_command(sock, 'command')

    # Telloのスピード(cm/s)を設定する
    send_command(sock, 'speed ' + str(settings_dict['speed']))

    # 離陸のカウントダウン
    print('離陸します！')
    count_list = [3, 2, 1]
    for number in count_list:
        print(number)
        time.sleep(1)

    # Telloへ離陸コマンドを送信
    send_command(sock, 'takeoff')
    time.sleep(settings_dict['interval_sec'])

    send_command(sock, 'foward 50')
    time.sleep(settings_dict['interval_sec'])

    send_command(sock, 'foward 300')
    time.sleep(settings_dict['interval_sec'])

    send_command(sock, 'back 300')
    time.sleep(settings_dict['interval_sec'])

    # 速度を10倍にする
    send_command(sock, 'speed ' + str(settings_dict['speed'] * 10))

    send_command(sock, 'right 300')
    time.sleep(settings_dict['interval_sec'])

    send_command(sock, 'left 300')
    time.sleep(settings_dict['interval_sec'])

    rotate_count = 0
    while rotate_count <= 3:
        send_command(sock, 'cw 360')
        rotate_count = rotate_count + 1
        time.sleep(settings_dict['interval_sec'])

    # Telloへ着陸コマンドを送信
    print('着陸します')
    send_command(sock, 'land')

    # ソケットを破棄する
    sock.close()

else:
    print('中止しました。')





















