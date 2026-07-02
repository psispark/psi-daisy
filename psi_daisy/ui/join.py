# ################################
# File:     join.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Join component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes
from .types import Orientation

def Join(*children, orientation: Orientation = "horizontal", **kw):
    """DaisyUI join (group) component."""
    root = "join"
    if orientation == "vertical": root += " join-vertical"
    user_cls = kw.pop("cls", None)
    return Div(*children, cls=merge_classes(root, user_cls), **kw)
