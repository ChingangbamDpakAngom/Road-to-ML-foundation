# 🗺️ Refined Roadmap — Road to ML Foundation

> Single source of truth for the learning schedule. The gamified README
> (README_igris_upgrade.md) is the fun layer; **this file is the plan**.
> Repo: https://github.com/ChingangbamDpakAngom/Road-to-ML-foundation
>
> Pace assumption: **1.5–3 hours/day, 6–7 days/week.** If a week isn't done,
> the week rolls over — never skip ahead with gaps.

---

## Why this revision?

The original 8-week plan had three problems:

1. **Two conflicting timelines** — an "8-Week Quest Plan" and a "Week 1–18"
   activity tracker in the same README. This is the merged, single timeline.
2. **No math phase** — the old plan jumped from Pandas straight to
   Scikit-Learn, and math only appeared as Week-8 interview questions.
   Deep learning without linear algebra + calculus + probability is where
   most self-taught journeys stall. Math now gets 2 dedicated weeks.
3. **No bridge to deep learning** — Week 8 quizzed backprop and vanishing
   gradients, but nothing in the plan ever taught them. Week 13 now builds
   a tiny neural network from scratch as the exit exam for this repo.

Also added: **SQL** (required in ~every data/ML job posting, absent from the
original plan) and two **portfolio-grade capstones** (weekly mini-projects
are practice; capstones are what recruiters actually open).

---

## 📅 The 14-Week Plan

### Phase 1 — Python (Weeks 1–2) ✅ keep as originally planned

| Week | Focus | Ship on Sunday |
|:---:|-------|----------------|
| 1 | Syntax, control flow, data structures (lists/tuples/sets/dicts), functions, args/kwargs, scope | CLI calculator |
| 2 | OOP (classes, inheritance, dunders), comprehensions, lambda/map/filter, decorators, generators, file I/O, exceptions, type hints | Task manager app (OOP, saves to JSON file) |

### Phase 2 — Data Stack (Weeks 3–5)

| Week | Focus | Ship on Sunday |
|:---:|-------|----------------|
| 3 | NumPy: array creation, indexing/slicing, reshape/concat, ufuncs, **broadcasting**, boolean masking, `np.random`, intro `np.linalg` | Image manipulation with raw NumPy arrays |
| 4 | Pandas: Series/DataFrame, `.loc`/`.iloc`, cleaning (`dropna`/`fillna`), groupby/agg, merge/concat, pivot, time series basics | Cleaned + analyzed messy Kaggle dataset |
| 5 | Matplotlib (plots, subplots, annotations) + Seaborn (dist, categorical, heatmap, pairplot) | **CAPSTONE 1: full EDA notebook** on a real dataset — question → cleaning → analysis → 6+ visualizations → written conclusions |

### Phase 3 — Math for ML (Weeks 6–7) 🆕 the missing piece

| Week | Focus | Ship on Sunday |
|:---:|-------|----------------|
| 6 | **Linear algebra**: vectors, matrix multiplication (by hand *and* `np.dot`), norms, linear transformations, eigenvalues/eigenvectors, SVD intuition. Resource: 3Blue1Brown "Essence of Linear Algebra" + NumPy exercises | Notebook: implement matrix ops from scratch, verify against NumPy |
| 7 | **Calculus + probability**: derivatives, chain rule, partial derivatives, gradients; then distributions, Bayes' theorem, expectation/variance, MLE, CLT. Resource: 3Blue1Brown "Essence of Calculus", StatQuest | **Gradient descent from scratch** minimizing a simple function, with a plot of the loss curve |

> Every math topic must end as a NumPy notebook, not just watched videos.
> Watching ≠ learning; implementing = learning.

### Phase 4 — Machine Learning (Weeks 8–10)

