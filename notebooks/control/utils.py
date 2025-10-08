"""Funciones auxiliares compartidas entre los cuadernos de control cinemático."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def time_vector(cfg: dict) -> tuple[np.ndarray, float]:
    """Genera un vector de tiempo uniforme a partir de la configuración."""
    t = np.linspace(cfg['t0'], cfg['tf'], cfg['n_steps'])
    if t.size < 2:
        raise ValueError('Se requieren al menos dos pasos de simulación')
    dt = float(t[1] - t[0])
    return t, dt


def circular_task_reference(
    radius: float,
    center: tuple[float, float],
    omega: float,
    t: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Genera referencias cartesianas en trayectoria circular."""
    if t is None:
        raise ValueError('Se requiere un vector de tiempo "t"')
    cx, cy = center
    xd = cx + radius * np.cos(omega * t)
    yd = cy + radius * np.sin(omega * t)
    xdp = -radius * omega * np.sin(omega * t)
    ydp = radius * omega * np.cos(omega * t)
    Xd = np.vstack((xd, yd))
    Vd = np.vstack((xdp, ydp))
    return Xd, Vd


def plot_tracking(X: np.ndarray, Xd: np.ndarray, t: np.ndarray) -> plt.Figure:
    """Grafica la trayectoria seguida y los errores de seguimiento."""
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    ax[0].plot(Xd[0], Xd[1], '--', label='Deseada')
    ax[0].plot(X[0], X[1], label='Seguimiento')
    ax[0].set_aspect('equal', adjustable='box')
    ax[0].set_xlabel('x [m]')
    ax[0].set_ylabel('y [m]')
    ax[0].legend()
    ax[0].set_title('Trayectorias cartesianas')

    ax[1].plot(t, Xd[0] - X[0], label='Error en x')
    ax[1].plot(t, Xd[1] - X[1], label='Error en y')
    ax[1].set_xlabel('Tiempo [s]')
    ax[1].set_ylabel('Error [m]')
    ax[1].legend()
    ax[1].set_title('Errores de seguimiento')

    fig.tight_layout()
    return fig


__all__ = ['time_vector', 'circular_task_reference', 'plot_tracking']
