import time
import tello

# 画面に「離陸します！」と表示する
print('離陸します！')

# telloを操作するコントローラーを作成する
tello_controller = tello.TelloController()

# telloとの通信を開始する
tello_controller.connect()

# telloを離陸させる
tello_controller.send_command('takeoff')

# 5秒間処理を止める
time.sleep(5)

# telloを着陸させる
tello_controller.send_command('land')

# ５秒間処理を止める
time.sleep(5)

# telloとの通信を終了する
tello_controller.disconnect()


