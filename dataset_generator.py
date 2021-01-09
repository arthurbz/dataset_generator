from pathlib import Path
import cv2


def generate(folder, video_path, steps, step_type, output_name='frame', verbose=1):
    options = {'frame': generate_by_frame, 'seconds': generate_by_seconds}

    if(step_type != 'frame' and step_type != 'seconds'):
        raise ValueError('Step has to be frame or seconds.')

    try:
        files_path = check_folder(folder)
    except FileNotFoundError or OSError:
        raise

    if verbose: print('Destiny folder:', files_path)
    options[step_type](files_path, video_path, output_name, steps, verbose)


def generate_by_seconds(folder, video_path, output_name, steps, verbose):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    currentframe = 0

    while (True):
        ret, frame = video.read()
        if ret:
            if (currentframe / fps) % steps == 0:
                name = folder + output_name + str(currentframe) + '.jpg'
                if verbose: print('Creating...' + name)
                cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break
    video.release()
    cv2.destroyAllWindows()


def generate_by_frame(folder, video_path, output_name, steps, verbose):
    video = cv2.VideoCapture(video_path)
    currentframe = 0

    while (True):
        ret, frame = video.read()
        if ret:
            if currentframe % steps == 0:
                name = folder + output_name + str(currentframe) + '.jpg'
                if verbose: print('Creating...' + name)
                cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break
    video.release()
    cv2.destroyAllWindows()


def check_folder(folder):
    try:
        Path(folder).mkdir(parents=True, exist_ok=True)
        return str(Path(folder).absolute()) + '/'
    except FileNotFoundError or OSError:
        raise
