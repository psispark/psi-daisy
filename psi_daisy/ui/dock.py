# ################################
# File:     dock.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Dock component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes, size_cls
from .types import Size

def Dock(*items, size: Size = "md", **kw):
    """DaisyUI dock/bottom-nav. items are (icon, label) tuples or FT elements."""
    sz = size_cls("dock", size)
    root = f"dock {sz}".strip()
    user_cls = kw.pop("cls", None)
    def make(it):
        if isinstance(it, tuple):
            return Div(it[0], Div(it[1], cls="dock-label"))
        return Div(it)
    return Div(*[make(i) for i in items], cls=merge_classes(root, user_cls), **kw)
