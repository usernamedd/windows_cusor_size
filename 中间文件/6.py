import ctypes
import pynput

# 定义鼠标光标样式
original_cursor = None
small_cursor = None

# 获取和设置系统光标的函数
def get_system_cursor():
    cursor = ctypes.windll.user32.LoadCursorW(0, 32512)  # 32512 is the standard arrow cursor
    return cursor

def set_system_cursor(cursor):
    ctypes.windll.user32.SetSystemCursor(cursor, 32512)

def create_small_cursor():
    # 创建一个小光标，你可以使用其他光标文件或者自定义创建
    cursor = ctypes.windll.user32.LoadCursorW(0, 32641)  # 32641 is the cross cursor
    return cursor

def on_click(x, y, button, pressed):
    global original_cursor, small_cursor
    if button == pynput.mouse.Button.left:
        if pressed:
            # 当鼠标左键按下时，改变鼠标光标为小光标
            set_system_cursor(small_cursor)
        else:
            # 当鼠标左键弹起时，恢复鼠标光标为原始光标
            set_system_cursor(original_cursor)

def main():
    global original_cursor, small_cursor
    original_cursor = get_system_cursor()
    small_cursor = create_small_cursor()

    # 开始监听鼠标事件
    with pynput.mouse.Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()
