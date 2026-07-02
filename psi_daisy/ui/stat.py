# ################################
# File:     stat.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Stat component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def Stat(title: str, value: str, desc: str = "", figure=None, **kw):
    """DaisyUI stat component."""
    user_cls = kw.pop("cls", None)
    children = [Div(title, cls="stat-title"), Div(value, cls="stat-value")]
    if figure: children.insert(0, Div(figure, cls="stat-figure"))
    if desc:   children.append(Div(desc, cls="stat-desc"))
    return Div(Div(*children, cls="stat"), cls=merge_classes("stats shadow", user_cls), **kw)
