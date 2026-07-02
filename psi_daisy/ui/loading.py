# ################################
# File:     loading.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Loading component.
# Release:  v0.2
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260623, added variant 
#   * version, who, when, why
# ################################

from fasthtml.common import Span
from ..utils import merge_classes, size_cls
from .types import Color, Size, LoadingVariant 


def Loading(*, color: Color = "primary", size: Size = "md", variant: LoadingVariant = "spinner", **kw):
    """DaisyUI loading component."""
    sz = size_cls("loading", size)
    parts = ["loading", f"loading-{variant}", f"text-{color}"]
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    return Span(cls=merge_classes(" ".join(parts), user_cls), **kw)
