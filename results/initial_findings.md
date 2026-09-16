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

**Standard GR, but the strongest 4D covariant bridge found so far for the original LTG intuition.**

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

## Finding F-007 — 4D-only novelty boundary

The following chain is established without new physics:

\[
\text{null/timelike mass shell}
\longrightarrow
\text{trace-free/traceful stress energy}
\longrightarrow
\text{different scalar curvature and FRW pressure response}.
\]

A genuinely new 4D LTG theory must add a covariantly derived residual beyond this chain and not merely reproduce rapidity, field-dependent mass, ordinary scalar-tensor dynamics, `f(R,T)` gravity, or a conventional fluid.

### Status

**4D novelty route remains open but strongly constrained.**

## Finding F-008 — A 5D null lift gives an exact geometrical time/mass correspondence

For a product metric with one spacelike hidden coordinate `psi`,

\[
dS_5^2=ds_4^2+d\psi^2,
\]

a 5D null trajectory obeys

\[
dS_5^2=0.
\]

If its 4D projection is timelike,

\[
ds_4^2=-c^2d\tau^2,
\]

then

\[
\boxed{c\,d\tau=|d\psi|.}
\]

The 5D null momentum condition similarly gives

\[
\boxed{mc=|p_\psi|.}
\]

Thus 4D proper-time displacement and rest mass can be interpreted as hidden-coordinate displacement and momentum in a higher-dimensional null geometry.

### Status

**Exact but known Kaluza-Klein/null-lift structure.**

It is the closest geometrical realization found so far of the LTG core intuition.

## Finding F-009 — 5D vacuum dynamics can correlate visible expansion, internal contraction, and an effective mass scale

For the 5D vacuum Kasner ansatz

\[
dS_5^2=-c^2dt^2+a(t)^2d\mathbf{x}^2+b(t)^2d\psi^2,
\]

with

\[
a\propto t^p,\qquad b\propto t^q,
\]

the nontrivial branch of

\[
3p+q=1,\qquad3p^2+q^2=1
\]

is

\[
\boxed{p=1/2,\qquad q=-1/2.}
\]

Therefore

\[
\boxed{a\propto t^{1/2},\qquad b\propto t^{-1/2},\qquad ab=\text{const}.}
\]

For a 5D null mode with conserved hidden momentum,

\[
m_{eff}=\frac{|p_\psi|}{bc},
\]

so on this branch

\[
\boxed{m_{eff}\propto b^{-1}\propto a.}
\]

Visible space expands while the internal direction contracts and the KK mass scale grows.

### Status

**Coherent known higher-dimensional realization; not novel.**

The relation is potentially useful but a literal late-time application to observed particle masses would require careful phenomenological testing and likely stabilization of the internal dimension.

## Finding F-010 — Massive 4D quantum phase is hidden-direction translation phase

Combining

\[
p_\psi=mc
\]

with

\[
d\psi=c\,d\tau
\]

gives

\[
\boxed{p_\psi d\psi=mc^2d\tau.}
\]

Hence the proper-time phase

\[
\frac{mc^2\tau}{\hbar}
\]

is identical, in the minimal null lift, to the hidden spatial plane-wave phase

\[
\frac{p_\psi\psi}{\hbar}.
\]

Moreover, a 5D massless scalar field

\[
\Box_5\Psi=0
\]

with mode

\[
\Psi(x,\psi)=\phi(x)e^{ik_\psi\psi}
\]

reduces to

\[
\left(\Box_4-k_\psi^2\right)\phi=0,
\]

which is the 4D massive Klein-Gordon equation when

\[
k_\psi=mc/\hbar.
\]

### Status

**Exact standard dimensional reduction, now verified at both classical and field levels.**

## Finding F-011 — Revised strongest LTG formulation

The original statement

> matter converts light into time and expands space

is too literal and conflicts with how standard QFT describes particle conversion.

The strongest mathematically coherent reformulation found so far is:

> 4D null and timelike behavior can be different projections or momentum sectors of a deeper null geometry; 4D rest mass and proper-time phase can emerge from hidden-direction momentum and phase, while higher-dimensional geometry can correlate visible expansion with internal evolution.

Every component of this formulation has known precedents in Kaluza-Klein, null-lift, and dynamical-compactification physics.

### Status

**Promising unifying interpretation; no isolated new invariant yet.**

The next research gate is to identify whether LTG supplies any invariant relation or dynamical coupling not equivalent to established higher-dimensional dimensional reduction, radion/scalar-tensor dynamics, or induced-matter constructions.
