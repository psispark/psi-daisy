# Getting Started with psi-daisy

`psi-daisy` is a Python DaisyUI component library for FastHTML.  
It provides a full component library for building DaisyUI-styled FastHTML websites.
  
---
  
## Install

```bash
pip install psi-daisy
```

For development, install with dev dependencies:

```bash
pip install "psi-daisy[dev]"
```
  
---
  
## Basic Usage

Import psi-daisy components ***after*** FastHTML:

```python
from fasthtml.common import *
from psi_daisy import *
from psi_daisy.ui import *
```

To use psi-daisy components inside a FastHTML app.

Example:

```python
from fasthtml.common import *
from psi_daisy.ui import Button, Card

app, rt = psi_app()

@rt("/")
def get():
    return Card(
        H2("Hello psi-daisy"),
        P("A DaisyUI component library for FastHTML."),
        Button("Click me", color="primary"), )
```
  
---
  
## Running the Example Apps

psi-daisy includes example apps to help you explore available components, themes, and icons.

Available examples include:

- `theme_builder`
- `theme_selector`
- `component_selector`
- `icon_selector`
  
  
### From Terminal

Run an example directly with Python:

```bash
python -m examples.theme_builder
```

You can use the same pattern for the other examples:

```bash
python -m examples.theme_selector
python -m examples.component_selector
python -m examples.icon_selector
```
  
  
### From a Python Script

You can also run an example app using `uvicorn`:

```python
import uvicorn
import examples.theme_selector as demo

uvicorn.run(demo.app, host="0.0.0.0", port=8001)
```

Then open:

```text
http://localhost:8001
```
  
  
### From Jupyter or Solveit

In notebook-style environments, use FastHTML’s `JupyUvi` helper:

```python
from fasthtml.jupyter import JupyUvi
import examples.icon_selector as demo

server = JupyUvi(demo.app)
```
  
---
  
## Themes

psi-daisy is designed to work with DaisyUI themes and Taiwind styles.

You can explore themes using:

```bash
python -m examples.theme_selector
```

or build custom themes using:

```bash
python -m examples.theme_builder
```
  
---
  
## Components

Components are available from:

```python
from psi_daisy.ui import *
```

The project aims to provide broad DaisyUI component coverage, including:

- Buttons
- Cards
- Alerts
- Badges
- Forms
- Modals
- Navigation
- Tables
- Tabs
- Toasts
- Themes
- Inputs
- Selects
- Toggles
- Ratings
- Progress components
- Layout helpers

See the component documentation at https://github.com/psispark/psi-daisy/tree/main/docs/Components.md for the full list of components.
  
---

## CSS Modes

By default, `psi-daisy` loads DaisyUI/Tailwind from CDN-style URLs:

```python
app = psi_app(theme="light")
```

To use the local packaged static CSS bundle instead:

```python
app = psi_app(theme="light", css="static")
```
\
Think of it like this: 
* In *CDN mode*, the browser gets DaisyUI/Tailwind from external URLs.  
* In *static mode*, the browser gets the prebuilt bundle from `/static/ui.css`. The components render the same HTML classes either way; only the CSS source changes.

See `docs/Static_CSS_Bundle.md` for details.

---
  
## Project Status

psi-daisy is currently in active alpha development.

APIs may change as the project evolves, but the package is ready for early testing, feedback, and experimentation.
  
---
  
## Links

* GitHub Home - https://github.com/psispark/psi-daisy
* Github Documentation - https://github.com/psispark/psi-daisy/tree/main/docs
* Github Issues & Ideas - https://github.com/psispark/psi-daisy/issues
---  
* PsiSpark - https://psispark.com/
* SolveIt - https://solve.it.com/
* FastHTML - https://fastht.ml/
* HTMX - https://htmx.org/
* DaisyUI - https://daisyui.com/
* Lucide - https://lucide.dev/
