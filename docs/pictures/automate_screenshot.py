import win32gui
import pygetwindow as gw
import time
import os
from PIL import ImageGrab
from pywinauto import Application

def get_window_rect(title):
    # Find the window by its title
    hwnd = win32gui.FindWindow(None, title)
    
    if hwnd == 0:
        raise Exception(f"Window with title '{title}' not found.")
    
    # Get the window rectangle (left, top, right, bottom)
    rect = win32gui.GetWindowRect(hwnd)
    
    return rect

def get_screenshot(window_title, window_name, filename):
   
    try:
        # Get the window boundaries
        rect = get_window_rect(window_title)
        print(f"Window coordinates and dimensions: {rect}")

        # RS2 file window name
        RS2window = gw.getWindowsWithTitle(window_name)

        if RS2window != []:
            try:
                # Usually this one doesn't work. It is a bug from the package.
                RS2window[0].activate()
                
            except:
                # This is a way to work around
                RS2window[0].minimize()
                RS2window[0].restore()

            # Wait for 0.5 second for everything load 
            # If the computer is not very good and show screenshot with other program, increase the sleep time
            time.sleep(0.5)
            
            # 18 is the extra space at left, right and bottom boundaries
            extra_space = 18
            # Define the bounding box for the screenshot
            bbox = (rect[0] + extra_space, rect[1], rect[2] - extra_space, rect[3] - extra_space)

            # Take the screenshot
            screenshot = ImageGrab.grab(bbox)

            # Get the directory of the current script
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Combine the script directory with the filename
            file_path = os.path.join(script_dir, filename)

            # Save or display the screenshot
            screenshot.save(file_path)
            screenshot.show()
            print(filename + " saved.")
        
    except Exception as e:
        print(e)

