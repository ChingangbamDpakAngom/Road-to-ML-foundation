# 📈 Progress Tracker — Road to ML Foundation

> Update this file **every study day**: tick the boxes you finished, then commit.
> Your git commits are the real heatmap — this file is the map of where you are.
>
> Legend: `[ ]` not started · `[x]` done · Move the 👉 marker to your current week.

---

## 🎯 Current Status

| | |
|---|---|
| **Current week** | 👉 Week 1 — Python Core (Phase 1) |
| **Started** | 2026-07-16 |
| **Plan** | v3 — project-first 26-week merge (see [`ROADMAP.md`](ROADMAP.md)) |
| **Target finish (26-week plan)** | ~2027-01-13 |
| **Guide to follow now** | [`guides/week01_python_core.md`](guides/week01_python_core.md) |

### Phase progress (v3 — 6-project spine)

```
Phase 1  Python Core         [░░░░]  0/4 weeks   → Expense Tracker CLI
Phase 2  Engineering         [░░░░]  0/4 weeks   → Job App Tracker API
Phase 3  Data                [░░░░]  0/4 weeks   → Job Skills Analysis (Capstone 1)
Phase 4  Math for ML         [░░]    0/2 weeks   🧮 kept — do not skip
Phase 5  Classical ML        [░░░░]  0/4 weeks   → Skill Classifier
Phase 6  Deep Learning       [░░░░]  0/4 weeks   → PyTorch experiment
Phase 7  Applied AI          [░░░░]  0/4 weeks   → RAG/Copilot (Capstone 2)
```

Cross-cutting (parallel from Day 1): **DSA** (NeetCode patterns, 3×/wk) ·
**MLOps** (woven from Phase 5) · **Professional Git/PR loop** (from Phase 2).

---

## ⚡ Week 1 — Python Core (7 days) → Expense Tracker v0

> Week 1 of the 4-week Python Core phase (v3). Guide:
> [`guides/week01_python_core.md`](guides/week01_python_core.md). DSA runs in
> parallel from Day 1. The tracker is **in-memory only** this week — JSON
> persistence is Week 2.

- [ ] **Day 1** — Setup + venv, variables, data types, strings/f-strings · *DSA: Two Sum · +2 interview Qs*
- [ ] **Day 2** — Control flow: if/elif/else, loops, range, enumerate · *DSA: Contains Duplicate · +2 Qs*
- [ ] **Day 3** — Functions, args/kwargs, scope/LEGB, `make_expense` record · *DSA: Valid Anagram · +2 Qs*
- [ ] **Day 4** — Just-enough collections: a list of expense dicts · *+2 interview Qs*
- [ ] **Day 5** — 🏗️ Expense Tracker v0: add + list + summary menu loop · *+2 interview Qs*
- [ ] **Day 6** — Validation + `argparse` CLI (add/list subcommands), ruff-clean · *+2 interview Qs*
- [ ] **Day 7** — Review + weekly check-in · *DSA: Group Anagrams*

**Week 1 exit test (all must be true):**
- [ ] `python expenses.py add …` and `python expenses.py list` run without crashing
- [ ] I can write a `*args`/`**kwargs` function and explain LEGB without notes
- [ ] Expenses modelled as a list of dicts; I can total/filter them
- [ ] 5+ meaningful commits; 4 DSA problems logged
- [ ] I answered all 12 interview questions out loud

---

## 📅 Weeks 2–26

> Day-level checklists get added when each week's guide is generated —
> ask Claude at the start of each week: *"create the week N guide"*.
> Full detail for every week lives in [`ROADMAP.md`](ROADMAP.md).

### Phase 1 — Python Core → *Expense Tracker CLI*
- [ ] **Week 1 — Setup + core syntax** · venv, variables, conditions, loops, functions → ship: repo + `add-expense`, 5+ commits *(current)*
- [ ] **Week 2 — Collections + persistence** · lists/dicts/sets, comprehensions, JSON, exceptions → ship: persistence + categories
- [ ] **Week 3 — OOP + tests** · modules, classes/inheritance/dunders, generators, type hints, pytest → ship: 10+ tests, modular code
- [ ] **Week 4 — Polish + release** · decorators, CLI UX (argparse/Typer), README → ship: **v1.0 release**, 15+ tests

