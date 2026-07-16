"""Day 7 Mini-Project — CLI Task Manager.

Run it:  python task_manager.py

This is a SKELETON — every `...` is yours to write. It must prove the whole
week: OOP, dunders, type hints, JSON persistence, a decorator, a generator,
comprehensions, custom exceptions, and a menu loop.

Definition of done (from the Week 1 guide):
  add / list / complete / delete tasks, saved to tasks.json,
  bad input never crashes it, mypy-clean.
"""

from __future__ import annotations

import json
from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Iterator

TASKS_FILE = Path(__file__).parent / "tasks.json"


class TaskNotFoundError(Exception):
    """Raised when a task id doesn't exist."""


def logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator: print the method name and arguments on every call."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        ...  # TODO: print, then call func

    return wrapper


class Task:
    """One task: title, priority (1=high..3=low), created date, done flag."""

    def __init__(self, title: str, priority: int = 2) -> None:
        ...  # TODO: also set self.created = datetime.now(), self.done = False

    def __str__(self) -> str:
        ...  # TODO: something like "[x] (1) buy milk  — 2026-07-22"

    # TODO: to_dict() and a from_dict() classmethod for JSON round-trips


class TaskManager:
    """Owns the task list and its persistence."""

    def __init__(self, path: Path = TASKS_FILE) -> None:
        ...  # TODO: load tasks from JSON if the file exists

    @logger
    def add(self, title: str, priority: int = 2) -> Task:
        ...

    @logger
    def complete(self, task_id: int) -> None:
        ...  # TODO: raise TaskNotFoundError if missing

    @logger
    def delete(self, task_id: int) -> None:
        ...  # TODO: raise TaskNotFoundError if missing

    def pending(self) -> Iterator[Task]:
        """Generator: yield unfinished tasks (use it in the menu)."""
        ...

    def high_priority_pending(self) -> list[Task]:
        """Comprehension: pending AND priority == 1."""
        ...

    def save(self) -> None:
        ...  # TODO: write all tasks to self.path as JSON


def main() -> None:
    manager = TaskManager()
    while True:
        print("\n1) add  2) list all  3) list pending  4) high-priority  "
              "5) complete  6) delete  q) quit")
        choice = input("> ").strip().lower()
        # TODO: dispatch on choice; wrap risky parts in try/except so
        #       bad input (letters where numbers go, unknown ids) NEVER crashes.
        if choice == "q":
            break


if __name__ == "__main__":
    main()
