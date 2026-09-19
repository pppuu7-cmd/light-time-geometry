# EXP-080 — Holographic–Poisson square-root bridge and the special role of 3+1 dimensions

## Objective

Test whether the LTG horizon-information count can be connected to a concrete global discreteness mechanism rather than an arbitrary boundary functional.

Use two established ingredients:

1. holographic/horizon information scales with boundary area;
2. Poisson sprinkling of a causal spacetime volume has number fluctuations of order the square root of the volume count.

Ask in what spacetime dimension these two counts scale identically.

---

## 1. General d-dimensional scaling

Let \(d\) be spacetime dimension and \(L\) a causal/horizon length scale.

### Horizon information

For Einstein gravity, horizon entropy/information scales as

\[
\mathcal N_H^{(d)}
\propto
\left(
\frac{L}{\ell_*}
\right)^{d-2}.
\]

### Poisson spacetime-volume fluctuations

A \(d\)-volume contains

\[
N_V^{(d)}
\propto
\left(
\frac{L}{\ell_*}
\right)^d
\]

fundamental spacetime cells.

For Poisson statistics,

\[
\Delta N_V
\sim
\sqrt{N_V}.
\]

Therefore

\[
\boxed{
\Delta N_V^{(d)}
\propto
\left(
\frac{L}{\ell_*}
\right)^{d/2}.
}
\]

---

## 2. Match the scaling exponents

Require the horizon information count and Poisson volume fluctuation count to have the same scale dependence:

\[
d-2
=
\frac d2.
\]

Then

\[
2d-4=d,
\]

hence

\[
\boxed{
d=4.
}
\]

### Result 080A — dimension-matching theorem

Within the stated assumptions,

\[
\boxed{
\text{horizon area information}
\sim
\text{Poisson fluctuation of spacetime-volume count}
}
\]

has matching powers of \(L\) **only in four spacetime dimensions**.

This is a scaling theorem, not a derivation that nature must have \(d=4\).

Its assumptions are essential:

- area-law horizon information;
- Poisson fundamental volume statistics;
- one common microscopic length scale.

---

## 3. Exact four-dimensional Euclidean de Sitter constants

For Euclidean de Sitter \(S^4\),

\[
V_4
=
\frac{8\pi^2}{3}L^4.
\]

Define the Planck-cell four-volume count

\[
\boxed{
N_4
\equiv
\frac{V_4}{\ell_P^4}.
}
\]

Then

\[
\sqrt{N_4}
=
\pi\sqrt{\frac83}
\frac{L^2}{\ell_P^2}.
\]

The LTG horizon count is

\[
\mathcal N_{\rm LTG}
=
\frac{A}{8\pi\ell_P^2}
=
\frac{L^2}{2\ell_P^2}.
\]

Therefore

\[
\boxed{
\mathcal N_{\rm LTG}
=
\frac{3}{4\pi\sqrt6}
\sqrt{N_4}.
}
\]

So the LTG area/information count is exactly proportional to the rms Poisson count scale of the four-volume.

---

## 4. Action count

For Euclidean de Sitter,

\[
\frac{|I_E|}{\hbar}
=
\frac{S_{\rm dS}}{k_B}
=
2\pi\mathcal N_{\rm LTG}.
\]

Using the previous relation,

\[
\boxed{
\frac{|I_E|}{\hbar}
=
\sqrt{\frac38}
\sqrt{N_4}.
}
\]

This is an exact identity for the Euclidean \(S^4\) geometry when \(N_4\) is defined as its volume in Planck four-cells.

### Result 080B

The de Sitter gravitational action count and the square-root spacetime-volume count have not merely the same scaling but a fixed geometric coefficient:

\[
\boxed{
|I_E|/\hbar
=
\sqrt{3/8}\,\sqrt{N_4}.
}
\]

---

## 5. Cosmological constant form

For de Sitter,

\[
L^2=\frac{3}{\Lambda}.
\]

Therefore

\[
\mathcal N_{\rm LTG}
=
\frac{3}{2\Lambda\ell_P^2}.
\]

Also,

\[
N_4
=
\frac{24\pi^2}
{\Lambda^2\ell_P^4}.
\]

Hence

\[
\boxed{
\Lambda\ell_P^2
=
\frac{2\pi\sqrt6}{\sqrt{N_4}}.
}
\]

