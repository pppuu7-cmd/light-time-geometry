# EXP-019 — Causal/topological phase-origin test

## Objective

Test whether the frame-robust LTG phase

\[
\Phi_{LTG}
=\frac1\hbar\int mc^2d\tau
=\frac1\hbar\int p_\psi d\psi
\]

and its compact-cycle integer can be derived from genuinely 4D causal/topological geometry rather than from assuming a compact `S1` fiber.

The first step is to restore the full Kaluza–Klein gauge connection and identify exactly what the integer `n` means.

## 1. Full KK metric with a gauge connection

Use the general circle-fiber form

\[
dS_5^2
=e^{2\alpha\varphi}g_{\mu\nu}dx^\mu dx^\nu
+e^{2\beta\varphi}
\left(d\psi+\kappa A_\mu dx^\mu\right)^2.
\]

The local fiber-coordinate transformation

\[
\psi\rightarrow\psi-\kappa\lambda(x)
\]

is accompanied by

\[
A_\mu\rightarrow A_\mu+\partial_\mu\lambda.
\]

Thus ordinary 4D `U(1)` gauge symmetry is the local freedom to choose a section of the compact circle bundle.

## 2. Hamilton–Jacobi phase decomposition

Take a 5D eikonal/action

\[
\mathcal S_5(x,\psi)
=\mathcal S_4(x)+p_\psi\psi.
\]

Under a fiber gauge transformation, invariance of the total phase requires

\[
\mathcal S_4
\rightarrow
\mathcal S_4+\kappa p_\psi\lambda.
\]

Therefore the gauge-invariant 4D kinetic momentum is

\[
\boxed{
\Pi_\mu
=\partial_\mu\mathcal S_4
-\kappa p_\psi A_\mu.
}
\]

Define

\[
\boxed{q\equiv\kappa p_\psi.}
\]

Then

\[
\Pi_\mu=\partial_\mu\mathcal S_4-qA_\mu,
\]

which is the standard charged-particle Hamilton–Jacobi combination.

Thus the same hidden momentum that generated effective 4D mass in the diagonal model also generates a 4D `U(1)` charge once the off-diagonal metric is restored.

## 3. 5D null shell → charged 4D mass shell

The inverse metric gives schematically

\[
0=G^{AB}\partial_A\mathcal S_5\partial_B\mathcal S_5
=e^{-2\alpha\varphi}
 g^{\mu\nu}\Pi_\mu\Pi_\nu
+e^{-2\beta\varphi}p_\psi^2.
\]

Therefore

\[
\boxed{
g^{\mu\nu}\Pi_\mu\Pi_\nu
=-e^{2(\alpha-\beta)\varphi}p_\psi^2.
}
\]

The 4D observer identifies an effective mass proportional to the same conserved hidden momentum:

\[
mc\propto
|p_\psi|e^{(\alpha-\beta)\varphi}.
\]

At the same time

\[
q=\kappa p_\psi.
\]

This mass/charge correlation is standard Kaluza–Klein physics and is one reason realistic models require additional structure beyond the most minimal historical ansatz.

## 4. Gauge-invariant phase one-form

The canonical 5D phase element can be written

\[
d\mathcal S_5
=\partial_\mu\mathcal S_4dx^\mu+p_\psi d\psi.
\]

Using

\[
\partial_\mu\mathcal S_4
=\Pi_\mu+qA_\mu
\]

and `q=kappa p_psi`, we get

\[
\boxed{
d\mathcal S_5
=\Pi_\mu dx^\mu
+p_\psi\left(d\psi+\kappa A_\mu dx^\mu\right).
}
\]

Both terms together are gauge invariant.

For a closed lifted loop `C`,

\[
\frac1\hbar\oint_C d\mathcal S_5
=\frac1\hbar\oint_C\Pi_\mu dx^\mu
+\frac{p_\psi}{\hbar}\oint_Cd\psi
+\frac{q}{\hbar}\oint_C A_\mu dx^\mu.
\]

If

\[
p_\psi=\frac{n\hbar}{R_0}
\]

and the fiber winds `w` times,

\[
\frac{p_\psi}{\hbar}\oint d\psi
=2\pi nw.
\]

Therefore

\[
\boxed{
\frac1\hbar\oint_C d\mathcal S_5
=
\frac1\hbar\oint_C\Pi_\mu dx^\mu
+2\pi nw
+\frac{q}{\hbar}\oint_C A.
}
\]

The last term is the ordinary 4D Wilson-loop/Aharonov–Bohm phase.

Under large changes of fiber section, winding and Wilson-line representatives can shift, but the full lifted holonomy is gauge invariant.

## 5. What is the integer `n`?

In this full bundle picture,

\[
\boxed{n=\text{KK momentum/charge representation number}.}
\]

It is not derived from 4D curvature. It exists because the fiber is compact and the wavefunction is single-valued around it.

Similarly,

\[
\boxed{w=\text{path winding number around the fiber}.}
\]

These are standard topological/representation data of a circle bundle.

A nontrivial circle bundle may also possess a first Chern number determined by the curvature `F=dA`. That topological integer characterizes the bundle/flux, but it is conceptually distinct from the KK momentum number `n` and path winding `w`.

