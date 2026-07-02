# ################################
# File:     swap.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Swap component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Label, Input, Div
from ..utils import merge_classes

def Swap(on, off, *, rotate: bool = False, flip: bool = False, **kw):
    """DaisyUI swap component."""
    root = "swap"
    if rotate: root += " swap-rotate"
    if flip:   root += " swap-flip"
    user_cls = kw.pop("cls", None)
    return Label(Input(type="checkbox"),
                 Div(on,  cls="swap-on"),
                 Div(off, cls="swap-off"),
                 cls=merge_classes(root, user_cls), **kw)
