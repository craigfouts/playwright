import imageio
from IPython.display import display, Video

class VideoWriter:
    def __init__(self, filename='_autoplay.mp4', size=400, frame_rate=30.):
        self.filename = filename
        self.size = size
        self.frame_rate = frame_rate

        self.frames = []

    def __enter__(self):
        return self
    
    def __exit__(self, *_):
        if self.filename == '_autoplay.mp4':
            self.show()
        else:
            self.save()

    def write(self, frame):
        self.frames.append(frame)

    def save(self):
        with imageio.imopen(self.filename, 'w', plugin='pyav') as out:
            out.init_video_stream('vp9', fps=self.frame_rate)
            for frame in self.frames:
                out.write_frame(frame)
    
    def show(self):
        self.save()
        video = Video(self.filename, width=self.size, height=self.size)
        display(video)
