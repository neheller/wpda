import shutil
import sys
from pathlib import Path

import numpy as np


""" Kidney cancer project """

def new_kc_set(src_dir, dst_dir, start, end, inc=1):
    """Create a new imageset for annotation

    src_dir: a directory containing a list of pngs numbered from 0 to n (Path)
    dst_dir: a directory in which to store generated set and place for
        annotations (Path)
    start: the first image to be annotated (int)
    inc: the increment (i.e. if 3 then select every third image) (int)
    end: don't select more than one image after this index (int)
    """
    # Check types
    if not isinstance(src_dir, Path):
        raise TypeError("src_dir must be Path object")
    if not isinstance(dst_dir, Path):
        raise TypeError("dst_dir must be Path object")
    if not isinstance(start, int):
        raise TypeError("start must be integer")
    if not isinstance(end, int):
        raise TypeError("end must be integer")
    if not isinstance(inc, int):
        raise TypeError("inc must be integer")

    # Check to make sure path arguments are valid
    if not src_dir.is_dir():
        raise ValueError("Source directory does not exist")
    num_pngs = sum([1 for _ in src_dir.glob("*.png")])
    if (end >= num_pngs):
        raise ValueError("End value larger than or equal to number of pngs in src")
    if dst_dir.exists():
        raise ValueError("Destination directory already exists")
    # TODO enforce location based on project configuration

    # Prep destination for new data
    dst_pngs = dst_dir / "raw_png"
    dst_anns = dst_dir / "annotated"
    dst_dir.mkdir()
    dst_pngs.mkdir()
    dst_anns.mkdir()

    # Check number to copy
    num = (end - start + inc)//inc
    if num >= 10**4:
        raise ValueError("Too many slices! Must be < 10^4 per set")

    # Copy selected slices over
    for i, ind in np.ndenumerate(np.arange(start, end+inc, inc)):
        src_im = src_dir / (str(ind) + '.png')
        dst_im = dst_pngs / ('%04d.png' % i[0])
        shutil.copy(str(src_im), str(dst_im))

if __name__ == '__main__':
    new_kc_set(
        Path(sys.argv[1]), # source
        Path(sys.argv[2]), # destination
        int(sys.argv[3]),  # start
        int(sys.argv[4]),  # end
        int(sys.argv[5])   # increment
    )
