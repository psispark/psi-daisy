# ################################
# File:     theme_builder.py
# Module:   examples
# Author:   lucien@psispark.com
# Task:     psi-daisy custom theme builder demo.
# Release:  v0.2
# History:
#   * 001, ai, 260610, build
#   * 002, ai, 260610, fix oklch, seed from builtins, custom theme registry
#   * 003, ai, 260615, refactor
#   * 004, luch, 260708, add runner
# ################################

import json
from fasthtml.common import *
from psi_daisy import psi_app
from psi_daisy.ui import Button, Select, Input, Badge, MyColor, get_color_picker_headers  
from psi_daisy.config import THEMES_DIR
from psi_daisy.themes import (BUILTIN_THEMES, BUILTIN_VARS, CSS_VARS, registered_themes,
    load_custom_vars, save_theme, oklch_to_hex, hex_to_oklch, hex_to_rgb,
    vals_to_css, form_to_css, form_to_save_css, parse_css_vars, theme_script)


app = psi_app(hdrs=get_color_picker_headers())
rt = app.route


def mk_var_row(var, val):
    hex_val = oklch_to_hex(val)
    return Tr(
        Td(var, cls="text-xs font-mono py-0 pr-1 text-base-content/70 whitespace-nowrap"),
        Td(Input(type="color", value=hex_val, name=f"var_{var.replace('-','_')}",
            cls="w-10 h-8 cursor-pointer rounded border-0 p-0",
            hx_trigger="change", hx_post="/preview", hx_target="#preview-area",
            hx_include="[name^='var_'],[name='theme-name']")),
        Td(Code(val, cls="text-xs text-base-content/50 whitespace-nowrap", id=f"val-{var}")),
        Td(Code(hex_to_rgb(hex_val), cls="text-xs text-base-content/40 whitespace-nowrap"), cls="text-right"),
    )


def mk_vars_table(vals=None):
    vals = vals or BUILTIN_VARS.get('light', {})
    return Table(*[mk_var_row(v, vals.get(v, 'oklch(50% 0 0)')) for v in CSS_VARS],
        cls="table table-xs w-full", id="vars-table", style="table-layout:fixed")


def mk_css_block(css=""):
    return Pre(Code(css, cls="language-css text-xs"), id="css-block",
        cls="bg-base-200 rounded-lg p-4 overflow-auto max-h-screen text-xs font-mono whitespace-pre")


def mk_preview_area(css=""):
    return Div(
        Span(css, id="css-data", style="display:none"),
        Div(
            Div(
                Button("Primary"), Button("Secondary", color="secondary"),
                Button("Accent", color="accent"), Button("Ghost", variant="ghost"),
                cls="flex gap-2 flex-wrap mb-4"),
            Div(
                Div(H3("Card Title", cls="font-bold"), P("Card body text.", cls="text-sm"),
                    cls="card bg-base-100 border border-base-300 p-4 w-48"),
                Div(Badge("Badge"), Badge("Info", color="secondary"), cls="flex gap-2 mt-2"),
                cls="flex gap-4 items-start mb-4"),
            Div(
                Input(type="text", placeholder="Text input", cls="input input-bordered input-sm w-40"),
                Input(type="text", placeholder="Input error", cls="input input-bordered input-error input-sm w-40"),
                Select(Option("Select option"), cls="select select-bordered select-sm w-40"),
                cls="flex gap-2 flex-wrap mb-4"),
            Div(
                Div(P("Info"), cls="alert alert-info text-sm py-2 px-3 flex-1"),
                Div(P("Success"), cls="alert alert-success text-sm py-2 px-3 flex-1"),
                Div(P("Warning"), cls="alert alert-warning text-sm py-2 px-3 flex-1"),
                Div(P("Error"), cls="alert alert-error text-sm py-2 px-3 flex-1"),
                cls="flex gap-2 mb-4"),
            Table(
                Thead(Tr(Th("Name"), Th("Role"), Th("Status"))),
                Tbody(
                    Tr(Td("Alice"), Td("Admin"), Td("Active")),
                    Tr(Td("Bob"), Td("User"), Td("Inactive"))),
                cls="table table-sm w-full bg-base-100 rounded-lg"),
            **{"data-theme": "custom-preview"},
            cls="p-6 bg-base-200 rounded-xl min-h-40"),
        H2("CSS", cls="text-lg font-semibold mt-4 mb-2 text-base-content"),
        mk_css_block(css),
        id="preview-area")


BUILDER_JS = r"""
function highlightCSS(css) {
    return css
        .replace(/oklch\([^)]+\)/g, m => `<span style="color:var(--color-success)">${m}</span>`)
        .replace(/--[\w-]+/g, m => `<span style="color:var(--color-primary)">${m}</span>`)
        .replace(/\[data-theme=[^\]]*\]/g, m => `<span style="color:var(--color-accent)">${m}</span>`);
}
function syncPreviewCSS() {
    const d = document.getElementById('css-data');
    if (d) {
        document.getElementById('custom-theme-style').textContent = d.textContent;
        const cb = document.getElementById('css-block');
        if (cb) cb.querySelector('code').innerHTML = highlightCSS(d.textContent.replace(/</g,'&lt;'));
    }
}
syncPreviewCSS();
document.body.addEventListener('htmx:afterSwap', syncPreviewCSS);
function exportCSS() {
    const vars = Object.fromEntries([...document.querySelectorAll('[name^=var_]')].map(i => [i.name, i.value]));
    const raw = document.getElementById('theme-name').value || 'theme';
    const name = 'my-' + raw.replace(/^my-/, '');
    const lines = Object.entries(vars).map(([k,v]) => `    --${k.replace('var_','').replace(/_/g,'-')}: ${v};`).join('\n');
    const css = `[data-theme='${name}'] {\n${lines}\n}`;
    const a = document.createElement('a'); a.href = 'data:text/css,' + encodeURIComponent(css);
    a.download = name + '.css'; a.click();
}
"""


