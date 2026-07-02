# ################################
# File:     link.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Link component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import A
from ..utils import merge_classes
from .types import Color

def Link(text: str, href: str = "#", *, color: Color = "primary", hover: bool = False, **kw):
    """DaisyUI link component."""
    parts = ["link", f"link-{color}"]
    if hover: parts.append("link-hover")
    user_cls = kw.pop("cls", None)
    return A(text, href=href, cls=merge_classes(" ".join(parts), user_cls), **kw)
