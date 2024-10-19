
from pynput import mouse
import ctypes
import time

# 定义光标大小
SMALL_CURSOR_SIZE = 32
NORMAL_CURSOR_SIZE = 48

# Windows API函数
def set_cursor_size(size):
    ctypes.windll.user32.SetSystemCursor(
        ctypes.windll.gdi32.LoadCursorW(0, ctypes.c_wchar_p('IDC_ARROW')),
        0x0001  # OCR_NORMAL
    )

def get_cursor_size():
    return NORMAL_CURSOR_SIZE

def change_cursor_size_on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed:
            set_cursor_size(SMALL_CURSOR_SIZE)
        else:
            set_cursor_size(NORMAL_CURSOR_SIZE)

# 监听鼠标事件
with mouse.Listener(on_click=change_cursor_size_on_click) as listener:
    listener.join()