| Week | Focus | Ship on Sunday |
|:---:|-------|----------------|
| 8 | Preprocessing (scaling, encoding, imputation), train/test split, **Linear & Logistic Regression** — connect these directly to Week 7's gradient descent | Linear regression two ways: sklearn *and* your own gradient descent — compare coefficients |
| 9 | Trees (Gini/entropy), Random Forest, Gradient Boosting, SVM (kernels), KNN, Naive Bayes | Classification on a Kaggle dataset, compare 4+ models honestly |
| 10 | K-Means, hierarchical, DBSCAN, PCA; cross-validation, confusion matrix, precision/recall/F1/ROC-AUC, GridSearchCV, `Pipeline` + `ColumnTransformer` | End-to-end pipeline with CV + tuning |

### Phase 5 — Job-Ready Layer (Weeks 11–12)

| Week | Focus | Ship on Sunday |
|:---:|-------|----------------|
| 11 | **SQL** 🆕: SELECT, WHERE, JOINs, GROUP BY, subqueries, window functions (SQLite + Python is enough). Practice: sqlbolt.com, LeetCode SQL easy/medium | Re-do a Week-4 Pandas analysis in pure SQL |
| 12 | **CAPSTONE 2**: end-to-end ML project — pick a dataset you care about; problem framing → EDA → features → model comparison → tuning → error analysis → proper README | The single repo/notebook you'd show in an interview |

### Phase 6 — Bridge to Deep Learning (Weeks 13–14)

| Week | Focus | Ship on Sunday |
|:---:|-------|----------------|
| 13 | **From-scratch week** (NumPy only): linear regression, logistic regression, K-Means, PCA, and a **2-layer neural network** — forward pass, backprop via chain rule, train it on a toy dataset | Working from-scratch NN that learns XOR or MNIST-subset |
| 14 | Interview prep: the 20 theory + 15 coding + 10 system design + 15 math/stats questions from the README; mock interview; polish both capstone READMEs and GitHub profile | Answered question bank committed to `04_interview_prep/` |

---

## ✅ Deep Learning Readiness Gate

Do **not** start the DL module until every box is checked:

- [ ] I can explain and hand-compute a matrix multiplication and explain why shapes must align
- [ ] I can derive the gradient of MSE loss for linear regression and explain the chain rule
- [ ] I implemented gradient descent from scratch and watched the loss decrease
- [ ] I implemented logistic regression from scratch (sigmoid + cross-entropy + gradients)
- [ ] I built a 2-layer neural network in NumPy with working backprop
- [ ] I can explain bias-variance, overfitting, regularization (L1/L2), and cross-validation without notes
- [ ] I have 2 capstone projects with proper READMEs pushed to GitHub
- [ ] I can write a JOIN and a GROUP BY in SQL without looking it up

**Then** the next module is, in order:
1. **Deep Learning Foundations** (PyTorch — pick one framework, don't split attention with TensorFlow): tensors → autograd → MLPs → CNNs → training loops properly
2. **NLP / Transformers** (embeddings → attention → fine-tuning)
3. **MLOps** (Docker, FastAPI, deployment) — do this *alongside* job applications, not before them
4. Multi-agent systems / LLM engineering

---

## 📏 Daily Rhythm

- **Study block**: learn the day's topic (video/docs/book)
- **Code block**: implement it yourself in a notebook — no copy-paste
- **Push**: one commit per day minimum with a meaningful message (this *is* the pixel/heatmap system — GitHub's real contribution graph tracks it for free)
- **Friday or Sunday**: 20-min review of the week — redo one thing from memory

## 📚 Core resources (don't collect more)

| Phase | Resource |
|-------|----------|
| Python | Official docs + Real Python |
| Data stack | Python Data Science Handbook (VanderPlas, free online) |
| Math | 3Blue1Brown (LinAlg + Calculus series), StatQuest |
| ML | Hands-On ML (Géron) ch. 1–9 + scikit-learn user guide |
| SQL | sqlbolt.com, LeetCode SQL |
| Later (DL) | PyTorch official tutorials, then Karpathy "Neural Networks: Zero to Hero" |

One resource per phase, finished, beats five resources sampled.
