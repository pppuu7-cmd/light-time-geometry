"""EXP-101/102 finite-volume target calculator.

This script computes the vacuum-energy scale implied by the
EXP-100 LTG/QCD-KMS hypothesis at ordinary lattice sizes.
It does not assume a cosmological Hubble scale.
"""

import math

F_PI_MEV = 92.07
M_PI_MEV = 134.9768
M_ETAP_MEV = 957.78
HBARC_MEV_FM = 197.3269804

ZETA = 0.825

X_QCD_MEV4 = 0.5 * F_PI_MEV**2 * M_PI_MEV**2

# Orientation scale only; not identified with Delta rho.
CHI_T_MEV4 = 78.1**4

print("L_fm,Delta_rho_MeV4,Delta_rho_quarter_MeV,Delta_rho_over_chi_t")
for L_fm in (2, 3, 4, 5, 6, 8, 10):
    inv_L_MeV = HBARC_MEV_FM / L_fm
    delta_rho = (
        ZETA
        * inv_L_MeV
        * X_QCD_MEV4
        / (math.pi * M_ETAP_MEV)
    )
    print(
        f"{L_fm},"
        f"{delta_rho:.12e},"
        f"{delta_rho**0.25:.9f},"
        f"{delta_rho/CHI_T_MEV4:.9f}"
    )
