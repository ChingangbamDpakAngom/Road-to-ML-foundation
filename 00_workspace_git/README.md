# 🧰 Module 0 — Workspace & GitHub, Learned by Using It

> **No theory week for git.** This module has no scheduled slot — you practice it
> **every single day** by shipping your real work to your real repo. One new skill
> per week, each one used immediately on this project. By Week 4 the commands are
> muscle memory, which is exactly how every working developer learned them.

---

## 🖥️ Your workspace (know your tools)

| Tool | Job | Sanity check (run in terminal) |
|------|-----|-------------------------------|
| **VS Code** | Editor — notebooks, scripts, terminal in one place | — |
| **Conda env** | Isolated Python so projects never fight over packages | `conda env list` → `ml-foundations` starred when active |
| **Jupyter** | Run notebooks cell by cell | open any `.ipynb`, kernel = ml-foundations |
| **Git** | Time machine — every commit is a save point you can return to | `git --version` |
| **GitHub** | Your public proof-of-work (recruiters read commit history!) | `git remote -v` → your repo URL |

**Workspace layout rule:** structured lessons live in the day notebooks
(`day1_basics.ipynb`…), free messy experiments live in
[`01_python_foundations/scratchpad.ipynb`](../01_python_foundations/scratchpad.ipynb).
Never fear breaking the scratchpad — that's what it's for.

---

## 🔁 The Daily Ritual (from Day 1 — this is the whole habit)

Every study day ends with these four commands. Type them — no copy-paste, same
rule as the exercises:

```bash
git status                        # 1. SEE what changed (never commit blind)
git add -A                        # 2. STAGE it (put changes in the box)
git commit -m "Day 2: data structures — word freq, gradebook"   # 3. SAVE POINT
git push                          # 4. PUBLISH → heatmap + quest graph update
```

**Commit message rule:** `<what unit>: <what you actually did>`. Six months from
now, `git log --oneline` should read like a diary. "update", "asdf", "final2" are
banned.

---

## 📈 One new skill per week (applied to THIS repo, immediately)

### Week 1 — See your history
- [ ] `git log --oneline` — read your diary so far
- [ ] `git diff` before staging — see exactly what today changed
- [ ] `git show HEAD` — inspect your last commit
- [ ] On github.com: open your repo → Commits tab → click one → see the green/red diff

### Week 2 — Undo mistakes (the fear-killer)
- [ ] Edit any file, then `git restore <file>` — watch the change vanish (undo unstaged)
- [ ] `git restore --staged <file>` — un-stage something you added too early
- [ ] Make a bad commit on purpose (typo message), then `git commit --amend -m "fixed"` **before** pushing
- [ ] Read `.gitignore` in the repo root — now you know why `__pycache__` never shows in `git status`

### Week 3 — Branches (work without breaking main)
- [ ] `git switch -c experiment/numpy-images` before Week 3's project
- [ ] Commit twice on the branch, `git switch main`, note the work "disappears", switch back
- [ ] Merge it: `git switch main && git merge experiment/numpy-images`
- [ ] Delete the branch: `git branch -d experiment/numpy-images`

### Week 4 — GitHub as your portfolio
- [ ] Open a GitHub **Issue** on your own repo for Capstone 1; reference it in the commit: `git commit -m "Capstone 1 EDA (closes #1)"` — watch GitHub auto-close it
- [ ] Star + pin the repo on your profile; write a 2-line profile README
- [ ] Check your contribution heatmap — it should already look alive

### Weeks 5+ — On-demand
`git stash` (shelve half-done work) · `git revert` (undo a *pushed* commit safely) ·
pull-request workflow (used at every job — practice by PR-ing a branch to yourself
for Capstone 2).

---

## 🆘 Rescue card (bookmark this section)

| Situation | Command |
|-----------|---------|
| What state am I in?? | `git status` (answers 90% of panics) |
| Undo edits I haven't staged | `git restore <file>` |
| Un-stage a file | `git restore --staged <file>` |
| Fix my last commit message (not pushed) | `git commit --amend -m "better message"` |
| See what a commit changed | `git show <hash>` |
| Push rejected ("fetch first") | `git pull`, resolve if asked, then `git push` |
| Committed to wrong branch (not pushed) | `git switch -c right-branch` — your commit comes with you |
| Total local mess, remote is fine | `git stash` (recoverable) — **never** `reset --hard` in panic |

> ⚠️ Commands that can destroy work: `git reset --hard`, `git push --force`,
> `git clean -f`. If you're typing one while frustrated — stop, ask first.
