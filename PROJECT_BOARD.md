# Survival Analysis in Python (workshop) Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** In progress (2026-10-19)

**Context:** SurvivalAnalysisPython is a "current" workshop (GreenTeaPress Task 24). The guide is the refresh checklist in `~/GreenTeaPress/plans/workshops.md` ("Refresh checklist"); BayesMadeSimple is the worked example. 50 stars; last workshop change 2021-11-01, last commit 2023-02-14 (`read_seer.ipynb`). Given once, at PyData Global 2021 (2021-10-29, [video](https://www.youtube.com/watch?v=3GL0AIlzR4Q)). This task replaces the SEO-only Task 1 from 2026-10-18; the SEO steps are now in step 6. The 2026-10-18 audit found no meta descriptions, no sitemap, and a landing page titled "Outline".

**0. Set up**
- [x] `git fetch`, pulled `862a708` (README: venues, recordings, link to the workshops list)
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-19)
- [x] Tags (pushed 2026-10-19): `pydata-global-2021` at `97458dc` (2021-10-27, the last commit before the 2021-10-29 session; the 2021-11-01 commits added the "Computing at risk" section to notebook 2, replaced its PMF-table approach, and changed "1000 samples" to "100" in notebook 1); `pre-refresh-2026` at `862a708`
- [ ] README: the recording lists its tag (step 5)
- [x] Inventory (below)
- [x] Leftovers moved to `extras/` (Allen: keep them, out of the way); untracked local files discarded (Decisions)
- [x] `jb/`, `build.sh`, `remove_soln.py` committed (they were never in git, but the published site was built from `jb/`)
- [x] Environment: `mamba env create -f environment.yml` (created 2026-10-19 as `SurvivalAnalysisPython`)

**1. Runs in a current environment**
- [x] `environment.yml` rewritten (2026-10-19): Python 3.12, conda-forge, numpy, pandas, scipy, matplotlib, lifelines, Jupyter, pytest, nbmake, Jupyter Book tools; the 2019 extras (`empiricaldist`, `pytables`, `seaborn`, `tabula-py`, `wget`) dropped. Env: NumPy 2.5.4, pandas 2.3.3, SciPy 1.18.1, Matplotlib 3.11.2, lifelines 0.30.3
- [x] `requirements.txt` (unpinned; Colab lacks only lifelines) and `requirements-dev.txt` (adds Jupyter, pytest, nbmake)
- [x] pandas 3: lifelines 0.30.3 requires `pandas<3`, so the env (and Colab after `pip install lifelines`) stays on pandas 2.x. Notebook 1 doesn't use lifelines and also runs clean on pandas 3.0.6 (scratch venv)
- [x] First code cell: notebook 2 installs lifelines if it can't import it (`%pip install -q`), replacing the `IN_COLAB` cell before the lifelines section. Notebook 1 downloads `lamps.csv` with a `download()` function (no `!wget`) if it's missing
- [x] Breakage and deprecation warnings: none. Both solution notebooks run with Deprecation/Future/PendingDeprecation/User/Runtime warnings as errors. The student versions stop at the first blank (`NameError`), as expected
- [x] Data URL: `lamps.csv` now comes from this repo (`raw/master/lamps.csv`) instead of the third-party gist (content issue 3); the markdown cell before it reworded to match, with the thanks to Evgeny Pogrebnyak kept
- [x] Student versions regenerated with `build.sh` (checked first that it reproduces the committed ones exactly)
- [ ] Install instructions: the README has none, and `jb/index.md` has NBViewer links but no Binder; both are rewritten in steps 3, 5 and 6

**2. Tests and CI**
- [x] `pytest --nbmake soln/01_light_bulb.ipynb soln/02_kaplan_meier.ipynb` (passes locally, 2026-10-19). The student versions aren't tested: their blanks are empty cells whose results later cells use, so they stop with `NameError`
- [x] `.github/workflows/tests.yml` (push to master, PR, monthly, manual; Python 3.12; pip; 20-minute timeout), badge in the README. First run passed (2026-10-19)

**3. Colab**
- [x] "Click here to run this notebook on Colab" cell after the title (2026-10-19); the solutions also link to the version with blanks. `remove_soln.py` rewrites the cell for the student versions, so `build.sh` keeps them right
- [ ] Colab links in the README notebook table (step 5)
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [ ] Typos, wrong docstrings, broken links (codespell, read the markdown); everything else under "Content issues"

**5. README in the standard shape**
- [ ] Title, badge, author, abstract, level and prerequisites, length (ask Allen), outline, notebook table, slides, recording with tag, running instructions, next steps (*Think Stats*, hub), license

**6. Site and visibility**
- [ ] Rework `jb/` on the BayesMadeSimple template (`prep_notebooks.py`, `build.sh [publish]`, clean URLs, page H1s, descriptions); landing title not "Outline"
- [ ] SEO checklist (`~/GreenTeaPress/plans/seo.md`): `sphinx-sitemap`, `sphinxext-opengraph`, base URL, social image (*Think Stats* cover?), page-view counter `extra_footer`, descriptions (Allen reviews), canonical
- [ ] Publish: `./build.sh publish` (also clears the stray `polviews`/`01_clean`/`03_outlook`/`04_worldview` pages on `gh-pages`, from another project); `Sitemap:` line in `~/AllenDowney.github.io/robots.txt`; Allen submits it in Search Console; tick in GreenTeaPress Task 22
- [ ] Hub entry, repo description, website field and topics (`jupyter-book`)

**7. Close**
- [ ] Tag `2026-refresh`; note in GreenTeaPress Task 24

### Inventory (2026-10-19)

**The workshop (PyData Global 2021, 2 notebooks, student versions at the root, solutions in `soln/`):**

| Notebook | Topic | Imports | Data |
|---|---|---|---|
| `01_light_bulb` / `soln/01_light_bulb` | PMF, CDF, survival and hazard functions; light bulb lifetimes | numpy, pandas, scipy.stats, matplotlib | `lamps.csv` (`!wget` from a gist on Colab; also at the repo root) |
| `02_kaplan_meier` / `soln/02_kaplan_meier` | Kaplan-Meier estimation; dog shelter example; lifelines | + `lifelines` | none (made-up data in the notebook) |

Student versions are made from the solutions by `build.sh` + `remove_soln.py` (clears `# Solution` cells and `fill-in` cells, strips outputs). The notebooks have a Colab link already ("Run this notebook on Colab", not the house wording). No `requirements.txt`, no tests, no CI. `environment.yml` is from 2019 (Python 3.7, `empiricaldist`, `tabula-py`, `wget`; the workshop needs none of these three).

**Site:** `jb/` (Jupyter Book 1, `jb-article` format, `execute_notebooks: off`), published to `gh-pages` by hand 2021-11-01. `jb/index.md` is the landing page ("Outline"): slides (Google Slides), a Zoom recording link, Colab and NBViewer links.

**Leftovers (moved to `extras/` 2026-10-19):** 2019–2020 explorations and drafts: `birth`, `fertility`, `kaplan-meier`, `light_bulb`, `life_table`, `marriage`, `nhl`, `popcorn`, `weibull`, `test`, `read_life_table`, `read_marriage`, `read_seer` (updated 2023), with `utils.py`, `nhl.hdf5`, `nsfg.hdf5` and `data/`. Not tested.

**Local state not in git (discarded 2026-10-19; all but `SEER/` backed up to the session scratchpad):** `SEER/` (6.1 GB raw SEER 1975–2016 data, downloadable again), NSFG 2015–2017 female respondent `.dat`/`.dct`, `brain.hd5`/`brain.hdf`, `mortality.ipynb` (2023), `Single_year_death_rates.txt`, `data/nvsr67_07-508.csv`, the gist zip of `lamps.csv`, copies of `empiricaldist.py` and its tests, `environment.yml~`, checkpoints; a kernel-metadata-only edit to `read_life_table.ipynb`.

### Decisions (Allen, 2026-10-19)

- Tags `pydata-global-2021` and `pre-refresh-2026` created and pushed.
- Leftovers go to `extras/`, not deleted.
- Untracked local files discarded (small ones backed up first; `SEER/` not backed up).
- `jb/` committed as the starting point for step 6.
- Length: 90 minutes, for the README.
- License: MIT for the code, CC BY-NC-SA 4.0 for the text. The notebook footers and `jb/index.md` now say both, in the books' wording ("Code license: … / Text license: …"); `LICENSE` stays MIT; the README says both (step 5).

### Content issues

(For Allen to decide.)

1. `jb/index.md`: "This material is a work in progress"; the video link is a Zoom recording, not the YouTube video.
2. Notebook 1 downloaded `lamps.csv` from a third-party gist; switched to the copy in this repo in step 1 (revert if you prefer the gist).
3. Copyright lines say 2021.
