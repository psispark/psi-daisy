# ################################
# File:     indicator.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Indicator component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes
from .types import Color

def Indicator(content, badge, *, color: Color = "primary", **kw):
    """DaisyUI indicator component."""
    user_cls = kw.pop("cls", None)
    return Div(Div(badge, cls=f"indicator-item badge badge-{color}"), content,
               cls=merge_classes("indicator", user_cls), **kw)
