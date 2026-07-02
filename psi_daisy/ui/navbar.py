# ################################
# File:     navbar.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Navbar component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def Navbar(start=None, center=None, end=None, **kw):
    """DaisyUI navbar component."""
    user_cls = kw.pop("cls", None)
    children = []
    if start:  children.append(Div(start,  cls="navbar-start"))
    if center: children.append(Div(center, cls="navbar-center"))
    if end:    children.append(Div(end,    cls="navbar-end"))
    return Div(*children, cls=merge_classes("navbar bg-base-100", user_cls), **kw)
