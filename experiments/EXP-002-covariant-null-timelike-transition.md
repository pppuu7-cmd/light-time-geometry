# EXP-002 — Covariant null-to-timelike transition

## Question

Can a covariant variable dynamically interpolate between a null sector and a timelike sector, and does doing so produce physics beyond standard relativity/QFT?

## Conventions

Unless stated otherwise, use natural units `c = 1` and metric signature `(-,+,+,+)`.

---

## Candidate A — mass-shell scalar

The most direct Lorentz scalar is

\[
\mu^2 \equiv -p_\mu p^\mu.
\]

Then

\[
\mu^2=0
\]

for a massless on-shell mode, while

\[
\mu^2=m^2>0
\]

for a massive on-shell mode.

This perfectly distinguishes the two causal sectors, but it is exactly the ordinary mass-shell invariant. It therefore fails the LTG novelty criterion.

**Status:** covariant, exact, non-novel.

---

## Candidate B — proper-time rate

One may attempt to use `d tau / d lambda` as an order parameter, with `lambda` a worldline parameter. This is not satisfactory by itself because `lambda` is arbitrary. Under a worldline reparameterization the numerical rate changes.

Proper time is invariant along a timelike curve, but it degenerates on a null curve. Therefore proper time is a derived quantity in the timelike sector, not an obvious fundamental parameter that smoothly labels both sectors.

**Status:** physically meaningful in the timelike sector, but not a universal order parameter.

---

## Candidate C — dynamical effective mass with an einbein

A reparameterization-invariant worldline action that treats massive and massless limits uniformly is

\[
S_p=\int d\lambda\left[
 p_\mu \dot x^\mu
 -\frac{e}{2}\left(g^{\mu\nu}p_\mu p_\nu+M(\chi)^2\right)
\right],
\]

where `e(lambda)` is the worldline einbein and `M(chi)` is allowed to depend on a scalar field `chi(x)`.

Variation with respect to `e` gives the constraint

\[
g^{\mu\nu}p_\mu p_\nu+M(\chi)^2=0.
\]

Variation with respect to `p_mu` gives

\[
\dot x^\mu=e p^\mu.
\]

Combining them,

\[
g_{\mu\nu}\dot x^\mu\dot x^\nu=-e^2M(\chi)^2.
\]

Therefore:

- if `M(chi)=0`, the trajectory is null;
- if `M(chi) != 0`, the trajectory is timelike.

The same action is regular in the massless limit; no proper-time parameter is required to define the crossing.

For the timelike segment,

\[
d\tau^2=-g_{\mu\nu}dx^\mu dx^\nu,
\]

so the constraint implies

\[
\boxed{\frac{d\tau}{d\lambda}=e\,|M(\chi)|.}
\]

This is important for LTG interpretation: a nonzero effective mass and a nonzero proper-time increment arise together from the same constraint. However, `e` is an auxiliary gauge variable. This equation does **not** establish that mass literally creates time; it shows that proper time is derived from the timelike mass-shell condition.

### Making chi dynamical

Take, schematically,

\[
S_\chi=\int d^4x\sqrt{-g}\left[-\frac12(\nabla\chi)^2-V(\chi)\right]
\]

and let, for example,

\[
M(\chi)=y\chi.
\]

Then a region or phase with `chi=0` supports a null mass shell for that degree of freedom, while a region/phase with `chi != 0` supports a timelike one.

Because the full matter+field action is diffeomorphism invariant, the total stress-energy is covariantly conserved on shell. Energy-momentum transferred into the particle sector is balanced by the `chi` sector; the particle stress tensor need not be separately conserved when `M(chi)` varies.

### Novelty test

This construction works, but its structure is already familiar: field-dependent masses, Yukawa couplings, spontaneous symmetry breaking, and the Brout-Englert-Higgs mechanism all realize closely related ideas. The Standard Model Higgs background gives masses to fields that couple to it, while the photon remains massless.

Thus a scalar `chi` whose only role is to turn `M(chi)` on and off does not yet constitute new LTG physics.

**Status:** dynamically consistent toy transition; known structural class; not yet novel.

---

## QFT caveat — radiation becoming matter is normally an interaction vertex, not one worldline changing identity

