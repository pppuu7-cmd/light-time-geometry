# EXP-077 — Global Causal Action Bound from quantum relative entropy

## Objective

Integrate the local quantum causal-balance relation of EXP-074 over a finite sequence of causal transitions and test whether it yields a genuine global law.

For each step \(i\), use

\[
\frac{\tau_i\Delta Q_i}{\hbar}
=
\Delta\mathcal N_i
+
\frac{D_i}{2\pi},
\qquad
D_i\ge0,
\]

where:

- \(\tau_i\) is the causal/modular time scale of the step;
- \(\Delta Q_i\) is its modular-energy transfer;
- \(\Delta\mathcal N_i\) is the generalized-information change;
- \(D_i\) is the relative-entropy residual for that step.

---

## 1. Sum over a finite causal history

For a sequence of \(m\) causal transitions,

\[
i=1,\dots,m,
\]

sum the exact step relations:

\[
\sum_{i=1}^{m}
\frac{\tau_i\Delta Q_i}{\hbar}
=
\sum_i\Delta\mathcal N_i
+
\frac{1}{2\pi}\sum_iD_i.
\]

If the \(\mathcal N_i\) changes telescope between an initial and final causal state,

\[
\sum_i\Delta\mathcal N_i
=
\mathcal N_f-\mathcal N_i.
\]

Define the dimensional causal action input

\[
\boxed{
\mathcal A_{\rm causal}
\equiv
\sum_i\tau_i\Delta Q_i.
}
\]

Then

\[
\boxed{
\mathcal A_{\rm causal}
=
\hbar(\mathcal N_f-\mathcal N_i)
+
\frac{\hbar}{2\pi}\sum_iD_i.
}
\]

### Result 077A — Global Causal Action Balance

\[
\boxed{
\mathcal A_{\rm causal}
=
\hbar\,\Delta\mathcal N_{\rm gen}
+
\mathcal A_{\rm irr},
}
\]

with

\[
\boxed{
\mathcal A_{\rm irr}
\equiv
\frac{\hbar}{2\pi}\sum_iD_i
\ge0.
}
\]

This gives a global action decomposition into:

1. reversible generalized-information change;
2. nonnegative quantum irreversibility action.

---

## 2. Causal Action Bound

Because every relative entropy satisfies

\[
D_i\ge0,
\]

the history obeys

\[
\boxed{
\mathcal A_{\rm causal}
\ge
\hbar\,\Delta\mathcal N_{\rm gen}.
}
\]

Equality holds if every step is reversible relative to its chosen reference:

\[
D_i=0
\quad\forall i.
\]

Thus

\[
\boxed{
\mathcal A_{\rm causal}^{\min}
=
\hbar\,\Delta\mathcal N_{\rm gen}.
}
\]

### Interpretation

A positive increase in generalized causal/horizon information requires at least one quantum of action \(\hbar\) per unit increase of the LTG-normalized information variable.

This is the rigorous descendant of the earlier intuitive statement that creating geometry may require energy.

The correct quantity is not energy alone:

\[
E.
\]

It is causal action:

\[
\boxed{
E\times\tau.
}
\]

---

## 3. Einstein-horizon specialization

For the reversible Einstein horizon,

\[
\mathcal N
=
\frac{A}{8\pi\ell_P^2}.
\]

Then

\[
\boxed{
\mathcal A_{\rm causal}^{\rm rev}
=
\frac{\hbar\,\Delta A}{8\pi\ell_P^2}.
}
\]

Using

\[
\ell_P^2=\frac{G\hbar}{c^3},
\]

this becomes

\[
\boxed{
\mathcal A_{\rm causal}^{\rm rev}
=
\frac{c^3}{8\pi G}\Delta A.
}
\]

Thus horizon-area creation and causal action are directly proportional in the reversible Einstein limit.

---

## 4. Relation to the original traversal hypothesis

EXP-052 ruled out

\[
\text{energy required to traverse a region}
=
\text{energy that created the region}.
\]

EXP-077 replaces that false statement with:

\[
\boxed{
\text{causal action needed for a generalized-information increase}
\ge
\hbar\,\Delta\mathcal N.
}
\]

This does not say a later probe must repay the history's action.

It says the **formation/evolution process itself** has a minimum action-information cost.

---

## 5. Prior-art map

The mathematical foundation is established quantum thermodynamics / quantum information:

- relative entropy measures distinguishability;
- dissipated work / entropy production can be written in terms of relative entropy;
- reversible processes saturate corresponding information-theoretic bounds.

Therefore the positivity and dissipation structure are not new.

The LTG contribution is the causal-horizon normalization in which the same bound becomes an action cost for generalized geometric information.

### Classification

\[
\boxed{
\text{GLOBAL CAUSAL ACTION BOUND — DERIVED}
}
\]

but

\[
\boxed{
\text{FOUNDATION IS PRIOR-ART RELATIVE ENTROPY / THERMODYNAMICS}.
}
\]

---

## 6. Does the minimum select a cosmic history?

Not by itself.

For fixed endpoints,

\[
\mathcal N_i,\mathcal N_f,
\]

every fully reversible history has the same minimum

\[
\mathcal A_{\rm causal}^{\min}
=
\hbar(\mathcal N_f-\mathcal N_i).
\]

Therefore a bare least-causal-action principle is degenerate.

It cannot choose one reversible path among many.

This is tested more explicitly in EXP-079.

---

## 7. Terminal classification

### Global action-information inequality

\[
\boxed{
\mathcal A_{\rm causal}
\ge
\hbar\,\Delta\mathcal N_{\rm gen}
}
\]

**ANALYTIC PASS.**

### Quantum irreversibility correction

\[
\boxed{
\mathcal A_{\rm irr}
=
\frac{\hbar}{2\pi}\sum_iD_i
\ge0
}
\]

**ANALYTIC PASS for the finite-step construction.**

### New global state-selection law

**NOT YET.**

The bound constrains histories but does not select the endpoint or a unique reversible trajectory.
