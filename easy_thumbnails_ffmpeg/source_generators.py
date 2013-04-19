# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
try:
    from PIL import Image
except ImportError:
    import Image


def ffmpeg_frame(source, frame='00:00:01', **options):
    """
    Try to load a frame of the given video with ffmpeg, ignoring all errors.
    """
    # noinspection PyBroadException
    try:
        data = Popen([
            'ffmpeg', '-i', source, '-an',
            '-vcodec', 'png', '-vframes', '1',
            '-ss', frame, '-y',
            '-f', 'rawvideo', '-'
        ], stdout=PIPE, stderr=PIPE).communicate()[0]

        image = Image.open(StringIO(data))
        image.load()

        return image
    except Exception:
        return
