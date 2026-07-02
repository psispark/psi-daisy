# ################################
# File:     timeline.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Timeline component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Ul, Li, Div, Hr
from ..utils import merge_classes
from .types import Orientation

def Timeline(*items, orientation: Orientation = "vertical", snap: bool = False, **kw):
    """DaisyUI timeline. items are (start, middle, end) tuples."""
    root = "timeline"
    if orientation == "horizontal": root += " timeline-horizontal"
    if snap: root += " timeline-snap-icon"
    user_cls = kw.pop("cls", None)
    def make(it):
        start, middle, end = it if len(it) == 3 else (*it, "")
        return Li(Div(start, cls="timeline-start"), Hr(),
                  Div(middle, cls="timeline-middle"), Hr(),
                  Div(end, cls="timeline-end"))
    return Ul(*[make(i) for i in items], cls=merge_classes(root, user_cls), **kw)
