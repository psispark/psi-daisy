# ################################
# File:     pagination.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Pagination component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Button
from ..utils import merge_classes

def Pagination(pages: int, current: int = 1, **kw):
    """DaisyUI pagination component."""
    user_cls = kw.pop("cls", None)
    items = [Button(str(i), cls="join-item btn btn-active" if i == current else "join-item btn")
             for i in range(1, pages + 1)]
    return Div(*items, cls=merge_classes("join", user_cls), **kw)
