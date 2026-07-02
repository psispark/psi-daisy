# ################################
# File:     list.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI List component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def List(*items, **kw):
    """DaisyUI list. items are (title, desc) tuples or FT elements."""
    user_cls = kw.pop("cls", None)
    def make(it):
        if isinstance(it, tuple):
            return Div(Div(it[0], cls="font-medium"),
                       Div(it[1], cls="text-sm text-base-content/70") if len(it) > 1 else None,
                       cls="list-row")
        return Div(it, cls="list-row")
    return Div(*[make(i) for i in items],
               cls=merge_classes("list bg-base-100 rounded-box shadow-md", user_cls), **kw)
