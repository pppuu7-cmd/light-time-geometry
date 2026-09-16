# EXP-029 — Minimal hidden-sector benchmark

## Objective

Turn the surviving LTG/null-lift interpretation into one concrete cosmological model that can be solved and falsified.

The benchmark deliberately contains no claimed new interaction. Its purpose is to determine whether the LTG variables add a predictive correlation beyond ordinary KK dark-sector physics.

## 1. Minimal model

Take one compact hidden spatial dimension with stabilized physical radius `R` and one real massless 5D scalar field,

\[
S=\int d^4x\,d\psi\sqrt{-G}
\left[
-\frac12(\partial\Phi)^2
-\frac{\lambda_5}{4!}\Phi^4
\right].
\]

Expand

\[
\Phi(x,\psi)
=\frac{1}{\sqrt{2\pi R}}
\sum_{n\in\mathbb Z}
\phi_n(x)e^{in\psi/R}.
\]

Keep only

\[
n=0,+1,-1.
\]

The zero mode is massless,

\[
\boxed{m_0=0,}
\]

while the first modes have

\[
\boxed{m_1c^2=\frac{\hbar c}{R}.}
\]

The 4D effective quartic coupling scales schematically as

\[
\lambda_4\sim\frac{\lambda_5}{2\pi R}
\]

up to normalization/convention factors.

## 2. Allowed conversion

Compact momentum conservation permits

\[
\boxed{0+0\leftrightarrow(+1)+(-1).}
\]

The center-of-mass threshold for pair production is

\[
\boxed{\sqrt{s}_{\rm thr}=2m_1c^2=\frac{2\hbar c}{R}.}
\]

Thus the compactification radius fixes both

- the first massive level;
- the null→timelike pair-production threshold.

This correlation is standard KK kinematics.

## 3. Number-density Boltzmann system

Let `n_0` be the zero-mode number density and, by hidden-charge neutrality,

\[
n_+=n_-\equiv n_1.
\]

For the reaction

\[
0+0\leftrightarrow+1-1,
\]

a convenient schematic Boltzmann equation is

\[
\boxed{
\dot n_1+3Hn_1
=\langle\sigma v\rangle
\left[
n_0^2
-n_1^2
\frac{(n_0^{\rm eq})^2}{(n_1^{\rm eq})^2}
\right],
}
\]

where convention-dependent symmetry factors may be absorbed into `sigma v`.

The zero-mode equation contains the opposite collision term, with the factor required by particle counting.

Detailed balance guarantees that the collision term vanishes in thermal equilibrium.

## 4. Total hidden-sector energy conservation

If the hidden sector is isolated from visible matter after reheating,

\[
\boxed{
\dot\rho_h+3H(\rho_h+P_h)=0.
}
\]

Write

\[
\rho_h=\rho_0+\rho_1,
\]

\[
P_h=\frac13\rho_0+P_1.
\]

The massless zero mode always has

\[
w_0=1/3.
\]

The first KK modes interpolate between

\[
w_1\rightarrow1/3
\]

when relativistic and

\[
w_1\rightarrow0
\]

when nonrelativistic.

## 5. Exact equilibrium equation of state for the massive mode

For a dilute Maxwell–Boltzmann gas define

\[
z\equiv\frac{m_1c^2}{T_h}.
\]

In natural units the standard equilibrium expressions are

\[
P_1
=C\,m_1^2T_h^2K_2(z),
\]

\[
\rho_1
=C\,m_1^2T_h^2
\left[3K_2(z)+zK_1(z)\right],
\]

where `C` contains the degeneracy and phase-space normalization.

Therefore

\[
\boxed{
w_1(z)
=\frac{K_2(z)}{3K_2(z)+zK_1(z)}.
}
\]

The massive-mode trace/proper-time fraction is

\[
\boxed{
\chi_1(z)
\equiv1-3w_1
=
\frac{zK_1(z)}{3K_2(z)+zK_1(z)}.
}
\]

Limits:

\[
z\ll1:\quad \chi_1\rightarrow0,
\]

\[
z\gg1:\quad \chi_1\rightarrow1.
\]

This is precisely the LTG hidden-pressure/proper-time interpolation, now expressed as an ordinary thermal function.

## 6. Total hidden-sector LTG fraction

For the mixture,

\[
T_{(4),h}
=-\rho_h+3P_h
=-(\rho_1-3P_1).
\]

Thus

\[
\boxed{
\chi_h
\equiv
-\frac{T_{(4),h}}{\rho_h}
=
\frac{\rho_1-3P_1}{\rho_0+\rho_1}.
}
\]

Equivalently,

\[
\boxed{w_h=\frac{1-\chi_h}{3}.}
\]

This remains within

\[
0\le w_h\le1/3.
\]

## 7. Important equilibrium result

At very high hidden temperature,

\[
T_h\gg m_1c^2,
\]

all retained modes are relativistic, so

\[
\chi_h\approx0,
\qquad
w_h\approx1/3.
\]

As the temperature crosses

\[
T_h\sim m_1c^2,
\]

the `n=±1` modes become nonrelativistic and their individual `chi_1` rises.

