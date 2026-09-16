# EXP-033 — Proper-time fraction to curvature-trace bridge

## Objective

Derive the strongest exact relation found so far connecting:

- light/null behavior;
- proper time;
- rest mass;
- matter equation of state;
- spacetime curvature;
- and, in FLRW, spatial expansion.

The goal is to determine whether the original LTG intuition has a precise standard-physics core.

## 1. Relativistic kinetic theory

For an isotropic ensemble of on-shell particles with one-particle energy

\[
E^2=p^2c^2+m^2c^4,
\]

the total energy density is schematically

\[
\varepsilon=\int E f(\mathbf p)\,d^3p,
\]

while the isotropic pressure is

\[
P=\frac13\int \frac{p^2c^2}{E}f(\mathbf p)\,d^3p.
\]

Therefore

\[
\varepsilon-3P
=
\int\left(E-\frac{p^2c^2}{E}\right)f\,d^3p.
\]

Using the mass-shell relation,

\[
E-\frac{p^2c^2}{E}
=
\frac{m^2c^4}{E},
\]

so

\[
\boxed{
\varepsilon-3P
=
\int \frac{m^2c^4}{E}f\,d^3p.
}
\]

## 2. Insert proper-time rate

For every massive on-shell particle in a local inertial frame,

\[
\frac{d\tau}{dt}=\frac{mc^2}{E}.
\]

Hence

\[
\frac{m^2c^4}{E}
=
E\left(\frac{d\tau}{dt}\right)^2.
\]

Therefore

\[
\boxed{
\varepsilon-3P
=
\int E
\left(\frac{d\tau}{dt}\right)^2
f\,d^3p.
}
\]

Define the energy-weighted proper-time fraction

\[
\chi_\tau
\equiv
\frac{
\int E(d\tau/dt)^2 f\,d^3p
}{
\int E f\,d^3p
}.
\]

Then

\[
\boxed{
\chi_\tau
=1-3w,
\qquad
w\equiv\frac{P}{\varepsilon}.
}
\]

This generalizes earlier LTG proper-time-fraction results and makes the mass dependence explicit.

## 3. Light and massive limits

### Pure ideal massless radiation

For `m=0`,

\[
\frac{d\tau}{dt}=0,
\qquad
\chi_\tau=0,
\qquad
w=\frac13.
\]

### Cold nonrelativistic matter

For `E approximately mc^2`,

\[
\frac{d\tau}{dt}\approx1,
\qquad
\chi_\tau\approx1,
\qquad
w\approx0.
\]

### Relativistic massive matter

A massive species with `E >> mc^2` has

\[
\frac{d\tau}{dt}\ll1,
\]

so it becomes radiation-like even though its invariant mass is nonzero.

Thus it is not mass alone but the **energy-weighted timelike/proper-time fraction** that controls the trace channel.

## 4. Einstein trace equation

With metric signature `(-,+,+,+)`, Einstein's equation with cosmological constant is

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
\]

Taking the trace gives

\[
R=4\Lambda-\frac{8\pi G}{c^4}T.
\]

For a perfect fluid,

\[
T=-\varepsilon+3P.
\]

Therefore

\[
\boxed{
R-4\Lambda
=\frac{8\pi G}{c^4}(\varepsilon-3P).
}
\]

Combining with the kinetic identity yields the central bridge:

\[
\boxed{
R-4\Lambda
=
\frac{8\pi G}{c^4}\,
\varepsilon\,\chi_\tau
}
\]

or explicitly

\[
\boxed{
R-4\Lambda
=
\frac{8\pi G}{c^4}\,
\varepsilon
\left\langle
\left(\frac{d\tau}{dt}\right)^2
\right\rangle_E.
}
\]

## 5. Interpretation

This is the closest exact relation found so far to the original statement that a transition from light-like behavior to massive proper-time-bearing behavior changes geometry.

The precise standard-physics statement is:

