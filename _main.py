"""functions for LabVIEW connections, version 1.2"""

from mask_import import create_movexy_2dlist
from mask_import import create_cpmask_pngtxt

def main01_create_scheme(
        lowerx_x: float,    # lower x boundary of the tissue scan               float / int
        upperx_a: float,    # upper x boundary of the tissue scan               float / int
        lowery_y: float,    # lower y boundary of the tissue scan               float / int
        uppery_b: float,    # upper y boundary of the tissue scan               float / int
        subgrp_w: int,      # number of subgroups, left-right                   int             >=1
        subgrp_h: int,      # number of subgroups, top-bottom                   int             >=1
        subgrp_g: float,    # distance between adjacent subgroups               float / int     >=0
        region_n: int,      # number of FOV scans, on one side of a subgroup    int             >=1
                            # (i.e. a 4x4 subgroup should have region_n = 4)
        region_s: float,    # xy size of FOV scans in given units               float / int     > 0
        region_d: float,    # distance between adjacent FOV scans               float / int     >=0
):
    """
    Return the xy delta values of a scan scheme in a 2D list.

    x : lower x boundary of the tissue scan.
    a : upper x boundary of the tissue scan.
    y : lower y boundary of the tissue scan.
    b : upper y boundary of the tissue scan.
    w : number of subgroups, left-right.
    h : number of subgroups, top-bottom.
    g : gap size between adjacent subgroups.
    n : number of FOV scans, on one side of a subgroup.
    s : xy size of FOV scans in given units.
    d : gap size between adjacent FOV scans.
    """
    return create_movexy_2dlist(
        [lowerx_x, upperx_a],
        [lowery_y, uppery_b],
        subgrp_w,
        subgrp_h,
        subgrp_g,
        region_n,
        region_s,
        region_d,
        True,
        False
    )


def main02_create_cpmask(
        images_f: str,          # file path to the original image folder     (file path)
        gettxt_g: bool,         # save ImageJ txt files for masks            bool
        sample_d = None         # average (pixel) diameter for all cells     'None' / int
):
    """
    Create laser masks for all multichannel images stored in a folder using cellpose 2.

    f : file path to the original image folder.
    g : save ImageJ txt files for masks.
    d : average (pixel) diameter for all cells.
    """
    create_cpmask_pngtxt(images_f, gettxt_g, sample_d)
