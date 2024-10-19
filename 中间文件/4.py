
import ctypes
from pynput import mouse

# 定义鼠标光标的句柄
IDC_ARROW = 32512
IDC_SIZE = 32640

# 获取系统默认的鼠标光标句柄
default_cursor = ctypes.windll.user32.LoadCursorW(0, IDC_ARROW)
small_cursor = ctypes.windll.user32.LoadCursorW(0, IDC_SIZE)

def set_cursor(cursor):
    ctypes.windll.user32.SetSystemCursor(cursor, 32512)

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed:
            # 当鼠标左键按下时，设置小光标
            set_cursor(small_cursor)
        else:
            # 当鼠标左键弹起时，恢复默认光标
            set_cursor(default_cursor)

# 监听全局鼠标事件
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
