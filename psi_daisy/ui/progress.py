# ################################
# File:     progress.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate DaisyUI Progress component.
# Release:  v0.1
# History:
#   * 001, luch, 260603, build
#   * version, who, when, why
# ################################

from fasthtml.common import Progress as FHProgress
from ..utils import merge_classes
from .types import Color

def Progress(value: int = 0, max: int = 100, *, color: Color = "primary", **kw):
    """DaisyUI progress component."""
    user_cls = kw.pop("cls", None)
    return FHProgress(value=value, max=max,
                      cls=merge_classes(f"progress progress-{color} w-full", user_cls), **kw)
