# ################################
# File:     theme_selector.py
# Module:   examples
# Author:   lucien@psispark.com
# Task:     psi-daisy theme selector demo.
# Release:  v0.2
# History:
#   * 001, luch, 260608, build
#   * 002, luch, 260628, xtra header for my-date-picker
#   * 003, luch, 260708, add runner
# ################################

import itertools
from fasthtml.common import *
from psi_daisy import psi_app
from psi_daisy.ui import Button, Divider, get_date_picker_headers, get_time_picker_headers, get_datetime_picker_headers, get_color_picker_headers
from psi_daisy.utils.introspect import get_component_fn, get_param_info, get_required_kw
from psi_daisy.utils.widgets import mk_comp_select, mk_args_panel, mk_theme_select
from psi_daisy.utils.constants import SAMPLE_CHILDREN
from psi_daisy.themes import theme_script


app = psi_app(hdrs=get_date_picker_headers() + get_time_picker_headers() + get_datetime_picker_headers() + get_color_picker_headers())
rt = app.route


def render_home():
    return Div(
        Div(
            H1("🔍 Theme Explorer", cls="text-3xl font-bold text-base-content"),
            cls="flex items-center mb-6"),
        Div(
            H2("Theme", cls="text-lg font-semibold mb-3 text-base-content"),
            mk_theme_select(),
            cls="flex flex-col mb-4"),
        Div(
            H2("Component", cls="text-lg font-semibold mb-3 text-base-content"),
            Div(
                mk_comp_select(),
                Button("View", hx_post="/render", hx_target="#display",
                    hx_include="#comp-sel,#theme-sel,[name]",
                    hx_on__htmx_before_request="document.getElementById('display').innerHTML=''"),
                cls="flex gap-3 items-center"),
            cls="flex flex-col"),
        Div(
            Divider(),
            H2("Options", cls="text-lg font-semibold mb-2 text-base-content"),
            mk_args_panel(),
            cls="flex flex-col"),
        Div(
            Divider(),
            H2("Result", cls="text-lg font-semibold mb-2 text-base-content"),
            Div(id="display", cls="mt-4"),
            cls="flex flex-col"),
        cls="p-10 max-w-6xl mx-auto bg-base-100 min-h-screen transition-colors")


def render_combinations(component, form_data):
    fn = get_component_fn(component)
    cname = getattr(fn, "__name__", component)
    if fn is None: return P(f"Component '{component}' not found.", cls="text-error")
    pos_args, literal_params, bool_params, var_positional = get_param_info(fn)
    base_kw = get_required_kw(fn)
    selected = {}
    for pname, all_vals in literal_params.items():
        chosen = form_data.getlist(pname) if hasattr(form_data, 'getlist') else (
            [form_data[pname]] if pname in form_data else all_vals[:1])
        selected[pname] = all_vals if "__all__" in chosen else (chosen or all_vals[:1])
    bool_selected = {p: p in form_data for p in bool_params}
    keys = list(selected.keys())
    combos = list(itertools.product(*[selected[k] for k in keys])) if keys else [()]
    children = SAMPLE_CHILDREN.get(component, SAMPLE_CHILDREN["_default"])
    cards = []
    for combo in combos:
        kw = {**base_kw, **dict(zip(keys, combo)), **{p: True for p, v in bool_selected.items() if v}}
        label = ", ".join(f"{k}={v!r}" for k, v in zip(keys, combo))
        label += "".join(f", {p}" for p, v in bool_selected.items() if v)
        try:
            result = fn(*pos_args, *children, **kw) if var_positional else fn(*pos_args, **kw)
            cards.append(Div(result,
                P(label or component, cls="text-xs text-base-content/50 mt-2"),
                cls="tooltip tooltip-bottom p-4 border border-base-300 rounded-lg flex flex-col items-stretch gap-1 w-full max-w-md", 
                data_tip=f"{cname}({label})" if label else f"{cname}()"))
        except Exception as e:
            cards.append(Div(
                P(f"⚠️ {e}", cls="text-xs text-error"),
                P(label, cls="text-xs text-base-content/50"),
                cls="p-4 border border-error rounded-lg"))
    return Div(*cards, cls="flex flex-wrap gap-4")


@rt("/")
def get(): return theme_script(), render_home()


@rt("/update-args")
async def post(req):
    form = await req.form()
    component = form.get("component", "button")
    panel = mk_args_panel(component)
    fn = get_component_fn(component)
    _, literal_params, bool_params, _ = get_param_info(fn) if fn else ([], {}, [], False)
    inner = render_combinations(component, form) if fn and not literal_params and not bool_params else ""
    display = Div(inner, id="display", cls="mt-6", hx_swap_oob="true")
    return panel, display


@rt("/render")
async def post(req):
    form = await req.form()
    return render_combinations(form.get("component", "button"), form)


def run(host:str="0.0.0.0", port:int=8001):
    """Runner to launch example from py."""
    import uvicorn
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__": run()
