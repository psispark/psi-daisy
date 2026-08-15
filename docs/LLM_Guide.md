---
type: guide  
title: "psi-daisy LLM Guide"  
id: psi-daisy-llm-guide  
updated: "2026-08-14"  
---

# psi-daisy LLM Guide

> 📌 save as `llms.txt` in app's root folder  

`psi-daisy` is a Python DaisyUI component library for FastHTML.

Its purpose is to make building DaisyUI-styled websites easier for both humans and AI by letting developers write clean Python component code instead of hand-writing HTML, JavaScript, or raw DaisyUI class strings.

When generating examples for this project, prefer `psi-daisy` syntax.

---

## Core Rule

Use `psi-daisy` components whenever possible.

Prefer this:

```python
Button("Save", color="success", variant="outline", hx_post="/save", hx_target="#out")
```

Instead of this:

```python
button = Button("Save", cls="btn btn-success btn-outline", hx_post="/save", hx_target="#out")
```

And instead of hand-written HTML or JavaScript.

---

## Standard Imports

Import FastHTML first, then `psi-daisy`:

```python
from fasthtml.common import *
from psi_daisy import *
from psi_daisy.ui import *
```

Use `psi_app()` to create the app:

```python
app, rt = psi_app()
```

Or with a theme:

```python
app, rt = psi_app(theme="light")
```

For local packaged CSS instead of CDN CSS:

```python
app, rt = psi_app(theme="light", css="static")
```

Some custom picker components require companion JavaScript headers. Include them through `psi_app(hdrs=...)`; they are not added automatically:

```python
app, rt = psi_app(hdrs=get_theme_picker_headers())
```

Required pairs include `MyDate`/`get_date_picker_headers()`, `MyTime`/`get_time_picker_headers()`, `MyDatetime`/`get_datetime_picker_headers()`, `MyColor`/`get_color_picker_headers()`, and `MyTheme`/`get_theme_picker_headers()`.

---

## Preferred Component Style

Use semantic Python parameters:

```python
Button("Save", color="success", size="sm", variant="outline")
Badge("Alpha", color="warning", variant="outline")
Alert("Saved successfully", color="success", variant="soft")
Input(name="email", placeholder="Email", color="primary")
Card(H2("Title"), P("Body text"), cls="p-6 border")
```

Do not manually recreate DaisyUI components with raw `Div`, `Button`, `Input`, or HTML when a `psi-daisy` component exists.

---

## HTMX

Use HTMX through FastHTML keyword arguments.

Prefer:

```python
Button("Search", hx_post="/search", hx_target="#results")
```

FastHTML renders Python keyword names as HTML attributes:

| Python | HTML |
| --- | --- |
| `hx_post` | `hx-post` |
| `hx_target` | `hx-target` |
| `hx_include` | `hx-include` |
| `hx_swap` | `hx-swap` |
| `data_theme` | `data-theme` |
| `cls` | `class` |

Avoid JavaScript for interactions that HTMX can handle.

---

## Avoid JavaScript Unless Necessary

Do not write JavaScript by default.

Prefer:

- `hx_post`
- `hx_get`
- `hx_target`
- `hx_include`
- `hx_trigger`
- `hx_swap`
- `hx_swap_oob`

Use JavaScript only when the requested behavior cannot reasonably be handled with FastHTML, HTMX, DaisyUI, or an existing `psi-daisy` component.

---

## Use `cls` for Layout and Extra Styling

`psi-daisy` components already provide DaisyUI component classes.

Use `cls` for additional Tailwind utilities:

```python
Card(
    H2("Hello"),
    P("Welcome to psi-daisy."),
    Button("Continue", color="primary"),
    cls="p-6 border max-w-md")
```

Do not use `cls` to manually rebuild the whole component unless there is no suitable `psi-daisy` component.

Good:

```python
Button("Delete", color="error", variant="outline")
```

Avoid:

```python
Button("Delete", cls="btn btn-error btn-outline")
```

---

## Common Components

Prefer these `psi-daisy` components:

### Actions

```python
Button("Save", color="success")
Dropdown(Button("Actions"), Li(A("Edit")), Li(A("Delete")))
Modal(H3("Confirm"), P("Are you sure?"), id="confirm-modal")
Swap(MyIcon("sun"), MyIcon("moon"), rotate=True)
```

### Data Display

```python
Card(H2("Title"), P("Card body"))
Alert("Something happened", color="info")
Badge("New", color="accent")
Table(["Name", "Role"], [["Ada", "Admin"], ["Grace", "User"]])
Progress(70, max=100, color="success")
Stat("Downloads", "12.4k", "Last 30 days")
```

