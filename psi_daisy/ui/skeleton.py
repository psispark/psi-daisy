# ################################
# File:     skeleton.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Skeleton component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def Skeleton(*, w: str = "w-full", h: str = "h-4", **kw):
    """DaisyUI skeleton component."""
    user_cls = kw.pop("cls", None)
    return Div(cls=merge_classes("skeleton", w, h, user_cls), **kw)
