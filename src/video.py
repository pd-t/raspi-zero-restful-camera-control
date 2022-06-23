from time import sleep
from picamera import PiCamera


class Camera:
    def __init__(
            self,
            src=0,
            picture_resolution=(3280, 2464),
            picture_framerate=6,
            video_resolution=(1280, 720),
            video_framerate=30

    ):
        self.picture_settings = {
            'resolution': picture_resolution,
            'framerate': picture_framerate
        }
        self.video_settings = {
            'resolution': video_resolution,
            'framerate': video_framerate
        }
        self.camera = PiCamera(camera_num=src)
        self.recording = False
        self.filename = "unknown"

    def start_video(self, filename: str) -> str:
        if not self.recording:
            self.recording = True
            self.filename = filename
            self.warm_up(self.video_settings)
            self.camera.start_recording(filename)
        return self.filename

    def take_picture(self, filename) -> str:
        self.warm_up(self.picture_settings)
        if not self.recording:
            self.camera.capture(filename)
        return filename

    def warm_up(self, settings):
        self.camera.framerate = settings['framerate']
        self.camera.resolution = settings['resolution']
        self.camera.start_preview()
        sleep(2)

    def stop_video(self):
        filename = self.filename
        if self.recording:
            self.camera.stop_recording()
            self.recording = False
            self.filename = "unknown"
        return filename


if __name__ == "__main__":
    # This is a short integration test
    camera = Camera()
    camera.take_picture('my_picture.jpg')
    camera.start_video('my_video.h264')
    sleep(10)
    camera.stop_video()
