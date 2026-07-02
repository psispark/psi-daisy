# ################################
# File:     label.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Label component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Label as FHLabel
from ..utils import merge_classes

def Label(*children, **kw):
    """DaisyUI label component."""
    user_cls = kw.pop("cls", None)
    return FHLabel(*children, cls=merge_classes("label", user_cls), **kw)
