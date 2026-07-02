# ################################
# File:     card.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Card component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def Card(*children, **kw):
    """DaisyUI card component."""
    user_cls = kw.pop("cls", None)
    return Div(*children, cls=merge_classes("card bg-base-100 shadow-xl", user_cls), **kw)
