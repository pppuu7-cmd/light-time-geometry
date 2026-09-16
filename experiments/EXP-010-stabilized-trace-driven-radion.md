# EXP-010 — Stabilized trace-driven radion test

## Objective

Determine whether any controlled relation between the massive/proper-time sector and cosmological expansion survives after the fifth dimension is stabilized strongly enough to avoid the large variation found in EXP-009.

## 1. Effective 4D description

A generic dimensional reduction with one dynamical compactification modulus can be represented in 4D Einstein frame by

\[
S=\int d^4x\sqrt{-g}\left[
\frac{M_P^2}{2}R
-\frac12(\partial\sigma)^2
-V(\sigma)
\right]
+S_m[A(\sigma)^2g_{\mu\nu},\Psi_m].
\]

Here `sigma` is a canonically normalized radion/modulus and `A(sigma)` represents its coupling to a matter sector.

Define

\[
\alpha(\sigma)\equiv\frac{d\ln A}{d\sigma}.
\]

For homogeneous cosmology, the radion equation has the schematic form

\[
\ddot\sigma+3H\dot\sigma+V_{,\sigma}
\simeq-\alpha(\sigma)T,
\]

up to the sign convention used for `T` and the scalar coupling.

The important invariant structural fact is that the **trace of the matter stress tensor sources the scalar**.

## 2. Radiation versus matter

For ideal radiation,

\[
T=-\rho+3P=0.
\]

For nonrelativistic matter,

\[
T\simeq-\rho_m\neq0.
\]

Therefore the simplest conformally coupled radion has the response

\[
\text{radiation}\quad\Rightarrow\quad T=0\quad\Rightarrow\quad\text{no direct trace source},
\]

while

\[
\text{massive matter}\quad\Rightarrow\quad T\neq0\quad\Rightarrow\quad\text{radion source}.
\]

This is a controlled version of the qualitative LTG idea that the massive/timelike sector couples to geometry differently from the null/radiative sector.

However, this mechanism is standard scalar–tensor/radion physics.

## 3. Stabilized limit

Assume a stable minimum at `sigma=0`:

\[
V(\sigma)\simeq\frac12M_\sigma^2\sigma^2,
\]

with

\[
M_\sigma^2>0.
\]

For a sufficiently heavy/adiabatic radion (`M_sigma` larger than the relevant cosmological variation scale), the field approximately follows the instantaneous source:

\[
M_\sigma^2\sigma\simeq-\alpha T.
\]

Hence

\[
\boxed{
\sigma\simeq-\frac{\alpha T}{M_\sigma^2}
}.
\]

For dust, `T approximately -rho_m`, so the displacement from the stabilized radius is proportional to the matter density rather than directly to the scale factor.

## 4. Residual mass variation

If a matter mass depends on the radion through

\[
m(\sigma)=A(\sigma)m_0,
\]

then

\[
\frac{d\ln m}{dt}=\alpha\dot\sigma.
\]

For small displacement,

\[
\frac{\delta m}{m}\simeq\alpha\sigma
\simeq-\frac{\alpha^2T}{M_\sigma^2}.
\]

For pressureless matter with `rho_m propto a^-3`, this gives schematically

\[
\boxed{
\frac{\delta m}{m}\propto\frac{\rho_m}{M_\sigma^2}
\propto a^{-3}
}
\]

for fixed coupling parameters.

Thus stabilization changes the strong vacuum result

\[
m\propto a
\]

into a small, trace-driven correction that decays as the matter density dilutes.

## 5. Interpretation

This result is important for LTG because it separates two ideas that had previously been mixed together:

1. **Unstabilized geometric conversion:** visible expansion is directly tied to contraction of the hidden dimension, giving large mass variation.
2. **Stabilized trace response:** massive matter perturbs a geometric modulus because `T != 0`, while ideal radiation does not directly source it through the trace.

The second mechanism is far more phenomenologically plausible, but it is also much more clearly part of standard scalar–tensor/radion physics.

## 6. Relation to proper time

The massive 4D sector still obeys

\[
d\tau>0,
\qquad
p^2=-m(\sigma)^2c^2,
\]

whereas the massless sector obeys

\[
d\tau=0,
\qquad
p^2=0.
\]

If the mass is generated from hidden momentum,

\[
m(\sigma)c\sim\frac{|p_\psi|}{b(\sigma)},
\]

then a radion displacement changes the effective timelike mass shell. In that precise sense, geometry controls the quantitative separation between the null and timelike sectors.

But proper time remains a derived quantity, not the fundamental scalar source.

## 7. Result

### F-010A

Stabilization removes the large universal relation `m propto a`.

### F-010B

A residual relation survives naturally through the stress-energy trace:

\[
\boxed{
T\neq0\ \Rightarrow\ \delta\sigma\neq0\ \Rightarrow\ \delta m\neq0
}
\]

while ideal radiation has `T=0` at the classical level.

### F-010C

Near a stable minimum, the residual effect is suppressed by the radion mass:

\[
\boxed{
\delta m/m\sim-\alpha^2T/M_\sigma^2
}.
\]

### F-010D

This provides a mathematically cleaner descendant of the original LTG intuition but remains known scalar–tensor/radion physics unless LTG supplies a new coupling law or invariant prediction.

## Next target

The next genuinely discriminating question is whether the three standard relations

\[
\text{null/timelike mass shell},\qquad
T^\mu{}_{\mu},\qquad
\text{radion response}
\]

can be derived from **one common invariant functional** rather than being connected phenomenologically after dimensional reduction.

If such a functional is just the ordinary higher-dimensional Einstein–Hilbert plus matter action, LTG remains a reinterpretation. If a minimal additional invariant is required and produces a distinct observable, that would be the first genuine novelty candidate.
