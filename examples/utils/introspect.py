# ################################
# File:     introspect.py
# Module:   examples.utils
# Author:   lucien@psispark.com
# Task:     Component introspection helpers for psi-daisy demos.
# Release:  v0.1
# History:
#   * 001, ai, 260607, refactor
#   * 002, Luch, 260608, fixed package path 
# ################################

import inspect, importlib, typing
from pathlib import Path
import psi_daisy.ui as ui
from examples.utils.constants import SAMPLE_ARGS


def components_dir():
    """Get the components directory from the ui module."""
    return Path(ui.__file__).parent


def all_components():
    """List all component modules in the ui directory."""
    return sorted(f.stem for f in components_dir().glob("*.py")
                  if not f.stem.startswith('_') and f.stem not in ('css', 'types'))


def get_literal_values(p_anot):
    if typing.get_origin(p_anot) is typing.Literal:
        return list(typing.get_args(p_anot))
    return None


def get_component_fn(name):
    """Import and return the component function from the ui module."""
    mod = importlib.import_module(f"psi_daisy.ui.{name}")
    fn_name = ''.join(w.title() for w in name.split('_'))
    return getattr(mod, fn_name, None)


def get_param_info(fn):
    """Return (positional args, literal params, bool params, var args)."""
    poz_args, lit_params, bool_params = [], {}, []
    var_args = False
    for pname, param in inspect.signature(fn).parameters.items():
        if param.kind == inspect.Parameter.VAR_POSITIONAL:
            var_args = True; continue
        if param.kind == inspect.Parameter.VAR_KEYWORD: 
            continue
        p_anot = param.annotation
        lits = get_literal_values(p_anot)
        if lits and param.default != inspect.Parameter.empty:
            lit_params[pname] = lits
        elif p_anot is bool or p_anot == typing.Optional[bool]:
            bool_params.append(pname)
        elif param.default == inspect.Parameter.empty:
            poz_args.append(SAMPLE_ARGS.get(pname, f"Sample {pname.title()}"))
    return poz_args, lit_params, bool_params, var_args
