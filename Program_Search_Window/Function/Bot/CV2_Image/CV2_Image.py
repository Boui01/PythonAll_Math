import cv2
import numpy as np
import pyautogui
import mss

import time
class CV2_Image:

    def __init__(self , time_):
        self.time = time_
        pass
    def capture_screen(self):
        time.sleep(self.time)
        with mss.mss() as sct:
            monitor = sct.monitors[1]  # Capture the primary screen
            screenshot = sct.grab(monitor)
            img = np.array(screenshot)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            return img

    def detect_image_on_screen(self,template_path, threshold=0.8):
        # Read the template image (the small image you want to find)
        template = cv2.imread(template_path, cv2.IMREAD_COLOR)
        
        # Get template dimensions        
        template_height, template_width = template.shape[:2]
        
        # Capture the current screen        
        screen = self.capture_screen()
        
        # Perform template matching        
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        
        # Get the locations where the result matches above the threshold
        locations = np.where(result >= threshold)

        # Draw rectangles around matched regions
        for point in zip(*locations[::-1]):
            cv2.rectangle(screen, point, (point[0] + template_width, point[1] + template_height), (0, 255, 0), 2)

        # Display the result (for debugging, you can comment this in production)
        cv2.imshow('Detected', screen)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()

        # Return True if we found at least one match, False otherwise
        return len(locations[0]) > 0
    
    def detect_position_click(self, template_path, threshold=0.8):
        # Load the template image

        template = cv2.imread(template_path, cv2.IMREAD_COLOR)
        template_height, template_width = template.shape[:2]

        # Capture the screen
        screen = self.capture_screen()

        # Perform template matching
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)

        # If matches found
        if len(locations[0]) > 0:
            for point in zip(*locations[::-1]):
                # Get the center of the matched image
                center_x = point[0] + template_width // 2
                center_y = point[1] + template_height  // 2

                # Move to the location and click
                pyautogui.moveTo(center_x, center_y)
                pyautogui.click()

                print(f"Clicked at: ( X : {center_x}, Y : {center_y})")
                break
        else:
            print("No matches found.")