# ################################
# File:     checkbox.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Checkbox component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Input
from ..utils import merge_classes, size_cls
from .types import Color, Size

def Checkbox(*, color: Color = "primary", size: Size = "md", checked: bool = False, **kw):
    """DaisyUI checkbox component."""
    sz = size_cls("checkbox", size)
    parts = ["checkbox", f"checkbox-{color}"]
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    return Input(type="checkbox", checked=checked, cls=merge_classes(" ".join(parts), user_cls), **kw)
