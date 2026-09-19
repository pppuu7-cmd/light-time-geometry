#!/usr/bin/env python3
"""EXP-044 deterministic numerical checks. Standard library only."""

from math import exp, log, sqrt

# Representative late-time cosmology used only for order-of-magnitude checks.
H0_km_s_Mpc = 67.4
MPC_M = 3.085677581e22
HBAR_EV_S = 6.582119569e-16
KB_EV_K = 8.617333262e-5
T0_K = 2.7255
OMEGA_LAMBDA = 0.685
OMEGA_GAMMA = 5.38e-5
Z_REC = 1089.0

H0 = H0_km_s_Mpc * 1000.0 / MPC_M
E_H = HBAR_EV_S * H0
E_CMB = 2.701 * KB_EV_K * T0_K
ratio = E_CMB / E_H
efolds = log(ratio)
H_lambda = H0 * sqrt(OMEGA_LAMBDA)
seconds_per_year = 365.25 * 24.0 * 3600.0
future_years = efolds / H_lambda / seconds_per_year

target = OMEGA_LAMBDA / OMEGA_GAMMA
a_i = 1.0 / (1.0 + Z_REC)

def generated_ratio(gamma):
    """rho_X0/rho_gamma0 for rho_X(ai)=0 and Q=gamma H rho_gamma."""
    return gamma / (4.0 + gamma) * (a_i ** (-(4.0 + gamma)) - 1.0)

# Deterministic bisection.
lo, hi = 0.0, 1e-4
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if generated_ratio(mid) < target:
        lo = mid
    else:
        hi = mid
gamma = 0.5 * (lo + hi)

print(f"H0_s^-1={H0:.12e}")
print(f"hbar_H0_eV={E_H:.12e}")
print(f"mean_CMB_photon_eV={E_CMB:.12e}")
print(f"CMB_to_hbarH_ratio={ratio:.12e}")
print(f"required_efolds={efolds:.9f}")
print(f"asymptotic_deSitter_years={future_years:.12e}")
print(f"OmegaLambda_over_OmegaGamma={target:.12e}")
print(f"Gamma_from_recombination={gamma:.12e}")
print(f"temperature_exponent_shift={gamma/4.0:.12e}")

assert E_H > 0.0
assert ratio > 1e29
assert 60.0 < efolds < 80.0
assert 1e11 < future_years < 1e13
assert 1e-9 < gamma < 1e-6
