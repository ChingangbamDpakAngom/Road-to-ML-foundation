# ⚔️ Week 1 Guide — Python Foundations Sprint (7 Days)

> **Read this first.** This guide compresses the roadmap's Weeks 1–2 into one week.
> It is doable, but only under these conditions:
>
> - **Time**: 4–5 focused hours/day (2 weeks of material in 1). If you only have
>   2 hours/day, use the original 2-week pace — don't pretend.
> - **Rule of hands**: every concept gets typed by you into a notebook or `.py`
>   file. Reading/watching without coding counts as **zero** progress.
> - **Fallback checkpoint**: end of Day 4. More than one day behind? Expand back
>   to 2 weeks. No shame — the plan absorbs it.
>
> **Daily structure (repeat all 7 days):**
> 1. 📖 Study (60–90 min) — read/watch the day's material
> 2. ⌨️ Code (2–3 h) — do every exercise, no copy-paste
> 3. 🎤 Interview reps (20 min) — answer the day's questions **out loud**, then write the answer in `04_interview_prep/python_qa.md`
> 4. ✅ Commit & push — update `PROGRESS.md`, meaningful commit message
>
> Work in `01_python_foundations/` — one folder per day is fine.

---

## 📅 Day 1 — Setup, Variables, Strings, Control Flow

