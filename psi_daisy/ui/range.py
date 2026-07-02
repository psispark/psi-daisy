# ################################
# File:     range.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Range component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Input
from ..utils import merge_classes, size_cls
from .types import Color, Size

def Range(*, color: Color = "primary", size: Size = "md", min: int = 0, max: int = 100,
          value: int = 50, **kw):
    """DaisyUI range slider component."""
    sz = size_cls("range", size)
    parts = ["range", f"range-{color}"]
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    return Input(type="range", min=min, max=max, value=value,
                 cls=merge_classes(" ".join(parts), user_cls), **kw)
