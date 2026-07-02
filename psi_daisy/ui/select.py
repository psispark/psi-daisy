# ################################
# File:     select.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Select component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260622, added variant
#   * version, who, when, why
# ################################

from fasthtml.common import Select as FHSelect, Option
from ..utils import merge_classes, size_cls
from .types import Color, Size, SelectVariant


def Select(*options, color: Color = "primary", size: Size = "md", variant: SelectVariant = "bordered", **kw):
    """DaisyUI select component. Options are (value, label) tuples or FT elements."""
    sz = size_cls("select", size)
    parts = ["select", f"select-{color}"]
    if variant: parts.append(f"select-{variant}")
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    def make_opt(o): return Option(o[1], value=o[0]) if isinstance(o, tuple) else o
    return FHSelect(*[make_opt(o) for o in options], cls=merge_classes(" ".join(parts), user_cls), **kw)