### Phase 2 — Engineering → *Job Application Tracker API*
- [ ] **Week 5 — FastAPI + schema** · HTTP/REST, Pydantic, SQLite → ship: create/list companies & applications
- [ ] **Week 6 — CRUD + validation** · endpoints, filters, API tests → ship: working API + interactive docs
- [ ] **Week 7 — SQL + observability** · SQL, logging, errors, env vars → ship: status/deadline queries, DB tests
- [ ] **Week 8 — CI + packaging + Docker** · GitHub Actions, README, first container → ship: passing CI, clean install

### Phase 3 — Data → *Job Skills Analysis*
- [ ] **Week 9 — NumPy + Pandas intake** · arrays, broadcasting, masking; import/inspect → ship: data dictionary + raw import
- [ ] **Week 10 — Cleaning pipeline** · missing values, merges, groupby, pivot → ship: reproducible cleaning
- [ ] **Week 11 — SQL + viz** · JOINs/GROUP BY/window fns, Matplotlib + Seaborn → ship: charts that each answer one question
- [ ] **Week 12 — 🏆 CAPSTONE 1** · narrative EDA notebook, reproducible → ship: full EDA report

### Phase 4 — Math for ML 🧮 *(kept — do not skip)*
- [ ] **Week 13 — Linear algebra** · vectors, matmul, norms, eigen/SVD (3Blue1Brown + NumPy) → ship: matrix ops from scratch
- [ ] **Week 14 — Calculus + probability** · chain rule, gradients, Bayes, MLE, CLT → ship: **gradient descent from scratch**

### Phase 5 — Classical ML → *Skill Classifier*
- [ ] **Week 15 — Regression + baselines** · split/leakage, preprocessing, TF-IDF, lin/log reg (sklearn *and* own GD) → ship: baseline classifier
- [ ] **Week 16 — Models + CV** · trees, RF, boosting, SVM, KNN, NB, pipelines, cross-validation → ship: 3+ model comparison
- [ ] **Week 17 — Metrics + tuning** · P/R/F1, ROC-AUC, imbalance, GridSearchCV, error analysis → ship: tuned pipeline
- [ ] **Week 18 — Serve + from-scratch mini-lab** · model card, inference API; linreg/logreg/K-Means/PCA in NumPy → ship: reproducible inference

### 🚪 Deep Learning Readiness Gate (from ROADMAP.md)
- [ ] All 8 gate boxes in [`ROADMAP.md`](ROADMAP.md#-deep-learning-readiness-gate--kept-from-v2) checked → **start PyTorch phase**

### Phase 6 — Deep Learning → *PyTorch experiment*
- [ ] **Week 19 — Tensors + data** · shapes, devices, Dataset/DataLoader (+ optional 2-layer NN in NumPy) → ship: data pipeline
- [ ] **Week 20 — Training loop** · nn.Module, loss, optimiser, autograd → ship: baseline loop, losses plotted
- [ ] **Week 21 — Experiment** · regularisation/augmentation, one controlled change → ship: change + effect stated
- [ ] **Week 22 — Evaluate + report** · saving/loading, failure cases → ship: complete experiment + model artefact

### Phase 7 — Applied AI → *RAG / Career Copilot*
- [ ] **Week 23 — Scope + ingestion** · architecture, retrieval/workflow → ship: diagram + samples
- [ ] **Week 24 — Grounded pipeline** · embeddings, chunking, retrieval, citations → ship: sources exposed
- [ ] **Week 25 — Evaluate + guardrails** · eval set, failure cases → ship: 20–30 examples documented
- [ ] **Week 26 — 🏆 CAPSTONE 2** · deploy (Docker + cloud), demo, model card → ship: 2–3 min demo, reproducible

### Cross-cutting (parallel, from Day 1)
- [ ] **DSA** — NeetCode 150 patterns, 3 sessions/week (see ROADMAP DSA table)
- [ ] **Professional Git/PR loop** — from Phase 2 onward, every feature
- [ ] **Interview sprint** — 8-week ramp near the end of Phase 7

---

## 🗓️ Push log

> One line per study day. Keeps you honest.

| Date | Day/Week | What I did | Commit? |
|------|----------|------------|:-------:|
| 2026-07-16 | W1 setup | Repo + roadmap + tracker + guide created | ✅ |
