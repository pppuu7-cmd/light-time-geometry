#!/usr/bin/env python3
"""Dimensionless freeze-out toy model for LTG EXP-029/030.

Assumptions
-----------
* A massless zero mode sets the hidden bath temperature T_h ~ a^-1.
* One +1 and one -1 KK mode have equal number density n_1.
* Entropy heating/backreaction of the bath is neglected in this first toy model.
* The pair-counting convention is absorbed into lambda_eff.

The equation is
    dY/dx = -(lambda_eff/x^2) (Y^2 - Y_eq^2),
with x=m_1/T_h and Y=n_1/s_h for each of the +/- modes.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

from scipy.integrate import solve_ivp
from scipy.special import kv, kve

A_YEQ = 45.0 / (4.0 * math.pi**4)


def y_eq(x: float, g1: float = 1.0, gsh: float = 1.0) -> float:
    """Maxwell-Boltzmann equilibrium yield per +/- species."""
    if x > 700.0:
        return 0.0
    return A_YEQ * (g1 / gsh) * x * x * float(kv(2, x))


def k1_over_k2(x: float) -> float:
    """Stable K1(x)/K2(x), including at large x."""
    return float(kve(1, x) / kve(2, x))


@dataclass
class State:
    x: float
    Y: float
    rho_massive_over_rho0: float
    w_hidden: float
    chi_hidden: float


def thermo_state(x: float, Y: float, gsh: float = 1.0, g0: float = 1.0) -> State:
    """Compute mixture thermodynamics in the fixed-zero-mode-bath approximation.

    There are two massive species (+1,-1), each with yield Y.
    rho0 = (pi^2/30) g0 T^4 and s_h=(2pi^2/45) gsh T^3.
    """
    r_k = k1_over_k2(x)
    pref = (8.0 / 3.0) * (gsh / g0) * Y
    rho_ratio = pref * (x * r_k + 3.0)
    pressure_ratio = pref
    w = (1.0 / 3.0 + pressure_ratio) / (1.0 + rho_ratio)
    chi = 1.0 - 3.0 * w
    return State(x, Y, rho_ratio, w, chi)


def integrate(lambda_eff: float, x0: float = 0.1, xmax: float = 1.0e4,
              g1: float = 1.0, gsh: float = 1.0):
    """Integrate in u=ln x to handle many decades robustly."""
    u0, umax = math.log(x0), math.log(xmax)
    y0 = [y_eq(x0, g1, gsh)]

    def rhs(u, y):
        x = math.exp(u)
        ye = y_eq(x, g1, gsh)
        return [-lambda_eff / x * (y[0] * y[0] - ye * ye)]

    sol = solve_ivp(
        rhs,
        (u0, umax),
        y0,
        method="Radau",
        rtol=1e-8,
        atol=1e-12,
        dense_output=True,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lambdas", nargs="+", type=float,
        default=[1e2, 1e4, 1e6, 1e8]
    )
    parser.add_argument("--xmax", type=float, default=1e4)
    parser.add_argument(
        "--samples", nargs="+", type=float,
        default=[1, 3, 10, 30, 100, 1000]
    )
    args = parser.parse_args()

    for lam in args.lambdas:
        sol = integrate(lam, xmax=args.xmax)
        y_inf = float(sol.y[0, -1])
        print(f"lambda={lam:.6g}  Y_inf={y_inf:.9g}")
        print("x,Y,rho1/rho0,w_h,chi_h")
        for x in args.samples:
            if x > args.xmax:
                continue
            y_val = float(sol.sol(math.log(x))[0])
            state = thermo_state(x, y_val)
            print(
                f"{x:g},{y_val:.9g},{state.rho_massive_over_rho0:.9g},"
                f"{state.w_hidden:.9g},{state.chi_hidden:.9g}"
            )
        print()


if __name__ == "__main__":
    main()