> the Ricci scalar above its cosmological-constant contribution measures the energy density multiplied by the energy-weighted proper-time fraction of an isotropic on-shell ensemble.

Thus:

- pure ideal radiation has `chi_tau=0` and does not source the **trace** Ricci scalar above `4 Lambda`;
- timelike/massive content has `chi_tau>0` and activates that scalar-curvature channel.

## 6. Critical caveat: zero Ricci scalar is not zero geometry

For `Lambda=0`, ideal radiation gives

\[
R=0.
\]

But this does **not** mean spacetime is flat or that geometry is absent.

Radiation still has a nonzero stress tensor, can produce Ricci curvature components, and gravitates. Vacuum spacetimes can also have nonzero Weyl curvature and gravitational waves while `T_{mu nu}=0`.

Therefore the supported statement is not

\[
\text{mass creates geometry}.
\]

It is

\[
\boxed{
\text{timelike/proper-time content activates a particular curvature-trace channel.}
}
\]

## 7. FLRW expansion form

For an FLRW metric with scale factor `a(t)`,

\[
R
=\frac{6}{c^2}
\left(
\dot H+2H^2+\frac{k c^2}{a^2}
\right),
\qquad
H=\frac{\dot a}{a}.
\]

Therefore

\[
\boxed{
\frac{6}{c^2}
\left(
\dot H+2H^2+\frac{k c^2}{a^2}
\right)
-4\Lambda
=
\frac{8\pi G}{c^4}\varepsilon\chi_\tau.
}
\]

For the spatially flat, zero-Lambda case,

\[
\boxed{
\dot H+2H^2
=\frac{4\pi G}{3c^2}\varepsilon\chi_\tau.
}
\]

This is an explicit relation between the proper-time fraction of matter and the geometry of cosmological expansion.

Again, it is not independent of the Einstein/Friedmann equations; it is a reformulation of them.

## 8. Relation to the time-light dual-norm branch

EXP-032 established

\[
\frac{d\tau}{dt}=\frac{mc^2}{E}.
\]

EXP-033 now inserts the square of that quantity into the Einstein trace equation:

\[
\boxed{
\text{mass shell}
\to
\text{proper-time fraction}
\to
\text{stress-energy trace}
\to
\text{Ricci scalar}.
}
\]

This gives the strongest four-way closure currently available:

\[
\boxed{
\text{light/null}
\leftrightarrow
\chi_\tau=0
\leftrightarrow
T=0
\leftrightarrow
R-4\Lambda=0
}
\]

for an ideal isotropic radiation fluid, while

\[
\boxed{
\text{timelike/massive fraction}>0
\leftrightarrow
\chi_\tau>0
\leftrightarrow
-T>0
\leftrightarrow
R-4\Lambda>0
}
\]

for ordinary positive-energy matter with `0 <= w < 1/3`.

## 9. Status

### Confirmed

The bridge identity is exact under the stated kinetic/isotropy assumptions and follows from standard relativistic kinetic theory plus Einstein's equation.

### Not confirmed

It does not prove that light literally converts into time, that mass creates spacetime, or that creation of mass necessarily causes spatial expansion.

### Novelty classification

**Strong unifying identity / reinterpretation; not new physics by itself.**

A genuinely new LTG theorem would require an additional relation that is not algebraically implied by the mass shell, kinetic stress tensor, and Einstein equations.

## 10. Next test

Use an explicit null-to-massive pair-production process and compute both sides dynamically:

1. the generated massive-particle distribution and `chi_tau(t)`;
2. the corresponding `T(t)`;
3. the local/FLRW curvature response `R(t)`;
4. whether any residual relation survives after subtracting the standard Einstein prediction.

If the residual is identically zero, the present branch is a compact reformulation of standard GR+QFT. If a consistent nonzero residual is required by an independently motivated LTG postulate, that would define the first genuinely new dynamical content.
