#!/usr/bin/env python3
"""EXP-047 deterministic late-time anomaly magnitude check."""

from math import pi, log10

H0_eV = 1.437722663192e-33
MPL_REDUCED_eV = 2.435e27

rho_anom_coeff = 31.0 / (480.0 * pi**2)
rho_anom = rho_anom_coeff * H0_eV**4
rho_de_scale = 3.0 * MPL_REDUCED_eV**2 * H0_eV**2
ratio = rho_anom / rho_de_scale

print(f"rho_anom_coeff={rho_anom_coeff:.15e}")
print(f"rho_anom_eV4={rho_anom:.15e}")
print(f"rho_DE_scale_eV4={rho_de_scale:.15e}")
print(f"rho_anom_over_rho_DE={ratio:.15e}")
print(f"log10_ratio={log10(ratio):.9f}")

assert rho_anom > 0.0
assert rho_de_scale > 0.0
assert 1e-125 < ratio < 1e-122
