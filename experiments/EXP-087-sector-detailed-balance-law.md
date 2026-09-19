# EXP-087 — Detailed balance for capacity-changing de Sitter sectors

## Objective

Continue the v13 frontier:

\[
\mathcal H=\bigoplus_n\mathcal H_n
\]

with different generalized horizon capacities.

Test whether known de Sitter transition physics plus the LTG sector normalization can determine the ratio of neighboring transition rates without introducing an arbitrary temperature.

---

## 1. Sector entropy

Let the generalized LTG count be quantized as

\[
\mathcal N_n=\alpha n,
\qquad
n\in\mathbb N,
\]

where \(\alpha\) records the area-quantization prescription.

Examples:

\[
\alpha=1
\]

for the conditional \(8\pi\ell_P^2\) spectrum,

and

\[
\alpha=2
\]

for the \(16\pi\ell_P^2\) pure-de-Sitter adiabatic benchmark.

The horizon entropy is

\[
\boxed{
\frac{S_n}{k_B}
=
2\pi\mathcal N_n
=
2\pi\alpha n.
}
\]

Therefore the degeneracy of a sector is

\[
g_n
\propto
e^{S_n/k_B}
=
e^{2\pi\alpha n}.
\]

---

## 2. de Sitter detailed balance

Semiclassical transitions between two de Sitter vacua satisfy the detailed-balance relation

\[
\boxed{
\frac{\Gamma_{i\to j}}
{\Gamma_{j\to i}}
=
\exp\left(
\frac{S_j-S_i}{k_B}
\right)
}
\]

for the standard entropy interpretation of the two dS states.

For neighboring LTG sectors,

\[
S_{n+1}-S_n
=
2\pi\alpha k_B.
\]

Hence

\[
\boxed{
\frac{\Gamma_{n\to n+1}}
{\Gamma_{n+1\to n}}
=
e^{2\pi\alpha}.
}
\]

### Result 087A — parameter-free directional ratio

The transition **ratio** is fixed by the entropy spacing once \(\alpha\) is specified.

No extra horizon temperature is needed because the Gibbons-Hawking entropy already determines detailed balance.

---

## 3. Numerical asymmetry

### Conditional \(8\pi\) spectrum

For

\[
\alpha=1,
\]

\[
\boxed{
\frac{\Gamma_+}{\Gamma_-}
=
e^{2\pi}
\approx
5.35\times10^2.
}
\]

### Pure-de-Sitter \(16\pi\) benchmark

For

\[
\alpha=2,
\]

\[
\boxed{
\frac{\Gamma_+}{\Gamma_-}
=
e^{4\pi}
\approx
2.87\times10^5.
}
\]

Thus entropy-detailed balance strongly favors transitions toward larger \(\mathcal N\), i.e. larger horizon area and smaller de Sitter curvature.

---

## 4. Prefactor remains undetermined

Detailed balance fixes only the ratio.

Write the most general symmetric-barrier factorization as

\[
\boxed{
\Gamma_{n\to n+1}
=
\gamma_{n+1/2}
e^{+\pi\alpha},
}
\]

\[
\boxed{
\Gamma_{n+1\to n}
=
\gamma_{n+1/2}
e^{-\pi\alpha},
}
\]

where

\[
\gamma_{n+1/2}>0
\]

contains instanton/barrier/matrix-element physics.

Then the ratio is automatically

\[
e^{2\pi\alpha}.
\]

### Result 087B

\[
\boxed{
\text{entropy fixes directional bias, not the clock rate.}
}
\]

The microscopic prefactor remains extra data.

This agrees with known vacuum-decay physics: the entropy ratio can be barrier independent even though the absolute rates depend sensitively on the instanton/barrier action.

---

## 5. Universal transition asymmetry

Define

\[
\mathcal B_\alpha
\equiv
\frac{\Gamma_+-\Gamma_-}
{\Gamma_++\Gamma_-}.
\]

Using the symmetric factorization,

\[
\boxed{
\mathcal B_\alpha
=
\tanh(\pi\alpha).
}
\]

Therefore:

\[
\alpha=1
\Rightarrow
\mathcal B\simeq0.99627,
\]

\[
\alpha=2
\Rightarrow
\mathcal B\simeq0.999993.
\]

This ratio is independent of the unknown absolute prefactor.

### Result 087C

If the neighboring-sector detailed-balance picture is valid, the **directional asymmetry** is fixed entirely by the entropy quantum.

---

## 6. Physical direction

For de Sitter,

\[
\mathcal N
=
\frac{c^5}{2G\hbar H^2}.
\]

Thus

\[
n\to n+1
\]

means

\[
\mathcal N\uparrow,
\qquad
A\uparrow,
\qquad
S\uparrow,
\qquad
H\downarrow,
\qquad
\Lambda\downarrow.
\]

So the thermodynamic bias is toward lower positive curvature.

This matches the familiar statement that upward tunneling in vacuum energy is entropy suppressed.

---

## 7. Relation to the causal action quantum

The reversible LTG action increment for one neighboring step is

\[
\Delta\mathcal A_{\rm causal}^{\min}
=
\hbar\Delta\mathcal N
=
\boxed{
\alpha\hbar.
}
\]

The same step has entropy increment

\[
\boxed{
\Delta S
=
2\pi\alpha k_B.
}
\]

Hence

\[
\boxed{
\frac{\Delta S}{k_B}
=
2\pi
\frac{\Delta\mathcal A_{\rm causal}^{\min}}{\hbar}.
}
\]

Detailed balance becomes

\[
\boxed{
\frac{\Gamma_+}{\Gamma_-}
=
\exp\left(
2\pi
\frac{\Delta\mathcal A_{\rm causal}^{\min}}{\hbar}
\right).
}
\]

This directly links sector-transition asymmetry to the LTG causal action quantum.

---

## 8. Novelty status

The ingredients are established:

- Gibbons-Hawking de Sitter entropy;
- detailed balance of dS vacuum transitions;
- conditional area quantization.

The LTG contribution is the common normalization that writes the rate ratio directly as a causal-action quantum.

### Classification

\[
\boxed{
\text{SECTOR RATE-RATIO LAW DERIVED / PRIOR-ART FOUNDATION.}
}
\]

It is not yet independent new physics.

## Active issue

Absolute rates and finite-\(n\) state selection remain undetermined.

The next gate tests whether entropy-detailed balance by itself admits a normalizable finite equilibrium distribution over the LTG sectors.
