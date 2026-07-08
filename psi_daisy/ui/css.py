# ################################
# File:     css.py
# Module:   ui
# Author:   lucien@psispark.com
# Task:     Provide Tailwind + DaisyUI CSS loader for this framework.
# Release:  v0.1
# History:
#   * 001, luch, 260512, build
#   * 002, luch, 260608, add themes
# ################################

from fasthtml.common import Link, Script, Style
from typing import Any
from psi_daisy.config import DAISYUI_CSS_PATH, DAISYUI_THEMES_CSS_PATH, TAILWIND_CSS_PATH, \
                         CALLY_JS_PATH, LUCIDE_JS_PATH     


def get_ui_headers(theme: str = "light") -> list[Any]:
    "Return UI headers for the given theme."
    return [Link(rel="stylesheet", href=DAISYUI_CSS_PATH),
            Link(rel="stylesheet", href=DAISYUI_THEMES_CSS_PATH),
            Script(src=TAILWIND_CSS_PATH),
            Script(type="module", src=CALLY_JS_PATH), 

            Script(src=LUCIDE_JS_PATH),
            Script("""
                document.addEventListener('DOMContentLoaded', () => lucide.createIcons());
                document.addEventListener('htmx:afterSwap', () => lucide.createIcons()); """), ]
