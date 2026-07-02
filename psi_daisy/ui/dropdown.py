# ################################
# File:     dropdown.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Dropdown component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Ul
from ..utils import merge_classes
from .types import Position

def Dropdown(trigger, *items, position: Position = "bottom", **kw):
    """DaisyUI dropdown component."""
    pos_cls = {"bottom":"dropdown-bottom","top":"dropdown-top","left":"dropdown-left","right":"dropdown-right"}.get(position,"dropdown-bottom")
    user_cls = kw.pop("cls", None)
    return Div(trigger,
               Ul(*items, cls="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"),
               cls=merge_classes(f"dropdown {pos_cls}", user_cls), **kw)
