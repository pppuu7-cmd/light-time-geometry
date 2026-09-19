# LTG Research Status v14 — q-ary sector dynamics, detailed balance, and finite-capacity interpretation through EXP-095

## Executive result

The sector-changing frontier from v13 has now been pushed through:

- de Sitter detailed balance;
- exact finite-state degeneracy;
- Landauer causal action;
- path fluctuation relations;
- finite total Hilbert capacity;
- unitarity constraints on "space creation."

The strongest update is that the literal integer formula should be reformulated if the horizon entropy is interpreted as the logarithm of an **exact finite number of states**.

---

## 1. q-ary exact sector spectrum

Instead of requiring

\[
S_n/k_B=2\pi\alpha n,
\]

exact finite degeneracy suggests

\[
\boxed{
\dim\mathcal H_n=q^n,
\qquad
q\in\{2,3,\ldots\}.
}
\]

Therefore

\[
\boxed{
\frac{S_n}{k_B}
=
n\ln q.
}
\]

Using the Bekenstein-Hawking entropy gives

\[
\boxed{
A_n
=
4\ell_P^2 n\ln q.
}
\]

At stationary de Sitter, the unified formula becomes

\[
\boxed{
\frac{A_n}{4\ell_P^2\ln q}
=
\frac{S_n}{k_B\ln q}
=
\frac{|I_{E,n}|}{\hbar\ln q}
=
\frac{2\pi E_{\rm geom}\tau_{\rm light}}
{\hbar\ln q}
=
n.
}
\]

This is the cleanest exact-integer LTG normalization if \(n\) literally counts multiplicative Hilbert-space capacity.

The older \(8\pi\ell_P^2\) spectrum would require

\[
q=e^{2\pi},
\]

which is not an integer.

Therefore the following cannot all be exact simultaneously:

1. \(A_n=8\pi\ell_P^2n\);
2. \(S=A/(4\ell_P^2)\);
3. \(e^{S/k_B}\) is an exact finite integer degeneracy for every \(n\).

This is Bekenstein-Mukhanov-type prior-art logic placed inside LTG.

---

## 2. Sector detailed balance

For de Sitter transitions,

\[
\frac{\Gamma_{i\to j}}
{\Gamma_{j\to i}}
=
e^{(S_j-S_i)/k_B}.
\]

For neighboring q-ary sectors,

\[
\Delta S=k_B\ln q,
\]

so

\[
\boxed{
\frac{\Gamma_{n\to n+1}}
{\Gamma_{n+1\to n}}
=
q.
}
\]

Thus exact microstate multiplicity and the transition directional bias coincide.

For the earlier semiclassical spacing

\[
\mathcal N=\alpha n,
\]

the corresponding ratio is

\[
e^{2\pi\alpha}.
\]

Detailed balance fixes the ratio, not the absolute transition clock.

---

## 3. Horizon Landauer action quantum

At horizon temperature

\[
k_BT_H=\frac{\hbar H}{2\pi},
\]

one q-ary entropy step requires reversible heat

\[
\Delta Q_{\rm rev}
=
T_H\Delta S
=
\frac{\hbar H}{2\pi}\ln q.
\]

Over one causal time

\[
\tau_H=H^{-1},
\]

the action cost is

\[
\boxed{
\Delta\mathcal A_{\rm rev}
=
\frac{\hbar}{2\pi}\ln q.
}
\]

This exactly saturates the LTG global causal-action bound for the q-ary step.

For the minimal binary alphabet,

\[
q=2,
\]

\[
\boxed{
\Delta\mathcal A_{\rm bit}
=
\frac{\hbar\ln2}{2\pi}.
}
\]

Landauer fixes the cost for a given \(q\), but does not uniquely select \(q=2\).

---

## 4. Geometric fluctuation theorem

Local detailed balance implies for a complete capacity-changing history \(\gamma\),

\[
\boxed{
\ln
\frac{P[\gamma]}
{P[\tilde\gamma]}
=
\frac{\Delta S}{k_B}.
}
\]

Using the LTG causal action,

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

Equivalently,

\[
\boxed{
\frac{P[\gamma]}
{P[\tilde\gamma]}
=
q^{n_f-n_i}.
}
\]

This gives a clean thermodynamic arrow for geometric-capacity growth.

Its foundation is standard fluctuation-theorem / local-detailed-balance physics.

---

## 5. Finite-scale no-go for an unbounded tower

For a reversible sector chain,

\[
P_n^{\rm eq}
\propto
e^{S_n/k_B}
=
q^n.
\]

If

