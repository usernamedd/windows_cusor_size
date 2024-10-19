import os
import ctypes as ct
import ctypes.wintypes as w
from time import sleep

SPI_SETDESKWALLPAPER  = 0x0014
SPIF_UPDATEINIFILE    = 0x0001
SPIF_SENDWININICHANGE = 0x0002

def boolcheck(result, func, args):
    if not result:
        raise ct.WinError(ct.get_last_error())
    return None

user32 = ct.WinDLL('user32', use_last_error=True)
SystemParametersInfo = user32.SystemParametersInfoW
SystemParametersInfo.argtypes = w.UINT, w.UINT, w.LPVOID, w.UINT
SystemParametersInfo.restype = w.BOOL
SystemParametersInfo.errcheck = boolcheck

# SystemParametersInfo(0x2029, 0, 0x30 , 3)
SystemParametersInfo(0x2029, 0, 0x30 , 1)
sleep(0.1)
# SystemParametersInfo(0x2029, 0, 0x20 , 3)
SystemParametersInfo(0x2029, 0, 0x20 , 1)
sleep(0.1)
# SystemParametersInfo(0x2029, 0, 0x10 , 3)
SystemParametersInfo(0x2029, 0, 0x10 , 1)
sleep(0.1)
# SystemParametersInfo(0x2029, 0, 0x30 , 3)
SystemParametersInfo(0x2029, 0, 0x30 , 1)
# SystemParametersInfo(0x2029, 0, 0x80 , 1)

# Parameters: rcx=
# rcx=0000000000000057
# rdx=
# rdx=0000000000000000
# r8=
# r8=0000000000000000
# r9=
# r9=0000000000000002
# Parameters: rcx=
# rcx=0000000000002029
# rdx=
# rdx=0000000000000000
# r8=
# r8=0000000000000090
# r9=
# r9=0000000000000003
# Parameters: rcx=
# rcx=0000000000002029
# rdx=
# rdx=0000000000000000
# r8=
# r8=0000000000000090
# r9=
# r9=0000000000000001
