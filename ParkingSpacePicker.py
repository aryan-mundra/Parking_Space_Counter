import cv2
import pickle

width, height = 107, 48

try:
    with open('car_parking_space/CarParkPos', 'rb') as f:  # Replace with the full path
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('car_parking_space/CarParkPos', 'wb') as f:  # Replace with the full path
        pickle.dump(posList, f)

while True:
    img = cv2.imread('car_parking_space/carParkImg.png')  # Provide the correct path to the image
    if img is None:
        break  # Exit the loop if the image cannot be loaded

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    key = cv2.waitKey(1)
    if key == 27:  # Press Esc key to exit the loop
        break

cv2.destroyAllWindows()
