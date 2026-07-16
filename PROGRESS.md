# 📈 Progress Tracker — Road to ML Foundation

> Update this file **every study day**: tick the boxes you finished, then commit.
> Your git commits are the real heatmap — this file is the map of where you are.
>
> Legend: `[ ]` not started · `[x]` done · Move the 👉 marker to your current week.

---

## 🎯 Current Status

| | |
|---|---|
| **Current week** | 👉 Week 1 — Python Sprint |
| **Started** | 2026-07-16 |
| **Target finish (14-week plan)** | ~2026-10-21 (earlier if the Week-1 sprint succeeds) |
| **Guide to follow now** | [`guides/week01_python_sprint.md`](guides/week01_python_sprint.md) |

### Phase progress

```
Phase 1  Python              [░░░░░░░]  0/7 days
Phase 2  Data Stack          [░░░]      0/3 weeks
Phase 3  Math for ML         [░░]       0/2 weeks
Phase 4  Machine Learning    [░░░]      0/3 weeks
Phase 5  SQL + Capstone      [░░]       0/2 weeks
Phase 6  Bridge to DL        [░░]       0/2 weeks
```

---

## ⚡ Week 1 — Python Foundations SPRINT (1 week, compressed)

> This compresses the roadmap's Weeks 1–2 into 7 days. **Fallback rule:** if by
> the end of Day 4 you are more than one day behind, stop compressing — switch
> back to the 2-week pace. Speed with gaps costs more later than one extra week.

- [ ] **Day 1** — Setup + variables, data types, strings/f-strings, if/elif/else, loops · *+2 interview Qs*
- [ ] **Day 2** — Lists, tuples, sets, dicts + list/dict/set comprehensions · *+2 interview Qs*
- [ ] **Day 3** — Functions, args/kwargs, scope, lambda, map/filter/reduce · *+2 interview Qs*
- [ ] **Day 4** — OOP: classes, `__init__`, inheritance, `super()`, dunder methods · *+2 interview Qs* ← **fallback checkpoint**
- [ ] **Day 5** — Decorators & generators (`yield`, generator expressions) · *+2 interview Qs*
- [ ] **Day 6** — File I/O, exceptions, context managers, type hints · *+2 interview Qs*
- [ ] **Day 7** — 🏗️ Mini-project: CLI Task Manager (OOP + files + exceptions) + weekly review

**Week 1 exit test (all must be true):**
- [ ] Task manager works: add/list/complete/delete tasks, saves to JSON
- [ ] I can write a class with inheritance without looking anything up
- [ ] I can explain a decorator and a generator in plain words
- [ ] I answered all 12 interview questions out loud

---

## 📅 Weeks 2–14

> If the Week-1 sprint succeeds, every week below shifts one week earlier.
> Day-level checklists get added when each week's guide is generated —
> ask Claude at the start of each week: *"create the week N guide"*.

### Phase 2 — Data Stack
- [ ] **Week 2 — NumPy** · arrays, indexing, broadcasting, masking, linalg → ship: image manipulation project
- [ ] **Week 3 — Pandas** · DataFrames, loc/iloc, cleaning, groupby, merge, pivot → ship: cleaned Kaggle dataset
- [ ] **Week 4 — Visualization** · Matplotlib + Seaborn → ship: 🏆 **CAPSTONE 1: full EDA notebook**

### Phase 3 — Math for ML
- [ ] **Week 5 — Linear algebra** · vectors, matmul, norms, eigenvalues (3Blue1Brown + NumPy) → ship: matrix ops from scratch
- [ ] **Week 6 — Calculus + probability** · chain rule, gradients, Bayes, MLE, CLT → ship: **gradient descent from scratch**

### Phase 4 — Machine Learning
- [ ] **Week 7 — Regression** · preprocessing, linear & logistic regression (sklearn *and* own GD) → ship: comparison notebook
- [ ] **Week 8 — Classifiers** · trees, random forest, boosting, SVM, KNN, NB → ship: 4-model Kaggle comparison
- [ ] **Week 9 — Unsupervised + evaluation** · clustering, PCA, CV, metrics, GridSearchCV, Pipeline → ship: end-to-end pipeline

### Phase 5 — Job-Ready Layer
- [ ] **Week 10 — SQL** · JOINs, GROUP BY, subqueries, window functions → ship: Pandas analysis redone in SQL
- [ ] **Week 11 — 🏆 CAPSTONE 2** · end-to-end ML project with proper README → ship: your interview showpiece

### Phase 6 — Bridge to Deep Learning
- [ ] **Week 12 — From-scratch week** · linreg, logreg, K-Means, PCA, **2-layer neural net with backprop** (NumPy only)
- [ ] **Week 13 — Interview prep** · 60-question bank from README + mock interview + portfolio polish

### 🚪 Deep Learning Readiness Gate (from ROADMAP.md)
- [ ] All 8 gate boxes in [`ROADMAP.md`](ROADMAP.md#-deep-learning-readiness-gate) checked → **start PyTorch module**

---

## 🗓️ Push log

> One line per study day. Keeps you honest.

| Date | Day/Week | What I did | Commit? |
|------|----------|------------|:-------:|
| 2026-07-16 | W1 setup | Repo + roadmap + tracker + guide created | ✅ |
