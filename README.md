# ADL Theory

**Current version: v0.5.0**

`adl-theory` is an educational Python library for exploring the theoretical
dynamic properties of Autoregressive Distributed Lag (ADL/ARDL) models.

The project is designed for students of econometrics and time-series analysis.
It allows users to specify model coefficients directly and investigate the
resulting stability conditions, dynamic effects, cumulative adjustment, and
long-run properties.

> [!IMPORTANT]
> `adl-theory` does **not** estimate ADL/ARDL models from data. Its purpose is
> to help students understand what a given set of theoretical model
> coefficients implies.

## Introduction

Consider the ADL(\(p,q\)) model

$$
y_t
=
\sum_{i=1}^{p}\phi_i y_{t-i}
+
\sum_{j=0}^{q}\beta_j x_{t-j}
+
u_t.
$$

Given the autoregressive coefficients
\(\phi_1,\ldots,\phi_p\) and the distributed-lag coefficients
\(\beta_0,\ldots,\beta_q\), the library helps answer questions such as:

- Is the model dynamically stable?
- Where are the roots and inverse roots of the AR characteristic polynomial?
- What is the effect of a change in \(x_t\) at each subsequent lag?
- How rapidly do the effects accumulate?
- What is the theoretical long-run multiplier?
- What are the mean and median lags?
- How many periods are required to reach a specified proportion of the
  long-run effect?

Students can change the coefficients, rerun the analysis, and immediately
observe how the model's dynamics change.

## Features

The current release includes:

- stability analysis based on the roots of the AR characteristic polynomial;
- calculation and interactive visualization of inverse roots and the unit
  circle;
- recursive calculation of dynamic effects;
- cumulative dynamic effects;
- each dynamic effect as a percentage of the theoretical long-run effect;
- cumulative effects as a percentage of the theoretical long-run effect;
- theoretical long-run multiplier;
- analytical mean lag;
- median lag;
- automatic horizon selection, using 99% of the long-run effect by default;
- optional user-defined calculation horizon;
- informative handling of unstable models;
- interactive Plotly graphs for dynamic and cumulative effects; and
- a formatted summary table for use in Jupyter notebooks.

The computational functions return their results without printing them, making
the library reusable in notebooks, scripts, and the planned web application.

## Repository Contents

The repository currently uses a deliberately simple, flat structure:

```text
adl-theory/
├── adl_theory.py
├── ADL_Theory_Demo.ipynb
├── environment.yml
├── README.md
└── LICENSE
```

- **`adl_theory.py`** — the main library, containing the calculations,
  summaries, and plotting functions.
- **`ADL_Theory_Demo.ipynb`** — a concise demonstration of the library's
  functions and their use.
- **`environment.yml`** — the Conda/Mamba environment specification.
- **`README.md`** — project overview and setup instructions.
- **`LICENSE`** — the MIT License.

## Installation

### 1. Clone the repository

Using SSH:

```bash
git clone git@github.com:maarranz/adl-theory.git
cd adl-theory
```

Alternatively, use HTTPS:

```bash
git clone https://github.com/maarranz/adl-theory.git
cd adl-theory
```

### 2. Create the environment

With Mamba:

```bash
mamba env create -f environment.yml
```

Or with Conda:

```bash
conda env create -f environment.yml
```

The environment name is defined in `environment.yml`. Activate it using the
name shown there:

```bash
mamba activate <environment-name>
```

or:

```bash
conda activate <environment-name>
```

If the environment has already been created, update it after pulling changes:

```bash
mamba env update -f environment.yml --prune
```

### 3. Start JupyterLab

From the repository directory:

```bash
jupyter lab
```

Open `ADL_Theory_Demo.ipynb` and confirm that the notebook is using the Python
kernel associated with the project environment.

## Quick Start

The following example analyzes an ADL(1,1) model:

$$
y_t
=
0.8y_{t-1}
+
0.5x_t
+
0.3x_{t-1}
+
u_t.
$$

```python
import adl_theory as adl

phi = [0.8]
beta = [0.5, 0.3]
```

Check stability and display the inverse-root graph:

```python
stability = adl.adl_stability(phi)
adl.plot_inverse_roots(stability)
```

Calculate the dynamic effects:

```python
results = adl.adl_dynamic_effects(phi, beta)
```

Inspect the numerical results:

```python
results["summary"]
results["table"]
```

Display the formatted summary and interactive graphs:

```python
adl.adl_summary(results)
adl.plot_dynamic_effects(results)
adl.plot_cumulative_effects(results)
```

For this example, the theoretical long-run effect is

\[
\frac{0.5+0.3}{1-0.8}=4.
\]

The first dynamic effects are \(0.5\), \(0.7\), \(0.56\), \(0.448\), and so
forth. Students are encouraged to change `phi` and `beta`, predict the
consequences, and compare their predictions with the computed results.

## Educational Philosophy

The project follows a **learning-by-doing** approach. Its objective is not to
turn ADL/ARDL analysis into a black-box calculation, but to make the
relationship between model coefficients and dynamic behavior easier to
understand.

Students are encouraged to:

1. specify or modify the model coefficients;
2. predict how the changes will affect stability and adjustment;
3. run the calculations;
4. examine the roots, tables, and graphs; and
5. explain why the observed dynamics follow from the model.

The notebook interface keeps the code required from students short, while the
implementation remains available in `adl_theory.py` for those who want to
inspect or extend it. The figures are intentionally informative and
consistently styled so that attention remains on the econometrics rather than
on graphical customization.

## Roadmap

### Available now

- **`ADL_Theory_Demo.ipynb`** provides a compact demonstration of the public
  functions and serves as a technical reference for using the library.

### Planned teaching material

- **`ADL_Theory_Examples.ipynb`** will provide explanatory Markdown and LaTeX,
  worked examples, interpretation, and exercises. Planned examples include:

  - persistent positive adjustment in a stable ADL model;
  - oscillatory adjustment;
  - higher-order autoregressive and distributed-lag dynamics;
  - real and complex-conjugate roots; and
  - unstable models and the resulting absence of well-defined long-run
    measures.

### Planned interface

- A web application will provide an abridged, code-free interface for students
  who prefer not to work directly with Python. It will reuse the calculations
  in `adl_theory.py` and provide coefficient controls, summaries, and
  interactive graphs.

The demonstration notebook, worked-examples notebook, and web application are
intended to complement one another: the demo documents the API, the examples
support guided exploration, and the app lowers the barrier to entry.

## License

This project is released under the [MIT License](LICENSE).
