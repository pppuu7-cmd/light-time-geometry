# EXP-004 — Can 4D mass/proper time be a projection of higher-dimensional null motion?

## Motivation

EXP-001 found that the simple 4D "space versus proper-time" circle is only standard SR. EXP-002 found that a field-dependent mass can change the causal class, but that construction sits inside known mass-generation physics.

A different possibility is geometrical rather than field-theoretic:

> What if both the 4D null and 4D timelike sectors are projections of a single higher-dimensional **null** geometry?

This idea is closely related to Kaluza-Klein/null-lift constructions and is therefore not new by itself. It is nevertheless unusually close to the original LTG intuition and gives a precise equation connecting proper time to an additional geometric direction.

## Minimal 5D product geometry

Take a five-dimensional line element

\[
dS_5^2=g_{\mu\nu}dx^\mu dx^\nu+dy^2,
\]

where `y` is a spacelike extra coordinate and the four-dimensional metric has signature `(-,+,+,+)`.

Assume the fundamental trajectory is null in 5D:

\[
dS_5^2=0.
\]

If its 4D projection is timelike, define ordinary 4D proper time by

\[
g_{\mu\nu}dx^\mu dx^\nu=-c^2d\tau^2.
\]

Substitution into the 5D null condition gives

\[
-c^2d\tau^2+dy^2=0,
\]

hence

\[
\boxed{c\,d\tau=|dy|.}
\]

This is an exact result for the minimal product metric.

### Interpretation

- If `dy=0`, the 4D projection is null and `d tau=0`.
- If `dy != 0`, the 4D projection is timelike and `d tau>0`.

Thus one higher-dimensional null trajectory can project either to lightlike or massive/timelike 4D behavior depending on whether it carries motion in the extra direction.

This is substantially closer to the original "light/time are two sides of one scale" idea than the EXP-001 decomposition: **4D proper-time distance is literally equal to hidden spatial distance in this simple lift.**

## Momentum-space version

Let the 5D momentum be

\[
P_A=(p_\mu,p_y).
\]

For a 5D massless mode,

\[
P_AP^A=0.
\]

With the product metric,

\[
p_\mu p^\mu+p_y^2=0.
\]

But the 4D massive mass shell is

\[
p_\mu p^\mu=-m^2c^2.
\]

Therefore

\[
\boxed{m=\frac{|p_y|}{c}.}
\]

So in the reduced 4D description, rest mass is the magnitude of momentum in the extra direction.

The two central relations are therefore

\[
\boxed{c\,d\tau=|dy|},
\qquad
\boxed{mc=|p_y|}.
\]

They form a position/momentum pair:

\[
\text{4D proper time}\leftrightarrow\text{extra-dimensional displacement},
\]

\[
\text{4D rest mass}\leftrightarrow\text{extra-dimensional momentum}.
\]

## Compact extra dimension

If `y` is periodic with radius `R_y`, quantum momentum is quantized schematically as

\[
p_y=\frac{n\hbar}{R_y}.
\]

Then the 4D observer sees a Kaluza-Klein mass tower

\[
\boxed{m_n=\frac{|n|\hbar}{R_y c}.}
\]

The `n=0` mode is massless in 4D; nonzero modes are massive.

This is a known Kaluza-Klein mechanism, not an LTG prediction.

## Generalized metric coefficient

For

\[
dS_5^2=g_{\mu\nu}dx^\mu dx^\nu+\Phi(x,y)^2dy^2,
\]

a 5D null trajectory with a timelike 4D projection obeys

\[
\boxed{c\,d\tau=\Phi|dy|.}
\]

If `Phi` or the compactification scale varies, the effective 4D relation between hidden motion, proper time, and mass can vary as well. This connects naturally to known Kaluza-Klein scalar/radion physics.

## Critical tautology test

There is an important danger.

Given **any** 4D timelike worldline, one can define an auxiliary coordinate by

\[
y\equiv c\tau.
\]

Then the lifted 5D curve is automatically null in the product metric. If this is all the model does, the 5D construction is only an embedding trick and contains no new physics.

Therefore a physical LTG null-lift model must satisfy at least one of the following:

1. `y` has independent dynamics determined by a higher-dimensional field equation;
2. its topology/compactification predicts a nontrivial mass spectrum;
3. motion in `y` predicts an observable coupling or correction;
4. the 5D metric dynamics predicts 4D spacetime evolution rather than merely reproducing a chosen 4D trajectory.

## Relation to known work

Higher-dimensional Kaluza-Klein literature explicitly contains the idea that a massless/null trajectory in 5D with momentum in a spacelike extra dimension can appear massive/timelike in 4D. Null-lift and Eisenhart-Duval constructions similarly embed lower-dimensional massive dynamics into higher-dimensional null geometry.

Therefore EXP-004 does **not** establish novelty.

## EXP-004 result

### Strong geometric identity

The minimal 5D null lift gives

\[
\boxed{dS_5^2=0
\quad\Rightarrow\quad
c\,d\tau=|dy|}
\]

and

\[
\boxed{P_5^2=0
\quad\Rightarrow\quad
mc=|p_y|.}
\]

This is the clearest mathematical realization found so far of a common structure underlying the 4D null and timelike sectors.

### Novelty classification

**KNOWN GEOMETRIC STRUCTURE / PROMISING LTG REFORMULATION.**

The result is known in higher-dimensional/null-lift physics, but it suggests a sharper LTG research question:

> Can the same higher-dimensional dynamics that makes hidden null motion appear as 4D mass/proper time also force a correlated evolution of the observable 3D scale factor?

That is no longer a purely kinematic question and leads directly to dynamical compactification cosmology.

## Next experiment

EXP-005 should study a 5D cosmological metric with two scale factors,

\[
dS_5^2=-c^2dt^2+a(t)^2d\mathbf{x}^2+b(t)^2dy^2,
\]

and ask whether the 5D Einstein equations produce a robust relation in which growth of observable space `a(t)` is correlated with evolution of the hidden direction `b(t)` that controls the null-lift proper-time relation.

## Nearby literature

- J. Ponce de Leon, *Mass and Charge in Brane-World and Non-Compact Kaluza-Klein Theories in 5 Dim*, arXiv:gr-qc/0207108.
- M. Cariglia, *Null lifts and projective dynamics*, arXiv:1506.00714.
- Kaluza-Klein literature on 5D null geodesics and 4D massive trajectories.
