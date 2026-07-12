# ################################
# File:     test_project.py
# Module:   tests
# Author:   lucien@psispark.com
# Task:     project/package sanity checks
# Release:  v0.1
# History:
#   * 001, luch, 260703, test
#   * version, who, when, why
# ################################

from pathlib import Path
import importlib, pytest  
import psi_daisy
import psi_daisy.ui as ui
from psi_daisy.config import STATIC_DIR, ICONS_DB, STATIC_UI_CSS_PATH, DAISYUI_CSS_PATH, DAISYUI_THEMES_CSS_PATH, TAILWIND_CSS_PATH

def _hdr_html(hdrs): return "".join(str(o) for o in hdrs)


def test_imports_from_checkout():
    """Tests import psi_daisy from this checkout, not site-packages."""
    root = Path(__file__).parents[1].resolve()
    assert Path(psi_daisy.__file__).resolve().is_relative_to(root)


@pytest.mark.parametrize("mod", ["examples.component_selector", "examples.theme_selector", "examples.icon_selector", "examples.theme_builder"])
def test_example_modules_import(mod):
    """Test example modules import cleanly."""
    assert importlib.import_module(mod)


def test_ui_all_exports_resolve():
    """Test 'All' UI exports resolve."""
    assert all(hasattr(ui, o) for o in ui.__all__)


def test_required_resources_exist():
    """Test required resource files exist."""
    assert (STATIC_DIR/"ui.css").exists()
    assert ICONS_DB.exists()


def test_get_ui_headers_cdn_mode():
    """Test CDN mode loads DaisyUI, themes, and Tailwind."""
    html = _hdr_html(ui.get_ui_headers(css="cdn"))
    assert DAISYUI_CSS_PATH in html
    assert DAISYUI_THEMES_CSS_PATH in html
    assert TAILWIND_CSS_PATH in html
    assert STATIC_UI_CSS_PATH not in html

def test_get_ui_headers_static_mode():
    """Test static mode loads bundled CSS without CDN CSS."""
    html = _hdr_html(ui.get_ui_headers(css="static"))
    assert STATIC_UI_CSS_PATH in html
    assert DAISYUI_CSS_PATH not in html
    assert DAISYUI_THEMES_CSS_PATH not in html
    assert TAILWIND_CSS_PATH not in html

def test_psi_app_passes_css_mode(monkeypatch):
    """Test psi_app passes theme and css mode to get_ui_headers."""
    import psi_daisy.app as app_mod
    seen = {}
    def fake_headers(theme="light", css="cdn"):
        seen.update(theme=theme, css=css)
        return []
    monkeypatch.setattr(app_mod, "get_ui_headers", fake_headers)
    app_mod.psi_app(theme="dark", css="static")
    assert seen == dict(theme="dark", css="static")
