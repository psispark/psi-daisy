# ################################
# File:     mockup_phone.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI MockupPhone component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def MockupPhone(*children, **kw):
    """DaisyUI phone mockup component."""
    user_cls = kw.pop("cls", None)
    return Div(Div(Div(*children), cls="mockup-phone-display"),
               cls=merge_classes("mockup-phone", user_cls), **kw)
