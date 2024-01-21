import cv2
from image_and_tile import tile, image
import numpy as np

def find_edges(tile_obj):
    img = cv2.imread(tile_obj.path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 150, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def find_area(contours):
    areas=np.zeros(len(contours))
    for i,cnt in enumerate(contours):
        areas[i]=cv2.contourArea(cnt)
    return areas

def draw_contours(tile_obj, contours, areas):
    original_img = cv2.imread(tile_obj.path)

    for i, cnt in enumerate(contours):
        cv2.imshow(f"Contour {i + 1}", original_img)
        cv2.waitKey(0)  # Wait for key press to show next contour
        # Make a copy of the image for drawing
        img = original_img.copy()

        # Draw the contour
        cv2.drawContours(img, [cnt], -1, (140, 140, 140), 3)

        # Place text (optional)
        x1, y1 = cnt[0, 0]
        area = areas[i]
        cv2.putText(img, f'Area:{area}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 140, 140), 2)

        # Display the image
        cv2.imshow(f"Contour {i + 1}", img)
        cv2.waitKey(0)  # Wait for key press to show next contour
        cv2.destroyAllWindows()