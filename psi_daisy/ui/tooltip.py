# ################################
# File:     tooltip.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Tooltip component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes
from .types import Color, Position

def Tooltip(*children, tip: str, color: Color = "primary", position: Position = "top", **kw):
    """DaisyUI tooltip component."""
    pos_cls = {"top":"","bottom":"tooltip-bottom","left":"tooltip-left","right":"tooltip-right"}.get(position,"")
    parts = ["tooltip", f"tooltip-{color}"]
    if pos_cls: parts.append(pos_cls)
    user_cls = kw.pop("cls", None)
    return Div(*children, data_tip=tip, cls=merge_classes(" ".join(parts), user_cls), **kw)