No standard identity forces these integers to be equal.

## 6. 4D-only gauge holonomy test

A 4D compact `U(1)` connection can produce a phase

\[
\exp\left(\frac{iq}{\hbar}\oint A\right)
\]

and topological flux quantization can occur on nontrivial bundles.

However this does **not** derive the rest-mass proper-time phase

\[
\frac1\hbar\int mc^2d\tau
\]

from the 4D metric alone. One has introduced a separate compact gauge connection whose representation label supplies the integer.

### Result 019-A

**Gauge holonomy reproduces standard KK/U(1) bundle topology, not a new 4D causal origin of `n`.**

## 7. Pure gravitational holonomy test

The Levi-Civita/spin connection produces gravitational holonomy around closed curves. It acts on tangent vectors or spinor/internal indices.

For a scalar massive particle, there is no generic theorem that equates a Levi-Civita holonomy angle to

\[
mc^2\tau/\hbar.
\]

Spinors can acquire spin-connection phases/signs on nontrivial loops, but these encode spin structure and curvature transport, not universal rest-mass quantization.

### Result 019-B

**Ordinary 4D gravitational holonomy does not, by itself, derive the LTG mass–proper-time integer.**

## 8. Horizon/Euclidean periodicity test

Stationary horizons provide another tempting 4D circle: regularity of the Euclidean continuation fixes an imaginary-time period `beta`, related to surface gravity/Hawking temperature.

Thermal bosonic modes then have Matsubara frequencies

\[
\omega_n=\frac{2\pi n}{\beta},
\]

so

\[
\boxed{\hbar\omega_n\beta=2\pi n\hbar.}
\]

This is formally similar to

\[
mc^2\Delta\tau=2\pi n\hbar.
\]

But the meanings differ:

- `omega_n` is a Euclidean thermal frequency;
- `beta` is a thermal/Euclidean period tied to a particular horizon or temperature;
- neither quantity is generically the rest mass or Lorentzian proper time of a particle.

Identifying

\[
\hbar\omega_n=mc^2
\]

would be an additional model assumption, not a consequence of ordinary horizon regularity.

Furthermore generic 4D spacetimes have no universal Euclidean thermal circle.

### Result 019-C

**Horizon/Matsubara periodicity supplies an analogous phase quantization but does not provide a universal 4D derivation of the LTG mass phase.**

## 9. Current topological classification

The integers encountered so far belong to known structures:

| Integer | Origin | Status |
|---|---|---|
| `n` | representation/momentum on compact `S1` | standard KK |
| `w` | winding of a lifted path around the fiber | standard topology |
| Chern number | nontrivial `U(1)` bundle flux | standard gauge topology |
| Matsubara `n` | Euclidean thermal periodicity | standard thermal QFT |
| spin-structure sign/index | spin bundle topology | standard geometry/QFT |

No tested construction derives the KK mass integer solely from the 4D metric/causal structure.

## 10. Stronger interpretation of the LTG phase

With the KK connection restored, the project’s phase is part of a larger gauge-invariant object:

\[
\boxed{
\frac1\hbar\int d\mathcal S_5
=
\frac1\hbar\int \Pi_\mu dx^\mu
+
\frac1\hbar\int p_\psi(d\psi+\kappa A).
}
\]

Thus mass/proper-time phase and gauge holonomy are not unrelated additions; they can descend from the same higher-dimensional canonical one-form.

This is conceptually strong but standard Kaluza–Klein geometry.

## 11. Novelty status

### F-019A

**Restoring the KK gauge field identifies the hidden-momentum integer `n` with ordinary KK momentum/charge representation data.**

### F-019B

**The total phase decomposes into a 4D kinetic/action contribution, a fiber-winding integer, and an ordinary Wilson-loop phase.**

### F-019C

**Pure 4D gravitational holonomy does not generically quantize `mc^2 tau`.**

### F-019D

**Euclidean horizon periodicity produces a mathematically similar integer phase but quantizes thermal frequency, not rest mass.**

### F-019E

**No genuinely 4D causal origin for the LTG integer has survived this first topological test.**

## 12. Next frontier

At this point two scientifically honest possibilities remain:

1. **Interpretive closure:** LTG is a particularly compact reinterpretation of standard KK/null-lift physics, with no independent invariant yet found.
2. **Constraint-first extension:** propose one new, sharply defined relation tying the hidden phase integer to a 4D invariant, then try to falsify it against gauge invariance, locality, covariance, and observation.

Any constraint-first extension must not merely rename a Wilson loop, Chern class, Matsubara number, or KK charge.

## Literature anchors

- In Kaluza–Klein theory the fifth momentum is associated with 4D charge and the Hamilton–Jacobi formalism gives invariant 4D mass/charge variables; see Ponce de Leon, arXiv:gr-qc/0207108.
- Circle-bundle topology and loop-group formulations are standard in KK reduction; see Bergman & Varadarajan, arXiv:hep-th/0406218.
- Wilson-loop phases are standard gauge holonomies.
- Bosonic thermal Matsubara frequencies obey `omega_n=2 pi n T`; Euclidean horizon regularity underlies Hawking temperature in stationary black-hole thermodynamics.
