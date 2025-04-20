import cv2
import numpy as np
import pyautogui
import mss
import os

# Function to capture the screen
def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Capture the primary screen
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img

# Function to detect a specific image (template) on the screen
def detect_image_on_screen(template_path, threshold=0.8):
    # Read the template image (the small image you want to find)
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    
    # Get template dimensions
    template_height, template_width = template.shape[:2]
    
    # Capture the current screen
    screen = capture_screen()

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


# Example usage
template_image_path = "Function/Bot/Image/screen.png"  # Path to the image you want to detect
if not os.path.exists(template_image_path):

    print(f"File not found: {template_image_path}")
else:
    print(f"File exists: {template_image_path}")
    detect_image_on_screen(template_image_path)






