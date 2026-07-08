# ################################
# File:     component_selector.py
# Module:   examples
# Author:   lucien@psispark.com
# Task:     psi-daisy component selector demo.
# Release:  v0.2
# History:
#   * 001, Luch, 260603, build
#   * 002, ai,   260607, refactor
#   * 003, Luch, 260608, fixed package path 
#   * 004, Luch, 260628, xtra header for my-date-picker
#   * 005, luch, 260708, add runner
# ################################

import itertools
from fasthtml.common import *
from psi_daisy import psi_app
from psi_daisy.ui import Button, Divider, get_date_picker_headers, get_time_picker_headers, get_datetime_picker_headers, get_color_picker_headers 
from psi_daisy.utils.introspect import get_component_fn, get_param_info, get_required_kw
from psi_daisy.utils.widgets import mk_theme_toggle, mk_comp_select, mk_args_panel
from psi_daisy.utils.constants import SAMPLE_CHILDREN


app = psi_app(hdrs=get_date_picker_headers() + get_time_picker_headers() + get_datetime_picker_headers() + get_color_picker_headers())
rt = app.route


def render_home():
    return Div(
        Div(
            H1(f"🔍 Component Explorer", cls="text-3xl font-bold text-base-content"),
            mk_theme_toggle(),
            cls="flex items-center mb-6"),
        Div(
            H2("Component", cls="text-lg font-semibold mb-3 text-gray-700 dark:text-gray-200"),
            Div(
                mk_comp_select(),
                Button("View",
                    hx_post="/render", hx_target="#display",
                    hx_include="#comp-sel,[name]",
                    hx_on__htmx_before_request="document.getElementById('display').innerHTML=''"),
                cls="flex gap-3 items-center"),
            cls="flex flex-col"),
        Div(
            Divider(),
            H2("Options", cls="text-lg font-semibold mb-2 text-gray-700 dark:text-gray-200"),
            mk_args_panel(),
            cls="flex flex-col"),
        Div(
            Divider(),
            H2("Result", cls="text-lg font-semibold mb-2 text-gray-700 dark:text-gray-200"),
            Div(id="display", cls="mt-4"),
            cls="flex flex-col"),
        cls="p-10 max-w-6xl mx-auto bg-base-100 min-h-screen transition-colors"
    )


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
            cards.append(
                Div(result,
                    P(label or component, cls="text-xs text-gray-400 dark:text-gray-500 mt-2"),
                    cls="tooltip tooltip-bottom p-4 border border-gray-100 dark:border-gray-700 rounded-lg flex flex-col items-start gap-1",
                    data_tip=f"{cname}({label})" if label else f"{cname}()"))
        except Exception as e:
            cards.append(
                Div(
                    P(f"⚠️ {e}", cls="text-xs text-red-500"),
                    P(label, cls="text-xs text-gray-400 dark:text-gray-500"),
                    cls="p-4 border border-red-200 dark:border-red-800 rounded-lg"))
    return Div(*cards, cls="flex flex-wrap gap-4")


@rt("/")
def get(): return render_home()


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
    component = form.get("component", "button")
    res = render_combinations(component, form)
    return (res, Script("setTimeout(() => lucide.createIcons(), 0)")) if component == "MyIcon" else res


def run(host:str="0.0.0.0", port:int=8001):
    """Runner to launch example from py."""
    import uvicorn
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__": run()
