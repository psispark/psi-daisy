# ################################
# File:     test_utils.py
# Module:   tests
# Author:   lucien@psispark.com
# Task:     test helper funcs.
# Release:  v0.1
# History:
#   * 001, luch, 260704, test
#   * version, who, when, why
# ################################

from fasthtml.common import to_xml
from psi_daisy.ui import Button
from psi_daisy.utils.constants import SAMPLE_ARGS, SAMPLE_CHILDREN
from psi_daisy.utils.introspect import all_components, get_component_fn, get_param_info, get_sample_call_args
from psi_daisy.utils import merge_classes


def test_all_components_finds_button():
    """Test it finds component modules"""
    comps = all_components()
    test_comps = ["button", "card", "alert", "badge"]
    for comp in test_comps:
        assert comp in comps


def test_get_component_fn_finds_button():
    """Test it finds component function from component name"""
    assert get_component_fn("button") is Button


def test_get_component_fn_missing_returns_none():
    """Test missing component returns None"""
    assert get_component_fn("not_a_component") is None


def test_get_param_info_finds_button_literals():
    """Test it finds literal params from component signature"""
    pos_args,literal_params,bool_params,var_positional = get_param_info(Button)
    assert pos_args == [SAMPLE_ARGS["label"]]
    assert "color" in literal_params
    assert "size" in literal_params
    assert var_positional is False


def test_get_sample_call_args_button_renders():
    """Test it builds callable sample args for a component"""
    args,kw = get_sample_call_args(Button, "button", SAMPLE_ARGS, SAMPLE_CHILDREN)
    assert "btn" in to_xml(Button(*args, **kw))


def test_get_sample_call_args_required_kw():
    """Test it builds required keyword-only sample args"""
    fn = get_component_fn("tooltip")
    args,kw = get_sample_call_args(fn, "tooltip", SAMPLE_ARGS, SAMPLE_CHILDREN)
    assert "tip" in kw
    assert "tooltip" in to_xml(fn(*args, **kw))


def test_merge_classes_combines_values():
    """Test it combines class strings"""
    assert merge_classes("btn btn-primary", "w-full") == "btn btn-primary w-full"


def test_merge_classes_ignores_empty_values():
    """Test it ignores empty class values"""
    assert merge_classes("btn", None, "", "mt-2") == "btn mt-2"    
