# ################################
# File:     stack.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Stack component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def Stack(*children, **kw):
    """DaisyUI stack component."""
    user_cls = kw.pop("cls", None)
    return Div(*children, cls=merge_classes("stack", user_cls), **kw)
