# Survival Analysis in Python

[![tests](https://github.com/AllenDowney/SurvivalAnalysisPython/actions/workflows/tests.yml/badge.svg)](https://github.com/AllenDowney/SurvivalAnalysisPython/actions/workflows/tests.yml)

[Allen Downey](https://allendowney.com)

Survival analysis is a powerful and versatile set of statistical tools that not enough people know about. It is usually presented mathematically, but in this tutorial we take a computational approach, using pandas objects to represent survival functions and hazard functions, and to implement basic algorithms like Kaplan-Meier estimation.

Each notebook has short explanations, worked examples you can run, and exercises. The examples are about light bulbs and dog adoptions, but the same methods apply to human lifetimes, mechanical failures, customer churn, and the time until almost any kind of event.

The tutorial site is [allendowney.github.io/SurvivalAnalysisPython](https://allendowney.github.io/SurvivalAnalysisPython/).

This is one of [my workshops and tutorials](https://allendowney.github.io/#workshops).

**Level:** intermediate. You should know basic Python; familiarity with pandas helps, but isn't required. You don't need any background in survival analysis.

**Length:** about 90 minutes.

## Outline

1. **Light bulbs:** four ways to represent a distribution of lifetimes (PMF, CDF, survival function, and hazard function), using data from an experiment that ran 50 light bulbs until they all failed; then the cumulative hazard function, and resampling to see how precise the estimates are.
2. **Kaplan-Meier estimation:** estimating the hazard and survival functions when some cases are incomplete, using hypothetical data from a dog shelter where some dogs have not been adopted yet; then the same computation with the `lifelines` library.

Each notebook comes in two versions: one with blanks for the exercises, and one with solutions.

| Notebook | Exercises | Solutions |
|---|---|---|
| 1. Light bulbs | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurvivalAnalysisPython/blob/master/01_light_bulb.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurvivalAnalysisPython/blob/master/soln/01_light_bulb.ipynb) |
| 2. Kaplan-Meier estimation | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurvivalAnalysisPython/blob/master/02_kaplan_meier.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurvivalAnalysisPython/blob/master/soln/02_kaplan_meier.ipynb) |

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vQfYxM-Fy8TScRbUyYSWqeyNtPy8teV_d6tieSVdIK5qRHYbuTcx9CKVRGbZzjiaJ2x5NAgy1Jddb4_/pub).

## Recording

I presented this tutorial at PyData Global 2021. The tag after the link is the version of the code that goes with the video; the current version has small changes, mostly in the Kaplan-Meier notebook.

* [PyData Global 2021](https://www.youtube.com/watch?v=3GL0AIlzR4Q): tag [`pydata-global-2021`](https://github.com/AllenDowney/SurvivalAnalysisPython/tree/pydata-global-2021)

## Running the notebooks

The easiest way to run the notebooks is on Colab: click one of the links above. You need a Google account, but you don't have to install anything.

To run them on your own computer, you need Python 3 with Jupyter, NumPy, pandas, SciPy, Matplotlib, and lifelines. You can [download the code in this zip file](https://github.com/AllenDowney/SurvivalAnalysisPython/archive/master.zip), or clone the repository:

```
git clone https://github.com/AllenDowney/SurvivalAnalysisPython
cd SurvivalAnalysisPython
```

Then install the packages with pip:

```
pip install -r requirements.txt
```

Or, if you use conda or mamba, create an environment:

```
mamba env create -f environment.yml
mamba activate SurvivalAnalysisPython
```

Then run `jupyter lab` and open `01_light_bulb.ipynb`.

The `extras` folder has explorations from earlier versions (NHL, marriage, fertility, life tables, SEER data); they are not part of the tutorial and may not run with current libraries.

## Next steps

To go further, read [the survival analysis chapter of *Think Stats*](https://allendowney.github.io/ThinkStats/chap13.html), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops).

## License

The code is available under the [MIT License](LICENSE). The text is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