**Study:** [Python tutorial ch. 3–4](https://docs.python.org/3/tutorial/introduction.html) · variables, `int/float/str/bool`, f-strings, `if/elif/else`, `for`, `while`, `range`, `break/continue`

**Code — exercises (all of them):**
1. FizzBuzz (1–50).
2. Given a string, print it reversed, uppercased, and report vowel count — f-strings only.
3. Guess-the-number game: random target, loop until guessed, count attempts.
4. Print a right triangle of `*` of height n (nested loops).
5. Sum all numbers 1–1000 divisible by 3 or 5 — once with a loop, once with `sum()` + `range`.

**🎤 Interview Qs of the day:**
- Q1: What's the difference between `is` and `==` in Python?
- Q2: Is Python pass-by-value or pass-by-reference? What actually happens when you pass a list to a function?

**Commit:** `Day 1: basics + control flow — FizzBuzz, string ops, guessing game`

---

## 📅 Day 2 — Data Structures + Comprehensions

**Study:** [Python tutorial ch. 5](https://docs.python.org/3/tutorial/datastructures.html) · list methods, slicing, tuples & unpacking, sets & set ops, dicts (`.get`, `.items`, nesting), then list/dict/set comprehensions

**Code — exercises:**
1. Word frequency counter for a paragraph → dict, print top 3 (no `collections` yet — then redo with `Counter`).
2. Given two lists, produce: common elements, elements only in the first, union — using sets.
3. Flatten `[[1,2],[3,4],[5]]` → `[1,2,3,4,5]` with a comprehension.
4. Build `{word: len(word)}` for a sentence — dict comprehension, only words longer than 3 chars.
5. Swap keys and values of a dict. What breaks if values aren't unique? Write the answer as a comment.
6. Student gradebook: nested dict `{name: {subject: score}}` — add, update, compute per-student average.

**🎤 Interview Qs:**
- Q3: List vs tuple — differences, and when do you *need* a tuple? (hint: dict keys, hashability)
- Q4: How does a Python dict work internally? What makes lookup O(1)?

**Commit:** `Day 2: data structures + comprehensions — word freq, set ops, gradebook`

---

## 📅 Day 3 — Functions & Functional Python

**Study:** functions, default args (⚠️ the mutable-default-argument trap), `*args/**kwargs`, return tuples, scope/LEGB, `lambda`, `map`, `filter`, `functools.reduce`, `sorted(key=...)`

**Code — exercises:**
1. `stats(*numbers)` → returns `(mean, min, max)` as a tuple; call it with a list using `*` unpacking.
2. Demonstrate the mutable-default-arg bug (`def f(x, acc=[])`), then fix it with `None`.
3. Sort a list of `(name, age, salary)` tuples by salary desc, then by age asc — `sorted` with `lambda`.
4. Rewrite these with comprehensions AND with map/filter — decide which reads better: squares of evens 1–20; lengths of words longer than 4.
5. `reduce` to compute the product of a list, then to find the longest word.
6. Write `apply_n_times(func, x, n)` — applies func to x, n times. Test with `lambda v: v*2`.

**🎤 Interview Qs:**
- Q5: What is the LEGB rule? What does `global`/`nonlocal` do?
- Q6: What are `*args` and `**kwargs`? Show a real use case (e.g., a wrapper function).

**Commit:** `Day 3: functions, lambda, map/filter/reduce`

---

## 📅 Day 4 — OOP ← ⚠️ FALLBACK CHECKPOINT

**Study:** [Real Python OOP](https://realpython.com/python3-object-oriented-programming/) · classes, `__init__`, instance vs class attributes, methods, inheritance, `super()`, dunders (`__str__`, `__repr__`, `__len__`, `__eq__`), `@property`

**Code — build a small bank system:**
1. `Account` class: `owner`, `balance`; methods `deposit`, `withdraw` (no overdraft — raise `ValueError`), nice `__str__`.
2. `SavingsAccount(Account)`: adds `interest_rate` and `apply_interest()`; use `super().__init__`.
3. Add `__eq__` (same owner+balance) and `__len__` (transaction count) — keep a transaction history list.
4. `@property` for `balance` so it can't be set directly from outside.
5. A `Bank` class holding many accounts: open account, find by owner, total assets.

**🎤 Interview Qs:**
- Q7: `__str__` vs `__repr__`? Class attribute vs instance attribute — show a bug caused by confusing them.
- Q8: What is MRO (method resolution order)? What does `super()` actually do in multiple inheritance?

**Checkpoint:** Days 1–4 all done? → continue. More than a day behind? → switch to 2-week pace (this becomes Day 1 of Week 2, guilt-free).

**Commit:** `Day 4: OOP — bank account system with inheritance and dunders`

---

## 📅 Day 5 — Decorators & Generators

**Study:** [Real Python decorators primer](https://realpython.com/primer-on-python-decorators/) · closures first, then decorators, `functools.wraps`; generators: `yield`, generator expressions, why they're memory-efficient; skim `itertools` (`count`, `islice`, `chain`)

**Code — exercises:**
1. Closure: `make_multiplier(n)` returning a function that multiplies by n.
2. `@timer` decorator — prints how long the function took. Use `functools.wraps`.
3. `@logger` — prints function name + arguments each call. Stack it with `@timer`; which order runs first? Write the answer as a comment.
4. `@retry(times=3)` — a decorator **with an argument** that retries on exception.
5. Generator `fibonacci()` — infinite; take the first 20 with `itertools.islice`.
6. `read_large_file(path)` generator yielding one line at a time; explain in a comment why this beats `f.readlines()` for a 10 GB file.
7. Sum of squares under 1,000,000 with a generator expression (no list in memory).

**🎤 Interview Qs:**
- Q9: What is a decorator? What problem does `functools.wraps` solve?
- Q10: Generator vs list — memory tradeoff. What does `yield` do to a function's execution?

**Commit:** `Day 5: decorators (timer/logger/retry) + generators`

---

## 📅 Day 6 — Files, Exceptions, Context Managers, Type Hints

**Study:** `open` modes, `with` blocks, `pathlib.Path`, `json` module, `csv` module; `try/except/else/finally`, raising, custom exceptions; type hints (`list[int]`, `dict[str, float]`, `Optional`, function signatures)

**Code — exercises:**
1. Write a dict to JSON, read it back, verify round-trip equality.
2. Read a CSV of students+scores, compute averages, write results to a new CSV.
3. `safe_divide(a, b)` — full `try/except/else/finally`, returns `None` on division by zero with a warning.
4. Custom exception `InsufficientFundsError` — retrofit it into Day 4's bank.
5. Write your own context manager class (`__enter__`/`__exit__`) that times a code block; then redo it with `@contextlib.contextmanager`.
6. Add type hints to ALL of Day 4's bank code; run `mypy` on it and fix every error.

**🎤 Interview Qs:**
- Q11: What does `with` do? What are `__enter__` and `__exit__`?
- Q12: `except Exception` vs bare `except:` — why is the bare one dangerous?

**Commit:** `Day 6: file I/O, exceptions, context managers, mypy-clean bank`

---

## 📅 Day 7 — 🏗️ Mini-Project: CLI Task Manager + Review

**Build (3–4 h) — `01_python_foundations/task_manager/`:**

A command-line task manager proving everything this week:

- `Task` class: title, priority, created date, done flag (**OOP, dunders, type hints**)
- `TaskManager` class: add / list / complete / delete; tasks persist to `tasks.json` (**file I/O, JSON**)
- `@logger` decorator on every state-changing method (**decorators**)
- Iterating tasks uses a generator; filtering ("show only pending, high-priority") uses comprehensions (**generators, comprehensions**)
- Bad input never crashes it — custom `TaskNotFoundError` etc. (**exceptions**)
- Simple menu loop: `while True` + `input()` (**control flow**)
- Fully type-hinted, `mypy` clean

**Review (1 h):**
1. Re-answer all 12 interview questions out loud, no notes. Any you fumble → reread that day's topic.
2. From memory, write: one decorator, one generator, one class with inheritance. Compare with your Day 4–5 code.
3. Update `PROGRESS.md`: tick Week 1 exit-test boxes honestly.

**Commit:** `Week 1 COMPLETE: CLI task manager — Python foundations sprint done 🟦`

> 🟦 **Stage 1: AWAKENED unlocked.** Next: ask Claude to *"create the week 2 guide"* (NumPy).

---

## 📚 If you get stuck

- One concept, ≤ 20 min stuck → reread + try smaller example
- Still stuck → ask Claude to *explain* (not solve) — you must still type the solution
- A whole day feels impossible → that's the signal: switch to the 2-week pace
