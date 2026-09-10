# ASTBIO 201 — Astrobiology (Rizal Technological University)

Course website for **Astrobiology**, Bachelor of Science in Astronomy, Department of Earth and Space Sciences,
College of Arts and Sciences. Faculty-in-charge: **Dr. Ryan Manuel D. Guido**.

Design: RTU Royal Blue ground with a Neon Green accent, matching the house format of the other RTU course sites
(dark landing page with live file-detection cards; light lecture and exercise pages with a sticky section nav,
reveal-to-check items, and a self-score box). Every page is a self-contained HTML file — no frameworks, no CDN,
no build step required to view.

## Contents

| Path | What it is |
| --- | --- |
| `index.html` | Course home: hero, three-term chapter cards (each checks its files on load), assessment summary |
| `syllabus.html` | Full outcomes-based syllabus with sticky section nav; print-ready; teaching plan cross-linked to chapter pages |
| `chapters/ch01.html` … `ch15.html` | Weekly lecture notes: course-thread callout, four numbered sections, inline SVG figure, key terms, in-class plan, prev/next |
| `exercises/ch01-exercises.html` … | Reinforcement exercises: 10 HOTS multiple-choice items (radio + reveal), 2 applied tasks with instructor notes, self-score table |
| `assets/rtu-logo.jpg` | University seal used in every hero |
| `build.py`, `meta.py`, `plan.py`, `term1-3.py` | Source content and generator |

## Publishing to GitHub Pages

1. Create a repository, e.g. `astrobiology-astbio201`, and push this folder's contents to `main`.
2. **Settings → Pages → Build and deployment**: *Deploy from a branch*, branch `main`, folder `/ (root)`.
3. The site appears at `https://<username>.github.io/<repository>/`. `.nojekyll` is included.

```bash
git init && git add . && git commit -m "ASTBIO 201 Astrobiology course site"
git branch -M main
git remote add origin https://github.com/<username>/<repository>.git
git push -u origin main
```

## Editing

Content is in plain Python dictionaries: `meta.py` (course info, outcomes, grading, policies), `plan.py`
(15-week plan as in the syllabus), `term1.py`–`term3.py` (lecture sections, figures, items, applied tasks).
Rebuild with `python3 build.py .` — answer keys are rebalanced across A–D automatically.

## Instructor notes

- Instructor notes on the applied tasks sit inside a reveal dropdown and are visible to anyone; delete those
  `<details>` blocks in `build_exercises()` if the pages are to be used for graded work.
- Self-scoring is client-side only; nothing is recorded or transmitted.
- The status pills on the home page turn green/red only when served over http(s); opened from disk they show "Open".
