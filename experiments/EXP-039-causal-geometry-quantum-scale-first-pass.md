# EXP-039 — Can causal geometry set the quantum scale? First pass

## Objective

Test whether spacetime geometry can determine or constrain the invariant scale that later appears as particle mass / clock frequency, rather than merely responding to matter through Einstein's equation.

This is the first genuinely upstream question after EXP-034–038.

## 1. Immediate no-go for a universal local algebraic mass law

Suppose one proposes a universal relation of the form

\[
m^2c^2/\hbar^2=F[g],
\]

where `F[g]` is a local curvature scalar with dimensions of inverse length squared.

Simple examples include

\[
F\sim R,
\qquad
F\sim\sqrt{R_{\mu\nu}R^{\mu\nu}},
\qquad
F\sim\sqrt{R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}},
\]

or expressions containing derivatives of curvature.

A universal identification fails immediately because ordinary massive particles exist in local regions arbitrarily close to Minkowski spacetime, for which all curvature invariants can be made arbitrarily small and, in exact Minkowski spacetime, vanish.

Therefore

\[
\boxed{
\text{observed rest mass cannot be a universal instantaneous local function of curvature alone.}
}
\]

The same problem applies to proposals such as

\[
m\propto H,
\qquad
m\propto\kappa_{\rm horizon},
\]

because local particle masses do not disappear when cosmological expansion or horizon surface gravity becomes negligible.

## 2. Standard curvature-induced mass exists, but is conditional

For a scalar field, curved-spacetime QFT allows the standard nonminimal coupling

\[
\boxed{
\mathcal L\supset-\frac12\xi R\phi^2.
}
\]

The local effective mass can therefore contain

\[
\boxed{
m_{\rm eff}^2=m_0^2+\xi R+\cdots.
}
\]

This is a real geometric influence on a mass parameter, but it is not a universal origin of rest mass:

- it is field/model dependent;
- it vanishes with `R` if no other scale remains;
- it is standard QFT in curved spacetime;
- ordinary masses can persist after curvature becomes small.

Therefore `xi R phi^2` does not supply new LTG content.

## 3. Renormalization-scale identification is not automatically physics

In cosmological effective-potential calculations one often chooses a renormalization scale related to a physical background scale, schematically

\[
\mu_{\rm RG}\sim H,
\qquad
\mu_{\rm RG}^2\sim |R|,
\qquad
\mu_{\rm RG}\sim\phi,
\]

to minimize large logarithms.

But a choice of `mu_RG` is not by itself a physical law equating particle mass with curvature.

A genuine prediction must be invariant under a consistent change of renormalization scheme/scale after all orders or controlled truncation effects are accounted for.

Thus the ansatz

\[
\mu_{\rm RG}=\sqrt{|R|}
\]

cannot count as an LTG law unless it produces a scheme-independent observable relation.

## 4. Horizon scales

A horizon can define a physical temperature/frequency scale.

For example, de Sitter space supplies a scale of order

\[
\omega_H\sim H
\]

and temperature of order

\[
k_BT\sim\hbar H.
\]

Likewise black-hole surface gravity supplies a Hawking temperature scale.

These are genuine geometric scales, but they are thermal/kinematic properties of a state/background. They do not universally determine the rest masses of local particles.

Hence

\[
\boxed{
\text{geometry can create physical frequency/temperature scales without fixing all rest masses.}
}
\]

This is important conceptually but is standard horizon thermodynamics.

## 5. Gravity can participate in dimensional transmutation

Classically scale-invariant gravity+matter models can generate scales through quantum effects. Known examples include Coleman-Weinberg-type mechanisms with gravitational radiative corrections, higher-derivative scale-invariant gravity, and asymptotic-safety/RG scenarios where gravitational running generates crossover scales.

Therefore the broad idea

> geometry/gravity participates in generating the mass scale

already has substantial prior art.

A distinct LTG law would have to predict a relation more restrictive than the existence of gravitational dimensional transmutation.

