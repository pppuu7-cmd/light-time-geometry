# EXP-022 — Mass–phase–curvature coupling test

## Objective

Test the most natural local 4D attempt to extend LTG after the prior-art boundary:

> Can rest mass / proper-time phase be generated or modified directly by 4D curvature in a way that is not already standard curved-spacetime QFT and that preserves the existence of massive particles in the flat-space limit?

This experiment is intentionally adversarial.

## 1. Standard curved-spacetime scalar equation

A scalar field in curved spacetime may obey

\[
\boxed{
\left(\Box
-\frac{m^2c^2}{\hbar^2}
-\xi R\right)\Phi=0,
}
\]

up to metric/sign conventions.

The dimensionless parameter `xi` is the standard nonminimal curvature coupling. Thus the obvious local operator

\[
R\Phi^2
\]

is established curved-spacetime QFT, not an LTG-specific interaction.

## 2. WKB / Hamilton–Jacobi limit

Write

\[
\Phi=A\exp(iS/\hbar).
\]

Substitution gives at leading eikonal order

\[
\boxed{
g^{\mu\nu}\partial_\mu S\partial_\nu S
+m^2c^2=0.
}
\]

The curvature term enters multiplied by `hbar^2` after the field equation is written in action units:

\[
\hbar^2\Box\Phi
-m^2c^2\Phi
-\xi\hbar^2R\Phi=0.
\]

Therefore `xi R` is a subleading quantum/field-curvature contribution in the ordinary short-wavelength WKB expansion; it does not replace the leading classical mass shell.

### Result 022-A

**The most obvious curvature correction is already standard and does not produce a new leading light↔mass transition law.**

## 3. Attempt 1 — mass entirely from Ricci scalar

The dimensional relation

\[
\frac{m^2c^2}{\hbar^2}
\stackrel{?}{=}\xi R
\]

would give

\[
\boxed{
m_{\rm eff}
=\frac{\hbar}{c}\sqrt{\xi R}.}
\]

It is covariant and dimensionally consistent where the right-hand side is nonnegative.

But it fails the most basic flat-space limit:

\[
R\rightarrow0
\Rightarrow
m_{\rm eff}\rightarrow0.
\]

Ordinary massive particles continue to possess rest mass in regions arbitrarily close to Minkowski spacetime.

More sharply, the exterior Schwarzschild spacetime is Ricci-flat:

\[
R=0
\]

outside the gravitating matter, while an electron/proton there remains massive.

### Result 022-B

**Universal rest mass cannot be identified with local Ricci scalar curvature.**

## 4. Attempt 2 — mass from a generic local curvature invariant

To obtain inverse-length-squared dimensions one can form, for example,

\[
\mathcal K_2
=R,
\]

\[
\mathcal K_2
=\sqrt{R_{\mu\nu}R^{\mu\nu}},
\]

or

\[
\mathcal K_2
=\sqrt{C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}}.
\]

A general curvature-generated mass ansatz would look like

\[
\boxed{
\frac{m^2c^2}{\hbar^2}
=F(\mathcal K_2,\ldots).
}
\]

If `F` vanishes with curvature, the same flat-space problem returns.

If `F` contains a nonzero constant term,

\[
F=\mu_0^2+\delta F(\text{curvature}),
\]

then the constant `mu_0` already supplies the rest mass and the curvature piece is merely a standard environment-dependent mass correction.

### Result 022-C

**Curvature can correct a pre-existing mass, but local curvature alone cannot generically explain stable nonzero rest mass while recovering Minkowski spacetime.**

## 5. Attempt 3 — use Weyl curvature in vacuum

The Weyl tensor remains nonzero in Ricci-flat regions such as Schwarzschild, so one might try

\[
m^2\propto \sqrt{C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}}.
\]

However the Weyl invariant decays with distance from the source and vanishes in exact Minkowski spacetime.

This would make particle rest masses environment dependent and tend toward zero as the local tidal field vanishes.

Such a universal relation is incompatible with the observed use of stable atomic/particle mass scales across weakly curved environments unless its coefficient is so small that it becomes only a tiny correction.

### Result 022-D

