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
    polynomial = np.concatenate((-phi[::-1], [1.0]))

    # Characteristic roots
    roots = np.roots(polynomial)

    # Inverse roots
    inverse_roots = 1 / roots

    # Stability
    stable = np.all(np.abs(roots) > 1)

    return {
            "phi": phi,
            "order": len(phi),
            "roots": roots,
            "inverse_roots": inverse_roots,
            "stable": stable,
            "max_inverse_root": np.max(np.abs(inverse_roots))
    }


# ============================================================
# Graphics
# ============================================================

import numpy as np
import plotly.graph_objects as go


def plot_inverse_roots(stability,
                       title="Inverse Roots of the Characteristic Polynomial"):
    """
    Plot the inverse roots of the characteristic polynomial.

    Parameters
    ----------
    stability : dict
        Dictionary returned by adl_stability().
    title : str, optional
        Figure title.

    Returns
    -------
    plotly.graph_objects.Figure
        Interactive Plotly figure.
    """

    inv_roots = stability["inverse_roots"]
    stable = stability["stable"]
    max_root = stability["max_inverse_root"]
    order = stability["order"]

    # ------------------------------------------------------------
    # Unit circle
    # ------------------------------------------------------------

    theta = np.linspace(0, 2*np.pi, 400)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=np.cos(theta),
            y=np.sin(theta),
            mode="lines",
            name="Unit circle",
            line=dict(color="gray", dash="dash")
        )
    )

    # ------------------------------------------------------------
    # Real and imaginary axes
    # ------------------------------------------------------------

    fig.add_hline(y=0,
                  line_color="black",
                  line_width=1)

    fig.add_vline(x=0,
                  line_color="black",
                  line_width=1)

    # ------------------------------------------------------------
    # Inverse roots
    # ------------------------------------------------------------

    colour = "royalblue" if stable else "firebrick"

    hover = []

    for i, r in enumerate(inv_roots):

        hover.append(
            f"<b>Inverse root {i+1}</b><br>"
            f"Real: {r.real:.4f}<br>"
            f"Imaginary: {r.imag:.4f}<br>"
            f"Modulus: {abs(r):.4f}"
        )

    fig.add_trace(
        go.Scatter(
            x=np.real(inv_roots),
            y=np.imag(inv_roots),
            mode="markers+text",
            text=[f"r{i+1}" for i in range(len(inv_roots))],
            textposition="top center",
            marker=dict(
                size=10,
                color=colour
            ),
            hovertemplate="%{customdata}<extra></extra>",
            customdata=hover,
            name="Inverse roots"
        )
    )

    # ------------------------------------------------------------
    # Annotation
    # ------------------------------------------------------------

    annotation = (
        f"<b>{'Stable' if stable else 'Unstable'} model</b><br>"
        f"ADL({order})<br>"
        f"Max |inverse root| = {max_root:.3f}"
    )

    fig.add_annotation(
        x=0.02,
        y=0.98,
        xref="paper",
        yref="paper",
        text=annotation,
        showarrow=False,
        align="left",
        bordercolor="black",
        borderwidth=1,
        bgcolor="white"
    )

    # ------------------------------------------------------------
    # Layout
    # ------------------------------------------------------------

    fig.update_layout(
        title=title,
        width=700,
        height=700,
        template="plotly_white",
        xaxis_title="Real",
        yaxis_title="Imaginary",
        legend=dict(
            x=0.02,
            y=0.02
        )
    )

    fig.update_xaxes(
        scaleanchor="y",
        scaleratio=1,
        zeroline=False
    )

    fig.update_yaxes(
        zeroline=False
    )

    return fig

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
