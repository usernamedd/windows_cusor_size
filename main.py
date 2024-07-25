import os
import ctypes as ct
import ctypes.wintypes as w


user32 = ct.WinDLL('user32', use_last_error=True)
SystemParametersInfo = user32.SystemParametersInfoW

# SystemParametersInfo(0x2029, 0, 0x30 , 3)
SystemParametersInfo(0x2029, 0, 0x30 , 1) # the third parameter 0x30 indicates size value 3 , 0x90 indicates size value 9 
