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
from psi_daisy.ui import Button, Dropdown 
from psi_daisy.utils.constants import SAMPLE_ARGS, SAMPLE_CHILDREN
from psi_daisy.utils.introspect import all_components, get_component_fn, get_param_info, get_sample_call_args
from psi_daisy.utils import merge_classes
from psi_daisy.ui._picker import picker_select, get_date_picker_headers, get_time_picker_headers, get_datetime_picker_headers, get_color_picker_headers
from psi_daisy.ui.my_color import MyColor, valid_hex, color_name
from psi_daisy.ui.my_date import MyDate
from psi_daisy.ui.my_time import MyTime
from psi_daisy.ui.my_datetime import MyDatetime
from psi_daisy.themes import hex_to_rgb, hex_to_oklch, vals_to_css, parse_css_vars


def test_all_components_finds_button():
    """Test it finds component modules."""
    comps = all_components()
    test_comps = ["button", "card", "alert", "badge"]
    for comp in test_comps:
        assert comp in comps


def test_get_component_fn_finds_button():
    """Test it finds component function from component name."""
    assert get_component_fn("button") is Button


def test_get_component_fn_missing_returns_none():
    """Test missing component returns None."""
    assert get_component_fn("not_a_component") is None


def test_get_param_info_finds_button_literals():
    """Test it finds literal params from component signature."""
    pos_args,literal_params,bool_params,var_positional = get_param_info(Button)
    assert pos_args == [SAMPLE_ARGS["label"]]
    assert "color" in literal_params
    assert "size" in literal_params
    assert var_positional is False


def test_get_sample_call_args_button_renders():
    """Test it builds callable sample args for a component."""
    args,kw = get_sample_call_args(Button, "button", SAMPLE_ARGS, SAMPLE_CHILDREN)
    assert "btn" in to_xml(Button(*args, **kw))


def test_get_sample_call_args_required_kw():
    """Test it builds required keyword-only sample args."""
    fn = get_component_fn("tooltip")
    args,kw = get_sample_call_args(fn, "tooltip", SAMPLE_ARGS, SAMPLE_CHILDREN)
    assert "tip" in kw
    assert "tooltip" in to_xml(fn(*args, **kw))


def test_merge_classes_combines_values():
    """Test it combines class strings."""
    assert merge_classes("btn btn-primary", "w-full") == "btn btn-primary w-full"


def test_merge_classes_ignores_empty_values():
    """Test it ignores empty class values."""
    assert merge_classes("btn", None, "", "mt-2") == "btn mt-2"    


def test_color_helpers():
    """Test color validation and CSS color name lookup."""
    assert valid_hex("#1e90ff")
    assert not valid_hex("dodgerblue")
    assert color_name("#1e90ff") == "dodgerblue"


def test_theme_color_helpers():
    """Test theme color conversion helpers."""
    assert hex_to_rgb("#1e90ff") == "rgb(30, 144, 255)"
    assert hex_to_oklch("#1e90ff").startswith("oklch(")


def test_picker_headers_include_expected_js():
    "Test header scripts include required JS functions."""
    html = "".join(to_xml(o) for o in get_date_picker_headers() + get_time_picker_headers() + get_datetime_picker_headers() + get_color_picker_headers())
    assert "psiUpdateDatePicker" in html
    assert "psiUpdateTimePicker" in html
    assert "psiUpdateDatetimePicker" in html
    assert "psiUpdateColorPicker" in html
    assert "psiColorPickerWeb" in html


def test_parse_css_vars():
    """Test CSS variable parser extracts theme vars."""
    d = parse_css_vars(":root { --color-primary: #123456; --radius-box: 1rem; }")
    assert d["color-primary"] == "#123456"
    assert d["radius-box"] == "1rem"


def test_vals_to_css():
    """Test theme values render as CSS variables."""
    css = vals_to_css(dict(color_primary="#123456"))
    assert "--color-primary" in css
    assert "oklch(" in css


def test_picker_select():
    """Test picker select renders selected padded options."""
    html = to_xml(picker_select("Minute", "minute", range(3), 2, 2))
    assert 'name="minute"' in html
    assert '>02<' in html
    assert "selected" in html    


def test_dropdown_menu_attrs():
    """Test dropdown supports menu classes and attrs."""
    html = to_xml(Dropdown(Button("open"), "item", menu_cls="max-h-32", menu_kw=dict(data_test_menu=True)))
    assert "dropdown" in html
    assert "max-h-32" in html
    assert "data-test-menu" in html    


def test_custom_picker_outputs():
    """Test custom pickers render canonical hidden outputs."""
    assert 'name="date"' in to_xml(MyDate(year=2026, month=7, day=8))
    assert 'value="2026-07-08"' in to_xml(MyDate(year=2026, month=7, day=8))
    assert 'value="01:02:03"' in to_xml(MyTime(hour=1, minute=2, second=3))
    assert 'value="2026-07-08T01:02:03"' in to_xml(MyDatetime(year=2026, month=7, day=8, hour=1, minute=2, second=3))


def test_my_color_wires_picker_js():
    """Test MyColor wires picker JS and dropdown menu."""
    html = to_xml(MyColor(show_outputs=True))
    assert "psiColorPickerPick" in html
    assert "psiColorPickerWeb" in html
    assert "data-color-menu" in html
    assert "data-color-name" in html


def test_date_picker_js_updates_output_and_days():
    """Test date picker JS updates days and hidden output."""
    html = "".join(to_xml(o) for o in get_date_picker_headers())
    assert "function psiDaysInMonth" in html
    assert "function psiUpdateDatePicker" in html
    assert "data-date-output" in html
    assert "d.innerHTML = \"\"" in html
    assert "padStart(4" in html
    assert "padStart(2" in html


def test_time_picker_js_updates_output():
    """Test time picker JS updates hidden output."""
    html = "".join(to_xml(o) for o in get_time_picker_headers())
    assert "function psiUpdateTimePicker" in html
    assert "data-time-output" in html
    assert "padStart(2" in html
    assert "`${h.value.padStart" in html


def test_datetime_picker_js_combines_date_and_time():
    """Test datetime picker JS combines date and time outputs."""
    html = "".join(to_xml(o) for o in get_datetime_picker_headers())
    assert "function psiUpdateDatetimePicker" in html
    assert "data-date-output" in html
    assert "data-time-output" in html
    assert "data-datetime-output" in html
    assert "`${date.value}T${time.value}`" in html


def test_color_picker_js_updates_outputs_and_menu():
    """Test color picker JS updates outputs and lazy menu."""
    html = "".join(to_xml(o) for o in get_color_picker_headers())
    assert "function psiUpdateColorPicker" in html
    assert "function psiColorPickerPick" in html
    assert "function psiColorPickerWeb" in html
    assert "window.psiColorNames" in html
    assert "window.psiColorList" in html
    assert "data-color-name" in html
    assert "data-color-menu" in html
