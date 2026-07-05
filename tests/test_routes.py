# ################################
# File:     test_routes.py
# Module:   tests
# Author:   lucien@psispark.com
# Task:     test app wiring & routing
# Release:  v0.1
# History:
#   * 001, luch, 260703, test
#   * version, who, when, why
# ################################

from fasthtml.common import to_xml
from examples.theme_selector import render_home as theme_rh, render_combinations as theme_rc
from examples.component_selector import render_home as comp_rh, render_combinations as comp_rc
from examples.icon_selector import render_home as icon_rh, render_results as icon_rr, search_icons as icon_si
from examples.theme_builder import get as theme_builder_get, mk_preview_area, mk_vars_table, mk_css_block


def test_theme_selector_home_renders():
    """Test theme selector's home renders"""
    html = to_xml(theme_rh())
    assert "Theme Explorer" in html
    assert "Component" in html
    assert "Result" in html


def test_theme_selector_unknown_component_renders_error():
    """Test an unknown component renders an error message"""
    html = to_xml(theme_rc("not_a_component", {}))
    assert "not_a_component" in html
    assert "text-error" in html


def test_component_selector_home_renders():
    """Test component selector's home renders"""
    html = to_xml(comp_rh())
    assert "Component Explorer" in html
    assert "Component" in html
    assert "Result" in html


def test_component_selector_unknown_component_renders_error():
    """Test an unknown component renders an error message"""
    html = to_xml(comp_rc("not_a_component", {}))
    assert "not_a_component" in html
    assert "text-error" in html


def test_icon_selector_home_renders():
    """Test icon selector's home renders"""
    html = to_xml(icon_rh())
    assert "Icon Selector" in html
    assert "Search" in html
    assert "Result" in html


def test_icon_selector_empty_results_renders():
    """Test icon selector empty results renders"""
    html = to_xml(icon_rr([]))
    assert "No icons found" in html


def test_icon_selector_search_icons_runs():
    """Test icon search runs against bundled db"""
    rows = icon_si("lightbulb", 3)
    assert len(rows) <= 3


def test_theme_builder_home_renders():
    """Test theme builder's home route renders"""
    html = to_xml(theme_builder_get())
    assert "Theme Builder" in html
    assert "Variables" in html
    assert "Preview" in html


def test_theme_builder_preview_parts_render():
    """Test theme builder preview helpers render"""
    assert "preview-area" in to_xml(mk_preview_area(""))
    assert "vars-table" in to_xml(mk_vars_table())
    assert "css-block" in to_xml(mk_css_block(""))  
  