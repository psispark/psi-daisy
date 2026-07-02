# ################################
# File:     alert.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Alert component.
# Release:  v0.2
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260622, added variant
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes
from .types import Color, AlertVariant


def Alert(*children, color: Color = "info", variant: AlertVariant = "", **kw):
    """DaisyUI alert component."""
    parts = ["alert", f"alert-{color}"]
    if variant: parts.append(f"alert-{variant}")
    user_cls = kw.pop("cls", None)
    return Div(*children, role="alert", cls=merge_classes(" ".join(parts), user_cls), **kw)
