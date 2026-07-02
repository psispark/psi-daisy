# ################################
# File:     collapse.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Collapse component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Input
from ..utils import merge_classes
from .types import IconStyle

def Collapse(title: str, *children, icon: IconStyle = "arrow", **kw):
    """DaisyUI collapse component."""
    icon_cls = {"arrow":"collapse-arrow","plus":"collapse-plus","none":""}.get(icon,"collapse-arrow")
    root = f"collapse bg-base-200 {icon_cls}".strip()
    user_cls = kw.pop("cls", None)
    return Div(
        Input(type="checkbox"),
        Div(title, cls="collapse-title font-medium"),
        Div(*children, cls="collapse-content"),
        cls=merge_classes(root, user_cls), **kw)
