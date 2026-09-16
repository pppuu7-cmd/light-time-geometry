# Initial Findings

## Finding F-001 — Complementarity identity is standard SR

From

\[
d\tau=dt\sqrt{1-v^2/c^2},
\]

we obtain

\[
\left(\frac{v}{c}\right)^2+\left(\frac{d\tau}{dt}\right)^2=1.
\]

Equivalent energy-momentum form:

\[
\left(\frac{pc}{E}\right)^2+\left(\frac{mc^2}{E}\right)^2=1.
\]

This provides a mathematically precise representation of the intuition that spatial motion and proper-time accumulation can appear as complementary normalized projections in a chosen inertial frame.

### Status

**Confirmed identity; not new physics.**

It is algebraically equivalent to standard special relativity and introduces no new invariant degree of freedom.

## Finding F-002 — The massless/timelike contrast is real but not yet a transition law

For timelike motion,

\[
d\tau>0,
\]

while for null motion,

\[
d\tau=0.
\]

The massless limit of the normalized decomposition approaches the null result smoothly. However, EXP-001 contained no equation describing a dynamical conversion of a null sector into a timelike sector.

### Status

**Established contrast.**

## Finding F-003 — A covariant transition can be written, but in a known structural class

Using the reparameterization-invariant worldline action

\[
S_p=\int d\lambda\left[
p_\mu\dot x^\mu-\frac e2\left(p^2+M(\chi)^2\right)
\right],
\]

the constraint is

\[
p^2+M(\chi)^2=0.
\]

Hence `M=0` gives a null trajectory while `M != 0` gives a timelike one. For the timelike segment,

\[
\frac{d\tau}{d\lambda}=e|M(\chi)|.
\]

This makes the association between nonzero effective mass and nonzero proper-time accumulation exact within the model.

However, promoting `M` to a scalar-field-dependent mass reproduces a known family of field-dependent-mass / symmetry-breaking constructions. The Brout-Englert-Higgs mechanism is the most important established nearby example.

### Status

**Dynamically viable, but non-novel as stated.**

## Finding F-004 — Proper time is derived, not a universal transition parameter

The einbein formulation remains well defined at `M=0`, while proper time degenerates there. This reverses the most naive LTG interpretation: proper time is not currently the fundamental variable spanning the null and timelike sectors. It emerges as a derived line element once the trajectory is timelike.

### Status

**Important constraint on future LTG models.**

A deeper model should not assume proper time itself as the parameter that exists before the null-to-timelike transition.

## Finding F-005 — Stress-energy trace is a covariant bridge from mass shell to scalar curvature

For a perfect fluid with metric signature `(-,+,+,+)`,

\[
T=T^\mu{}_{\mu}=-\varepsilon+3P.
\]

Ideal radiation satisfies `P=epsilon/3`, hence

\[
T=0.
\]

Pressureless matter satisfies `P approximately 0`, hence

\[
T\simeq-\varepsilon.
\]

This mirrors the microscopic mass-shell distinction because contraction of the kinetic-theory momentum product brings in `p^2`, which vanishes on a classical massless shell and is nonzero on a massive shell.

The traced Einstein equation is

\[
R=4\Lambda-8\pi G T
\]

in units `c=1` with the conventions used in EXP-002/003.

Thus trace-free radiation and traceful matter source the Ricci scalar differently even though both gravitate through the full stress tensor.

### Status

**Standard GR, but the strongest covariant bridge found so far for the original LTG intuition.**

## Finding F-006 — Radiation-to-matter conversion changes curvature and acceleration, not instantaneous H at fixed total density

For an FRW universe,

\[
H^2=\frac{8\pi G}{3}\rho+\frac{\Lambda}{3}-\frac{k}{a^2}.
\]

If radiation energy `delta rho` is converted into pressureless matter while total `rho` is continuous, then at the conversion instant

\[
\delta H^2=0.
\]

But pressure decreases by

\[
\delta P=-\frac13\delta\rho,
\]

and therefore

\[
\delta\left(\frac{\ddot a}{a}\right)
=\frac{4\pi G}{3}\delta\rho>0.
\]

The universe is therefore less strongly decelerated. With zero cosmological constant, both a pure radiation fluid and pure pressureless matter still decelerate.

At the same time, for a radiation+matter mixture,

\[
R=4\Lambda+8\pi G\rho_m,
\]

so radiation-to-matter conversion increases the Ricci scalar.

### Status

**Partial standard-physics echo of the original hypothesis; no extra expansion law found.**

## Finding F-007 — Current novelty boundary

The following chain is now established without new physics:

\[
\text{null/timelike mass shell}
\longrightarrow
\text{trace-free/traceful stress energy}
\longrightarrow
\text{different scalar curvature and FRW pressure response}.
\]

A genuinely new LTG theory must add a covariantly derived residual beyond this chain. It must not be merely:

- rapidity/proper-time reparameterization;
- a field-dependent mass already covered by ordinary QFT mechanisms;
- an ordinary scalar-tensor model;
- an `f(R,T)` re-labeling;
- a cosmological constant or conventional fluid component.

### Status

**Next source of possible novelty identified.**

The next experiment should search for a minimal covariant residual and attempt to prove either that it reduces to an established theory class or that it produces one distinct invariant prediction.
