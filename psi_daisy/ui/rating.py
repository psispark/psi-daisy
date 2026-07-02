# ################################
# File:     rating.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Rating component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Input
from ..utils import merge_classes, size_cls
from .types import Size

def Rating(value: int = 0, max: int = 5, *, name: str = "rating", size: Size = "md",
           half: bool = False, **kw):
    """DaisyUI rating component."""
    sz = size_cls("rating", size)
    root = "rating"
    if half:     root += " rating-half"
    if sz: root += f" {sz}"
    user_cls = kw.pop("cls", None)
    items = [Input(type="radio", name=name, cls="mask mask-star-2 bg-orange-400", checked=(i+1 == value))
             for i in range(max)]
    return Div(*items, cls=merge_classes(root, user_cls), **kw)
