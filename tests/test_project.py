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
from psi_daisy.config import STATIC_DIR, ICONS_DB


def test_imports_from_checkout():
    """Tests import psi_daisy from this checkout, not site-packages"""
    root = Path(__file__).parents[1].resolve()
    assert Path(psi_daisy.__file__).resolve().is_relative_to(root)


@pytest.mark.parametrize("mod", ["examples.component_selector", "examples.theme_selector", "examples.icon_selector", "examples.theme_builder"])
def test_example_modules_import(mod):
    """Test example modules import cleanly"""
    assert importlib.import_module(mod)


def test_ui_all_exports_resolve():
    """Test 'All' UI exports resolve"""
    assert all(hasattr(ui, o) for o in ui.__all__)


def test_required_resources_exist():
    """Test required resource files exist"""
    assert (STATIC_DIR/"ui.css").exists()
    assert ICONS_DB.exists()
    