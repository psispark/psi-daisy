# ################################
# File:     diff.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Diff component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def Diff(item1, item2, **kw):
    """DaisyUI diff component."""
    user_cls = kw.pop("cls", None)
    return Div(
        Div(item1, cls="diff-item-1"),
        Div(item2, cls="diff-item-2"),
        Div(cls="diff-resizer"),
        cls=merge_classes("diff aspect-16/9", user_cls), **kw)
