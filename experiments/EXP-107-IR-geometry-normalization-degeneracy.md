# EXP-107 — IR geometry normalization degeneracy of the QCD-KMS hierarchy

## Objective

Audit a hidden normalization in EXP-100.

The original QCD finite-size proposal is naturally written in terms of a compactification/infrared length \(L_{\rm IR}\), while EXP-100 identified this with the de Sitter KMS thermal length

\[
L_{\rm KMS}=\frac{2\pi}{H}.
\]

Test which parameter combination is actually predicted.

---

## 1. General finite-size form

Write the topological vacuum term as

\[
\boxed{
\rho_X
=
C_{\rm top}
\frac{X_{\rm QCD}}
{m_{\eta'}L_{\rm IR}},
}
\]

where

\[
X_{\rm QCD}
=
|m_q\langle\bar qq\rangle|.
\]

Parameterize the cosmological infrared map as

\[
\boxed{
L_{\rm IR}
=
\frac{\lambda}{H}.
}
\]

Then

\[
\boxed{
\rho_X
=
C_{\rm eff}
H
\frac{X_{\rm QCD}}
{m_{\eta'}},
\qquad
C_{\rm eff}
\equiv
\frac{C_{\rm top}}{\lambda}.
}
\]

Only the ratio \(C_{\rm top}/\lambda\) enters the background cosmology.

---

## 2. EXP-100 convention

EXP-100 used

\[
\rho_X
=
\zeta
\frac{H X_{\rm QCD}}
{\pi m_{\eta'}}.
\]

Therefore

\[
\boxed{
C_{\rm eff}
=
\frac{\zeta}{\pi}.
}
\]

The previously required value

\[
\zeta_{\rm match}\simeq0.825
\]

corresponds to

\[
\boxed{
C_{\rm eff,match}
\simeq0.2626.
}
\]

This is the actual coefficient constrained by the cosmological scale.

---

## 3. KMS choice is not a microscopic QCD derivation

The de Sitter horizon has a thermal periodicity

\[
\beta_H
=
\frac{2\pi}{H}.
\]

Thus

\[
\lambda=2\pi
\]

is geometrically natural for thermal/KMS physics.

However the original ghost/topological finite-size proposal does not derive that the non-dispersive QCD sector responds specifically to the Euclidean thermal circumference rather than to, for example,

- the horizon radius \(H^{-1}\);
- a spatial compactification length;
- a causal-diamond diameter;
- another topology-dependent global length.

The original compact-FLRW treatment explicitly introduces an unknown geometry-dependent function because the exact propagator/subtraction problem is not solved.

### Result 107A

\[
\boxed{
L_{\rm QCD}=2\pi/H
}
\]

is a physically motivated LTG closure, not a first-principles result of 4D QCD.

---

## 4. Hierarchy sensitivity

From Friedmann closure,

\[
H
=
\frac{C_{\rm eff}X_{\rm QCD}}
{3m_{\eta'}\bar M_P^2}.
\]

Therefore

\[
\boxed{
\ln D_{\rm tot}
\propto
C_{\rm eff}^{-2}.
}
\]

An order-unity ambiguity in the geometry normalization produces an order-unity squared ambiguity in the coefficient multiplying the \(10^{122}\) hierarchy.

It does not normally change the exponent \(122\), because that exponent primarily comes from the QCD/Planck hierarchy.

But it prevents an exact parameter-free prediction.

---

## 5. What a lattice calculation can and cannot determine

A flat finite-box lattice calculation can determine a coefficient associated with its own box geometry,

\[
C_{\rm top}^{\rm box}.
\]

It cannot by itself determine

\[
\lambda_{\rm cosmology}.
\]

A complete prediction therefore requires two independent steps:

\[
\boxed{
\text{QCD topology}
\to
C_{\rm top}^{\rm box}
}
\]

and

\[
\boxed{
\text{causal/global geometry}
\to
\lambda
\text{ and the box-to-cosmology map}.
}
\]

Only their ratio predicts \(H\).

---

## 6. Refined falsification target

The microphysical target should no longer be stated simply as

\[
\zeta_{\rm 4D\,QCD}\simeq0.825.
\]

The invariant target is

\[
\boxed{
C_{\rm eff}
=
C_{\rm top}/\lambda
\simeq0.263
}
\]

in the conventions of EXP-100.

A lattice result can test \(C_{\rm top}\).

A separate curved-background/topological calculation must test \(\lambda\).

---

## Terminal classification

### KMS geometry normalization

\[
\boxed{\text{PHYSICALLY MOTIVATED / NOT DERIVED}.}
\]

### Exact coefficient in EXP-100

\[
\boxed{\text{GEOMETRY-MICROPHYSICS DEGENERATE}.}
\]

### Robust achievement

The QCD/Planck hierarchy still naturally generates the order

\[
10^{122}
\]

for order-unity infrared coefficients.

### Exact prediction

\[
\boxed{\text{NOT YET}.}
\]