\[
n=1,2,\ldots,\infty,
\]

the equilibrium weights are not normalizable.

Therefore exact detailed balance on an unbounded capacity tower drives the theory toward

\[
\boxed{
n\to\infty,
\qquad
H\to0,
\qquad
\Lambda\to0^+.
}
\]

Barrier prefactors can slow the dynamics but do not change the equilibrium weights as long as detailed balance remains exact.

Thus a finite positive late cosmological scale requires:

- a finite maximum capacity;
- a terminal/nonequilibrium structure;
- or an extra weight opposing entropy growth.

---

## 6. Finite total Hilbert capacity

Assume

\[
\boxed{
D_{\rm tot}
=
\dim\mathcal H_{\rm tot}
<\infty.
}
\]

For q-ary accessible sectors,

\[
q^n\le D_{\rm tot},
\]

so

\[
\boxed{
n_{\max}
=
\left\lfloor
\frac{\ln D_{\rm tot}}{\ln q}
\right\rfloor.
}
\]

The endpoint de Sitter scale is

\[
\boxed{
H_*^2
=
\frac{\pi c^5}
{G\hbar\ln D_{\rm tot}},
}
\]

and

\[
\boxed{
\Lambda_*
=
\frac{3\pi c^3}
{G\hbar\ln D_{\rm tot}}.
}
\]

The dependence on the microscopic alphabet \(q\) cancels.

This is exactly the finite-state interpretation of de Sitter entropy, not a new scale-selection theorem.

The missing number becomes

\[
\boxed{
D_{\rm tot}.
}
\]

---

## 7. Unitarity no-go for literal state creation

A closed unitary map preserves Hilbert-space dimension.

Therefore one cannot literally have

\[
\mathcal H_n
\stackrel{U}{\longrightarrow}
\mathcal H_{n+1}
\]

as entire fundamental Hilbert spaces with

\[
\dim\mathcal H_{n+1}
>
\dim\mathcal H_n.
\]

Thus the unitary-compatible interpretation is:

\[
\boxed{
\text{growing geometry}
=
\text{growing causal accessibility / entanglement / code capacity}
}
\]

inside a larger fixed global quantum state space.

This replaces the naive statement that expansion creates brand-new fundamental states.

---

## 8. Early Planck patch versus total capacity

At

\[
H=H_P,
\]

the LTG accessible count is

\[
\mathcal N_i=1/2,
\]

so the semiclassical horizon entropy is only

\[
S_i/k_B=\pi.
\]

A late de Sitter horizon has an enormously larger entropy.

Therefore, in a fixed-Hilbert-space unitary model,

\[
\boxed{
\text{the early Planck causal patch cannot be the entire fundamental Hilbert space}.
}
\]

It must be an early accessible subsystem/code sector of a much larger global state, or the earliest semiclassical entropy interpretation must fail.

This is a major conceptual refinement of the original "hot point without space" idea.

---

## 9. Current strongest physical picture

The project now supports the hierarchy

\[
\boxed{
\text{fixed/global quantum capacity}
\to
\text{time-dependent causal accessibility}
\to
\text{generalized horizon information}
\to
\text{emergent geometry}.
}
\]

Energy/action controls transitions among accessible geometric sectors:

\[
\boxed{
\mathcal A_{\rm causal}
\ge
\hbar\Delta\mathcal N_{\rm gen}.
}
\]

Detailed balance gives the forward/reverse ratio.

The geometry does not literally manufacture the total state space.

---

## 10. Novelty status

### Established/prior-art foundations

- dS transition detailed balance;
- Bekenstein-Mukhanov degeneracy logic;
- Landauer information cost;
- fluctuation theorems;
- finite-state interpretations of de Sitter entropy;
- unitary fixed-Hilbert-space quantum mechanics.

### LTG-specific synthesis

The project now connects all of them in one chain:

\[
\boxed{
\text{Hilbert capacity}
\leftrightarrow
\text{horizon entropy}
\leftrightarrow
\text{causal action}
\leftrightarrow
\text{sector transition bias}
\leftrightarrow
\text{emergent geometric accessibility}.
}
\]

This is a coherent synthesis but still not an independently established new law of nature.

---

## Active next frontier

There is now only one genuinely missing global datum:

\[
\boxed{
D_{\rm tot}
}
\]

or an equivalent maximum generalized entropy.

The next useful gate must attempt to derive the total/global Hilbert capacity from a microscopic invariant rather than re-express it in terms of the observed \(\Lambda\).

No local causal equation, detailed-balance relation, or ordinary entropy principle tested so far can determine it.
