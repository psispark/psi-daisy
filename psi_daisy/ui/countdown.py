# ################################
# File:     countdown.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Countdown component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Span
from ..utils import merge_classes
from .types import Size

def Countdown(*values, labels=None, size: Size = "md", **kw):
    """DaisyUI countdown. values are ints (h, m, s etc)."""
    size_map = {"xs":"text-2xl","sm":"text-4xl","md":"text-5xl","lg":"text-7xl"}
    item_cls = f"countdown font-mono {size_map.get(size,'text-5xl')}"
    user_cls = kw.pop("cls", None)
    labels = labels or []
    def make(v, label=None):
        inner = Div(Span(style=f"--value:{v}"), cls=item_cls)
        return Div(inner, Div(label) if label else None)
    items = [make(v, labels[i] if i < len(labels) else None) for i, v in enumerate(values)]
    return Div(*items, cls=merge_classes("flex gap-5", user_cls), **kw)
