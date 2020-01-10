
# Telloへコマンドを送信するための関数
def send_command(sock, command):
    tello_address = (settings_dict['tello_ip_address'], 8889)
    encoded_command = command.encode(encoding='utf-8')

    sock.sendto(encoded_command, tello_address)

# Telloと通信するためのソケットを作成する
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Telloとの通信を開始する
send_command(sock, 'command')

