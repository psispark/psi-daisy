# ################################
# File:     my_theme.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Generate custom Theme Picker component.
# Release:  v0.2
# History:
#   * 001, luch, 260812, build
# ################################

from fasthtml.common import Option
from . import Select
from ..themes import BUILTIN_THEMES, registered_themes
from ..utils import merge_classes


def _theme_sort_key(theme):
    theme = theme.lower()
    return (0, theme) if theme == "light" else (1, theme) if theme == "dark" else (2, theme)


def MyTheme(name:str="theme", current:str="light", id:str="theme-sel", **kw):
    "Custom selector that applies a theme to the page."
    user_cls = kw.pop("cls", None)
    themes = sorted(set(BUILTIN_THEMES) | set(registered_themes()), key=_theme_sort_key)
    opts = [Option(t.title() if t in BUILTIN_THEMES else t, value=t, selected=t == current) for t in themes]
    return Select(*opts, name=name, id=id, onchange="applyPageTheme(this.value)", cls=merge_classes("w-full max-w-xs", user_cls), **kw)
    