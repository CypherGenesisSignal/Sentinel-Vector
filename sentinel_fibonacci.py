"""Utility to render a Fibonacci spiral for Sentinel Vector visualizations."""
from __future__ import annotations

from pathlib import Path
from typing import List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np


def fibonacci_sequence(count: int) -> List[int]:
    """Return the first ``count`` Fibonacci numbers.

    Parameters
    ----------
    count:
        Number of Fibonacci numbers to generate. Must be greater than zero.
    """
    if count <= 0:
        raise ValueError("`count` must be a positive integer")

    if count == 1:
        return [1]

    sequence = [1, 1]
    for _ in range(2, count):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def fibonacci_spiral(
    n: int = 10,
    *,
    scale: float = 1.0,
    show_axes: bool = False,
    color: str = "cyan",
    linewidth: float = 2.0,
    ax: Optional[plt.Axes] = None,
    save_path: Optional[Path | str] = None,
    show: bool = True,
) -> Tuple[plt.Figure, plt.Axes]:
    """Render a Fibonacci spiral with ``n`` curved segments.

    Parameters
    ----------
    n:
        Number of segments to render (must be >= 1).
    scale:
        Multiplier applied to each Fibonacci radius.
    show_axes:
        Whether to display Matplotlib axes on the output figure.
    color:
        Spiral color.
    linewidth:
        Width of spiral lines.
    ax:
        Optional Matplotlib axes to draw onto. If omitted, a new figure is
        created.
    save_path:
        Optional path to save the figure instead of just displaying it.
    show:
        Whether to call :func:`plt.show` after drawing.

    Returns
    -------
    (figure, axes):
        The Matplotlib figure and axes containing the spiral.
    """
    if n <= 0:
        raise ValueError("`n` must be a positive integer")

    radii = [value * scale for value in fibonacci_sequence(n)]

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure

    angle = 0.0
    x, y = 0.0, 0.0

    for index, radius in enumerate(radii):
        theta = np.linspace(angle, angle + np.pi / 2, 100)
        xs = x + radius * np.cos(theta)
        ys = y + radius * np.sin(theta)
        ax.plot(xs, ys, color=color, linewidth=linewidth)

        # Shift origin to the next quadrant corner to continue the spiral.
        quadrant = index % 4
        if quadrant == 0:
            x += radius
        elif quadrant == 1:
            y += radius
        elif quadrant == 2:
            x -= radius
        else:
            y -= radius

        angle += np.pi / 2

    ax.set_aspect("equal")
    ax.axis("on" if show_axes else "off")
    ax.set_title("Fibonacci Spiral - Sentinel Vector Memory Geometry")

    if save_path is not None:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, bbox_inches="tight")

    if show:
        plt.show()

    return fig, ax


if __name__ == "__main__":
    fibonacci_spiral(n=12, scale=1.0)
