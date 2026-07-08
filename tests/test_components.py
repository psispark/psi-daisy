# ################################
# File:     test_components.py
# Module:   tests
# Author:   lucien@psispark.com
# Task:     psi-daisy component testing.
# Release:  v0.1
# History:
#   * 001, luch, 260703, test
#   * version, who, when, why
# ################################

import pytest, inspect 
from inspect import Parameter
from fasthtml.common import to_xml
from psi_daisy.ui import Button, Card, Alert, Badge
from psi_daisy.utils.introspect import all_components, get_component_fn, get_param_info, get_sample_call_args 
from psi_daisy.utils.constants import SAMPLE_ARGS, SAMPLE_CHILDREN, ROOT_CLASSES
from examples.component_selector import render_combinations as component_render_combinations
from examples.theme_selector import render_combinations as theme_render_combinations


def test_basic_components_render(): 
    """1st quick component rendering smoke test"""
    comps = [Button("Click"), Card("Body"), Alert("Heads up"), Badge("New")]
    assert all(to_xml(o) for o in comps)


def test_basic_components_have_classes():
    """Test components have their DaisyUI class"""
    comps = dict(button=Button("Click"), card=Card("Body"), alert=Alert("Heads up"), badge=Badge("New"))
    for cls, o in comps.items(): assert cls in to_xml(o)


def test_button_variants_render_classes():
    """Test button variants add expected DaisyUI classes"""
    html = to_xml(Button("Save", color="secondary", size="lg", variant="outline"))
    assert "btn" in html
    assert "btn-secondary" in html
    assert "btn-lg" in html
    assert "btn-outline" in html


def test_button_merges_user_classes():
    """Test button keeps custom classes"""
    html = to_xml(Button("Save", cls="w-full"))
    assert "btn" in html and "w-full" in html


def test_button_passes_attrs():
    """Test button passes HTML attrs through"""
    html = to_xml(Button("Save", id="save-btn", type="submit"))
    assert 'id="save-btn"' in html
    assert 'type="submit"' in html


def test_badge_variants_render_classes():
    """Test badge variants add expected DaisyUI classes"""
    html = to_xml(Badge("New", color="accent", variant="outline"))
    assert "badge" in html
    assert "badge-accent" in html
    assert "badge-outline" in html


@pytest.mark.parametrize("component", all_components())
def test_all_component_sample_args_render(component):
    """Test all components render with generated sample args"""
    fn = get_component_fn(component)
    args,kw = get_sample_call_args(fn, component, SAMPLE_ARGS, SAMPLE_CHILDREN)
    assert to_xml(fn(*args, **kw))


def test_get_sample_call_args_returns_args_and_kwargs():
    """Test sample arg helper still returns callable args and kwargs"""
    args,kw = get_sample_call_args(Button, "button", SAMPLE_ARGS, SAMPLE_CHILDREN)
    html = to_xml(Button(*args, **kw))
    assert "btn" in html


@pytest.mark.parametrize("component", all_components())
def test_component_selector_renders_all_components(component):
    """Test component selector renders every component"""
    html = to_xml(component_render_combinations(component, {}))
    assert html
    assert "⚠️" not in html
    assert "text-error" not in html


@pytest.mark.parametrize("component", all_components())
def test_theme_selector_renders_all_components(component):
    """Test theme selector renders every component."""
    html = to_xml(theme_render_combinations(component, {}))
    assert html
    assert "⚠️" not in html
    assert "text-error" not in html


@pytest.mark.parametrize("component,checks", ROOT_CLASSES.items())
def test_component_output_structure(component, checks):
    """Test components render expected structural classes and attrs"""
    fn = get_component_fn(component)
    args,kw = get_sample_call_args(fn, component, SAMPLE_ARGS, SAMPLE_CHILDREN)
    html = to_xml(fn(*args, **kw))
    assert all(o in html for o in checks)


@pytest.mark.parametrize("component", all_components())
def test_required_params_have_sample_args(component):
    """Test required non-child params have sample args"""
    fn = get_component_fn(component)
    sig = inspect.signature(fn)
    missing = [p.name for p in sig.parameters.values() if p.default is Parameter.empty and p.kind not in (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD) and p.name not in SAMPLE_ARGS]
    assert not missing


@pytest.mark.parametrize("component", all_components())
def test_variadic_components_have_sample_children(component):
    """Test variadic components have sample children"""
    fn = get_component_fn(component)
    *_, var_positional = get_param_info(fn)
    assert not var_positional or component in SAMPLE_CHILDREN