Thus the familiar causal-set scaling

\[
\Lambda
\sim
N_4^{-1/2}
\]

is exactly the same power law as the de Sitter horizon-information relation in four dimensions.

---

## 6. Relation to Sorkin's everpresent-Lambda mechanism

Causal-set theory uses:

1. spacetime element number
   \[
   N_4\sim V_4/\ell_c^4;
   \]
2. Poisson fluctuation
   \[
   \Delta N_4\sim\sqrt{N_4};
   \]
3. unimodular-type conjugacy of \(\Lambda\) and four-volume.

This leads heuristically to

\[
\Delta\Lambda
\sim
V_4^{-1/2}.
\]

Dynamical versions also model the causal-set action as a random accumulation of microscopic action increments.

EXP-080 shows that in \(d=4\), the square-root count appearing in that mechanism is precisely the same scaling object as the LTG horizon/action count.

### Structural bridge

\[
\boxed{
\text{Poisson volume fluctuation}
\sim
\sqrt{N_4}
\sim
\mathcal N_{\rm horizon}
\sim
|I_E|/\hbar.
}
\]

This is a concrete bridge between:

- causal-set discreteness;
- holographic area information;
- Euclidean gravitational action.

---

## 7. Random-action coefficient test

Suppose a microscopic discrete model has independent zero-mean action increments

\[
\delta I_j
=
\pm\alpha\hbar
\]

with unit-variance signs.

Then after \(N_4\) elements,

\[
I_{\rm rms}
=
\alpha\hbar\sqrt{N_4}.
\]

Matching the Euclidean de Sitter action magnitude would require

\[
\alpha\sqrt{N_4}
=
\sqrt{\frac38}\sqrt{N_4}.
\]

Hence

\[
\boxed{
\alpha_{\rm match}
=
\sqrt{\frac38}
\approx0.612372.
}
\]

### Result 080C

If a causal discrete theory independently predicted a microscopic rms action coefficient

\[
\alpha=\sqrt{3/8},
\]

its Poisson action fluctuation would match the Euclidean de Sitter action normalization.

At present no such derivation has been established.

This is therefore a **new matching target**, not a prediction.

---

## 8. Why this still does not select Lambda

The matching

\[
|I_E|/\hbar
\propto
\sqrt{N_4}
\]

holds for every de Sitter radius \(L\).

Equating the two sides fixes only the dimensionless microscopic coefficient \(\alpha\).

The scale \(L\), \(H\), or \(\Lambda\) cancels.

Therefore:

\[
\boxed{
\text{correct fluctuation scaling does not select the cosmological scale.}
}
\]

It supplies a possible microscopic normalization bridge but not state selection.

---

## 9. Important geometry caveat

Sorkin's cosmological mechanism usually uses the Lorentzian four-volume of a causal past.

EXP-080 used the compact Euclidean de Sitter \(S^4\) because that is where the exact LTG action/entropy identity is controlled.

These volumes are not the same object.

Therefore the exact coefficient

\[
\sqrt{3/8}
\]

must not be transferred directly into an everpresent-\(\Lambda\) stochastic cosmology without a Lorentzian/Euclidean bridge.

The robust statement is the **four-dimensional scaling match**.

---

## 10. Novelty audit

Targeted literature searches found:

- causal-set Poisson number fluctuations;
- the everpresent-\(\Lambda\) scaling \(\Lambda\sim V^{-1/2}\);
- horizon area entropy;
- causal-set horizon/link entropy studies.

The audit did not locate an authoritative source explicitly formulating the exponent-matching condition

\[
d-2=d/2
\Rightarrow
d=4
\]

as a bridge between holographic horizon information and Poisson spacetime-volume fluctuations.

Absence of a located source is not proof of novelty.

### Classification

\[
\boxed{
\text{CANDIDATE NOVEL LTG/CAUSAL-SET SYNTHESIS}
}
\]

for the dimension-matching observation.

The underlying ingredients are established prior art.

---

## 11. Next decisive tests

1. Repeat the coefficient calculation using a Lorentzian causal diamond/past volume rather than Euclidean \(S^4\).
2. Compare with known causal-set action fluctuation coefficients.
3. Test whether the dimension-matching survives generalized/Wald entropy.
4. Determine whether any microscopic discreteness law fixes the coefficient rather than merely the scaling.
