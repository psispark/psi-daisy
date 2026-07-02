# ################################
# File:     mockup_browser.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI MockupBrowser component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div
from ..utils import merge_classes

def MockupBrowser(*children, url: str = "https://example.com", **kw):
    """DaisyUI browser mockup component."""
    user_cls = kw.pop("cls", None)
    return Div(Div(Div(url, cls="input"), cls="mockup-browser-toolbar"),
               Div(*children, cls="bg-base-200 flex justify-center px-4 py-16"),
               cls=merge_classes("mockup-browser bg-base-300 border", user_cls), **kw)
