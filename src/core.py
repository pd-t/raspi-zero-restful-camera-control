import datetime
import os
from pathlib import Path

from src.models import Media
from src.video import Camera

CAMERA_DATA_PATH: str = "../data/" if os.getenv("CAMERA_DATA_PATH") is None else os.getenv("CAMERA_DATA_PATH")

camera = Camera()


def get_filename(extension: str):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    os.makedirs(CAMERA_DATA_PATH, exist_ok=True)
    filename = str(Path(CAMERA_DATA_PATH).joinpath(timestamp)) + extension
    return filename


def get_take_picture_core():
    filename = camera.take_picture(get_filename(extension=".jpg"))
    media = Media(filename=filename)
    return media


def get_start_video_core():
    filename = camera.start_video(get_filename(extension=".h264"))
    return Media(filename=filename)


def get_stop_video_core():
    filename = camera.stop_video()
    return Media(filename=filename)
