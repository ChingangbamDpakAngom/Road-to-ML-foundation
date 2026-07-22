# 🎤 Python Interview Q&A Log — Week 1 (Python Core)

> After answering each day's questions **out loud**, write your final answer here
> in your own words. On Day 7 you re-answer all 12 from memory — this file is
> your answer key. Don't paste textbook definitions; write what YOU would say.
>
> *(Updated for the v3 plan: Week 1 is now Python Core syntax + functions. OOP,
> decorators and file-handling questions move to the Week 2–3 logs.)*

## Day 1 — Setup, variables, strings
**Q1: `is` vs `==`?**
> The `==` operator compares the value or equality of two objects, whereas the Python `is` operator checks whether two variables point to the same object in memory

**Q2: Is Python pass-by-value or pass-by-reference? What happens when you pass a list to a function?**
> Pass-by-Reference (Mutable Objects) When dealing with mutable objects, such as lists and dictionaries, Python passes a reference to the object instead of copying its value. This means changes within the function are reflected outside it

## Day 2 — Control flow
**Q3: What values are "falsy" in Python? How does `if my_list:` behave for an empty list?**
>

**Q4: Difference between `range(n)` and `list(range(n))` — why doesn't `range` build the whole list?**
>

## Day 3 — Functions & scope
**Q5: The LEGB rule? What do `global`/`nonlocal` do?**
>

**Q6: `*args` and `**kwargs` — what are they, and a real use case?**
>

## Day 4 — Collections as records
**Q7: When would you use a list vs a dict? Why is a dict the right shape for one expense?**
>

**Q8: What does `dict.get("x")` return if the key is missing, and why is that safer than `dict["x"]`?**
>

## Day 5 — Structuring the tracker
**Q9: Why break a script into small functions instead of one long block?**
>

**Q10: Your tracker forgets everything on exit — what one change fixes that, and why isn't it in Week 1?**
>

## Day 6 — Validation & CLI
**Q11: Why validate user input at the boundary instead of trusting it? Give a bad-input example for the tracker.**
>

**Q12: Why use `argparse` over hardcoded variables or `input()` for a real tool?**
>
