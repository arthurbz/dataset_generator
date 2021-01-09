from pathlib import Path


def generate(folder, video_path, steps, step_type='frame'):
    check_folder(folder)
    if step_type == 'frame':
        pass
    elif step_type == 'seconds':
        pass
    else:
        return 'Step type has to be frame or seconds.'


def check_folder(folder):
    Path(folder).mkdir(parents=True, exist_ok=True)
