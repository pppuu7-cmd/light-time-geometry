# EXP-021 — Equation-of-state domain and acceleration no-go

## Objective

Determine the full 4D equation-of-state range allowed by the current 5D-null kinetic interpretation and test whether the mechanism can, by itself, explain accelerated expansion.

This is a domain-of-validity experiment rather than a novelty search.

## 1. Start from the robust ensemble identity

EXP-016 established for an arbitrary isotropic classical distribution of on-shell 5D-null KK modes:

\[
3P+P_\psi=\rho.
\]

Define

\[
\chi\equiv\frac{P_\psi}{\rho}
=\left\langle
\frac{m^2c^4}{E^2}
\right\rangle_E
=\left\langle
\left(\frac{d\tau}{dt}\right)^2
\right\rangle_E.
\]

Every on-shell massive mode satisfies

\[
0\le\frac{m^2c^4}{E^2}\le1,
\]

so for a positive-energy ensemble

\[
\boxed{0\le\chi\le1.}
\]

## 2. Effective 4D equation of state

Let

\[
w\equiv\frac{P}{\rho}.
\]

From `3P + P_psi = rho`,

\[
3w+\chi=1.
\]

Therefore

\[
\boxed{w=\frac{1-\chi}{3}.}
\]

Because `0 <= chi <= 1`,

\[
\boxed{0\le w\le\frac13.}
\]

This is an exact domain restriction for the stated kinetic sector.

## 3. Limiting cases

### Massless/zero-mode radiation

\[
\chi=0
\]

gives

\[
\boxed{w=1/3.}
\]

### Nonrelativistic massive KK matter

\[
\chi\rightarrow1
\]

gives

\[
\boxed{w\rightarrow0.}
\]

Thus the null-to-timelike conversion explored in EXP-014 interpolates naturally between radiation-like and matter-like behavior.

## 4. Vacuum energy is outside the kinetic null sector

A cosmological constant/vacuum-energy component has

\[
w=-1.
\]

If one tried to force the kinetic identity onto it,

\[
\chi=1-3w=4,
\]

which violates

\[
0\le\chi\le1.
\]

Therefore

\[
\boxed{
\text{positive-energy on-shell 5D-null KK particles cannot represent }w=-1\text{ vacuum energy.}
}
\]

Likewise any component with

\[
w<0
\]

lies outside this simple positive kinetic-particle sector.

Negative pressure requires additional physics such as a potential, vacuum contribution, modified stress sector, boundary effect, or other non-kinetic structure.

## 5. 4D acceleration test

In ordinary 4D Einstein-frame GR with zero cosmological constant,

\[
\frac{\ddot a}{a}
=-\frac{4\pi G}{3}\rho(1+3w).
\]

For the allowed LTG kinetic range,

\[
0\le w\le1/3,
\]

so

\[
1+3w\ge1>0.
\]

For positive density,

\[
\boxed{\ddot a<0.}
\]

Hence a stabilized compactification whose late-time 4D matter content consists only of this kinetic KK sector cannot produce accelerated expansion by itself.

## 6. Radiation → matter conversion

As energy moves from the zero mode toward nonrelativistic KK modes,

\[
\chi:0\rightarrow1,
\]

and

\[
w:\frac13\rightarrow0.
\]

The source of 4D deceleration changes from

\[
1+3w=2
\]

to

\[
1+3w=1.
\]

Thus the conversion makes expansion **less strongly decelerating**, but does not make it accelerating.

This reproduces and sharpens EXP-003 in the hidden-pressure language.

## 7. Relation to the original intuition

The original phrase

> matter converts light into time and increases space

cannot be retained as a universal expansion mechanism in the minimal model.

The supported statement is narrower:

\[
\boxed{
\text{null/visible momentum}
\rightarrow
\text{hidden momentum}
\rightarrow
\text{4D mass/proper-time fraction}
\rightarrow
w:1/3\rightarrow0
}
\]

with a corresponding redistribution of higher-dimensional directional stress.

This can weaken deceleration and alter visible/internal shear, but it does not generate negative pressure.

## 8. Dark-energy no-go at this level

The minimal LTG null-kinetic sector cannot explain dark energy or inflation because both require an effective source capable of sufficiently negative pressure in the 4D Einstein frame.

Any attempt to obtain acceleration must add something beyond the current null-particle kinetic sector, for example:

- radion/scalar potential energy;
- vacuum energy;
- higher-curvature terms;
- nonminimal interactions;
- boundary/brane contributions;
- another sector with negative effective pressure.

Each such extension belongs to well-developed existing theory classes and must be tested for equivalence before being called LTG-specific.

## 9. A useful inverse relation

Within the valid kinetic domain,

\[
\boxed{
\chi=1-3w.
}
\]

Thus a measured fluid equation of state fixes the ensemble proper-time fraction predicted by the null-lift interpretation:

\[
\boxed{
\left\langle
\left(\frac{d\tau}{dt}\right)^2
\right\rangle_E
=1-3w.
}
\]

Examples:

- `w=1/3 -> chi=0`;
- `w=0 -> chi=1`;
- `w=1/6 -> chi=1/2`.

This relation is not new physics; it is the kinetic mass-shell trace identity expressed in LTG language.

## 10. Results

### F-021A

**The current positive-energy on-shell 5D-null kinetic sector has the strict 4D equation-of-state domain**

\[
\boxed{0\le w\le1/3.}
\]

### F-021B

**Radiation-to-massive-mode conversion interpolates from `w=1/3` to `w=0`.**

### F-021C

**The mechanism weakens ordinary 4D deceleration but cannot generate acceleration by itself after stabilization.**

### F-021D

**Vacuum energy/dark energy (`w=-1`) cannot be represented as this kinetic proper-time/hidden-pressure fraction; it would require the impossible value `chi=4`.**

### F-021E

**The original LTG expansion claim is therefore falsified in its strongest form. The surviving role of mass/proper time is stress redistribution and equation-of-state change, not a universal source of spatial expansion.**

## 11. Next research gate

The next scientifically useful question is not how to force acceleration, but whether the phase variable

\[
\Phi=\frac1\hbar\int mc^2d\tau
\]

can supply any new observable dynamics at all.

A clean next test is to write the most general local 4D WKB/Hamilton–Jacobi correction linear in curvature and check whether every natural `mass–phase–curvature` coupling reduces to standard curved-spacetime QFT (`xi R phi^2`, higher-derivative EFT) or fails the flat-space massive-particle limit.
