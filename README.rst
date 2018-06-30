
Forked from easy-thumbnails-ffmpeg by aldarund_.

To install THIS version of easy-thumbnails-ffmpeg, do:
```pip install git+https://github.com/denBot/easy-thumbnails-ffmpeg```

Synopsis
--------
A video thumbnail source generator for django easy-thumbnails_ using ffmpeg_.

Requirements
------------

* ``easy_thumbnails``
* ``ffmpeg``

Install
-------

Add this package to your Python path or ``pip install easy-thumbnails-ffmpeg``.

Add ``easy_thumbnails_ffmpeg.source_generators.ffmpeg_frame`` to ``THUMBNAIL_SOURCE_GENERATORS`` in your ``settings.py``::

    THUMBNAIL_SOURCE_GENERATORS = (
        'easy_thumbnails.source_generators.pil_image', # Default
        'easy_thumbnails_ffmpeg.source_generators.ffmpeg_frame',
    )

License
-------

CC0 1.0 Universal (Public Domain)

.. _easy-thumbnails: https://github.com/SmileyChris/easy-thumbnails
.. _ffmpeg: http://www.ffmpeg.org
.. _aldarund https://github.com/aldarund/easy-thumbnails-ffmpeg