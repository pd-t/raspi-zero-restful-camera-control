from threading import Thread
import cv2


class VideoStream:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        self.size = (
            int(self.stream.get(3)),
            int(self.stream.get(4))
        )
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True


class VideoRecord:
    """
    Class that continuously record a frame using a dedicated thread.
    """

    def __init__(self, frame, size):
        self.frame = frame
        self.size = size
        self.recording = False
        self.filename = None
        self.video_writer = None

    def start(self, filename: str):
        if not self.recording:
            self.recording = True
            self.filename = filename
            self.video_writer = cv2.VideoWriter(self.filename,
                                                cv2.VideoWriter_fourcc('M',
                                                                       'J',
                                                                       'P',
                                                                       'G'),
                                                10,
                                                self.size)
            Thread(target=self.record, args=()).start()
        return self.filename

    def record(self):
        while self.recording:
            self.video_writer.write(self.frame)

    def stop(self):
        self.recording = False
        return self.filename