But if chemical equilibrium remains efficient, their equilibrium abundance becomes Boltzmann suppressed:

\[
n_1^{\rm eq}\propto e^{-m_1c^2/T_h}.
\]

They annihilate through

\[
(+1)+(-1)\rightarrow0+0.
\]

At late equilibrium times the hidden sector again becomes dominated by massless zero-mode radiation:

\[
\boxed{
\chi_h\rightarrow0,
\qquad
w_h\rightarrow1/3.
}
\]

### F-029A

**Thermal equilibrium does not generically leave a permanent massive sector. Cooling drives heavy KK modes back into the null/radiation sector.**

This reverses the naive one-way phrase "light becomes matter".

## 8. Freeze-out is required for a persistent matter component

A relic massive population survives if the annihilation rate

\[
\Gamma_{ann}
\sim n_1\langle\sigma v\rangle
\]

falls below the Hubble expansion rate,

\[
\boxed{
\Gamma_{ann}\lesssim H.
}
\]

After chemical freeze-out,

\[
n_1\propto a^{-3},
\]

while the remaining zero-mode radiation scales approximately as

\[
\rho_0\propto a^{-4}.
\]

For nonrelativistic survivors,

\[
\rho_1\simeq2m_1c^2n_1
\propto a^{-3}.
\]

Therefore, if stable KK relics survive, their fraction relative to hidden radiation grows as the universe expands.

Then

\[
\chi_h
\]

can evolve from near zero toward unity.

### F-029B

**A lasting null→timelike cosmological conversion requires nonequilibrium relic survival, not merely the existence of the kinematically allowed pair-production process.**

## 9. Three dynamical regimes

The benchmark naturally has three regimes.

### I. Relativistic equilibrium

\[
T_h\gg m_1c^2,
\]

\[
w_h\simeq1/3,
\qquad
\chi_h\simeq0.
\]

### II. Transition / annihilation

\[
T_h\sim m_1c^2.
\]

Massive modes become timelike/nonrelativistic and hidden pressure/trace becomes important, but annihilation is also strongest in determining the relic abundance.

### III. Frozen relic + dark radiation

If freeze-out occurs,

\[
\rho_1\propto a^{-3},
\qquad
\rho_0\propto a^{-4}.
\]

The massive fraction grows relative to radiation and

\[
w_h\rightarrow0
\]

if the relic eventually dominates the hidden sector.

This is standard hot-to-cold relic cosmology.

## 10. Relation to proper time

For each massive relic,

\[
\left(\frac{d\tau}{dt}\right)^2
=1-\frac{v^2}{c^2}.
\]

As the relic cools,

\[
v/c\rightarrow0,
\]

so

\[
\frac{d\tau}{dt}\rightarrow1.
\]

The ensemble LTG fraction

\[
\chi_h
\]

therefore grows both because surviving massive particles become nonrelativistic and because their matter-like energy density redshifts more slowly than the zero-mode radiation.

## 11. Does LTG reduce the parameter count?

The cosmological outcome depends on

- `R` or `m_1`;
- the effective coupling/cross section `lambda_4` / `sigma v`;
- the hidden-sector initial temperature or entropy ratio;
- radion stabilization assumptions;
- any portal to visible matter;
- cosmological expansion history.

The LTG identities

\[
\chi=1-3w
\]

and

\[
m_1c^2=\hbar c/R
\]

do not eliminate any of these standard model parameters.

### F-029C

**At this stage the benchmark is exactly ordinary compact-extra-dimension hidden-sector cosmology written in LTG variables.**

No new parameter-reducing relation has appeared.

## 12. What would be a real LTG prediction here?

A genuine LTG-specific addition would have to predict, rather than choose, something like

\[
\langle\sigma v\rangle
=F(m_1,M_{\rm Pl})
\]

or

\[
T_{h,\rm initial}/T_{vis}
=F(n,w),
\]

or an exact relation between

- the compactification scale;
- the conversion/freeze-out rate;
- the phase integer;
- and the relic abundance.

Nothing derived so far supplies such a relation.

## 13. Falsification status

### F-029D

**The minimal hidden-sector benchmark successfully realizes the LTG narrative dynamically, but produces no new prediction beyond standard KK + Boltzmann physics.**

### F-029E

**The benchmark therefore passes consistency but fails the novelty criterion.**

## 14. Next experiment

The most efficient next step is quantitative rather than formal:

1. choose dimensionless variables `x=m_1/T_h` and yields `Y_i=n_i/s_h`;
2. derive the reduced Boltzmann system;
3. scan the single combination controlling freeze-out, schematically `M_Pl m_1 <sigma v>` together with the hidden/visible temperature ratio;
4. compute `Omega_1`, `Delta N_eff`, and `w_h(a)`;
5. compare the resulting allowed region with ordinary hidden thermal relic models.

If the allowed region has no LTG-specific correlation, close this branch as known-equivalent.

## Literature anchors

- KK-number conservation / KK parity and pair production are standard universal-extra-dimension results.
- Thermal freeze-out and relic abundance follow ordinary Boltzmann cosmology.