## 6. The route that survives the flat-space no-go: trigger plus memory

There is one logically viable way geometry can be important without making today's mass proportional to today's curvature.

Geometry may act as a **trigger** for a phase transition:

\[
\text{large/early curvature}
\to
\text{effective potential changes}
\to
\text{symmetry breaking / condensate forms}
\to
\text{vacuum selects a nonzero scale}.
\]

Afterward the order parameter can remain in the broken phase even when the curvature becomes small:

\[
\boxed{
\text{geometric trigger}
\to
\text{vacuum memory}
\to
\text{persistent mass scale}.
}
\]

This evades the local relation `m^2 proportional R`.

However, curvature-induced symmetry breaking and gravitational Coleman-Weinberg mechanisms are already known examples of precisely this general strategy.

Thus this route is viable physics but not yet unique to LTG.

## 7. A concrete toy potential

Consider a scalar order parameter with

\[
V(\phi,R)
=\frac\lambda4\phi^4
+\frac12\xi R\phi^2
+V_{\rm q}(\phi),
\]

where `V_q` denotes quantum corrections capable of generating a nonzero scale.

The effective quadratic term is

\[
m_\phi^2(R)=\xi R+\cdots.
\]

As the cosmological background evolves, the sign/shape of the effective potential can change. A transition can create

\[
\langle\phi\rangle=v\neq0.
\]

Matter coupled through a Yukawa-like term then obtains

\[
m_f=yv.
\]

Once `v` is stabilized by the vacuum potential, `m_f` need not track the later value of `R`.

This gives an explicit standard mechanism with the desired logical structure:

\[
\boxed{
\text{geometry history}
\to
\text{scale selection}
\to
\text{persistent mass}
\to
\text{proper-time clock scale}.
}
\]

## 8. Relation to the original LTG intuition

The original intuition was close to

\[
\text{mass appears}
\to
\text{geometry/space appears}.
\]

The research now suggests a more defensible possible causal order in some models:

\[
\boxed{
\text{pre-existing causal geometry/background}
\to
\text{scale generation or symmetry breaking}
\to
\text{massive timelike excitations}
\to
\text{new stress trace}
\to
\text{backreaction on geometry}.
}
\]

This is a feedback loop, not one-way creation:

\[
\boxed{
\text{geometry}
\to
\text{mass/scale}
\to
T_{\mu\nu}
\to
\text{geometry}.
}
\]

Such feedback is physically coherent but is already natural in semiclassical gravity and curved-spacetime effective field theory.

## 9. Result

### EXP-039A

A universal instantaneous relation between observed particle mass and local curvature/expansion is ruled out by the flat-space limit.

### EXP-039B

Geometry can nevertheless influence or trigger scale generation through standard curvature couplings, horizon scales, quantum effective potentials, and gravitational RG dynamics.

### EXP-039C

The most viable version is a **trigger-and-memory** mechanism in which geometry affects an early phase transition and the resulting vacuum scale persists after curvature decreases.

### EXP-039D

No LTG-specific parameter-reducing relation has yet emerged; all mechanisms identified in this first pass have established precedents.

## 10. Sharp next test

To move beyond interpretation, LTG would need to explain why the generated clock/mass scale takes a particular value.

The next useful benchmark is therefore not another general argument but a minimal self-consistent feedback model:

1. a scale-free scalar sector;
2. curvature-sensitive effective potential;
3. dynamical FLRW geometry;
4. symmetry breaking generating `v` and `m`;
5. stress-energy backreaction on `H` and `R`;
6. numerical evolution through the transition;
7. search for a dimensionless attractor or invariant ratio such as

\[
\frac{m^2c^2/\hbar^2}{|R_*|},
\qquad
\frac{\omega_C}{H_*},
\]

where `*` denotes the transition epoch.

If such a ratio is fixed only by arbitrary couplings, this branch is standard curvature-induced symmetry breaking. If a coupling-independent attractor appears from an independently justified LTG condition, that would be genuinely new.
