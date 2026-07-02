# ################################
# File:     textarea.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Textarea component.
# Release:  v0.2
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260622, added variant
#   * version, who, when, why
# ################################

from fasthtml.common import Textarea as FHTextarea
from ..utils import merge_classes, size_cls
from .types import Color, Size, TextareaVariant


def Textarea(value: str = "", *, color: Color = "primary", size: Size = "md", variant: TextareaVariant = "bordered", **kw):
    """DaisyUI textarea component."""
    sz = size_cls("textarea", size)
    parts = ["textarea", f"textarea-{color}"]
    if variant: parts.append(f"textarea-{variant}")
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    return FHTextarea(value, cls=merge_classes(" ".join(parts), user_cls), **kw)
