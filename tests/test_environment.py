"""Smoke checks for the local development environment."""

import sys

import telegram

import quiniela_bot


def test_project_uses_python_312() -> None:
    assert sys.version_info[:2] == (3, 12)


def test_application_package_imports() -> None:
    assert quiniela_bot.__doc__


def test_telegram_dependency_matches_initial_pin() -> None:
    assert telegram.__version__ == "22.8"
