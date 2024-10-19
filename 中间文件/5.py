from pynput import mouse
import ctypes
import time

# 定义原始和小光标的ID
ORIGINAL_CURSOR_ID = 0
SMALL_CURSOR_ID = 1

# 定义更改光标大小的函数（适用于Windows系统）
def set_cursor_size(size_id):
    ctypes.windll.user32.LoadCursorW.restype = ctypes.c_void_p
    if size_id == SMALL_CURSOR_ID:
        # 更改光标为小型光标
        ctypes.windll.user32.SetSystemCursor(ctypes.windll.user32.LoadCursorW(None, 32512), 32512)
    else:
        # 恢复为原始光标
        ctypes.windll.user32.SetSystemCursor(ctypes.windll.user32.LoadCursorW(None, 32512), 32512)

# 当鼠标按下时调用
def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed:
            set_cursor_size(SMALL_CURSOR_ID)
            print('pres按下')
        else:
            set_cursor_size(ORIGINAL_CURSOR_ID)

# 监听鼠标事件
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
