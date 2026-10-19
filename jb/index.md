---
myst:
  html_meta:
    description: "A tutorial on survival analysis in Python: survival functions, hazard functions and Kaplan-Meier estimation, computed with pandas and lifelines."
og:description: "A tutorial on survival analysis in Python: survival functions, hazard functions and Kaplan-Meier estimation, computed with pandas and lifelines."
---

# Computational Survival Analysis: A Tutorial in Python

[Allen Downey](https://allendowney.com)

Survival analysis is a powerful and versatile set of statistical tools that not enough people know about. It is usually presented mathematically, but in this tutorial we take a computational approach, using pandas objects to represent survival functions and hazard functions, and to implement basic algorithms like Kaplan-Meier estimation.

The examples are about light bulbs and dog adoptions, but the same methods apply to human lifetimes, mechanical failures, customer churn, and the time until almost any kind of event.

**Level:** intermediate. You should know basic Python; familiarity with pandas helps, but isn't required. You don't need any background in survival analysis.

**Length:** about 90 minutes.

## The notebooks

The pages on this site show the notebooks with solutions. To do the exercises, run the versions with blanks on Colab:

1. [Survival and hazard functions](01_light_bulb): four ways to represent a distribution of lifetimes (PMF, CDF, survival function, and hazard function), using data from an experiment that ran 50 light bulbs until they all failed. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/SurvivalAnalysisPython/blob/master/01_light_bulb.ipynb)
2. [Kaplan-Meier estimation](02_kaplan_meier): estimating the hazard and survival functions when some cases are incomplete, using hypothetical data from a dog shelter; then the same computation with the `lifelines` library. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/SurvivalAnalysisPython/blob/master/02_kaplan_meier.ipynb)

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vQfYxM-Fy8TScRbUyYSWqeyNtPy8teV_d6tieSVdIK5qRHYbuTcx9CKVRGbZzjiaJ2x5NAgy1Jddb4_/pub).

## Recording

I presented this tutorial at [PyData Global 2021](https://pydata.org/global2021/schedule/presentation/39/computational-survival-analysis/); [here is the video](https://www.youtube.com/watch?v=3GL0AIlzR4Q). The code in the video is an earlier version; the [repository README](https://github.com/AllenDowney/SurvivalAnalysisPython) has a link to the version that goes with it.

Your feedback is welcome.  The best way to provide it is to [click here and create an issue in this GitHub repository](https://github.com/AllenDowney/SurvivalAnalysisPython/issues).

## Next steps

To go further, read [the survival analysis chapter of *Think Stats*](https://allendowney.github.io/ThinkStats/chap13.html), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops).

Code license: [MIT License](https://mit-license.org/)

Text license: [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)
