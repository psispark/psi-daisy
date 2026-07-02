# ################################
# File:     fab.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI FAB component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Button
from ..utils import merge_classes
from .types import FABPosition

def FAB(icon, *actions, position: FABPosition = "bottom-right", **kw):
    """DaisyUI floating action button. actions are FT elements."""
    pos = {"bottom-right":"bottom-4 right-4","bottom-left":"bottom-4 left-4",
           "top-right":"top-4 right-4","top-left":"top-4 left-4"}.get(position,"bottom-4 right-4")
    user_cls = kw.pop("cls", None)
    return Div(
        Div(*actions, cls="dropdown-content mb-2 flex flex-col gap-2"),
        Button(icon, cls="btn btn-circle btn-primary"),
        cls=merge_classes(f"fixed {pos} dropdown dropdown-top dropdown-end", user_cls), **kw)
