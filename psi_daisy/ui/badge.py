# ################################
# File:     badge.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Badge component.
# Release:  v0.2
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260622, added variant
#   * version, who, when, why
# ################################

from fasthtml.common import Span
from ..utils import merge_classes
from .types import Color, BadgeVariant


def Badge(text: str, *, color: Color = "primary", variant: BadgeVariant = "", **kw):
    """DaisyUI badge component."""
    parts = ["badge", f"badge-{color}"]
    if variant: parts.append(f"badge-{variant}")
    user_cls = kw.pop("cls", None)
    return Span(text, cls=merge_classes(" ".join(parts), user_cls), **kw)
