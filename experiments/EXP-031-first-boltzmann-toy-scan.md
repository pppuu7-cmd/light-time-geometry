# EXP-031 — First reproducible Boltzmann toy scan

## Objective

Numerically integrate the dimensionless freeze-out system proposed in EXP-029/030 and test the qualitative LTG evolution of the hidden proper-time fraction

\[
\chi_h=1-3w_h.
\]

The reproducible code is

`simulations/boltzmann_toy.py`.

## 1. Approximation used

This first scan intentionally uses a simplified bath treatment:

- the massless zero mode sets the hidden temperature `T_h ~ a^-1`;
- the `+1` and `-1` massive modes have equal number density;
- entropy heating of the zero mode by annihilation is **not** fed back into `T_h`;
- visible-sector evolution is absorbed into one effective freeze-out strength;
- the pair-counting convention is absorbed into the effective parameter `lambda`.

Thus this is a controlled **dimensionless freeze-out toy**, not yet a precision cosmology solver.

## 2. Dimensionless system

Define

\[
x=\frac{m_1}{T_h}
\]

in natural units and the per-species yield

\[
Y=\frac{n_1}{s_h}.
\]

The integrated equation is

\[
\boxed{
\frac{dY}{dx}
=-\frac{\lambda}{x^2}
\left(Y^2-Y_{eq}^2\right).
}
\]

For Maxwell-Boltzmann equilibrium,

\[
\boxed{
Y_{eq}
=\frac{45}{4\pi^4}x^2K_2(x)
}
\]

for unit degeneracy and the chosen hidden-entropy normalization.

The effective parameter `lambda` corresponds schematically to

\[
\lambda
\sim
0.264\,
\frac{g_{*s,h}}{\sqrt{g_{*,vis}}}
\xi^2M_{Pl}m_1\langle\sigma v\rangle.
\]

Larger `lambda` means annihilation remains efficient longer.

## 3. Reconstruct hidden thermodynamics

With two massive species `+1,-1`, define the zero-mode radiation density `rho_0`.

For the massive modes,

\[
\frac{\rho_1}{\rho_0}
=\frac83Y
\left[
x\frac{K_1(x)}{K_2(x)}+3
\right].
\]

Their pressure satisfies

\[
\frac{P_1}{\rho_0}=\frac83Y.
\]

Therefore the total hidden equation of state is

\[
\boxed{
w_h
=\frac{1/3+P_1/\rho_0}
{1+\rho_1/\rho_0}
}
\]

and

\[
\boxed{\chi_h=1-3w_h.}
\]

## 4. Scan

The first scan used

\[
\lambda=10^2,10^4,10^6,10^8
\]

and integrated from

\[
x=0.1
\]

to

\[
x=10^4.
\]

The asymptotic per-species yields were:

| `lambda` | `Y_inf` |
|---:|---:|
| `1e2` | `2.4737e-2` |
| `1e4` | `6.4128e-4` |
| `1e6` | `1.0706e-5` |
| `1e8` | `1.5120e-7` |

As expected, stronger annihilation produces a much smaller relic yield.

## 5. Weak-annihilation example — lambda = 1e2

Selected values:

| `x` | `Y` | `rho_1/rho_0` | `w_h` | `chi_h` |
|---:|---:|---:|---:|---:|
| 1 | 0.1894 | 1.702 | 0.3103 | 0.0692 |
| 3 | 0.08327 | 1.101 | 0.2643 | 0.2070 |
| 10 | 0.03286 | 1.022 | 0.2081 | 0.3756 |
| 30 | 0.02695 | 2.268 | 0.1240 | 0.6281 |
| 100 | 0.02536 | 6.865 | 0.0510 | 0.8471 |
| 1000 | 0.02479 | 66.21 | 0.00594 | 0.9822 |

The relic freezes out early and subsequently redshifts as matter relative to the zero-mode radiation. Therefore

\[
\boxed{\chi_h\rightarrow1}
\]

at late times.

This is the numerical realization of the LTG narrative: the surviving hidden sector becomes overwhelmingly timelike/matter-like.

## 6. Intermediate example — lambda = 1e4

