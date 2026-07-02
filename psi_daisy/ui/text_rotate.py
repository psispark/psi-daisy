# ################################
# File:     text_rotate.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI TextRotate component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def TextRotate(*texts, **kw):
    """DaisyUI text-rotate component."""
    user_cls = kw.pop("cls", None)
    return Div(*[Div(t, cls="text-rotate-item") for t in texts],
               cls=merge_classes("text-rotate", user_cls), **kw)
