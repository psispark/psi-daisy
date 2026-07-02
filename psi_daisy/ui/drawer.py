# ################################
# File:     drawer.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Drawer component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Input, Label
from ..utils import merge_classes

def Drawer(content, sidebar, *, id: str = "drawer", end: bool = False, **kw):
    """DaisyUI drawer component."""
    root = "drawer"
    if end: root += " drawer-end"
    user_cls = kw.pop("cls", None)
    return Div(
        Input(id=id, type="checkbox", cls="drawer-toggle"),
        Div(content, cls="drawer-content"),
        Div(Label(htmlfor=id, cls="drawer-overlay"),
            sidebar,
            cls="drawer-side"),
        cls=merge_classes(root, user_cls), **kw)
