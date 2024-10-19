import ctypes

# Define Windows API constants
SPI_SETCURSORS = 0x0057
SPIF_UPDATEINIFILE = 0x0001
SPIF_SENDCHANGE = 0x0002

def reset_to_default_arrow_cursor():
    # Load the user32.dll
    user32 = ctypes.WinDLL('user32')

    # Attempt to set the default system cursor (arrow cursor)
    success = user32.SystemParametersInfoW(SPI_SETCURSORS, 0, None, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
    
    if success:
        print("Cursor set to default arrow successfully.")
    else:
        print("Failed to set cursor to default arrow.")

# Call the function to reset the cursor
reset_to_default_arrow_cursor()
