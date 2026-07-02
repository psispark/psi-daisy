# ################################
# File:     file_input.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI FileInput component.
# Release:  v0.2
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260622, added variant
#   * version, who, when, why
# ################################

from fasthtml.common import Input
from ..utils import merge_classes, size_cls
from .types import Color, Size, FileInputVariant


def FileInput(*, color: Color = "primary", size: Size = "md", variant: FileInputVariant = "bordered", **kw):
    """DaisyUI file input component."""
    sz = size_cls("file-input", size)
    parts = ["file-input", f"file-input-{color}"]
    if variant: parts.append(f"file-input-{variant}")
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    return Input(type="file", cls=merge_classes(" ".join(parts), user_cls), **kw)
