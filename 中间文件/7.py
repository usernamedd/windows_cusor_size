import ctypes
from pynput import mouse

# 设置系统光标的函数
def set_cursor(cursor_type):
    cursor_types = {
        'normal': 32512,  # Standard arrow and small hourglass
        'small': 32648,   # Cross
    }
    ctypes.windll.user32.SetSystemCursor(ctypes.windll.user32.LoadCursorW(0, cursor_types[cursor_type]), 32512)

# 鼠标事件处理器
def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed:
            set_cursor('small')  # 当按下左键时，设置光标为小光标
        else:
            set_cursor('normal')  # 当松开左键时，恢复光标为正常大小

# 监听鼠标事件
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
