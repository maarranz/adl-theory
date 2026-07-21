"""
adl_theory.py

Teaching toolkit for exploring the dynamics of
Autoregressive Distributed Lag (ADL) models.

Author
------
Miguel A. Arranz

License
-------
MIT

Version
-------
0.1.0
"""

from __future__ import annotations

__version__ = "0.1.0"

import numpy as np
import pandas as pd
import plotly.graph_objects as go


# ============================================================
# Stability
# ============================================================

def adl_stability(phi):
    """
    Check the stability of an ADL model.

    Parameters
    ----------
    phi : array-like
        Autoregressive coefficients.

    Returns
    -------
    dict
        Dictionary containing

        - characteristic polynomial
        - roots
        - inverse roots
        - stability indicator

    Notes
    -----
    The characteristic polynomial is

        1 - phi1*z - phi2*z² - ... - phip*z^p

    The model is stable if all roots lie outside
    the unit circle.

    Examples
    --------
    >>> phi = [0.8]
    >>> results = adl_stability(phi)
    >>> results["stable"]
    True
    """

    phi = np.asarray(phi, dtype=float)

    # Polynomial coefficients
    polynomial = np.concatenate(([1.0], -phi))

    # Characteristic roots
    roots = np.roots(polynomial)

    # Inverse roots
    inverse_roots = 1 / roots

    # Stability
    stable = np.all(np.abs(roots) > 1)

    return {
        "phi": phi,
        "polynomial": polynomial,
        "roots": roots,
        "inverse_roots": inverse_roots,
        "stable": stable,
    }


# ============================================================
# Graphics
# ============================================================

def plot_inverse_roots(results):
    """
    Plot the inverse roots together with the unit circle.

    Parameters
    ----------
    results : dict
        Output returned by adl_stability().
    """
    raise NotImplementedError(
        "This function will be implemented in Version 0.2."
    )


# ============================================================
# Dynamic effects
# ============================================================

def adl_dynamic_effects(phi, beta, horizon=None):
    """
    Compute the dynamic effects of an ADL model.

    Parameters
    ----------
    phi : array-like
        Autoregressive coefficients.

    beta : array-like
        Distributed lag coefficients.

    horizon : int, optional
        Horizon used for computing the effects.
        If None, an automatic rule will be used.

    Returns
    -------
    dict
        Results of the dynamic analysis.
    """
    raise NotImplementedError(
        "This function will be implemented in Version 0.3."
    )


# ============================================================
# Dynamic effect graphics
# ============================================================

def plot_dynamic_effects(results):
    """
    Plot the dynamic effects.

    Parameters
    ----------
    results : dict
        Output returned by adl_dynamic_effects().
    """
    raise NotImplementedError(
        "This function will be implemented in Version 0.4."
    )


def plot_cumulative_effects(results):
    """
    Plot cumulative dynamic effects.

    Parameters
    ----------
    results : dict
        Output returned by adl_dynamic_effects().
    """
    raise NotImplementedError(
        "This function will be implemented in Version 0.5."
    )


# ============================================================
# Summary table
# ============================================================

def adl_summary(results):
    """
    Produce a publication-quality summary table.

    Parameters
    ----------
    results : dict
        Output returned by adl_dynamic_effects().

    Returns
    -------
    pandas.DataFrame
    """
    raise NotImplementedError(
        "This function will be implemented in Version 1.0."
    )
