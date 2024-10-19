import ctypes

# Define Windows API constants
SPI_SETCURSORS = 0x0057
SPIF_UPDATEINIFILE = 0x0001
SPIF_SENDCHANGE = 0x0002

# Cursor ID for the hand cursor
IDC_HAND = 32648

def set_cursor_to_hand():
    # Load the user32.dll
    user32 = ctypes.WinDLL('user32')
    
    # Attempt to set the hand cursor as the system cursor
    success = user32.SetSystemCursor(user32.LoadCursorW(None, IDC_HAND), IDC_HAND)
    
    if success:
        # Notify the system that the cursor settings have changed
        # user32.SystemParametersInfoW(SPI_SETCURSORS, 0, None, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
        print("Cursor set to hand shape successfully.")
    else:
        print("Failed to set cursor to hand shape.")

# Call the function to set the cursor to the hand shape
set_cursor_to_hand()
