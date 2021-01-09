import cv2

video = cv2.VideoCapture('kimi.mp4')

fps = video.get(cv2.CAP_PROP_FPS)
total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
duration_in_seconds = float(total_frames) / float(fps)


print(fps, total_frames, duration_in_seconds)
