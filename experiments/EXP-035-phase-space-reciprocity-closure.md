# EXP-035 — Phase-space reciprocity closure and no-go

## Objective

Test whether the tangent/cotangent duality found in EXP-032 can be promoted to a genuinely new local phase-space geometry without adding arbitrary structure.

The key question is whether treating spacetime displacement and four-momentum symmetrically produces a new invariant relation, or whether it closes on ordinary Hamiltonian/symplectic mechanics and known Born-reciprocal constructions.

## 1. Canonical phase-space structure

For spacetime `M`, one-particle phase space is the cotangent bundle

\[
T^*M.
\]

It carries the canonical one-form

\[
\theta=p_\mu dx^\mu
\]

and symplectic two-form

\[
\omega=d\theta=dp_\mu\wedge dx^\mu.
\]

The free relativistic mass-shell Hamiltonian constraint may be written

\[
\mathcal H
=\frac12\left(g^{\mu\nu}p_\mu p_\nu+m^2c^2\right)=0.
\]

Thus the action pairing already found by LTG,

\[
p_\mu dx^\mu=-mc^2d\tau,
\]

is precisely the canonical phase-space one-form evaluated on the free on-shell trajectory.

## 2. Local invariant algebra

Let

\[
X^\mu\equiv dx^\mu,
\qquad P_\mu\equiv p_\mu.
\]

Using only the metric and inverse metric, the elementary quadratic scalar invariants are

\[
A=g_{\mu\nu}X^\mu X^\nu,
\]

\[
B=g^{\mu\nu}P_\mu P_\nu,
\]

and

\[
C=P_\mu X^\mu.
\]

Any local quadratic scalar constructed only from `{g,X,P}` is a linear combination of these three after inserting whatever dimensional conversion constants are required.

For a free on-shell massive trajectory,

\[
A=-c^2d\tau^2,
\qquad
B=-m^2c^2,
\qquad
C=-mc^2d\tau,
\]

hence

\[
\boxed{C^2=AB.}
\]

So the invariant algebra is already saturated by ordinary relativistic mechanics.

## 3. Why a reciprocal `x <-> p` metric requires new scales

Coordinate displacement has dimensions of length, while momentum has dimensions of momentum. To add their norms in one phase-space line element one must introduce at least one conversion scale.

For example, introduce a length `L_*` and momentum `P_*` and define normalized variables

\[
\hat X^\mu=X^\mu/L_*,
\qquad
\hat P_\mu=P_\mu/P_*.
\]

A reciprocal quadratic form can then be written schematically as

\[
\boxed{
 d\Sigma^2
 =g_{\mu\nu}d\hat X^\mu d\hat X^\nu
 +g^{\mu\nu}D\hat P_\mu D\hat P_\nu
}
\]

or with more general cross terms involving the symplectic structure.

But `L_*` and `P_*` are additional physical data. Choosing

\[
L_*P_*\sim\hbar
\]

is natural quantum-mechanically, but it is still an extra principle, not a consequence of the LTG identities.

## 4. Reciprocity is known prior art

The proposal to treat coordinates and momenta on a more symmetric footing is the content of Born reciprocity and modern Born-geometry / phase-space approaches.

Therefore the statement

> `x` and `p` should enter a deeper geometry symmetrically

is not by itself a novel LTG postulate.

Similarly, frameworks with curved momentum space and relative locality already explore nontrivial geometry in the momentum sector and its coupling to spacetime geometry.

## 5. Adding momentum differentials changes the physical question

The original LTG duality used `p_mu` itself. A genuine phase-space metric normally contains `Dp_mu` along a trajectory.

For a forced particle,

\[
Dp_\mu\neq0.
\]

Hence a reciprocal line element generates corrections depending on force/acceleration rather than only on mass and proper time.

Such constructions are closely related to phase-space/maximal-acceleration models. They can be physically distinct, but the novelty then comes from the new reciprocal scale and acceleration dependence, not from the already-established LTG identity.

## 6. Algebraic no-go at lowest local order

With no extra field, no preferred vector, no nonlocal data, and no new conversion scale, the local quadratic phase-space information carried by `{g,X,P}` closes on

\[
\boxed{A,\;B,\;C}
\]

with the free on-shell saturation relation

\[
\boxed{C^2=AB.}
\]

Therefore there is no additional independent local quadratic invariant that can encode a new light-time-mass law.

### EXP-035A

The tangent/cotangent pairing found by LTG is naturally interpreted as canonical cotangent-bundle geometry.

### EXP-035B

Promoting that pairing to an explicit coordinate-momentum reciprocity requires new scale/metric structure and enters known Born-reciprocity/Born-geometry territory.

### EXP-035C

No unique new LTG prediction is produced at this level.

## 7. New clue: scale rather than mass alone

The failure of a purely phase-space local extension suggests returning to what physically distinguishes the massless and massive sectors.

A nonzero rest mass introduces an intrinsic Compton scale

\[
\lambda_C=\frac{\hbar}{mc},
\qquad
\tau_C=\frac{\hbar}{mc^2}.
\]

This creates an intrinsic length/time scale absent from ideal classical massless propagation.

The stress-energy trace is also closely connected to scale/conformal symmetry: classically conformal massless systems have vanishing trace, while explicit mass terms break scale invariance and generally generate a trace.

This suggests the next hypothesis refinement:

> the deeper contrast may be not `light versus time`, and not even simply `massless versus massive`, but `scale-free/null-like sector versus scale-bearing/timelike sector`.

Quantum trace anomalies provide an immediate falsification test because they can create a nonzero trace even in a theory with no explicit particle mass.

This becomes EXP-036.
