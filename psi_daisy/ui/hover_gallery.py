# ################################
# File:     hover_gallery.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI HoverGallery component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def HoverGallery(*items, **kw):
    """DaisyUI hover gallery component."""
    user_cls = kw.pop("cls", None)
    return Div(*[Div(item, cls="hover-gallery-item") for item in items],
               cls=merge_classes("hover-gallery", user_cls), **kw)
