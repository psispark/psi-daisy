# ################################
# File:     diff.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Diff component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260708, convert to Figure
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Figure
from ..utils import merge_classes


def Diff(item1, item2, **kw):
    """DaisyUI diff component."""
    user_cls = kw.pop("cls", None)
    return Figure(
        Div(item1, cls="diff-item-1 w-full h-full", role="img", tabindex="0"),
        Div(item2, cls="diff-item-2 w-full h-full", role="img"),
        Div(cls="diff-resizer"),
        cls=merge_classes("diff aspect-16/9 w-full max-w-md", user_cls), tabindex="0", **kw)