@rt("/")
def get():
    reg = registered_themes()
    init_css = vals_to_css(BUILTIN_VARS.get('light', {}))
    return (Title("Theme Builder"),
        Style(init_css, id="custom-theme-style"),
        theme_script(),
        Div(
            Div(H1("🎨 Theme Builder", cls="text-3xl font-bold text-base-content"), cls="mb-6"),
            Div(
                Div(
                    Label("Seed theme:", cls="text-sm font-semibold mr-2"),
                    Select(*[Option(t.title(), value=t) for t in BUILTIN_THEMES],
                        *[Option(t, value=t, cls="text-accent") for t in reg],
                        id="seed-sel", cls="select select-sm w-48",
                        hx_post="/seed", hx_target="#vars-table", hx_trigger="change",
                        hx_include="#seed-sel",
                        onchange="applyPageTheme(this.value)"),
                    cls="flex items-center gap-2"),
                Div(
                    Label("Theme name:", cls="text-sm font-semibold mr-2"),
                    Span("my-", cls="text-sm font-mono text-base-content/60"),
                    Input(value="theme", name="theme-name", id="theme-name", cls="input input-sm w-40"),
                    cls="flex items-center gap-2"),
                Div(
                    Button("💾 Save", size="sm",
                        hx_post="/save", hx_include="[name^='var_'],[name='theme-name']",
                        hx_target="#save-msg",
                        onclick="const n='my-'+document.getElementById('theme-name').value.replace(/^my-/,''); if(SAVED_THEMES.includes(n) && !confirm(`Overwrite theme '${n}'?`)) return false;"),
                    Button("📤 Export CSS", color="secondary", size="sm", onclick="exportCSS()"),
                    Button("📥 Import CSS", size="sm", variant="ghost",
                        onclick="document.getElementById('import-modal').showModal()"),
                    cls="flex gap-2"),
                cls="flex flex-wrap gap-4 items-center mb-6"),
            Span(id="save-msg", cls="text-sm text-success"),
            Div(
                Div(
                    MyColor(label=None, show_outputs=True),
                    H2("Variables", cls="text-lg font-semibold mb-2 text-base-content"),
                    mk_vars_table(),
                    cls="flex-1 min-w-64"),
                Div(
                    H2("Preview", cls="text-lg font-semibold mb-2 text-base-content"),
                    mk_preview_area(init_css),
                    cls="flex-1 min-w-80"),
                cls="flex gap-8 flex-wrap"),
            Div(
                H2("Saved Custom Themes", cls="text-lg font-semibold mt-6 mb-2"),
                P("None saved yet." if not reg else ", ".join(reg), cls="text-sm text-base-content/60"),
                cls="mt-4"),
            Dialog(
                Form(
                    H3("Import CSS", cls="font-bold text-lg mb-2"),
                    Textarea(name="css-import", placeholder="Paste your theme CSS here...",
                        cls="textarea textarea-bordered w-full h-48 font-mono text-xs"),
                    Div(Button("Import", size="sm",
                            hx_post="/import", hx_target="#vars-table", hx_include="[name='css-import']",
                            onclick="document.getElementById('import-modal').close()"),
                        Button("Cancel", size="sm", variant="ghost",
                            onclick="document.getElementById('import-modal').close()"),
                        cls="flex gap-2 mt-2"),
                    method="dialog"),
                id="import-modal", cls="modal"),
            cls="p-6 w-full max-w-7xl mx-auto"),
        Script(BUILDER_JS))


@rt("/preview")
async def post(req):
    form = await req.form()
    css = form_to_css(form)
    val_updates = [Code(hex_to_oklch(form.get('var_' + v.replace('-','_'), '#888888')),
        cls="text-xs text-base-content/50", id=f"val-{v}", hx_swap_oob="true") for v in CSS_VARS]
    return mk_preview_area(css), *val_updates


@rt("/seed")
async def post(req):
    form = await req.form()
    theme = form.get("seed-sel", "light")
    vals = load_custom_vars(theme) if theme.startswith('my-') else BUILTIN_VARS.get(theme, {})
    css = vals_to_css(vals)
    oob_preview = mk_preview_area(css)
    oob_preview.attrs['hx-swap-oob'] = 'true'
    return mk_vars_table(vals), oob_preview


@rt("/save")
async def post(req):
    form = await req.form()
    name = "my-" + form.get("theme-name", "theme").strip().removeprefix("my-")
    css = form_to_save_css(form, name)
    save_theme(name, css)
    return Span(f"✅ Saved '{name}'", cls="text-sm text-success")


@rt("/import")
async def post(req):
    form = await req.form()
    vals = parse_css_vars(form.get("css-import", ""))
    return mk_vars_table(vals)


def run(host:str="0.0.0.0", port:int=8001):
    """Runner to launch example from py."""
    import uvicorn
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__": run()
