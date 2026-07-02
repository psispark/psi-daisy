# ################################
# File:     kbd.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Kbd component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Kbd as FHKbd
from ..utils import merge_classes, size_cls
from .types import Size

def Kbd(text: str, *, size: Size = "md", **kw):
    """DaisyUI kbd component."""
    sz = size_cls("kbd", size)
    parts = ["kbd"]
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    return FHKbd(text, cls=merge_classes(" ".join(parts), user_cls), **kw)
