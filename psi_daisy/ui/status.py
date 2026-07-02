# ################################
# File:     status.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Status component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes, size_cls
from .types import Color, Size

def Status(*, color: Color = "primary", size: Size = "md", **kw):
    """DaisyUI status indicator component."""
    sz = size_cls("status", size)
    parts = ["status", f"status-{color}"]
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    return Div(cls=merge_classes(" ".join(parts), user_cls), **kw)
