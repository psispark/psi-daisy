# ################################
# File:     accordion.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Accordion component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Input
from ..utils import merge_classes
from .types import IconStyle

def Accordion(title: str, *children, name: str = "accordion", icon: IconStyle = "arrow",
              checked: bool = False, **kw):
    """DaisyUI accordion component."""
    icon_cls = {"arrow":"collapse-arrow","plus":"collapse-plus","none":""}.get(icon,"collapse-arrow")
    root = f"collapse bg-base-100 border border-base-300 {icon_cls}".strip()
    trigger = "collapse-title font-semibold"
    content = "collapse-content text-sm"
    user_cls = kw.pop("cls", None)
    return Div(
        Input(type="radio", name=name, checked=checked),
        Div(title, cls=trigger),
        Div(*children, cls=content),
        cls=merge_classes(root, user_cls), **kw)
