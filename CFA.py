import cv2
import numpy as np

def detect_fire_by_color(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return "picture is not Load"

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_fire1 = np.array([0, 100, 100])
    upper_fire1 = np.array([30, 255, 255])
    lower_fire2 = np.array([160, 100, 100])
    upper_fire2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_fire1, upper_fire1)
    mask2 = cv2.inRange(hsv, lower_fire2, upper_fire2)
    fire_mask = cv2.bitwise_or(mask1, mask2)

    fire_pixels = cv2.countNonZero(fire_mask)
    total_pixels = img.shape[0] * img.shape[1]
    fire_ratio = (fire_pixels / total_pixels) * 100

    if fire_ratio > 5.0:
        return f"Fire! (Ratio: {fire_ratio:.2f}%)"
    else:
        return f"Safe! (Ratio: {fire_ratio:.2f}%)"

print(detect_fire_by_color('fire_image.jpg'))
