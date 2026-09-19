# EXP-092 — Geometric fluctuation theorem for capacity-changing histories

## Objective

Combine:

1. sector detailed balance;
2. q-ary exact degeneracy;
3. LTG causal action;

to derive the ratio of a complete capacity-changing history and its time reverse.

---

## 1. Local detailed balance

For one neighboring sector transition,

\[
\frac{\Gamma_{n\to n+1}}
{\Gamma_{n+1\to n}}
=
q.
\]

Equivalently,

\[
\ln
\frac{\Gamma_+}{\Gamma_-}
=
\ln q
=
\frac{\Delta S}{k_B}.
\]

---

## 2. Path probability ratio

Consider a history \(\gamma\) containing \(N_+\) upward-capacity steps and \(N_-\) downward-capacity steps.

Its reversed history \(\tilde\gamma\) exchanges the directions.

Assuming the same symmetric kinetic/barrier factors for forward/reverse neighboring links, the ratio telescopes:

\[
\frac{P[\gamma]}
{P[\tilde\gamma]}
=
q^{N_+-N_-}.
\]

Since

\[
n_f-n_i
=
N_+-N_-,
\]

we obtain

\[
\boxed{
\frac{P[\gamma]}
{P[\tilde\gamma]}
=
q^{n_f-n_i}.
}
\]

---

## 3. Entropy form

Because

\[
\Delta S
=
k_B(n_f-n_i)\ln q,
\]

the path ratio becomes

\[
\boxed{
\ln
\frac{P[\gamma]}
{P[\tilde\gamma]}
=
\frac{\Delta S}{k_B}.
}
\]

This is the standard fluctuation-theorem / local-detailed-balance structure.

---

## 4. LTG causal-action form

EXP-091 gives the reversible action change

\[
\Delta\mathcal A_{\rm rev}
=
\frac{\hbar}{2\pi}
(n_f-n_i)\ln q.
\]

Therefore

\[
\boxed{
\ln
\frac{P[\gamma]}
{P[\tilde\gamma]}
=
\frac{2\pi}{\hbar}
\Delta\mathcal A_{\rm rev}.
}
\]

Or

\[
\boxed{
\frac{P[\gamma]}
{P[\tilde\gamma]}
=
\exp\left[
\frac{2\pi}{\hbar}
\Delta\mathcal A_{\rm rev}
\right].
}
\]

### Result 092A — geometric fluctuation theorem

The arrow of capacity growth can be written equivalently as:

- entropy increase;
- Hilbert-space multiplicity increase;
- causal-action increase.

---

## 5. Consequence for macroscopic histories

For a macroscopic net increase

\[
\Delta n\gg1,
\]

the reverse history is suppressed by

\[
q^{-\Delta n}.
\]

Thus a large growth of horizon capacity has an overwhelmingly directed thermodynamic arrow even if every elementary transition is microscopically reversible.

This gives a clean information-theoretic interpretation of geometric irreversibility.

---

## 6. Does this select the endpoint?

No.

The theorem fixes forward/reverse ratios but not:

- the absolute transition clock;
- the maximum \(n\);
- a finite equilibrium endpoint.

On an unbounded tower it still favors

\[
n\to\infty.
\]

### Result 092B

\[
\boxed{
\text{arrow of geometric time: obtained;}
}
\]

\[
\boxed{
\text{finite cosmological scale selection: not obtained.}
}
\]

---

## 7. Novelty status

Crooks/fluctuation-theorem and local detailed-balance structures are established statistical physics.

The LTG contribution is the geometric/action normalization,

\[
\Delta S/k_B
=
(2\pi/\hbar)\Delta\mathcal A_{\rm rev},
\]

for horizon-capacity sectors.

### Classification

\[
\boxed{
\text{GEOMETRIC FLUCTUATION-THEOREM SYNTHESIS / PRIOR-ART FOUNDATION.}
}
\]

## Active frontier

The remaining unknown is a finite capacity bound, terminal sector, or controlled nonequilibrium drive.

No reversible detailed-balance law can choose a finite \(n\) on an unbounded entropy-increasing tower.
