# EXP-079 — Least causal action and path-selection degeneracy

## Objective

EXP-077 derived

\[
\mathcal A_{\rm causal}
=
\hbar\Delta\mathcal N
+
\frac{\hbar}{2\pi}\sum_iD_i.
\]

Test whether the variational principle

\[
\boxed{
\delta\mathcal A_{\rm causal}=0
}
\]

can select a unique cosmic history.

---

## 1. Fixed endpoints

Fix

\[
\mathcal N_i,
\qquad
\mathcal N_f.
\]

Then

\[
\hbar\Delta\mathcal N
\]

is path independent.

Therefore minimizing the causal action is equivalent to minimizing

\[
\sum_iD_i.
\]

The minimum is

\[
\sum_iD_i=0
\]

whenever the history can be decomposed into reversible steps relative to its chosen references.

Thus

\[
\boxed{
\mathcal A_{\rm causal}^{\min}
=
\hbar(\mathcal N_f-\mathcal N_i).
}
\]

---

## 2. Degeneracy

If more than one reversible history connects the same endpoints, every such history has exactly the same minimum action.

Therefore the least-causal-action rule alone does not determine:

- \(w(a)\);
- \(H(a)\);
- the duration of the transition;
- the intermediate state path.

### Result 079A

\[
\boxed{
\text{least causal action with fixed endpoints is path-degenerate.}
}
\]

This is a no-go for using the first-order action bound as a complete cosmological variational principle.

---

## 3. Free final endpoint

If the final endpoint is not fixed, then the reversible lower bound is

\[
\mathcal A_{\rm causal}^{\min}
=
\hbar(\mathcal N_f-\mathcal N_i).
\]

Minimizing over \(\mathcal N_f\ge\mathcal N_i\) gives the trivial choice

\[
\boxed{
\mathcal N_f=\mathcal N_i.
}
\]

Thus a bare least-action principle prefers no information/geometry growth at all.

It cannot select a large finite late horizon.

### Result 079B

\[
\boxed{
\text{least causal action does not select the observed large } \mathcal N.
}
\]

---

## 4. Can second-order relative entropy remove the degeneracy?

For nearby states parametrized by coordinates \(\theta^a\),

\[
D(\theta+d\theta\Vert\theta)
=
\frac12
g_{ab}^{\rm QFI}\,
d\theta^a d\theta^b
+
O(d\theta^3),
\]

where \(g_{ab}^{\rm QFI}\) is the quantum Fisher / Kubo-Mori information metric.

A tempting continuum path cost is therefore

\[
\int
g_{ab}\dot\theta^a\dot\theta^b\,dt.
\]

But this functional requires:

1. a choice of state-space coordinates / physical controls;
2. a time parametrization;
3. a kinetic/friction normalization;
4. a microscopic information metric.

Bare relative entropy alone does not supply a unique finite continuum action by simply summing infinitesimal \(D\)'s; under increasingly fine partitions, each \(D_i=O(d\theta^2)\), so the naive sum is discretization dependent and tends to zero for a smooth path.

### Result 079C

A nondegenerate global path-selection functional requires additional microscopic transport data.

Relative entropy positivity alone is insufficient.

---

## 5. Thermodynamic-length prior art

Information geometry and finite-time thermodynamics already use:

- Fisher/Kubo-Mori metrics;
- thermodynamic length;
- minimum-dissipation paths.

Therefore even after a microscopic metric is specified, a least-dissipation geodesic would map to established information-geometric thermodynamics unless LTG predicts the metric or transport coefficients independently.

---

## 6. Consequence for the global LTG program

The global functional cannot be obtained by merely summing the local CIB residual.

A genuinely predictive global rule must add one of:

1. a fixed microscopic information metric;
2. a quantized global boundary term;
3. a topological constraint;
4. a finite-capacity constraint;
5. a dynamical reference-state family with independently specified evolution.

This extra structure must be independently derived.

---

## Terminal classification

### Global Causal Action Bound

**VALID.**

### Least causal action as unique history selector

\[
\boxed{\text{FAIL}.}
\]

### Relative-entropy second order as unique continuum action

\[
\boxed{\text{FAIL without extra microscopic metric/transport data}.}
\]

## Strongest lesson

\[
\boxed{
\text{the missing LTG ingredient is not another local entropy inequality;
it is a microscopic rule for the geometry of state space or a global boundary constraint.}
}
