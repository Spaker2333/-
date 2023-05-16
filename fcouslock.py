import time
import winsound

def focus_timer(duration, break_duration):
    while True:
        # 专注时间
        print("专注开始！")
        time.sleep(duration)  # 在这里设置专注的时间（以秒为单位）

        # 提醒休息
        frequency = 2500  # 发出声音的频率（以赫兹为单位）
        duration = 1000  # 声音的持续时间（以毫秒为单位）
        winsound.Beep(frequency, duration)  # 发出声音提醒休息

        print("休息一下！")
        time.sleep(break_duration)  # 在这里设置休息的时间（以秒为单位）

# 设置专注时间为25分钟，休息时间为5分钟
focus_timer(25*60, 5*60)
