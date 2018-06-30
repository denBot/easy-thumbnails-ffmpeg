from django.utils.six import BytesIO
import os
from subprocess import Popen, PIPE
from PIL import Image
from random import choices
from string import ascii_lowercase, ascii_uppercase

def ffmpeg_frame(source, frame='00:00:01', **options):

    if not source:
        return
    # Generates random filename for data stream and writes stream to temp-file
    filename = ''.join(choices(ascii_lowercase + ascii_uppercase, k=8))
    with open(filename, 'wb') as f:
        f.write(source.read())

    try:
        # Opens file with ffmpeg, grabs frame at 1 second & removes tempfile
        cmd = ['ffmpeg', '-i', filename, '-ss', frame, '-vframes', '1', '-f', 'image2', 'pipe:1']
        data = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate(source.read())
        os.remove(filename)
        if not data[0]:
            return
    except (Exception, IndexError, FileNotFoundError):
        return
    
    image = Image.open(BytesIO(data[0]))
    try:
        image.load()
    except IOError:
        pass
    
    image = utils.exif_orientation(image)
    return image
