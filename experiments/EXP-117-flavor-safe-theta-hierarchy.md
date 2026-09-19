# EXP-117 — Flavor-safe independent hierarchy formula in terms of the QCD theta potential

## Objective

Rewrite the entire QCD-to-de-Sitter hierarchy without GMOR normalization ambiguities or explicit flavor-count conventions.

Use only two QCD quantities:

1. the infinite-volume theta-potential amplitude \(B_\theta\);
2. the dimensionless curved-background response coefficient \(\kappa_{\rm dS}\).

---

## 1. Microscopic response

Define

\[
B_\theta
=
-\epsilon_\theta(0)>0.
\]

Postulate the leading nonlocal/topological de Sitter response in the invariant form

\[
\boxed{
\rho_{\rm top}^{\rm dS}
=
\kappa_{\rm dS}
\frac{H}{m_{\eta'}}
B_\theta.
}
\]

No \(N_f\), condensate normalization, GMOR convention, or arbitrary infrared length appears.

---

## 2. Self-consistent de Sitter solution

The vacuum-dominated Friedmann equation is

\[
3\bar M_P^2H^2
=
\rho_{\rm top}^{\rm dS}.
\]

For the nonzero branch,

\[
\boxed{
H_*
=
\kappa_{\rm dS}
\frac{B_\theta}
{3m_{\eta'}\bar M_P^2}.
}
\]

This is the flavor-safe version of the EXP-100 closure.

---

## 3. Global LTG capacity

The de Sitter entropy is

\[
\frac{S_{\rm dS}}{k_B}
=
8\pi^2\frac{\bar M_P^2}{H_*^2}.
\]

Substituting the microscopic solution gives

\[
\boxed{
\ln D_{\rm tot}
=
\frac{S_{\rm dS}}{k_B}
=
72\pi^2
\frac{
m_{\eta'}^2\bar M_P^6
}{
\kappa_{\rm dS}^2B_\theta^2
}.
}
\]

### Result 117A — flavor-safe hierarchy law

\[
\boxed{
\text{QCD theta potential}
+
\text{nonlocal curvature response}
\Longrightarrow
D_{\rm tot}
}
\]

without cosmological data, provided \(\kappa_{\rm dS}\) is independently computed.

---

## 4. Two-flavor benchmark

For two approximately degenerate light flavors at leading chiral order,

\[
B_\theta
\simeq
f_\pi^2m_\pi^2.
\]

Then

\[
\boxed{
H_*
=
\kappa_{\rm dS}
\frac{
f_\pi^2m_\pi^2
}{
3m_{\eta'}\bar M_P^2
}.
}
\]

EXP-100 corresponds to

\[
\boxed{
\kappa_{\rm dS}
=
\frac{\zeta}{2\pi}.
}
\]

The benchmark

\[
\zeta=1
\]

therefore means

\[
\kappa_{\rm dS}=\frac{1}{2\pi},
\]

and reproduces the same EXP-100 numerical result.

---

## 5. Exact microscopic target

The earlier late-de-Sitter comparison requires approximately

\[
\boxed{
\kappa_{\rm dS,target}
\simeq0.131
}
\]

for the two-flavor benchmark.

Equivalently,

\[
\boxed{
\mathcal C_{\rm dS,target}
=
2\kappa_{\rm dS,target}
\simeq0.263
}
\]

when the response is normalized to the one-flavor quantity \(X_q=m_q|\langle\bar q q\rangle|\).

---

## 6. Lattice-to-de-Sitter bridge

A flat-box finite-volume calculation can define

\[
\boxed{
\kappa_{\rm box}
=
-
m_{\eta'}
\lim_{L\to\infty}
L
\left[
\frac{\chi_t(L)}
{\chi_t(\infty)}-1
\right].
}
\]

The independent cosmological prediction additionally requires

\[
\boxed{
\kappa_{\rm dS}
=
{\cal T}_{\rm geom}
\kappa_{\rm box},
}
\]

where

\[
{\cal T}_{\rm geom}
\]

is a calculable geometry/state transfer factor.

The naive identification

\[
{\cal T}_{\rm geom}=1
\]

is not established.

---

## 7. Why this is the preferred final target

The program has now reduced all normalization ambiguity to two independently meaningful calculations:

### QCD finite-volume problem

\[
\boxed{
\kappa_{\rm box}
}
\]

from the \(L\)-dependence of the theta-dependent QCD vacuum sector.

### Curved-background problem

\[
\boxed{
{\cal T}_{\rm geom}
}
\]

from transporting that nonlocal topological response from a flat box to de Sitter.

Then

\[
\boxed{
\kappa_{\rm dS}
=
{\cal T}_{\rm geom}\kappa_{\rm box}.
}
\]

No KMS convention or flavor counting can fake agreement after these quantities are separately fixed.

---

## Terminal classification

### Independent hierarchy formula

\[
\boxed{\text{DERIVED CONDITIONALLY}.}
\]

### Flavor/convention ambiguity

\[
\boxed{\text{REMOVED}.}
\]

### Remaining unknowns

\[
\boxed{
\kappa_{\rm box},
\quad
{\cal T}_{\rm geom}.
}
\]

### True verification criterion

The QCD branch predicts the late hierarchy only if the independent product satisfies approximately

\[
\boxed{
\kappa_{\rm dS}\simeq0.131
}
\]

for the two-light-flavor benchmark.
