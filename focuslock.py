import time

def start_timer(duration):
    """启动专注时钟定时器，在指定时间内运行"""
    # 将分钟转换为秒
    timer = duration * 60
    while timer:
        # 将剩余时间格式化为 MM:SS，并打印出来
        mins, secs = divmod(timer, 60)
        timer_str = f"{mins:02d}:{secs:02d}"
        print(timer_str, end="\r")
        # 延迟一秒并将计时器减 1
        time.sleep(1)
        timer -= 1

    print("专注时间到！")

# 测试
start_timer(25)  # 启动一个 25 分钟的专注时钟
