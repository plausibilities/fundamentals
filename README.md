<br>

**Plausibilities**

<br>
<br>

# Fundamentals

Upcoming

* mybinder.org
* CodeSpaces  
* GitHub Actions
* Docker

<br>
<br>

Analysing, modelling, forecasting, etc., amidst uncertainty.

Content

* [Studies](#studies)  
* [Development Notes](#development-notes)
  * [Environment](#environment)
  * [Environment Updates](#environment-updates)  
  * [Requirements](#requirements)
  * [Graphing](#graphing)
* [References](#references)


<br>
<br>

## Studies

[Notebooks](./notebooks):

* **Regression**

  * A contrasts of linear regression models <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/plausibilities/fundamentals/blob/develop/notebooks/regression/linear/contrasts.ipynb)

  * Simple linear regression<br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/plausibilities/fundamentals/blob/develop/notebooks/regression/linear/simple.ipynb)

  * Robust linear regression<br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/plausibilities/fundamentals/blob/develop/notebooks/regression/linear/robust.ipynb)

* **Gaussian Processes**

  * Gaussian process regression<br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/plausibilities/fundamentals/blob/develop/notebooks/regression/gp/gp.ipynb)


<br>
<br>

## Development Notes

### Environment

The environment of the projects of *Uncertainty*

```
conda create --prefix ~/Anaconda3/envs/uncertainty
```

The installations are

```bash
conda install -c anaconda pymc3 # installs: python, theano, arviz, numpy, pandas
conda install -c anaconda seaborn # installs: matplotlib
conda install -c anaconda python-graphviz # installs: graphviz
conda install -c anaconda pywin32 jupyterlab nodejs # installs: requests, urllib3
pip install dotmap


# For norms & testing
conda install -c anaconda pytest coverage pylint pytest-cov

# Upgrading PyMC3
pip install --upgrade pymc3==3.9.3

```

<br>

### Environment Updates

Update `python` via `conda install -c anaconda python==3.8.13`, `numpy` via `conda update -c anaconda numpy`, `pandas` 
via `conda update -c anaconda pandas`.  

In terms of `pymc3` & `pymc` &Rarr; `pip unistall pymc3`, subsequently `pip install pymc`. Update `pymc` 
via `pip install --upgrade pymc`

Reference:  [conda commands](https://docs.conda.io/projects/conda/en/latest/commands.html)

<br>

### Requirements

For project *fundamentals*

```bash
conda activate uncertainty
pip freeze -r docs/filter.txt > requirements.txt
```

and

```bash
pylint --generate-rcfile > .pylintrc
```

<br>

### Graphing

Aesthetics

* [Matplotlib Style Sheets](https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html), e.g., `plt.style.use('fivethirtyeight')`

* Arviz, e.g., `az.style.use('arviz-darkgrid')`

* [Seaborn](http://seaborn.pydata.org/api.html#themes), e.g., `sns.set_style("darkgrid")`, `sns.set_context("poster")`, `sns.set_color_codes("pastel")`

<br>

Layouts

* [Constrained Layout](https://matplotlib.org/3.3.2/tutorials/intermediate/constrainedlayout_guide.html)

* matplotlib.rcParams['figure.constrained_layout.use'] = False

* plt.rcParams['figure.constrained_layout.use'] = False

* plt.figure(constrained_layout=False)

* [Adjust](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html): plt.tight_layout(pad=1.0, h_pad=1.5, w_pad=1.5, rect=(0,0,1,1))

<br>
<br>

## References

* [PyMC](https://www.pymc.io/welcome.html)
* [actions/checkout@v2](https://github.com/marketplace/actions/checkout)
* [GitHub Glossary](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/github-glossary)
* [Google Colaboratory & GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb#scrollTo=8QAWNjizy_3O)
* [Seaborn Graph Types](https://seaborn.pydata.org/api.html)
* [``pip`` commands](https://pip.pypa.io/en/stable/cli/)
* [``conda`` commands](https://docs.conda.io/projects/conda/en/latest/commands.html)  
* [The ``Anaconda`` repository](https://anaconda.org/anaconda/repo)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>

