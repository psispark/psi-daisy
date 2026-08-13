# psi-daisy

A modern Python DaisyUI component library for FastHTML  
The goal of `psi-daisy` is to make developing websites in Python much easier.

---

`psi-daisy` provides:

- A Python component API
- Full DaisyUI component coverage
- Tailwind class support
- A theming engine
- Interactive components powered by FastHTML and HTMX
- A plugin architecture
- FastHTML DaisyUI demos
- Custom theming
- Custom components

---

Coming Soon:
- A psi-daisy powered documentation site
- More psi-daisy demos
- More custom components
- More custom themes
- Page Templates

---

## Status

psi-daisy is in active alpha development. 

## Install

```bash
pip install psi-daisy
```

## Tested With

- python-fasthtml 0.14.4, 
- starlette 1.3.1
- httpx 0.28.1
- matplotlib 3.11.0
- uvicorn 0.49.0 

## Examples

- theme_builder
- theme_selector
- component_selector
- icon_selector

### From Terminal:

* theme_builder
```bash
python -m examples.theme_builder
```
* ditto for the other examples

### From Python script:

* theme_selector
```python
import uvicorn
import examples.theme_selector as demo
uvicorn.run(demo.app, host="0.0.0.0", port=8001)
```
* ditto for the other examples

### From Jupyter / SolveIt notebook:

* icon_selector
```python
from fasthtml.jupyter import JupyUvi
import examples.icon_selector as demo
server = JupyUvi(demo.app)
```
* ditto for the other examples

---

## CSS Modes

By default, `psi-daisy` loads DaisyUI/Tailwind from CDN-style URLs:

```python
app = psi_app(theme="light")
```

To use the packaged static CSS bundle instead:

```python
app = psi_app(theme="light", css="static")
```

See `docs/Static_CSS_Bundle.md` for details.

---

## Documentation

* Getting Started - docs/Getting_Started.md
* Components - docs/Components.md
* LLM Guide - docs/LLM_Guide.md
* Component Rendering Flow - docs/Component_Rendering_Flow.md
* Static CSS Bundle - docs/Static_CSS_Bundle.md

---

## Acknowledgements

Built in SolveIt using Codex GPT-5.5 

## Links

* `psi-daisy` docs - https://psispark.com/psi-daisy-docs
* GitHub Home - https://github.com/psispark/psi-daisy
* Github Docs - https://github.com/psispark/psi-daisy/tree/main/docs
* Github Issues & Ideas - https://github.com/psispark/psi-daisy/issues
---  
* PsiSpark - https://psispark.com/
* SolveIt - https://solve.it.com/
* FastHTML - https://fastht.ml/
* HTMX - https://htmx.org/
* DaisyUI - https://daisyui.com/
* Lucide - https://lucide.dev/
