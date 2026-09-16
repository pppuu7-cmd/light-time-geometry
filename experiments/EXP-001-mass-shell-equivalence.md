# EXP-001 — Mass-shell decomposition versus standard SR

## Question

Does

\[
E^2=(pc)^2+(mc^2)^2
\]

support an invariant "light-time" degree of freedom beyond standard special relativity?

## Step 1 — Standard parameterization

For one-dimensional motion introduce rapidity `eta`:

\[
\beta \equiv v/c = \tanh\eta,
\]

\[
\gamma=\cosh\eta,
\qquad
\gamma\beta=\sinh\eta.
\]

The standard energy and momentum of a particle of invariant mass `m` are

\[
E=\gamma mc^2=mc^2\cosh\eta,
\]

\[
pc=\gamma mvc=mc^2\sinh\eta.
\]

Hence

\[
E^2-(pc)^2=m^2c^4,
\]

which is the Lorentzian hyperbola in energy-momentum space.

## Step 2 — Relation to the proposed bookkeeping split

Define

\[
Q_s=pc,\qquad Q_\tau=mc^2.
\]

Then algebraically

\[
E=\sqrt{Q_s^2+Q_\tau^2}.
\]

Substituting the rapidity parameterization gives

\[
Q_s=mc^2\sinh\eta,
\qquad
Q_\tau=mc^2,
\qquad
E=mc^2\cosh\eta.
\]

Therefore the pair `(Q_s,Q_tau)` does not supply two freely varying invariant components for a fixed particle. `Q_tau` is simply the invariant rest energy, while `Q_s` is ordinary momentum times `c`.

## Step 3 — Proper time

Standard SR gives

\[
\frac{d\tau}{dt}=\frac{1}{\gamma}=\operatorname{sech}\eta.
\]

Using `E=\gamma mc^2`,

\[
\frac{d\tau}{dt}=\frac{mc^2}{E}=\frac{Q_\tau}{E}.
\]

This is a genuine and useful identity:

\[
\boxed{\frac{d\tau}{dt}=\frac{Q_\tau}{E}}
\]

and, since `pc/E=v/c`,

\[
\boxed{\frac{pc}{E}=\frac{v}{c}}.
\]

Thus the normalized algebraic pair obeys

\[
\left(\frac{pc}{E}\right)^2+
\left(\frac{mc^2}{E}\right)^2=1,
\]

or equivalently

\[
\boxed{
\left(\frac{v}{c}\right)^2+
\left(\frac{d\tau}{dt}\right)^2=1
}.
\]

## Interpretation test

This equation looks exactly like a unit-circle decomposition between a normalized spatial velocity and a normalized proper-time rate. However it follows algebraically from standard SR:

\[
\frac{d\tau}{dt}=\sqrt{1-v^2/c^2}.
\]

Therefore, by itself, it is **not new physics**.

It does provide a precise mathematical version of the original intuition that spatial propagation and proper-time accumulation behave like complementary projections when parameterized by coordinate time.

## Important dimensional form

Multiplying by `c^2` gives

\[
\boxed{
v^2+c^2\left(\frac{d\tau}{dt}\right)^2=c^2
}.
\]

This can be read cautiously as a constant-norm decomposition in the chosen inertial frame. It must not yet be described as an invariant "speed through spacetime" because that popular phrase can be misleading: `dt` is frame dependent, while four-velocity has Lorentzian norm `c`.

## Massless limit

For `m -> 0` on a null trajectory with finite `E`,

\[
\frac{mc^2}{E}\to0,
\qquad
\frac{pc}{E}\to1,
\]

so

\[
\frac{d\tau}{dt}\to0,
\qquad
v\to c.
\]

This reproduces the null limit but does not derive mass generation or a null-to-timelike transition.

## Result

**EXP-001A result:** the simplest two-component "light/time scale" is exactly reducible to standard SR kinematics.

This is a useful negative result. The identity

\[
(v/c)^2+(d\tau/dt)^2=1
\]

captures the intuition cleanly, but it introduces no new degree of freedom.

## Next falsification target

To obtain potentially new content, LTG must add something that standard rapidity does not contain. Candidate directions:

1. Promote the mixing between null and timelike sectors to a **dynamical field** rather than a kinematic parameter.
2. Identify a scalar or tensor order parameter that vanishes for null propagation and is nonzero for timelike matter.
3. Test whether such a field can couple covariantly to stress-energy and geometry without violating
   \(\nabla_\mu T^{\mu\nu}=0\).
4. Determine whether known mass-generation physics (especially the Higgs mechanism and interacting QFT) already exhausts the proposed transition.

The next experiment should therefore examine whether a null-to-timelike transition can be defined covariantly at all, and whether known particle interactions already provide the complete explanation.