### Forms

```python
Input(name="email", placeholder="Email")
Textarea(name="body", placeholder="Message")
Select(("light", "Light"), ("dark", "Dark"), name="theme")
Checkbox(name="active", checked=True)
Toggle(name="enabled", color="success")
Radio(name="plan", value="pro")
Range(name="volume", min=0, max=100, value=40)
```

### Layout

```python
Navbar(start=A("psi-daisy", href="/"), end=Button("Login"))
Hero(H1("Build faster"), Button("Get started"))
Footer(P("© 2026 psi-daisy"), center=True)
Divider("OR")
Toast(Alert("Saved", color="success"))
```

### Navigation

```python
Menu(("Home", "/"), ("Docs", "/docs"))
Tabs(("Preview", Div("Preview")), ("Code", Pre("...")))
Breadcrumbs(("Home", "/"), ("Docs", "/docs"), "Components")
Steps("Account", "Profile", "Done", color="success")
```

### Custom Components

```python
MyIcon("search", color="primary")
MyDate(name="start_date")
MyTime(name="start_time")
MyDatetime(name="scheduled_at")
MyColor(name="primary", web_color="dodgerblue")
MyTheme(current="light")
ThemeController("dark")
MyEmpty("No results", body="Try changing your filters.")
```

When using picker components, include their companion headers in the app setup. `MyTheme` specifically requires:

```python
app, rt = psi_app(hdrs=get_theme_picker_headers())
```

Do not show a picker component without also showing its required header when the example includes app construction.

---

## Minimal Page Example

Prefer examples like this:

```python
from fasthtml.common import *
from psi_daisy import *
from psi_daisy.ui import *

app, rt = psi_app(theme="light")

@rt("/")
def get():
    return Div(
        Card(
            H2("Hello psi-daisy"),
            P("A DaisyUI component library for FastHTML."),
            Button("Click me", color="primary"),
            cls="p-6 border"),
        cls="min-h-screen bg-base-200 p-8")
```

This is the preferred style: Python components, semantic parameters, HTMX/FastHTML kwargs, and minimal manual class construction.

---

## Dynamic Interactions

Use FastHTML routes plus HTMX.

```python
@rt("/")
def get():
    return Div(
        Button("Load", hx_get="/message", hx_target="#out"),
        Div(id="out"))

@rt("/message")
def get():
    return Alert("Loaded!", color="success")
```

Do not use JavaScript for simple request/swap interactions.

---

## Static CSS Mode

By default, `psi_app()` uses CDN CSS:

```python
app, rt = psi_app()
```

Use static mode when the app should use the packaged local CSS bundle:

```python
app, rt = psi_app(css="static")
```

The Python component code does not change between CDN and static mode.

---

## Important Mental Model

A `psi-daisy` component returns a FastHTML element with DaisyUI and Tailwind classes applied.

The browser then applies:

1. DaisyUI component styles
2. Tailwind utility styles
3. DaisyUI theme variables
4. HTMX behavior
5. Optional JavaScript enhancement such as Lucide icons

When debugging, check:

1. Did the Python component return the expected element?
2. Did FastHTML render the expected HTML?
3. Are the expected classes present?
4. Are the `hx-*` attributes present?
5. Is the correct `data-theme` set?
6. Are DaisyUI/Tailwind styles loaded?

---

## What Not To Do

Avoid generating raw DaisyUI HTML like this:

```html
<button class="btn btn-primary">Save</button>
```

Prefer:

```python
Button("Save", color="primary")
```

Avoid unnecessary JavaScript like this:

```javascript
fetch("/save").then(...)
```

Prefer:

```python
Button("Save", hx_post="/save", hx_target="#out")
```

Avoid manually recreating existing components with raw FastHTML:

```python
Div("Saved", cls="alert alert-success")
```

Prefer:

```python
Alert("Saved", color="success")
```

---

## Summary for AI Assistants

When helping users build with `psi-daisy`:

1. Use Python, not handwritten HTML.
2. Use `psi-daisy` components, not raw DaisyUI class strings.
3. Use semantic component parameters like `color`, `size`, and `variant`.
4. Use `cls` only for extra layout/styling utilities.
5. Use HTMX kwargs instead of JavaScript for interactivity.
6. Use `psi_app()` for app setup.
7. Include each custom picker's required header helper in `psi_app(hdrs=...)`; in particular, `MyTheme` requires `get_theme_picker_headers()`.
8. Prefer clear, small, idiomatic examples.
9. Keep the user in the `psi-daisy` component API unless they explicitly ask to go lower-level.
