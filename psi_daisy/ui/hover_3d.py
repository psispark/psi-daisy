# ################################
# File:     hover_3d.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Hover3D component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def Hover3D(*children, **kw):
    """DaisyUI hover-3d component."""
    user_cls = kw.pop("cls", None)
    return Div(Div(*children, cls="hover-3d-inner"),
               cls=merge_classes("hover-3d", user_cls), **kw)
