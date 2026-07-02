# ################################
# File:     carousel.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Carousel component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes
from .types import Orientation, SnapAlign

def Carousel(*items, orientation: Orientation = "horizontal", snap: SnapAlign = "start", **kw):
    """DaisyUI carousel component."""
    root = "carousel"
    if orientation == "vertical": root += " carousel-vertical"
    snap_cls = {"start":"carousel-start","center":"carousel-center","end":"carousel-end"}.get(snap,"carousel-start")
    root += f" {snap_cls}"
    user_cls = kw.pop("cls", None)
    return Div(*[Div(item, cls="carousel-item") for item in items],
               cls=merge_classes(root, user_cls), **kw)
