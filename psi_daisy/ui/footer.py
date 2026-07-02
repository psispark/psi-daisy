# ################################
# File:     footer.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Footer component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Footer as FHFooter
from ..utils import merge_classes

def Footer(*children, center: bool = False, **kw):
    """DaisyUI footer component."""
    root = "footer bg-neutral text-neutral-content p-10"
    if center: root += " footer-center"
    user_cls = kw.pop("cls", None)
    return FHFooter(*children, cls=merge_classes(root, user_cls), **kw)
