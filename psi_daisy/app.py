# ################################
# File:     app.py
# Module:   psi_daisy
# Author:   lucien@psispark.com
# Task:     Initialize FastHTML app with the UI CSS.
# Release:  v0.2
# History:
#   * 001, luch, 260603, build
#   * 002, luch, 260628, add hdrs arg to pass in xtra headers
#   * version, who, when, why
# ################################

from fasthtml import FastHTML as fast_app
from starlette.staticfiles import StaticFiles

from psi_daisy.config import STATIC_DIR
from psi_daisy.ui import get_ui_headers 


def psi_app(*, theme: str = "light", hdrs=None, **kw):
    """Create a FastHTML app with the UI CSS loaded."""
    hdrs = get_ui_headers(theme) + (hdrs or [])

    app = fast_app(hdrs=hdrs, htmlkw={"data-theme": theme}, **kw)
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
    return app
