import datetime
import os
from pathlib import Path

import cv2

from src.models import Media
from src.video import VideoRecord, VideoStream

CAMERA_DATA_PATH: str = "../data/" if os.getenv("CAMERA_DATA_PATH") is None else os.getenv("CAMERA_DATA_PATH")

video_stream = VideoStream(0).start()
video_record = VideoRecord(video_stream, video_stream.size)


def get_filename(extension: str):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    os.makedirs(CAMERA_DATA_PATH, exist_ok=True)
    filename = str(Path(CAMERA_DATA_PATH).joinpath(timestamp)) + extension
    return filename


def get_take_picture_core():
    img = video_stream.frame
    media = Media(filename=get_filename(extension=".jpg"))
    cv2.imwrite(media.filename, img)
    return media


def get_start_video_core():
    filename = video_record.start(get_filename(extension=".avi"))
    return Media(filename=filename)


def get_stop_video_core():
    filename = video_record.stop()
    return Media(filename=filename)
