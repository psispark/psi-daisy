# Components

`psi-daisy` provides Python component functions for building DaisyUI-styled FastHTML apps.

Most components follow the same pattern:

- accept semantic Python parameters such as `color`, `size`, `variant`, `orientation`, etc.
- build DaisyUI/Tailwind class strings
- merge user-provided `cls`
- return a FastHTML element
- pass extra `**kw` through to FastHTML

That means normal FastHTML attributes such as `id`, `name`, `value`, `onclick`, `hx_post`, `hx_target`, `hx_include`, and `data_*` can usually be passed directly.

Example:

```python
Button("Save", color="success", variant="outline", hx_post="/save", hx_target="#out")
```

renders as a FastHTML button with DaisyUI classes and HTMX attributes.

---

## Table of Contents

- [Common Parameters](#common-parameters)
- [App and CSS Helpers](#app-and-css-helpers)
- [Actions](#actions)
  - [Button](#button)
  - [FAB](#fab)
  - [Dropdown](#dropdown)
  - [Modal](#modal)
  - [Swap](#swap)
- [Data Display](#data-display)
  - [Accordion](#accordion)
  - [Alert](#alert)
  - [Avatar](#avatar)
  - [Badge](#badge)
  - [Card](#card)
  - [Carousel](#carousel)
  - [ChatBubble](#chatbubble)
  - [Collapse](#collapse)
  - [Countdown](#countdown)
  - [Diff](#diff)
  - [Indicator](#indicator)
  - [Kbd](#kbd)
  - [List](#list)
  - [Loading](#loading)
  - [Progress](#progress)
  - [RadialProgress](#radialprogress)
  - [Skeleton](#skeleton)
  - [Stat](#stat)
  - [Status](#status)
  - [Table](#table)
  - [Tooltip](#tooltip)
- [Forms and Inputs](#forms-and-inputs)
  - [Checkbox](#checkbox)
  - [Fieldset](#fieldset)
  - [FileInput](#fileinput)
  - [Filter](#filter)
  - [Input](#input)
  - [Label](#label)
  - [Radio](#radio)
  - [Range](#range)
  - [Rating](#rating)
  - [Select](#select)
  - [Textarea](#textarea)
  - [Toggle](#toggle)
  - [Validator](#validator)
- [Layout](#layout)
  - [Divider](#divider)
  - [Drawer](#drawer)
  - [Footer](#footer)
  - [Hero](#hero)
  - [Join](#join)
  - [Navbar](#navbar)
  - [Stack](#stack)
  - [ThemeController](#themecontroller)  
  - [Toast](#toast)
- [Navigation](#navigation)
  - [Breadcrumbs](#breadcrumbs)
  - [Dock](#dock)
  - [Link](#link)
  - [Menu](#menu)
  - [Pagination](#pagination)
  - [Steps](#steps)
  - [Tabs](#tabs)
  - [Timeline](#timeline)
- [Mockups](#mockups)
  - [MockupBrowser](#mockupbrowser)
  - [MockupCode](#mockupcode)
  - [MockupPhone](#mockupphone)
  - [MockupWindow](#mockupwindow)
- [Media and Effects](#media-and-effects)
  - [Mask](#mask)
  - [MyIcon](#myicon)
  - [Hover3D](#hover3d)
  - [HoverGallery](#hovergallery)
  - [TextRotate](#textrotate)
- [Custom Components](#custom-components)
  - [Calendar](#calendar)
  - [MyColor](#mycolor)
  - [MyDate](#mydate)
  - [MyTime](#mytime)
  - [MyDatetime](#mydatetime)
  - [MyEmpty](#myempty)

---

## Common Parameters

Many components share these parameters.

### `color`

Most colored components use:

```text
primary
secondary
accent
info
success
warning
error
```

Examples:

```python
Button("Save", color="success")
Alert("Saved", color="success")
Badge("New", color="accent")
```

### `size`

Most sized components use:

```text
xs
sm
md
lg
```

Examples:

```python
Button("Small", size="sm")
Input(size="lg")
Loading(size="xs")
```

### `variant`

Variants depend on the component.

Common button/badge/alert variants include:

```text
""
outline
soft
dash
ghost
link
```

Examples:

```python
Button("Cancel", variant="ghost")
Badge("Beta", variant="outline")
Alert("Warning", variant="dash")
```

### `orientation`

Common orientation values:

```text
horizontal
vertical
```

Examples:

```python
Join(Button("A"), Button("B"), orientation="horizontal")
Divider("OR", orientation="vertical")
```

### `cls`

Most components accept `cls` through `**kw`.

`psi-daisy` merges the component’s default classes with your custom classes.

```python
Card(H2("Hello"), cls="p-6 border")
```

### `**kw`

Extra keyword arguments pass through to FastHTML.

That includes HTML attributes and HTMX attributes:

```python
Button("Search", hx_post="/search", hx_target="#results")
Input(name="query", placeholder="Search...")
Div("Hello", data_theme="dark")
```

FastHTML converts Python-style names to HTML attributes:

| Python | HTML |
| --- | --- |
| `cls` | `class` |
| `hx_post` | `hx-post` |
| `hx_target` | `hx-target` |
| `data_theme` | `data-theme` |

---

## App and CSS Helpers

### `get_ui_headers`

```python
get_ui_headers(theme="light", css="cdn")
```

Returns the CSS and JS headers needed by `psi-daisy`.

Use indirectly through `psi_app()` in most apps.

Modes:

- `css="cdn"` loads DaisyUI, DaisyUI themes, and Tailwind browser support from configured CDN URLs.
- `css="static"` loads the bundled `/static/ui.css`.

Example:

```python
from psi_daisy import psi_app

app = psi_app(theme="light")
app_static = psi_app(theme="light", css="static")
```

### Picker Headers

These helpers provide JavaScript needed by custom picker components.

```python
get_date_picker_headers()
get_time_picker_headers()
get_datetime_picker_headers()
get_color_picker_headers()
```

Use when an app includes the corresponding picker components.

Example:

```python
app = psi_app(hdrs=get_date_picker_headers() + get_time_picker_headers())
```

---

# Actions

## Button

```python
Button(label, *, color="primary", size="md", variant="", **kw)
```

DaisyUI button component.

Use for normal actions, form buttons, HTMX triggers, and navigation-like controls.

Parameters:

- `label`: button text
- `color`: semantic DaisyUI color
- `size`: `xs`, `sm`, `md`, `lg`
- `variant`: `""`, `outline`, `soft`, `dash`, `link`, `ghost`
- `**kw`: passed to FastHTML button

Example:

```python
Button("Save", color="success", variant="outline", hx_post="/save", hx_target="#out")
```

Rendered example:

```html
<button hx-post="/save" hx-target="#out" class="btn btn-success btn-outline btn-sm">Save</button>
```

---

## FAB

```python
FAB(icon, *actions, position="bottom-right", **kw)
```

DaisyUI floating action button.

Use for persistent page actions such as create, edit, share, or quick menus.

Parameters:

- `icon`: main icon/content
- `*actions`: action elements shown with the FAB
- `position`: `bottom-right`, `bottom-left`, `top-right`, `top-left`
- `**kw`: passed to the wrapper

Example:

```python
FAB(MyIcon("plus"), Button("New", color="primary"), position="bottom-right")
```

---

## Dropdown

```python
Dropdown(trigger, *items, position="bottom", orientation="vertical", menu_cls=None, menu_kw=None, **kw)
```

DaisyUI dropdown component.

Use for menus, action lists, selectors, and compact option groups.

Parameters:

- `trigger`: element that opens the dropdown
- `*items`: menu items
- `position`: `top`, `bottom`, `left`, `right`
- `orientation`: `vertical` or `horizontal`
- `menu_cls`: extra classes for menu container
- `menu_kw`: extra attrs for menu container
- `**kw`: passed to dropdown wrapper

Example:

```python
Dropdown(Button("Actions"), Li(A("Edit")), Li(A("Delete")), position="bottom")
```

---

## Modal

```python
Modal(*children, id, actions=None, **kw)
```

DaisyUI modal component.

Use for dialogs, confirmations, forms, and focused interactions.

Parameters:

- `*children`: modal content
- `id`: modal DOM id
- `actions`: optional modal action elements
- `**kw`: passed to modal element

Example:

```python
Modal(H3("Delete item?"), P("This cannot be undone."), id="delete-modal", actions=[Button("Cancel"), Button("Delete", color="error")])
```

Open with JavaScript:

```javascript
document.getElementById("delete-modal").showModal()
```

---

## Swap

```python
Swap(on, off, *, rotate=False, flip=False, **kw)
```

DaisyUI swap component.

Use for toggling between two visual states, such as menu/close icons, sun/moon icons, or active/inactive labels.

Parameters:

- `on`: content for active state
- `off`: content for inactive state
- `rotate`: use DaisyUI rotate animation
- `flip`: use DaisyUI flip animation
- `**kw`: passed to wrapper

Example:

```python
Swap(MyIcon("sun"), MyIcon("moon"), rotate=True)
```

---

# Data Display

## Accordion

```python
Accordion(title, *children, name="accordion", icon="arrow", checked=False, **kw)
```

DaisyUI accordion component.

Use to show expandable content sections where usually one or more sections can open.

Parameters:

- `title`: accordion title
- `*children`: expanded content
- `name`: input group name
- `icon`: `arrow` or `plus`
- `checked`: open by default
- `**kw`: passed to wrapper

Example:

```python
Accordion("Details", P("More information here."), checked=True)
```

---

## Alert

```python
Alert(*children, color="info", variant="", **kw)
```

DaisyUI alert component.

Use for status messages, warnings, success messages, and error notices.

Parameters:

- `*children`: alert content
- `color`: semantic color
- `variant`: `""`, `soft`, `outline`, `dash`
- `**kw`: passed to alert wrapper

Example:

```python
Alert("Saved successfully", color="success", variant="soft")
```

---

## Avatar

```python
Avatar(src, alt="", *, online=False, offline=False, placeholder=False, **kw)
```

DaisyUI avatar component.

Use for user profile images, placeholders, and online/offline status indicators.

Parameters:

- `src`: image URL
- `alt`: image alt text
- `online`: show online indicator
- `offline`: show offline indicator
- `placeholder`: render as placeholder style
- `**kw`: passed to wrapper

Example:

```python
Avatar("/static/me.png", alt="Lucien", online=True)
```

---

## Badge

```python
Badge(text, *, color="primary", variant="", **kw)
```

DaisyUI badge component.

Use for labels, status pills, counts, tags, and small metadata.

Parameters:

- `text`: badge text
- `color`: semantic color
- `variant`: `""`, `outline`, `soft`, `dash`, `ghost`
- `**kw`: passed to badge element

Example:

```python
Badge("Alpha", color="warning", variant="outline")
```

---

## Card

```python
Card(*children, **kw)
```

DaisyUI card component.

Use for grouped content, panels, previews, summaries, and layout blocks.

Defaults include:

```text
card bg-base-100 shadow-xl
```

Parameters:

- `*children`: card content
- `**kw`: passed to the card wrapper

Example:

```python
Card(H2("Title"), P("Card body"), Button("Open"), cls="p-6 border")
```

---

## Carousel

```python
Carousel(*items, orientation="horizontal", snap="start", **kw)
```

DaisyUI carousel component.

Use for scrolling image/content galleries.

Parameters:

- `*items`: carousel items
- `orientation`: `horizontal` or `vertical`
- `snap`: `start`, `center`, `end`
- `**kw`: passed to carousel wrapper

Example:

```python
Carousel(Img(src="/static/a.png"), Img(src="/static/b.png"), snap="center")
```

---

## ChatBubble

```python
ChatBubble(message, *, side="start", header="", footer="", avatar=None, **kw)
```

DaisyUI chat bubble component.

Use for chat interfaces, message timelines, and conversational UIs.

Parameters:

- `message`: bubble text
- `side`: `start` or `end`
- `header`: optional header text
- `footer`: optional footer text
- `avatar`: optional avatar element
- `**kw`: passed to wrapper

Example:

```python
ChatBubble("Hello!", side="end", footer="Seen")
```

---

## Collapse

```python
Collapse(title, *children, icon="arrow", **kw)
```

DaisyUI collapse component.

Use for a single expandable panel.

Parameters:

- `title`: collapse title
- `*children`: expanded content
- `icon`: `arrow` or `plus`
- `**kw`: passed to wrapper

Example:

```python
Collapse("Advanced options", P("Hidden controls here."))
```

---

## Countdown

```python
Countdown(*values, labels=None, size="md", **kw)
```

DaisyUI countdown component.

Use for timers, stats, countdowns, and numeric displays.

Parameters:

- `*values`: numeric values
- `labels`: optional labels for each value
- `size`: `xs`, `sm`, `md`, `lg`
- `**kw`: passed to wrapper

Example:

```python
Countdown(1, 23, 45, labels=["days", "hours", "minutes"])
```

---

## Diff

```python
Diff(item1, item2, **kw)
```

DaisyUI diff component.

Use for before/after comparisons.

Parameters:

- `item1`: first item
- `item2`: second item
- `**kw`: passed to wrapper

Example:

```python
Diff(Img(src="/before.png"), Img(src="/after.png"))
```

---

## Indicator

```python
Indicator(content, badge, *, color="primary", **kw)
```

DaisyUI indicator component.

Use to overlay badges or notification indicators on content.

Parameters:

- `content`: main content
- `badge`: indicator content
- `color`: semantic color
- `**kw`: passed to wrapper

Example:

```python
Indicator(Button("Inbox"), Badge("3", color="error"))
```

---

## Kbd

```python
Kbd(text, *, size="md", **kw)
```

DaisyUI keyboard key component.

Use for keyboard shortcuts and key hints.

Parameters:

- `text`: key text
- `size`: `xs`, `sm`, `md`, `lg`
- `**kw`: passed to kbd element

Example:

```python
Kbd("⌘", size="sm")
```

---

## List

```python
List(*items, **kw)
```

DaisyUI list component.

Use for stacked lists of items, rows, and summaries.

Items can be tuples or FastHTML elements.

Parameters:

- `*items`: `(title, desc)` tuples or FT elements
- `**kw`: passed to list wrapper

Example:

```python
List(("FastHTML", "Python web apps"), ("DaisyUI", "Styled components"))
```

---

## Loading

```python
Loading(*, color="primary", size="md", variant="spinner", **kw)
```

DaisyUI loading component.

Use for loading states and async activity indicators.

Parameters:

- `color`: semantic color
- `size`: `xs`, `sm`, `md`, `lg`
- `variant`: `spinner`, `dots`, `ring`, `ball`, `bars`, `infinity`
- `**kw`: passed to loading element

Example:

```python
Loading(color="info", variant="dots")
```

---

## Progress

```python
Progress(value=0, max=100, *, color="primary", **kw)
```

DaisyUI progress component.

Use for completion indicators.

Parameters:

- `value`: current value
- `max`: maximum value
- `color`: semantic color
- `**kw`: passed to progress element

Example:

```python
Progress(70, max=100, color="success")
```

---

## RadialProgress

```python
RadialProgress(value=0, *, color="primary", **kw)
```

DaisyUI radial progress component.

Use for circular progress indicators and dashboard metrics.

Parameters:

- `value`: progress value
- `color`: semantic color
- `**kw`: passed to wrapper

Example:

```python
RadialProgress(75, color="accent")
```

---

## Skeleton

```python
Skeleton(*, w="w-full", h="h-4", **kw)
```

DaisyUI skeleton component.

Use for placeholder loading layouts.

Parameters:

- `w`: Tailwind width class
- `h`: Tailwind height class
- `**kw`: passed to skeleton element

Example:

```python
Skeleton(w="w-64", h="h-8")
```

---

## Stat

```python
Stat(title, value, desc="", figure=None, **kw)
```

DaisyUI stat component.

Use for dashboards, metrics, and summary cards.

Parameters:

- `title`: stat title
- `value`: stat value
- `desc`: optional description
- `figure`: optional figure/icon
- `**kw`: passed to stat wrapper

Example:

```python
Stat("Downloads", "12.4k", "Last 30 days", figure=MyIcon("download"))
```

---

## Status

```python
Status(*, color="primary", size="md", **kw)
```

DaisyUI status indicator component.

Use for small status dots and presence indicators.

Parameters:

- `color`: semantic color
- `size`: `xs`, `sm`, `md`, `lg`
- `**kw`: passed to status element

Example:

```python
Status(color="success", size="sm")
```

---

## Table

```python
Table(headers, rows, *, size="md", zebra=False, pin_rows=False, **kw)
```

DaisyUI table component.

Use for tabular data.

Parameters:

- `headers`: list of column headers
- `rows`: list of row lists
- `size`: `xs`, `sm`, `md`, `lg`
- `zebra`: striped rows
- `pin_rows`: pinned rows
- `**kw`: passed to table wrapper

Example:

```python
Table(["Name", "Role"], [["Ada", "Admin"], ["Grace", "User"]], zebra=True)
```

---

## Tooltip

```python
Tooltip(*children, tip, color="primary", position="top", **kw)
```

DaisyUI tooltip component.

Use to show extra information on hover/focus.

Parameters:

- `*children`: wrapped content
- `tip`: tooltip text
- `color`: semantic color
- `position`: `top`, `bottom`, `left`, `right`
- `**kw`: passed to wrapper

Example:

```python
Tooltip(Button("Info"), tip="More details", position="bottom")
```

---

# Forms and Inputs

## Checkbox

```python
Checkbox(*, color="primary", size="md", checked=False, **kw)
```

DaisyUI checkbox component.

Use for boolean options and multi-select inputs.

Parameters:

- `color`: semantic color
- `size`: `xs`, `sm`, `md`, `lg`
- `checked`: initially checked
- `**kw`: passed to input

Example:

```python
Checkbox(name="active", color="success", checked=True)
```

---

## Fieldset

```python
Fieldset(legend, *children, hint="", **kw)
```

DaisyUI fieldset component.

Use for grouped form controls.

Parameters:

- `legend`: group title
- `*children`: form controls
- `hint`: optional help text
- `**kw`: passed to fieldset

Example:

```python
Fieldset("Account", Input(name="email"), hint="Use your work email.")
```

---

## FileInput

```python
FileInput(*, color="primary", size="md", variant="bordered", **kw)
```

DaisyUI file input component.

Use for file uploads.

Parameters:

- `color`: semantic color
- `size`: `xs`, `sm`, `md`, `lg`
- `variant`: `""`, `bordered`, `ghost`
- `**kw`: passed to input

Example:

```python
FileInput(name="upload", color="primary")
```

---

## Filter

```python
Filter(*options, name="filter", **kw)
```

DaisyUI filter component.

Use for filter chips and option groups.

Parameters:

- `*options`: `(value, label)` tuples
- `name`: input group name
- `**kw`: passed to wrapper

Example:

```python
Filter(("all", "All"), ("open", "Open"), ("closed", "Closed"), name="status")
```

---

## Input

```python
Input(*, color="primary", size="md", variant="bordered", **kw)
```

DaisyUI input component.

Use for text, email, password, search, and other HTML input types.

Parameters:

- `color`: semantic color
- `size`: `xs`, `sm`, `md`, `lg`
- `variant`: `""`, `bordered`, `ghost`
- `**kw`: passed to input

Example:

```python
Input(name="email", type="email", placeholder="Email", color="primary")
```

---

## Label

```python
Label(*children, **kw)
```

DaisyUI label component.

Use for form labels and helper text.

Parameters:

- `*children`: label content
- `**kw`: passed to label element

Example:

```python
Label("Email", cls="label")
```

---

## Radio

```python
Radio(*, color="primary", size="md", checked=False, **kw)
```

DaisyUI radio component.

Use for single-choice option groups.

Parameters:

- `color`: semantic color
- `size`: `xs`, `sm`, `md`, `lg`
- `checked`: initially checked
- `**kw`: passed to input

Example:

```python
Radio(name="plan", value="pro", color="accent")
```

---

## Range

```python
Range(*, color="primary", size="md", min=0, max=100, value=50, **kw)
```

DaisyUI range slider component.

Use for numeric sliders.

Parameters:

- `color`: semantic color
- `size`: `xs`, `sm`, `md`, `lg`
- `min`: minimum value
- `max`: maximum value
- `value`: current value
- `**kw`: passed to input

Example:

```python
Range(name="volume", min=0, max=100, value=40)
```

---

## Rating

```python
Rating(value=0, max=5, *, name="rating", size="md", half=False, **kw)
```

DaisyUI rating component.

Use for star ratings and scoring controls.

Parameters:

- `value`: selected rating
- `max`: maximum rating
- `name`: input group name
- `size`: `xs`, `sm`, `md`, `lg`
- `half`: allow half steps
- `**kw`: passed to wrapper

Example:

```python
Rating(3, max=5, name="score")
```

---

## Select

```python
Select(*options, color="primary", size="md", variant="bordered", **kw)
```

DaisyUI select component.

Use for dropdown select inputs.

Options can be `(value, label)` tuples or FastHTML option elements.

Parameters:

- `*options`: choices
- `color`: semantic color
- `size`: `xs`, `sm`, `md`, `lg`
- `variant`: `""`, `bordered`, `ghost`
- `**kw`: passed to select

Example:

```python
Select(("light", "Light"), ("dark", "Dark"), name="theme", color="primary")
```

---

## Textarea

```python
Textarea(value="", *, color="primary", size="md", variant="bordered", **kw)
```

DaisyUI textarea component.

Use for multi-line text input.

Parameters:

- `value`: initial text
- `color`: semantic color
- `size`: `xs`, `sm`, `md`, `lg`
- `variant`: `""`, `bordered`, `ghost`
- `**kw`: passed to textarea

Example:

```python
Textarea("Initial text", name="body", placeholder="Write something...")
```

---

## Toggle

```python
Toggle(*, color="primary", size="md", checked=False, **kw)
```

DaisyUI toggle component.

Use for switch-style boolean controls.

Parameters:

- `color`: semantic color
- `size`: `xs`, `sm`, `md`, `lg`
- `checked`: initially checked
- `**kw`: passed to input

Example:

```python
Toggle(name="enabled", color="success", checked=True)
```

---

## Validator

```python
Validator(*children, **kw)
```

DaisyUI validator wrapper component.

Use to wrap validation-related form content.

Parameters:

- `*children`: validator content
- `**kw`: passed to wrapper

Example:

```python
Validator(Input(required=True, name="email"))
```

---

# Layout

## Divider

```python
Divider(text="", *, color=None, orientation="horizontal", **kw)
```

DaisyUI divider component.

Use to separate sections of content.

Parameters:

- `text`: optional divider text
- `color`: optional semantic color
- `orientation`: `horizontal` or `vertical`
- `**kw`: passed to divider

Example:

```python
Divider("OR")
```

---

## Drawer

```python
Drawer(content, sidebar, *, id="drawer", end=False, **kw)
```

DaisyUI drawer component.

Use for sidebars and slide-out navigation.

Parameters:

- `content`: main page content
- `sidebar`: drawer/sidebar content
- `id`: drawer input id
- `end`: put drawer on the end side
- `**kw`: passed to wrapper

Example:

```python
Drawer(Main("Page"), Aside(Menu(("Home", "/"))), id="main-drawer")
```

---

## Footer

```python
Footer(*children, center=False, **kw)
```

DaisyUI footer component.

Use for page footers, links, copyright, and footer nav.

Parameters:

- `*children`: footer content
- `center`: center layout
- `**kw`: passed to footer

Example:

```python
Footer(P("© 2026 psi-daisy"), center=True)
```

---

## Hero

```python
Hero(*children, **kw)
```

DaisyUI hero component.

Use for landing page hero sections.

Parameters:

- `*children`: hero content
- `**kw`: passed to wrapper

Example:

```python
Hero(H1("Build FastHTML apps faster"), Button("Get started"))
```

---

## Join

```python
Join(*children, orientation="horizontal", **kw)
```

DaisyUI join component.

Use to visually group controls such as buttons, inputs, and pagination controls.

Parameters:

- `*children`: joined elements
- `orientation`: `horizontal` or `vertical`
- `**kw`: passed to wrapper

Example:

```python
Join(Button("Left"), Button("Right"))
```

---

## Navbar

```python
Navbar(start=None, center=None, end=None, **kw)
```

DaisyUI navbar component.

Use for top navigation bars.

Parameters:

- `start`: left/start region
- `center`: center region
- `end`: right/end region
- `**kw`: passed to wrapper

Example:

```python
Navbar(start=A("psi-daisy", href="/"), end=Button("Login"))
```

---

## Stack

```python
Stack(*children, **kw)
```

DaisyUI stack component.

Use for layered visual stacks.

Parameters:

- `*children`: stacked elements
- `**kw`: passed to wrapper

Example:

```python
Stack(Card("One"), Card("Two"), Card("Three"))
```

---

## Toast

```python
Toast(*children, h="end", v="bottom", **kw)
```

DaisyUI toast container component.

Use for notification containers.

Parameters:

- `*children`: toast alerts/content
- `h`: horizontal position, `start`, `center`, `end`
- `v`: vertical position, `top`, `middle`, `bottom`
- `**kw`: passed to wrapper

Example:

```python
Toast(Alert("Saved", color="success"))
```

---

# Navigation

## Breadcrumbs

```python
Breadcrumbs(*items, **kw)
```

DaisyUI breadcrumbs component.

Use to show page hierarchy.

Items can be strings or `(label, href)` tuples.

Parameters:

- `*items`: breadcrumb items
- `**kw`: passed to wrapper

Example:

```python
Breadcrumbs(("Home", "/"), ("Docs", "/docs"), "Components")
```

---

## Dock

```python
Dock(*items, size="md", **kw)
```

DaisyUI dock/bottom-nav component.

Use for mobile-style bottom navigation.

Items can be `(icon, label)` tuples or FastHTML elements.

Parameters:

- `*items`: dock items
- `size`: `xs`, `sm`, `md`, `lg`
- `**kw`: passed to wrapper

Example:

```python
Dock((MyIcon("home"), "Home"), (MyIcon("settings"), "Settings"))
```

---

## Link

```python
Link(text, href="#", *, color="primary", hover=False, **kw)
```

DaisyUI link component.

Use for styled anchors.

Parameters:

- `text`: link text
- `href`: target URL
- `color`: semantic color
- `hover`: add hover style
- `**kw`: passed to anchor

Example:

```python
Link("Documentation", href="/docs", color="info", hover=True)
```

---

## Menu

```python
Menu(*items, size="md", horizontal=False, **kw)
```

DaisyUI menu component.

Use for navigation menus and option lists.

Items can be `(label, href)` tuples or FastHTML elements.

Parameters:

- `*items`: menu items
- `size`: `xs`, `sm`, `md`, `lg`
- `horizontal`: render horizontally
- `**kw`: passed to menu wrapper

Example:

```python
Menu(("Home", "/"), ("Docs", "/docs"), horizontal=True)
```

---

## Pagination

```python
Pagination(pages, current=1, **kw)
```

DaisyUI pagination component.

Use for page navigation.

Parameters:

- `pages`: total page count
- `current`: current page
- `**kw`: passed to wrapper

Example:

```python
Pagination(10, current=3)
```

---

## Steps

```python
Steps(*labels, color="primary", orientation="horizontal", **kw)
```

DaisyUI steps component.

Use for progress through ordered steps.

Parameters:

- `*labels`: step labels
- `color`: semantic color
- `orientation`: `horizontal` or `vertical`
- `**kw`: passed to wrapper

Example:

```python
Steps("Account", "Profile", "Done", color="success")
```

---

## Tabs

```python
Tabs(*tabs, active=0, size="md", variant="", **kw)
```

DaisyUI tabs component.

Use for switching between related panels.

Parameters:

- `*tabs`: `(label, content)` tuples
- `active`: active tab index
- `size`: `xs`, `sm`, `md`, `lg`
- `variant`: `""`, `box`, `border`
- `**kw`: passed to wrapper

Example:

```python
Tabs(("Preview", Div("Preview content")), ("Code", Pre("...")), active=0)
```

---

## Timeline

```python
Timeline(*items, orientation="vertical", snap=False, **kw)
```

DaisyUI timeline component.

Use for histories, release notes, process steps, and event timelines.

Items are `(start, middle, end)` tuples.

Parameters:

- `*items`: timeline items
- `orientation`: `horizontal` or `vertical`
- `snap`: snap timeline layout
- `**kw`: passed to wrapper

Example:

```python
Timeline(("2025", "●", "Started"), ("2026", "●", "Released"))
```

---

# Mockups

## MockupBrowser

```python
MockupBrowser(*children, url="https://example.com", **kw)
```

DaisyUI browser mockup component.

Use for showing page previews.

Parameters:

- `*children`: browser content
- `url`: mock URL
- `**kw`: passed to wrapper

Example:

```python
MockupBrowser(H1("Demo"), url="https://example.com/app")
```

---

## MockupCode

```python
MockupCode(*lines, **kw)
```

DaisyUI code mockup component.

Use for terminal/code examples.

Lines can be strings or `(prefix, code)` tuples.

Parameters:

- `*lines`: code lines
- `**kw`: passed to wrapper

Example:

```python
MockupCode((">", "pip install psi-daisy"), ("✓", "Installed"))
```

---

## MockupPhone

```python
MockupPhone(*children, **kw)
```

DaisyUI phone mockup component.

Use for mobile UI previews.

Parameters:

- `*children`: phone screen content
- `**kw`: passed to wrapper

Example:

```python
MockupPhone(Div("Mobile preview"))
```

---

## MockupWindow

```python
MockupWindow(*children, **kw)
```

DaisyUI window mockup component.

Use for desktop/window UI previews.

Parameters:

- `*children`: window content
- `**kw`: passed to wrapper

Example:

```python
MockupWindow(H2("App Window"), P("Content"))
```

---

# Media and Effects

## Mask

```python
Mask(*children, shape="squircle", **kw)
```

DaisyUI mask component.

Use to clip images or content into predefined shapes.

Parameters:

- `*children`: masked content
- `shape`: `squircle`, `heart`, `hexagon`, `triangle`, `circle`, `diamond`, `square`, `parallelogram`
- `**kw`: passed to wrapper

Example:

```python
Mask(Img(src="/avatar.png"), shape="circle")
```

---

## MyIcon

```python
MyIcon(icon="lightbulb", color="primary", size=24, stroke_width=3, hex_color=None, **kw)
```

Lucide icon component.

Use for iconography throughout the app.

Parameters:

- `icon`: Lucide icon name
- `color`: semantic color
- `size`: icon size
- `stroke_width`: Lucide stroke width
- `hex_color`: optional raw hex color
- `**kw`: passed to icon element

Example:

```python
MyIcon("search", color="primary", size=20)
```

---

## Hover3D

```python
Hover3D(*children, **kw)
```

Custom hover-3D component.

Use for cards or panels with a 3D hover interaction.

Parameters:

- `*children`: content
- `**kw`: passed to wrapper

Example:

```python
Hover3D(Card("Hover me", cls="p-6"))
```

---

## HoverGallery

```python
HoverGallery(*items, **kw)
```

Custom hover gallery component.

Use for image/content galleries with hover effects.

Parameters:

- `*items`: gallery items
- `**kw`: passed to wrapper

Example:

```python
HoverGallery(Img(src="/a.png"), Img(src="/b.png"))
```

---

## TextRotate

```python
TextRotate(*texts, **kw)
```

Custom text rotation component.

Use for animated rotating words or phrases.

Parameters:

- `*texts`: text values to rotate through
- `**kw`: passed to wrapper

Example:

```python
TextRotate("FastHTML", "DaisyUI", "HTMX")
```

---

# Custom Components

## Calendar

```python
Calendar(**kw)
```

DaisyUI calendar component using Cally web components.

Use for date selection when you want a calendar UI.

Parameters:

- `**kw`: passed to calendar element

Example:

```python
Calendar(name="date")
```

Requires Cally JS headers, normally included by `psi_app()`.

---

## MyColor

```python
MyColor(name="color", web_color="dodgerblue", hex_color=None, label="Color", show_outputs=False, input_kw=None, **kw)
```

Custom color picker component with color code outputs.

Use for color selection and theme-building interfaces.

Parameters:

- `name`: input name
- `web_color`: CSS color name
- `hex_color`: optional hex color override
- `label`: label text, or `None`
- `show_outputs`: show web/rgb/hex/oklch outputs
- `input_kw`: extra attrs for color input
- `**kw`: passed to wrapper

Example:

```python
MyColor(name="primary", web_color="dodgerblue", show_outputs=True)
```

Use with:

```python
get_color_picker_headers()
```

---

## MyDate

```python
MyDate(name="date", year=2026, month=1, day=1, start_year=1900, end_year=2100, color="primary", size="md", variant="bordered", year_kw=None, month_kw=None, day_kw=None, **kw)
```

Custom date picker composed from select controls.

Use for controlled date selection.

Parameters:

- `name`: base field name
- `year`, `month`, `day`: initial date values
- `start_year`, `end_year`: year range
- `color`: semantic color
- `size`: select size
- `variant`: select variant
- `year_kw`, `month_kw`, `day_kw`: extra attrs for each select
- `**kw`: passed to wrapper

Example:

```python
MyDate(name="start", year=2026, month=7, day=12)
```

Use with:

```python
get_date_picker_headers()
```

---

## MyTime

```python
MyTime(name="time", hour=0, minute=0, second=0, color="primary", size="md", variant="bordered", hour_kw=None, minute_kw=None, second_kw=None, **kw)
```

Custom time picker composed from select controls.

Use for selecting hour/minute/second values.

Parameters:

- `name`: base field name
- `hour`, `minute`, `second`: initial time values
- `color`: semantic color
- `size`: select size
- `variant`: select variant
- `hour_kw`, `minute_kw`, `second_kw`: extra attrs for each select
- `**kw`: passed to wrapper

Example:

```python
MyTime(name="start_time", hour=9, minute=30)
```

Use with:

```python
get_time_picker_headers()
```

---

## MyDatetime

```python
MyDatetime(name="datetime", year=2026, month=1, day=1, start_year=1900, end_year=2100, hour=0, minute=0, second=0, color="primary", size="md", variant="bordered", date_kw=None, time_kw=None, **kw)
```

Custom datetime picker composed from `MyDate` and `MyTime`.

Use for selecting date and time together.

Parameters:

- `name`: base field name
- `year`, `month`, `day`: initial date values
- `start_year`, `end_year`: year range
- `hour`, `minute`, `second`: initial time values
- `color`: semantic color
- `size`: select size
- `variant`: select variant
- `date_kw`: extra attrs passed to date picker
- `time_kw`: extra attrs passed to time picker
- `**kw`: passed to wrapper

Example:

```python
MyDatetime(name="scheduled_at", year=2026, month=7, day=12, hour=14)
```

Use with:

```python
get_datetime_picker_headers()
```

---

## MyEmpty

```python
MyEmpty(title, *, body="", icon=None, action=None, color=None, variant="hero", compact=True, **kw)
```

Custom empty-state component.

Use when a page, list, search result, or panel has no data.

Parameters:

- `title`: empty state title
- `body`: optional explanatory text
- `icon`: optional icon/content
- `action`: optional action element
- `color`: optional semantic color
- `variant`: empty-state layout variant
- `compact`: compact layout
- `**kw`: passed to wrapper

Example:

```python
MyEmpty("No results", body="Try changing your filters.", action=Button("Reset"))
```

---

## ThemeController

```python
ThemeController(theme, **kw)
```

DaisyUI theme controller component.

Use to switch DaisyUI themes with the DaisyUI `theme-controller` pattern.

Parameters:

- `theme`: target theme name
- `**kw`: passed to input

Example:

```python
ThemeController("dark")
```

Conceptual output:

```html
<input type="checkbox" value="dark" class="theme-controller">
```

---

## Notes on Static CSS Bundles

When using `psi_app(css="static")`, only classes present in the generated static bundle are available.

Many `psi-daisy` components generate classes dynamically, such as:

```python
f"btn-{color}"
f"select-{variant}"
```

For static builds, those dynamic class families need to be included in `styles/daisyui/input.css` using `@source inline(...)`.

See:

```text
docs/Static_CSS_Bundle.md
```

for bundle build and safelisting details.
