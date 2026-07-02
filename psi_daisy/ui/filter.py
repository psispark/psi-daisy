# ################################
# File:     filter.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Filter component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Input, Label
from ..utils import merge_classes

def Filter(*options, name: str = "filter", **kw):
    """DaisyUI filter component. options are (value, label) tuples."""
    user_cls = kw.pop("cls", None)
    reset = Input(type="radio", name=name, aria_label="All", cls="btn filter-reset")
    items = [Label(Input(type="radio", name=name, value=v), label) for v, label in options]
    return Div(reset, *items, cls=merge_classes("filter", user_cls), **kw)
