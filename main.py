#!/usr/bin/env python3
import importlib
import importlib.util
from pathlib import Path
import sys


def load_custom_node(path: str) -> str:
    pkg = Path(path)
    if pkg.is_dir():
        pkg = Path(sys.argv[1]) / "__init__.py"

    spec = importlib.util.spec_from_file_location("jobs", pkg)
    if spec is None or spec.loader is None:
        raise ImportError(f"Failed to import {sys.argv[1]}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    print("here")
    print(module.NODE_CLASS_MAPPINGS)
    print("here")
    return


if __name__ == "__main__":
    load_custom_node(sys.argv[1])
