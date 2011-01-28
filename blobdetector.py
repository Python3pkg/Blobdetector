"""
Test detect() with a small 4x4 square
>>> input = '\xee\xee\x11\x11\xee\x11\x11\x11\x11\x11\xee\xee\x11\x11\xee\xee'
>>> output = detect(PIL.Image.fromstring('L', (4, 4), input))
>>> output
'\\x01\\x01\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x02\\x02\\x00\\x00\\x02\\x02'
>>> input
'\\xee\\xee\\x11\\x11\\xee\\x11\\x11\\x11\\x11\\x11\\xee\\xee\\x11\\x11\\xee\\xee'
"""

import blobs
import PIL.Image

def detect(i):
    """ Take an instance of single-channel PIL.Image, detect blobs and return
    """
    assert i.mode == 'L'
    s = blobs.detect(i.size[0], i.size[1], i.tostring())
    o = PIL.Image.fromstring('L', i.size, s)
    return o

if __name__ == '__main__':
    import doctest
    doctest.testmod()