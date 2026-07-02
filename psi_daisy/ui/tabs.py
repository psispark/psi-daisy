# ################################
# File:     tab.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Tabs component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260623, added variant
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes, size_cls
from .types import Size, TabsVariant

def Tabs(*tabs, active: int = 0, size: Size = "md", variant: TabsVariant = "", **kw):
    """DaisyUI tabs component. tabs is a list of (label, content) tuples."""
    sz = size_cls("tabs", size)
    parts = ["tabs"]
    if variant: parts.append(f"tabs-{variant}")
    if sz: parts.append(sz)
    user_cls = kw.pop("cls", None)
    items = [Div(label, cls="tab tab-active" if i == active else "tab") for i, (label, _) in enumerate(tabs)]
    return Div(*items, cls=merge_classes(" ".join(parts), user_cls), **kw)