Selected values:

| `x` | `Y` | `rho_1/rho_0` | `w_h` | `chi_h` |
|---:|---:|---:|---:|---:|
| 3 | 0.06423 | 0.8493 | 0.2729 | 0.1814 |
| 10 | 0.001781 | 0.0554 | 0.3203 | 0.0390 |
| 30 | 0.0008150 | 0.0686 | 0.3140 | 0.0581 |
| 100 | 0.0006847 | 0.1854 | 0.2827 | 0.1518 |
| 1000 | 0.0006450 | 1.723 | 0.1231 | 0.6308 |

This case illustrates a non-monotonic history:

1. `chi_h` initially grows as the massive modes become nonrelativistic;
2. annihilation reduces their abundance and `chi_h` falls back toward zero;
3. the small frozen relic later redshifts more slowly than radiation and `chi_h` grows again.

### F-031A

**The proper-time fraction need not grow monotonically.**

The mass shell of individual particles and the cosmological abundance of those particles are separate effects.

## 7. Strong-annihilation example — lambda = 1e6

The relic abundance is much smaller:

\[
Y_\infty\simeq1.07\times10^{-5}.
\]

At `x=30`,

\[
\chi_h\simeq1.3\times10^{-3},
\]

and even at `x=1000`,

\[
\chi_h\simeq2.8\times10^{-2}.
\]

Thus the hidden sector remains radiation dominated for a long time after the first KK modes become nonrelativistic.

## 8. Very strong annihilation — lambda = 1e8

The relic yield is

\[
Y_\infty\simeq1.51\times10^{-7}.
\]

At `x=1000`,

\[
\chi_h\simeq4.1\times10^{-4}.
\]

The massive component is practically erased over the scanned range.

### F-031B

**A kinematically available null→timelike channel does not imply a cosmologically significant timelike sector. Its importance is controlled by nonequilibrium abundance dynamics.**

## 9. Late matter/radiation equality estimate

For a deeply nonrelativistic frozen relic,

\[
\frac{\rho_1}{\rho_0}
\simeq\frac83Y_\infty x.
\]

Therefore the approximate hidden matter-radiation equality point is

\[
\boxed{
x_{eq}\simeq\frac{3}{8Y_\infty}.}
\]

Using the numerical relic yields gives roughly:

| `lambda` | approximate `x_eq` |
|---:|---:|
| `1e2` | `1.5e1` |
| `1e4` | `5.8e2` |
| `1e6` | `3.5e4` |
| `1e8` | `2.5e6` |

The exact early value differs from this asymptotic estimate when the massive particles are not yet deeply nonrelativistic.

## 10. Main conceptual result

The numerical experiment separates two ideas that were initially conflated:

### Particle-level transition

A mode with hidden momentum has

\[
m>0,
\qquad
d\tau>0.
\]

### Cosmological transition

The universe/sector becomes matter-like only if enough such modes **survive**.

Therefore

\[
\boxed{
\text{mass generation / timelike kinematics}
\neq
\text{matter domination}.
}
\]

The latter requires abundance dynamics.

## 11. Novelty status

The scan reproduces standard thermal-relic behavior.

### F-031C

**LTG's `chi_h` is a useful compact diagnostic of the radiation-to-matter history, but the evolution is completely determined by ordinary Boltzmann dynamics in this benchmark.**

### F-031D

**No new parameter relation appears numerically.**

## 12. Numerical-validation status

The code was executed successfully with a stiff `Radau` integrator and the outputs above are reproducible from

`simulations/boltzmann_toy.py`.

## 13. Next numerical upgrade

The next simulation should remove the largest approximation of this toy model by evolving the zero-mode temperature/entropy simultaneously.

That requires coupled equations for

- `Y_1`;
- hidden energy or temperature `T_h`;
- entropy transfer from `+1,-1` annihilation;
- visible expansion through `H(T_vis)`;
- hidden/visible temperature ratio `xi`;
- `Delta N_eff`.

This will determine quantitatively the tradeoff identified in EXP-030 between

\[
\text{massive relic abundance}
\]

and

\[
\text{dark-radiation heating}.
\]
