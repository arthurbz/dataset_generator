from pathlib import Path
import cv2


def generate(folder, video_path, steps, step_type='frame'):
    if(step_type != 'frame' and step_type != 'seconds'):
        return 'Step type has to be frame or seconds.'
    files_path = check_folder(folder)
    print(files_path)
    options = {'frame': generate_by_frame,
               'seconds': generate_by_seconds}
    options[step_type](files_path, video_path, steps)


def generate_by_seconds(folder, video_path, steps):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)

    currentframe = 0

    while (True):
        ret, frame = video.read()
        if ret:
            if (currentframe / fps) % steps == 0:
                name = folder + str(currentframe) + '.jpg'
                print('Creating...' + name)
                cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break
    video.release()
    cv2.destroyAllWindows()


def generate_by_frame(folder, video_path, steps):
    video = cv2.VideoCapture(video_path)
    currentframe = 0

    while (True):
        ret, frame = video.read()
        print(currentframe)
        if ret:
            if currentframe % steps == 0:
                name = folder + str(currentframe) + '.jpg'
                print('Creating...' + name)
                cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break
    video.release()
    cv2.destroyAllWindows()


def check_folder(folder):
    Path(folder).mkdir(parents=True, exist_ok=True)
    return str(Path(folder).absolute()) + '/'
