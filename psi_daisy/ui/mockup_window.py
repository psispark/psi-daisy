# ################################
# File:     mockup_window.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI MockupWindow component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def MockupWindow(*children, **kw):
    """DaisyUI window mockup component."""
    user_cls = kw.pop("cls", None)
    return Div(Div(*children, cls="bg-base-200 flex justify-center px-4 py-16"),
               cls=merge_classes("mockup-window bg-base-300 border", user_cls), **kw)
