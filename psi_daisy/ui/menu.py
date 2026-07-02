# ################################
# File:     menu.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Menu component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Ul, Li, A
from ..utils import merge_classes, size_cls
from .types import Size

def Menu(*items, size: Size = "md", horizontal: bool = False, **kw):
    """DaisyUI menu component. Each item is a tuple (label, href) or an FT element."""
    sz = size_cls("menu", size)
    root = "menu"
    if horizontal: root += " menu-horizontal"
    if sz:   root += f" {sz}"
    user_cls = kw.pop("cls", None)
    def make_item(it):
        if isinstance(it, tuple): return Li(A(it[0], href=it[1]))
        return Li(it)
    return Ul(*[make_item(i) for i in items], cls=merge_classes(root, user_cls), **kw)