Processes in which radiation produces massive particles are already described by interacting quantum field theory. At a vertex, total four-momentum is conserved, but a photon worldline is not normally interpreted as continuously becoming an electron worldline. The incoming and outgoing excitations are different field quanta.

Therefore the literal statement "a light trajectory turns into a matter trajectory" is too classical. A viable LTG theory must either:

1. be an effective semiclassical description of changing dispersion relations; or
2. provide a field-theoretic formulation in which null and timelike excitations are phases/modes of a deeper common field.

---

## Candidate D — stress-energy trace as a macroscopic null/timelike discriminator

A more interesting covariant bridge appears after coarse-graining.

For a perfect fluid,

\[
T\equiv T^\mu{}_{\mu}=-\varepsilon+3P.
\]

For ideal radiation,

\[
P=\varepsilon/3
\quad\Rightarrow\quad
T=0.
\]

For pressureless matter,

\[
P\simeq0
\quad\Rightarrow\quad
T\simeq-\varepsilon.
\]

In relativistic kinetic theory the stress tensor is built from momentum products `p^mu p^nu`. Contracting the integrand gives the mass-shell invariant `p^2`. Consequently, a classical on-shell massless population contributes zero to the trace, while massive modes generically generate a nonzero trace (subject to the state/pressure caveats below).

This gives the chain

\[
\boxed{
 p^2\;(\text{null/timelike})
 \;\longrightarrow\;
 T^\mu{}_{\mu}
}
\]

without introducing a new field.

### Direct bridge to geometry in GR

Einstein's equation is

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}.
\]

Taking the trace with the chosen signature gives

\[
\boxed{R=4\Lambda-8\pi G\,T.}
\]

Hence:

- ideal classical radiation: `T=0`, so `R=4 Lambda`;
- pressureless matter: `T=-epsilon`, so `R=4 Lambda + 8 pi G epsilon`.

Thus standard GR already contains a covariant sequence

\[
\boxed{
\text{null mass shell}
\to \text{trace-free stress-energy}
\to \text{no matter contribution to }R
}
\]

versus

\[
\boxed{
\text{timelike mass shell}
\to \text{traceful stress-energy}
\to \text{nonzero matter contribution to }R.
}
\]

This is the closest standard-physics analogue found so far to the original LTG intuition.

### Critical caveats

1. `T=0` does **not** mean radiation does not gravitate. Radiation contributes to the full tensor `T_{mu nu}` and curves spacetime even when its trace vanishes.
2. The trace is not a perfect microscopic "amount of proper time". A highly relativistic massive gas can have a small trace.
3. Quantum trace anomalies can make the renormalized trace nonzero even for classically conformal/massless fields.
4. Vacuum energy has a nonzero trace without representing ordinary massive particles.

Therefore `T` is a useful bridge, but not a universal LTG order parameter.

---

## EXP-002 result

### Result 1
A smooth covariant null/timelike interpolation is possible at the level of an einbein worldline with a field-dependent effective mass.

### Result 2
The identity

\[
\frac{d\tau}{d\lambda}=e|M(\chi)|
\]

shows a precise association between nonzero mass-shell scale and nonzero proper-time accumulation, but it is a consequence of standard reparameterization-invariant particle mechanics rather than evidence that mass creates time.

### Result 3
Promoting the mass scale to a scalar field reproduces a known class of mass-generation/variable-mass constructions. This route is therefore **dynamically viable but non-novel as stated**.

### Result 4
The stress-energy trace provides a second, macroscopic bridge from null/timelike character to spacetime geometry through the traced Einstein equation. This connection is standard GR but gives LTG a much sharper next falsification target.

## Classification

**EXP-002 status: INTERPRETIVE / KNOWN-STRUCTURE.**

No genuinely new degree of freedom has yet survived the equivalence test.

## Next question

Does conversion between trace-free radiation and traceful matter force, or even systematically favor, expansion of spatial volume in standard cosmology?

This is EXP-003.

## References / nearby established structures

- CERN, Brout-Englert-Higgs mechanism: https://home.cern/science/physics/origins-brout-englert-higgs-mechanism/
- CERN, Higgs overview: https://home.cern/science/physics/higgs-boson/
- Standard einbein/worldline formulations have a smooth massless limit; see e.g. discussions of the relativistic particle einbein action in the literature.
