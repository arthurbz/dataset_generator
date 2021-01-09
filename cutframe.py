import cv2
import os

videopath = ''
cam = cv2.VideoCapture(videopath)
frame_step = 5


try:
    if not os.path.exists('dataset'):
        os.makedirs('dataset')
except OSError:
    print('Error: Creating directory of data')

currentframe = 0

while (True):
    ret, frame = cam.read()
    print(currentframe)
    if ret:
        if currentframe % frame_step == 0:
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()
