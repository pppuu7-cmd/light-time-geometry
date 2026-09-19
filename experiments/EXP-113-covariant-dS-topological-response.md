# EXP-113 — Covariant de Sitter topological-response coefficient

## Objective

Remove the infrared-length convention ambiguity found in EXP-107, EXP-111 and EXP-112.

Replace the heuristic finite-size formula

\[
\rho_X\sim\frac{1}{L}
\]

by a covariant dimensionless response coefficient on the de Sitter background.

---

## 1. QCD dimension-three input

Define

\[
\boxed{
X_{\rm QCD}
=
|m_q\langle\bar q q\rangle|
}
\]

with mass dimension four.

The combination

\[
\boxed{
\frac{X_{\rm QCD}}{m_{\eta'}}
}
\]

has mass dimension three.

A curvature rate \(H\) then produces a dimension-four vacuum density.

Therefore the most general leading linear-curvature topological response can be written

\[
\boxed{
\rho_{\rm top}^{\rm dS}
=
\mathcal C_{\rm dS}
H
\frac{X_{\rm QCD}}{m_{\eta'}}
+
O(H^2).
}
\]

Here

\[
\boxed{
\mathcal C_{\rm dS}
}
\]

is a dimensionless, coordinate-independent coefficient determined by the QCD state on de Sitter.

---

## 2. What C_dS contains

The coefficient may depend on dimensionless global information such as:

- topology;
- vacuum choice;
- theta angle;
- flavor content;
- quark-mass ratios;
- the precise subtraction against Minkowski;
- boundary or horizon conditions.

It is **not** fixed by de Sitter symmetry or dimensional analysis alone.

For the de Sitter-invariant state at \(\theta=0\), it reduces to a pure dimensionless number once QCD parameters are fixed.

---

## 3. Friedmann closure

Use

\[
3\bar M_P^2H^2
=
\rho_{\rm top}^{\rm dS}.
\]

The nonzero solution is

\[
\boxed{
H_*
=
\mathcal C_{\rm dS}
\frac{X_{\rm QCD}}
{3m_{\eta'}\bar M_P^2}.
}
\]

Then

\[
\boxed{
\frac{S_{\rm dS}}{k_B}
=
8\pi^2
\frac{\bar M_P^2}{H_*^2}.
}
\]

Thus a first-principles calculation of one number,

\[
\mathcal C_{\rm dS},
\]

determines the entire late de Sitter hierarchy.

---

## 4. Required value

Using the same QCD benchmark and the previously used late-de-Sitter comparison scale, the required invariant coefficient is

\[
\boxed{
\mathcal C_{\rm dS,target}
\simeq
0.263.
}
\]

This is the convention-independent target.

---

## 5. Relation to earlier parameterizations

### EXP-100 KMS notation

\[
\rho_X
=
\zeta
\frac{H X_{\rm QCD}}
{\pi m_{\eta'}},
\]

so

\[
\boxed{
\mathcal C_{\rm dS}
=
\frac{\zeta}{\pi}.
}
\]

Thus

\[
\zeta_{\rm target}\simeq0.825.
\]

### Original Urban-Zhitnitsky-style notation

With

\[
\rho_X
\simeq
2c
H
\frac{X_{\rm QCD}}{m_{\eta'}},
\]

one has

\[
\boxed{
\mathcal C_{\rm dS}=2c.
}
\]

Therefore

\[
\boxed{
c_{\rm target}
\simeq0.131.
}
\]

The numerical values

\[
0.825
\]

and

\[
0.131
\]

are not two different physical predictions.

They are parameterizations of the same invariant target

\[
\boxed{
\mathcal C_{\rm dS}\simeq0.263.
}
\]

### Result 113A

The earlier apparent significance of the \(2\pi\) KMS normalization is largely a parameterization issue once the unknown microscopic coefficient is kept explicit.

---

## 6. Relation to a flat finite-box lattice coefficient

If physical QCD on a large spatial box obeys

\[
\frac{\Delta\chi_t}{\chi_t}
=
-\frac{A_\chi}{L}
+\cdots,
\]

define the dimensionless box coefficient

\[
\boxed{
c_{\rm box}
=
\frac{m_{\eta'}A_\chi}{\hbar c}.
}
\]

The EXP-104 benchmark

\[
A_\chi\simeq0.02705\ {\rm fm}
\]

corresponds to

\[
\boxed{
c_{\rm box}\simeq0.131.
}
\]

Numerically this equals the original-style

\[
c_{\rm target}
=
\mathcal C_{\rm dS,target}/2.
\]

But equality between

\[
c_{\rm box}
\]

and the curved de Sitter response coefficient divided by two is itself a **geometry-transfer hypothesis**.

A lattice box can measure \(c_{\rm box}\).

Only a curved-background/global calculation can establish the map to

\[
\mathcal C_{\rm dS}.
\]

---

## 7. Clean hierarchy of tests

The independent LTG/QCD route now has three logically distinct gates.

### Gate A — physical-QCD power law

Does

\[
c_{\rm box}\ne0
\]

exist in real 4D QCD?

### Gate B — geometry transfer

Does curved de Sitter QCD imply

\[
\mathcal C_{\rm dS}
=
{\cal T}_{\rm geom}
c_{\rm box}
\]

with a calculable transfer factor?

### Gate C — numerical value

Does the resulting coefficient satisfy

\[
\boxed{
\mathcal C_{\rm dS}\simeq0.263?
}
\]

Only if all three pass is the \(10^{122}\) scale independently predicted.

---

## 8. Why this formulation is stronger

It eliminates the unphysical question

> Is the correct infrared length \(H^{-1}\), \(\pi/(2H)\), or \(2\pi/H\)?

The answer is encoded in the curved effective action and therefore in

\[
\mathcal C_{\rm dS}.
\]

No coordinate length has to be chosen by hand.

---

## Terminal classification

### Convention-independent microscopic target

\[
\boxed{
\mathcal C_{\rm dS}\simeq0.263.
}
\]

### Current first-principles value

\[
\boxed{\text{UNKNOWN}.}
\]

### Exact independent \(10^{122}\) prediction

\[
\boxed{\text{NOT YET}.}
\]

## Strongest next calculation

Compute the coefficient of the term linear in \(H\) in the QCD topological effective action directly on a de Sitter/static-patch or Euclidean-\(S^4\) background.
