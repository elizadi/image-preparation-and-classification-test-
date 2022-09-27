from moviepy.editor import VideoFileClip
import numpy as np
import os
from datetime import timedelta

SAVING_FRAMES_PER_SECOND = 1

def format_timedelta():
    result = str(td)
    try:
        result, ms = result.split('.')
    except ValueError:
        return result + ".00".replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

def main(video_file):
    # загрузить видеоклип
    video_clip = VideoFileClip(video_file)
    # создаем папку по названию видео файла
    filename, _ = os.path.splitext(video_file)
    filename += "-moviepy"
    if not os.path.isdir(filename):
        os.mkdir(filename)

    # если SAVING_FRAMES_PER_SECOND выше видео FPS, то установите его на FPS (как максимум)
    saving_frames_per_second = min(video_clip.fps, SAVING_FRAMES_PER_SECOND)
    # если SAVING_FRAMES_PER_SECOND установлен в 0, шаг равен 1 / fps, иначе 1 / SAVING_FRAMES_PER_SECOND
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
    # перебираем каждый возможный кадр
    for current_duration in np.arange(0, video_clip.duration, step):
        # отформатируйте имя файла и сохраните его
        frame_duration_formatted = format_timedelta(timedelta(seconds=current_duration)).replace(":", "-")
        frame_duration_formatted = frame_duration_formatted[115:210, 350:445]
        frame_filename = os.path.join(filename, f"frame{frame_duration_formatted}.jpg")
        # сохраняем кадр с текущей длительностью
        video_clip.save_frame(frame_filename, current_duration)
        count += 1
        print(f"{frame_filename} сохранен")

    print(f"Итого сохранено кадров: {count}")


if __name__ == "__main__":
    import sys
    video_file = sys.argv[1]
    import time
    begtime = time.perf_counter()
    main(video_file)
    endtime = time.perf_counter()
    print(f"\nЗатрачено, с: {endtime - begtime} ")