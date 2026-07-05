# ################################
# File:     introspect.py
# Module:   utils
# Author:   lucien@psispark.com
# Task:     Component introspection helpers for psi-daisy demos & tests.
# Release:  v0.1
# History:
#   * 001, ai, 260607, refactor
#   * 002, Luch, 260608, fixed package path 
#   * 003, Luch, 260704, get sample args 
# ################################

import inspect, importlib, typing
from pathlib import Path
import psi_daisy.ui as ui
from psi_daisy.utils.constants import SAMPLE_ARGS


def components_dir():
    """Get the components directory from the ui module."""
    return Path(ui.__file__).parent


def all_components():
    """List all component modules in the ui directory."""
    return sorted(f.stem for f in components_dir().glob("*.py")
                  if not f.stem.startswith('_') and f.stem not in ('css', 'types'))


def get_literal_values(p_anot):
    """Returns a list of values if the annotation is a typing.Literal"""
    if typing.get_origin(p_anot) is typing.Literal:
        return list(typing.get_args(p_anot))
    return None


def get_component_fn(name):
    """Get component function by component name"""
    try: mod = importlib.import_module(f"psi_daisy.ui.{name}")
    except ModuleNotFoundError: return None
    target = name.replace("_", "").lower()
    return next((o for k,o in vars(mod).items() if callable(o) and not k.startswith("_") and k.replace("_", "").lower() == target), None)


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


def get_sample_call_args(fn, component, sample_args, sample_children):
    """Get sample args/kwargs for a component call"""
    sig = inspect.signature(fn)
    pos_args,literal_params,bool_params,var_positional = get_param_info(fn)
    children = sample_children.get(component, sample_children["_default"])
    vals = {k:v[0] for k,v in literal_params.items() if v and v[0] != ""}
    vals.update({p.name:sample_args[p.name] for p in sig.parameters.values() if p.kind is inspect.Parameter.KEYWORD_ONLY and p.default is inspect.Parameter.empty and p.name in sample_args})
    bools = {k:True for k in bool_params[:1]}
    args = [*pos_args, *children] if var_positional else pos_args
    return args, {**vals, **bools}


def get_required_kw(fn):
    """Get required keyword-only sample args"""
    sig = inspect.signature(fn)
    return {p.name:SAMPLE_ARGS[p.name] for p in sig.parameters.values() if p.kind is inspect.Parameter.KEYWORD_ONLY and p.default is inspect.Parameter.empty and p.name in SAMPLE_ARGS}
    