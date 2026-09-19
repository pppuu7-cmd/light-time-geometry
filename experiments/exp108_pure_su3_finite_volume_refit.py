"""EXP-108: re-fit published Table IX finite-volume susceptibility data.

Data: Durr & Fuwa, Phys. Rev. D 113, 054508 (2026), Table IX.
This is a simple diagonal-statistical-error audit, not the collaboration's
full correlated/systematic analysis.
"""

import numpy as np
from scipy.optimize import curve_fit

N = np.array([12, 14, 16, 18, 20, 24, 28], dtype=float)
q2 = np.array([0.1911, 0.6689, 1.3482, 2.2154, 3.394, 7.019, 13.050])
sq2 = np.array([0.0017, 0.0038, 0.0063, 0.0081, 0.015, 0.025, 0.053])

chi = q2 / N**4
schi = sq2 / N**4

mask = N >= 14
x = N[mask]
y = chi[mask]
s = schi[mask]

def one_over_L(x, c, d):
    return c + d/x

def exponential(x, c, b, m):
    return c + b*np.exp(-m*x)

MGA_PUBLISHED = 0.903

def exponential_plus_power(x, c, d, b):
    return c + d/x + b*np.exp(-MGA_PUBLISHED*x)

def fit(model, p0):
    p, cov = curve_fit(
        model, x, y, sigma=s, absolute_sigma=True,
        p0=p0, maxfev=100000
    )
    residual = (y-model(x, *p))/s
    chi2 = float(np.sum(residual**2))
    return p, np.sqrt(np.diag(cov)), chi2, len(x)-len(p)

p1, e1, c1, d1 = fit(one_over_L, [2.13e-5, -1e-4])
pe, ee, ce, de = fit(exponential, [2.12e-5, -1.0, 0.9])
px, ex, cx, dx = fit(exponential_plus_power, [2.12e-5, 0.0, -1.0])

r0_fm = 0.4757
r0_over_a = 7.263
a_fm = r0_fm/r0_over_a

c, d, b = px
A_fm = -(d/c)*a_fm
sigma_A_fm = (ex[1]/c)*a_fm

print("pure 1/L:", p1, e1, "chi2/dof", c1, d1)
print("exponential:", pe, ee, "chi2/dof", ce, de)
print("exp + 1/L:", px, ex, "chi2/dof", cx, dx)
print("A_YM_fm =", A_fm, "+/-", sigma_A_fm)
print("95% diagonal interval =", A_fm-1.96*sigma_A_fm,
      A_fm+1.96*sigma_A_fm)

A_target_fullQCD = 0.02705
print("formal target distance in sigma =",
      (A_target_fullQCD-A_fm)/sigma_A_fm)
