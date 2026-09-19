"""EXP-100 QCD-KMS numerical benchmark.

No cosmological H0 or Lambda is used as an input.
All energies are in GeV unless otherwise stated.
"""

import math

# Representative low-energy QCD inputs
f_pi = 92.07e-3
m_pi = 134.9768e-3
m_eta_prime = 957.78e-3

# Reduced Planck mass
Mbar = 2.435e18

# hbar in GeV s
hbar_GeV_s = 6.582119569e-25

zeta = 1.0

H_GeV = zeta * f_pi**2 * m_pi**2 / (
    6.0 * math.pi * m_eta_prime * Mbar**2
)
H_s = H_GeV / hbar_GeV_s

ln_D = 8.0 * math.pi**2 * Mbar**2 / H_GeV**2
log10_D = ln_D / math.log(10.0)
bits = ln_D / math.log(2.0)

print(f"H_GeV={H_GeV:.12e}")
print(f"H_s^-1={H_s:.12e}")
print(f"ln_D={ln_D:.12e}")
print(f"log10_D={log10_D:.12e}")
print(f"bits={bits:.12e}")

# Previously used LTG benchmark only for a posteriori comparison,
# not as an input to H_GeV or ln_D.
ln_D_benchmark = 3.30721347e122
zeta_match = math.sqrt(ln_D / ln_D_benchmark)
print(f"zeta_match={zeta_match:.12f}")
