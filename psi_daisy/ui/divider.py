# ################################
# File:     divider.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Divider component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes
from .types import Color, Orientation

def Divider(text: str = "", *, color: Color | None = None,
            orientation: Orientation = "horizontal", **kw):
    """DaisyUI divider component."""
    parts = ["divider"]
    if orientation == "vertical": parts.append("divider-vertical")
    if color: parts.append(f"divider-{color}")
    user_cls = kw.pop("cls", None)
    return Div(text or None, cls=merge_classes(" ".join(parts), user_cls), **kw)
