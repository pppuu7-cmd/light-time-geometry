# EXP-003 — Does radiation-to-matter conversion increase space?

## Question

The original LTG intuition included the stronger claim that converting light/radiation into matter might generate proper time and thereby increase spatial volume.

EXP-003 asks the narrow standard-physics question first:

> In an FRW universe governed by general relativity, does conversion of radiation into pressureless matter at fixed total energy density necessarily increase the expansion rate or acceleration?

Use units `c = 1`.

---

## Standard FRW equations

For a homogeneous and isotropic universe,

\[
H^2=\left(\frac{\dot a}{a}\right)^2
=\frac{8\pi G}{3}\rho+\frac{\Lambda}{3}-\frac{k}{a^2},
\]

and

\[
\frac{\ddot a}{a}
=-\frac{4\pi G}{3}(\rho+3P)+\frac{\Lambda}{3}.
\]

The total continuity equation is

\[
\dot\rho+3H(\rho+P)=0
\]

when the total stress tensor is conserved.

For radiation,

\[
P_r=\frac13\rho_r,
\]

while for pressureless matter,

\[
P_m\simeq0.
\]

---

## Allow explicit radiation -> matter energy transfer

Introduce an interaction rate `Q`:

\[
\dot\rho_r+4H\rho_r=-Q,
\]

\[
\dot\rho_m+3H\rho_m=+Q.
\]

Adding the equations gives the ordinary total conservation law. `Q>0` means energy is transferred from radiation to matter.

This is important: conversion does not require violation of local energy-momentum conservation.

---

## Test 1 — instantaneous Hubble rate

Suppose an amount `delta rho` is converted from radiation to matter over a time short enough that `a`, `k`, and `Lambda` can be treated as fixed, while total energy density is continuous:

\[
\delta\rho_r=-\delta\rho,
\qquad
\delta\rho_m=+\delta\rho,
\qquad
\delta\rho_{tot}=0.
\]

The first Friedmann equation depends on the total `rho`, not separately on `rho_r` and `rho_m`.

Therefore

\[
\boxed{\delta H^2=0}
\]

at the conversion instant under these assumptions.

So standard GR does **not** say that converting radiation into matter directly increases the instantaneous expansion rate.

---

## Test 2 — acceleration / deceleration

The pressure does change. The conversion gives

\[
\delta P
=\frac13\delta\rho_r
=-\frac13\delta\rho.
\]

From the acceleration equation,

\[
\delta\left(\frac{\ddot a}{a}\right)
=-4\pi G\,\delta P
=\frac{4\pi G}{3}\delta\rho.
\]

Thus

\[
\boxed{
\delta(\ddot a/a)>0
}
\]

for radiation-to-matter conversion at fixed total density.

But the interpretation is crucial: the conversion makes the cosmological deceleration **weaker** because pressure drops. It does not, by itself, guarantee positive acceleration.

For example with `Lambda=0` and the same energy density `rho`:

radiation-dominated:

\[
\frac{\ddot a}{a}=-\frac{8\pi G}{3}\rho,
\]

matter-dominated:

\[
\frac{\ddot a}{a}=-\frac{4\pi G}{3}\rho.
\]

Both are decelerating, but matter decelerates only half as strongly at equal energy density.

This is a real standard-GR effect that qualitatively points in the same direction as the original intuition, but it is weaker than "matter creates expansion."

---

## Test 3 — stress-energy trace and Ricci scalar

For the radiation+matter mixture,

\[
T=-\rho+3P.
\]

Since radiation has `P_r=rho_r/3`, its contribution cancels in the trace. Pressureless matter contributes

\[
T=-\rho_m.
\]

The traced Einstein equation gives

\[
R=4\Lambda-8\pi G T,
\]

hence

\[
\boxed{R=4\Lambda+8\pi G\rho_m.}
\]

Therefore, at fixed total energy density, converting radiation into pressureless matter gives

\[
\boxed{\delta R=8\pi G\,\delta\rho_m>0.}
\]

This is a striking result for LTG:

- the instantaneous `H^2` need not change;
- the deceleration becomes weaker;
- the Ricci scalar increases because the stress-energy becomes traceful.

So the closest established statement to the original idea is not

> matter conversion directly creates more space,

but rather

> converting trace-free radiation into traceful matter changes spacetime curvature and changes the subsequent expansion dynamics through the pressure term.

---

## A compact chain

Within standard GR:

\[
\boxed{
\text{radiation }(p^2=0)
\to T=0
\to R-4\Lambda=0
}
\]

while ideal pressureless matter gives

\[
\boxed{
\text{massive matter }(p^2<0)
\to T<0
\to R-4\Lambda>0.
}
\]

For a conversion at fixed total energy density,

\[
\boxed{
\rho_r\to\rho_m:
\quad H^2\text{ continuous},
\quad \ddot a/a\text{ shifts upward},
\quad R\text{ increases}.
}
\]

---

## Does this confirm LTG H2?

No. These effects are already completely contained in standard GR. They do not show that proper time is a substance, nor that matter creates spatial volume.

But they identify a precise mathematical bridge connecting the three elements that motivated LTG:

1. null versus timelike mass shell;
2. radiation versus matter stress-energy trace;
3. scalar curvature and cosmological dynamics.

This bridge is much more promising than the original Euclidean-looking decomposition of energy.

---

## Falsification consequence

Any stronger LTG law claiming that trace production itself creates extra expansion must predict an additional term beyond the standard Friedmann equations.

Schematically, one would need something like

\[
H^2=H^2_{GR}+\Delta_{LTG}
\]

or

\[
\frac{\ddot a}{a}
=\left(\frac{\ddot a}{a}\right)_{GR}+A_{LTG},
\]

where the extra contribution is covariantly derived, vanishes in the GR limit, and cannot be absorbed into an ordinary scalar field, cosmological constant, modified-gravity coupling, or redefinition of matter.

Until such a term is derived, the expansion part of LTG remains an interpretation rather than new dynamics.

## EXP-003 status

**PARTIAL STANDARD-PHYSICS ECHO, NO NEW DYNAMICS.**

Radiation-to-matter conversion does not directly increase `H` at fixed total density, but it decreases pressure, weakens deceleration, and increases the Ricci scalar through the stress-energy trace.

## Next target

Search for the minimal covariant extension that could connect a null-to-timelike conversion measure to geometry while:

1. preserving diffeomorphism invariance;
2. preserving total stress-energy conservation;
3. reducing exactly to GR when the new coupling vanishes;
4. not being merely a standard scalar-tensor or `f(R,T)` reparameterization;
5. producing a distinct observable.