**Weyl-generated universal mass also fails; a small Weyl-dependent correction is possible but belongs to ordinary EFT/modified-matter phenomenology.**

## 6. Attempt 4 — curvature locks the proper-time phase

A stronger LTG-style postulate might be

\[
\frac{mc^2}{\hbar}d\tau
\stackrel{?}{=}d\Phi_{\rm geom},
\]

where `Phi_geom` is built solely from 4D curvature/holonomy.

For a universal local law, this has an immediate problem:

- a freely propagating massive particle in Minkowski spacetime has
  \[
  mc^2d\tau/\hbar\neq0,
  \]
- while any local curvature scalar and ordinary Levi-Civita curvature holonomy can vanish.

Therefore no phase built **only** from local 4D curvature can universally equal the rest-mass phase.

One can add a flat-space term, but then the mass phase is already present independently and curvature supplies only a correction.

### Result 022-E

**A pure curvature origin of the massive proper-time phase is ruled out by the flat-space massive-particle limit.**

## 7. Attempt 5 — topological curvature integral

Four-dimensional curvature admits topological integrals such as Euler/Gauss–Bonnet and Pontryagin numbers on suitable compact manifolds/boundary conditions.

These are dimensionless global integers, making them superficially attractive candidates for phase quantization.

But they characterize the topology of a spacetime region/bundle, not the species-dependent rest mass of an arbitrary particle worldline.

A relation of the form

\[
\frac1\hbar\oint mc^2d\tau
\stackrel{?}{=}2\pi\,\chi_{\rm Euler}
\]

would force unrelated particles/worldlines sharing the same background topology to satisfy the same phase condition unless additional non-geometric data were introduced.

That additional data would reintroduce precisely the representation/winding labels already encountered in KK/gauge theory.

### Result 022-F

**Known 4D topological curvature integers do not naturally replace the KK momentum/winding labels.**

## 8. General no-go under the tested assumptions

Assume:

1. mass is a local scalar function only of the 4D metric and finitely many curvature invariants;
2. the relation is universal for ordinary matter;
3. exact Minkowski spacetime is an allowed limit;
4. ordinary particles retain finite nonzero rest mass in that limit.

Then a curvature-only origin

\[
m=m[g_{\mu\nu},R_{\cdots},\nabla R_{\cdots},\ldots]
\]

must contain a nonzero curvature-independent constant/field expectation value.

Therefore curvature is not the sole origin of mass.

### F-022G

**Within local 4D metric-only theories, stable rest mass requires non-geometric input in the flat limit. Curvature may modulate mass but cannot universally generate it from zero.**

## 9. Consequence for LTG

This eliminates another tempting route:

\[
\boxed{
\text{4D curvature}\not\Rightarrow\text{universal rest mass/proper-time phase}
}
\]

by itself.

The higher-dimensional null-lift picture remains internally coherent because the nonzero mass survives flat 4D geometry through hidden momentum:

\[
R_{(4)}=0,
\qquad
p_\psi\neq0
\Rightarrow
m_{4D}\neq0.
\]

That is a genuine conceptual advantage of the KK/null-lift language, although it is standard higher-dimensional physics.

## 10. Next frontier

After EXP-020–022, the project has tested three broad novelty routes:

1. **local new operator:** reduces to known EFT classes;
2. **4D topological/holonomy origin:** reduces to known bundle/thermal/spin structures;
3. **local curvature-generated mass/phase:** either standard `xi R` coupling or fails the flat-space massive limit.

The remaining scientifically defensible options are now very narrow:

- formulate one new nonlocal/global constraint and confront causality/locality;
- identify an experimentally distinct consequence of the existing synthesis;
- or declare theoretical closure at this level and move to phenomenology/experimental discriminators.

The preferred next step is the third: search for an observable that would distinguish **hidden-momentum-generated mass** from ordinary Higgs/rest-mass physics rather than adding more formal structure.

## Literature anchors

- Nonminimal scalar-curvature interaction `xi R phi^2` is standard curved-spacetime QFT and appears broadly in scalar–tensor/inflation literature.
- Curvature-dependent effective masses are therefore not novel by themselves.
