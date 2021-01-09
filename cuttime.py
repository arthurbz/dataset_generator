import cv2


videopath = ''
video = cv2.VideoCapture(videopath)
time_step = 5
fps = video.get(cv2.CAP_PROP_FPS)
total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
duration_in_seconds = float(total_frames) / float(fps)

currentframe = 0

while (True):
    ret, frame = video.read()
    if ret:
        if (currentframe / fps) % time_step == 0:
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

video.release()
cv2.destroyAllWindows()
