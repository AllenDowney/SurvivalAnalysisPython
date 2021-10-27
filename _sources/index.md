# Political Alignment Case Study

This data science case study explores the relationship between political alignment (conservative, moderate, or liberal) and other attitudes and beliefs.  It is meant primarily for teaching and learning about data science, but we might do some research along the way.

If you are working through [the *Elements of Data Science* curriculum](https://allendowney.github.io/ElementsOfDataScience/), you should be ready to start this case study when you have completed Notebook 6, which covers basic Pandas.

This material is a work in progress, so your feedback is welcome.  The best way to provide that feedback is to [click here and create an issue in this GitHub repository](https://github.com/AllenDowney/PoliticalAlignmentCaseStudy/issues).


## Videos and Slides

I presented this case study for [PyData Global 2020](https://global.pydata.org/talks/363).

Here are the [slides I presented](https://docs.google.com/presentation/d/e/2PACX-1vSqifcdVGQmMoLDNlmbnugZ58jieItA_weGEF9oRsQCAa6iICLmehevGRzINYVv0tCGqcSTvuIQOSJo/pub)

And here are the videos:

* [Part 1](https://www.youtube.com/watch?v=6Bg7v5EGiWY)

* [Part 2](https://www.youtube.com/watch?v=y8A3bKjpJe4)

* [Part 3](https://www.youtube.com/watch?v=vfuXyXXSNtM)

* [Part 4](https://www.youtube.com/watch?v=XFPi-AUiJSo)



## The notebooks

For each of the notebooks below, you have two options: if you view the notebook on NBViewer, you can read it, but you can't run the code.  If you run the notebook on Colab, you'll be able to run the code, do the exercises, and save your modified version of the notebook in a Google Drive (if you have one).

### Notebook 1

**Cleaning and validation**: The first notebook loads data from the General Social Survey (GSS) and walks through the process of cleaning and validating the data.  At the end, you can help me by choosing a random variable, checking the values against the codebook, and reporting your results.

* [Click here to read Notebook 1 on NBViewer](https://nbviewer.jupyter.org/github/AllenDowney/PoliticalAlignmentCaseStudy/blob/master/01_clean.ipynb)

* [Click here to run Notebook 1 on Colab](https://colab.research.google.com/github/AllenDowney/PoliticalAlignmentCaseStudy/blob/master/01_clean.ipynb)


### Notebook 2

**Exploration**: This notebook uses the tools of exploratory data analysis to look at survey responses about political alignment.  It uses PMFs to display distributions, time series to represent changes over time, and cross tabulation to look at changes in distribution over time.  It also introduces local regression as a way to plot a smooth line through noisy data.

* [Click here to read Notebook 2 on NBViewer](https://nbviewer.jupyter.org/github/AllenDowney/PoliticalAlignmentCaseStudy/blob/master/02_polviews.ipynb)

* [Click here to run Notebook 2 on Colab](https://colab.research.google.com/github/AllenDowney/PoliticalAlignmentCaseStudy/blob/master/02_polviews.ipynb)


### Notebook 3

**Political alignment and outlook**: This notebook explores the relationship between political alignment and three survey questions related to "outlook".  It uses a pivot table to compute the mean of the response variable grouped by political alignment and time.

* [Click here to read Notebook 3 on NBViewer](https://nbviewer.jupyter.org/github/AllenDowney/PoliticalAlignmentCaseStudy/blob/master/03_outlook.ipynb)

* [Click here to run Notebook 3 on Colab](https://colab.research.google.com/github/AllenDowney/PoliticalAlignmentCaseStudy/blob/master/03_outlook.ipynb)


### Notebook 4

**Political alignment and other beliefs**: This notebook explores the relationship between political alignment and other attitudes and beliefs.  It is a template for a do-it-yourself, choose-your-own-adventure mini-project, where you have the chance to explore a variable in the GSS dataset and report the results.

* [Click here to read Notebook 4 on NBViewer](https://nbviewer.jupyter.org/github/AllenDowney/PoliticalAlignmentCaseStudy/blob/master/04_worldview.ipynb)

* [Click here to run Notebook 4 on Colab](https://colab.research.google.com/github/AllenDowney/PoliticalAlignmentCaseStudy/blob/master/04_worldview.ipynb)


Copyright 2020 Allen B. Downey

License: [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
