# EXP-012 — Minimal covariant novelty search

## Objective

Search for the lowest-order generally covariant interaction that could couple hidden momentum/internal geometry to visible spacetime in a way that is not merely standard Kaluza–Klein, radion/scalar–tensor, Horndeski/DHOST, or preferred-vector EFT.

The goal is not to manufacture novelty. If the minimal operator basis is exhausted by known structures, record that as a no-go result at this order.

## 1. Symmetry assumptions

Start from a local 5D theory with metric `G_AB` and a matter field `Phi`, invariant under 5D diffeomorphisms.

The compactification background may later admit a spacelike Killing direction `K^A`, but a fundamental local action built only from `G_AB` and `Phi` cannot refer to a preferred coordinate `psi` before that background structure is specified.

This immediately creates a useful distinction:

- operators made only from `G_AB`, curvature, `Phi`, and covariant derivatives preserve full 5D covariance;
- operators that explicitly distinguish the compact direction require either a Killing/vector structure, a foliation scalar, boundary/orbifold data, or nonlocal/global information.

## 2. Two-derivative local basis

With only `G_AB` and an ordinary scalar, the local parity-even two-derivative building blocks are schematically

\[
\sqrt{-G},\qquad
\sqrt{-G}R_5,\qquad
\sqrt{-G}G^{AB}\nabla_A\Phi\nabla_B\Phi,
\]

plus scalar potentials/functions and nonminimal functions such as

\[
\sqrt{-G}F(\Phi)R_5.
\]

After dimensional reduction these generate ordinary Einstein/radion/scalar–tensor structures.

### Result 012-A

At two-derivative order, with no extra geometric field, there is no local scalar that can distinguish "hidden momentum" from any other component of the 5D gradient before a compactification direction is chosen.

Therefore the desired LTG-specific coupling cannot appear at this order without additional structure.

## 3. Curvature × hidden-gradient candidates

A tempting term is symbolically

\[
R_5\,(\partial_\psi\Phi)^2.
\]

Written this way it is not 5D covariant because `psi` is a coordinate label.

A covariant version needs a vector selecting the compact direction,

\[
R_5\,(K^A\nabla_A\Phi)^2.
\]

This adds a preferred geometric structure. If `K^A` is promoted to a dynamical normalized vector, the theory belongs to the broad vector–tensor / Einstein–aether EFT class. If `K^A` is treated as fixed background data, full dynamical 5D diffeomorphism symmetry has been reduced.

Generic curvature-derivative couplings can also generate higher-derivative equations; healthy combinations fall into already studied Horndeski/beyond-Horndeski/DHOST-type structures after reduction.

### Classification

**Known-equivalent / extra-structure required.**

No uniquely LTG operator survives here.

## 4. Ricci tensor projected onto the hidden direction

Candidates such as

\[
R_{AB}K^AK^B
\]

or

\[
R_{AB}K^A K^B\,(K\cdot\nabla\Phi)^2
\]

again require a preferred vector/Killing structure.

Once such a vector is dynamical, the allowed kinetic contractions of `nabla_A K_B` are precisely of the familiar vector–tensor/Eintein–aether type. Once it is nondynamical, covariance is only formal because a preferred background has been inserted by hand.

### Classification

**Known vector–tensor EFT or symmetry-breaking background.**

## 5. Radion–matter derivative couplings

After compactification, write the canonically normalized radion as `sigma`. Possible terms include

\[
(\nabla\sigma)^2|\phi_n|^2,
\qquad
\nabla_\mu\sigma\nabla^\mu\phi_n\,F(\phi_n),
\]

or matter coupling through a conformal/disformal effective metric,

\[
\tilde g_{\mu\nu}
=A(\sigma)^2g_{\mu\nu}
+B(\sigma)\nabla_\mu\sigma\nabla_\nu\sigma.
\]

These are standard scalar–tensor/multi-scalar/disformal interaction classes. More general higher-derivative matter couplings must satisfy degeneracy constraints to avoid an Ostrogradsky mode.

### Classification

**Known-equivalent.**

## 6. Coupling visible expansion to hidden momentum

One might try a term containing an expansion scalar,

\[
\Theta=\nabla_Au^A,
\]

combined with hidden momentum or an internal projector.

But `Theta` itself requires a timelike vector/foliation `u^A`. A scalar such as

\[
F(\sigma,K\cdot\nabla\Phi)\,\nabla_Au^A
\]

therefore introduces a preferred frame. Up to integrations by parts and field redefinitions, such constructions belong to preferred-foliation/vector–tensor EFT rather than defining a new LTG invariant.

### Classification

**Known preferred-frame EFT / redundant at simple linear order.**

## 7. Topological or quantization conditions

For a compact circle of coordinate period `2 pi R0`, single-valuedness gives

\[
\Phi(x,\psi+2\pi R_0)=\Phi(x,\psi),
\]

and hence

\[
p_\psi=\frac{n\hbar}{R_0},\qquad n\in\mathbb Z.
\]

This fixes hidden momentum without inserting a local operator, but it is exactly standard Kaluza–Klein momentum quantization.

Twists, Wilson lines, orbifolds, and Scherk–Schwarz-type boundary conditions enlarge the possibilities but remain established compactification mechanisms.

### Classification

**Known topology/compactification physics.**

## 8. Minimal-order no-go statement

Under the assumptions

1. locality;
2. full 5D diffeomorphism covariance;
3. metric plus ordinary matter fields only;
4. no preferred vector/foliation inserted by hand;
5. lowest derivative order;

there is no LTG-specific local operator that singles out hidden momentum and couples it directly to visible expansion while remaining outside standard dimensional reduction/scalar–tensor EFT.

Any such operator must do at least one of the following:

- introduce extra geometric structure;
- move to higher derivative EFT;
- use global/topological information;
- or impose a new constraint not derivable from the minimal local action.

## 9. Scientific status

### F-012A

**The minimal local operator route is exhausted at the tested order.**

### F-012B

**Adding a preferred direction explicitly does not by itself create new LTG physics; it maps to known vector–tensor/preferred-frame EFT.**

### F-012C

**The cleanest surviving direction is global/topological rather than another arbitrary local operator.**

This motivates EXP-013: search for a phase/topological invariant built from the already established relations

\[
m c=|p_\psi|/b,
\qquad
c\,d\tau=b|d\psi|.
\]

## Literature equivalence anchors

- Higher-dimensional reductions can generate Horndeski and beyond-Horndeski scalar–tensor structures: Jana, Dalang, Lombriser, *Horndeski theories and beyond from higher dimensions*, arXiv:2007.06907.
- Nonminimal derivative couplings to the Einstein tensor are standard Horndeski-sector operators.
- Preferred unit-vector gravitational EFT is the Einstein–aether/vector–tensor class.
- Compact-circle momentum quantization and KK towers are standard Kaluza–Klein physics.
