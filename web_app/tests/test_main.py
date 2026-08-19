"""Unit tests for main.py"""

import sys
from pathlib import Path

# Automatically finds the 'web_apps' directory and adds it to Python
sys.path.append(str(Path(__file__).resolve().parent.parent))

import main


def test_root():
    """Docstring"""
    assert main.root() == {"message": "Hello World"}


def test_convert():
    """Docstring"""
    assert main.convert("PA", "Pittsburgh") == {
        "lat": "40.4416941",
        "long": "-79.9900861",
    }
