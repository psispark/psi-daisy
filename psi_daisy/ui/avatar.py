# ################################
# File:     avatar.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Avatar component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Div, Img
from ..utils import merge_classes

def Avatar(src: str, alt: str = "", *, online: bool = False, offline: bool = False,
           placeholder: bool = False, **kw):
    """DaisyUI avatar component."""
    root = "avatar"
    if online:    root += " avatar-online"
    elif offline: root += " avatar-offline"
    if placeholder: root += " avatar-placeholder"
    user_cls = kw.pop("cls", None)
    return Div(Div(Img(src=src, alt=alt, cls="rounded-full w-12")),
               cls=merge_classes(root, user_cls), **kw)
