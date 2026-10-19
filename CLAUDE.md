# SurvivalAnalysisPython

Allen Downey's tutorial "Survival Analysis in Python": an introduction to survival analysis using computation rather than math (PMFs, CDFs, survival and hazard functions, Kaplan-Meier, lifelines). Given at PyData Global 2021. The site is a Jupyter Book built from `jb/` and published to `gh-pages` (`allendowney.github.io/SurvivalAnalysisPython/`).

**Guide for the 2026 refresh:** the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md` (BayesMadeSimple is the worked example). Progress goes on `PROJECT_BOARD.md` here (Task 1) and in GreenTeaPress Task 24.

## Which notebooks are the workshop

Two notebooks; the solutions in `soln/` are the source, and the student versions at the root are generated from them:

- `soln/01_light_bulb.ipynb` → `01_light_bulb.ipynb` (reads `lamps.csv`)
- `soln/02_kaplan_meier.ipynb` → `02_kaplan_meier.ipynb` (uses lifelines)

To regenerate a student version: `./build.sh 01_light_bulb.ipynb` (copies from `soln/` and runs `remove_soln.py`, which clears `# Solution` and `fill-in` cells and strips outputs). Edit the solution, not the student version.

`lamps.csv` stays at the root: notebook 1 links to its raw URL on `master`. `extras/` holds 2019–2023 explorations that are not part of the workshop or its tests.

## Tags

- `pydata-global-2021`: the code in the PyData Global 2021 video.
- `pre-refresh-2026`: the state before the 2026 refresh.

## Testing

Environment: `mamba env create -f environment.yml` (name `SurvivalAnalysisPython`). Run the solution notebooks top to bottom:

```
pytest --nbmake soln/01_light_bulb.ipynb soln/02_kaplan_meier.ipynb
```

The target environment is Google Colab's current Python and libraries.

## Conventions

- Branch is `master`; don't rename it (Colab and raw links depend on it).
- Don't change the substance of the text; list content questions under "Content issues" on the board for Allen to decide.
- Keep student and solution versions in sync by regenerating the student versions with `build.sh`.
