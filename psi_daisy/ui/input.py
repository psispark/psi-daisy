# ################################
# File:     input.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Input component.
# Release:  v0.2
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260622, added variant
#   * version, who, when, why
# ################################

from fasthtml.common import Input as FHInput
from ..utils import merge_classes, size_cls
from .types import Color, Size, InputVariant


def Input(*, color: Color = "primary", size: Size = "md", variant: InputVariant = "bordered", **kw):
    """DaisyUI input component."""
    sz = size_cls("input", size)
    parts = ["input", f"input-{color}"]
    if variant: parts.append(f"input-{variant}")
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    return FHInput(cls=merge_classes(" ".join(parts), user_cls), **kw)
