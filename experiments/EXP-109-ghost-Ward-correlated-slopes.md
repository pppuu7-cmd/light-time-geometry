# EXP-109 — Ward-identity signature of the original Veneziano-ghost finite-size mechanism

## Objective

Resolve the ambiguity identified in EXP-106 by checking the original Urban-Zhitnitsky mechanism itself.

The key question is whether its proposed \(1/L\) effect is:

1. topological-contact-only, or
2. accompanied by the same leading finite-size shift in the chiral condensate.

---

## 1. QCD Ward identity

For light quarks,

\[
\boxed{
\chi_t
=
m_q\langle\bar q q\rangle
+
O(m_q^2)
}
\]

in the convention used by the original ghost analysis.

Therefore, at fixed quark mass,

\[
\boxed{
\frac{\Delta\chi_t}{\chi_t}
=
\frac{\Delta\langle\bar q q\rangle}
{\langle\bar q q\rangle}
+
O(m_q).
}
\]

The original Urban-Zhitnitsky finite-volume discussion explicitly uses this relation and argues, from the solvable 2D analogue, that the chiral condensate itself acquires a linear inverse-size correction.

---

## 2. Consequence for GMOR

At leading chiral order,

\[
M_\pi^2F_\pi^2
=
-(m_u+m_d)\langle\bar q q\rangle.
\]

At fixed quark masses,

\[
\boxed{
\frac{\Delta(M_\pi^2F_\pi^2)}
{M_\pi^2F_\pi^2}
=
\frac{\Delta\langle\bar q q\rangle}
{\langle\bar q q\rangle}.
}
\]

Combine with the Ward identity:

\[
\boxed{
\frac{\Delta\chi_t}{\chi_t}
\simeq
\frac{\Delta\Sigma}{\Sigma}
\simeq
\frac{\Delta(M_\pi^2F_\pi^2)}
{M_\pi^2F_\pi^2}.
}
\]

### Result 109A — correlated-slope prediction

For the original ghost mechanism, the natural leading signature is

\[
\boxed{
A_\chi
\simeq
A_\Sigma
\simeq
A_{M_\pi^2F_\pi^2}.
}
\]

This favors Branch B of EXP-106 over a purely isolated susceptibility shift.

---

## 3. Ratio prediction

Define

\[
R_\chi
=
\frac{\chi_t}
{M_\pi^2F_\pi^2}.
\]

If the same \(1/L\) factor multiplies numerator and denominator,

\[
\boxed{
R_\chi(L)
=
R_\chi(\infty)
+
O(L^{-2},e^{-m_\pi L}).
}
\]

Thus the ratio proposed in EXP-105 can cancel the very anomalous effect that EXP-100 requires.

### Result 109B

\[
\boxed{
\text{a null }1/L\text{ signal in }R_\chi
\text{ does not falsify the original ghost mechanism}.
}
\]

---

## 4. Revised physical-QCD lattice signature

The prospectively preferred signature is now the correlated pattern

\[
\boxed{
A_\chi
=
A_\Sigma
=
A_{M_\pi^2F_\pi^2}
\ne0,
}
\]

together with

\[
\boxed{
A_{R_\chi}\simeq0.
}
\]

If the finite-size correction is also a pure common rescaling of the full theta-dependent topological amplitude, then

\[
\boxed{
A_{b_2}\simeq0.
}
\]

Therefore the strong signature vector is

\[
\boxed{
(
A_\chi,\,
A_\Sigma,\,
A_{M_\pi^2F_\pi^2},\,
A_{R_\chi},\,
A_{b_2}
)
\sim
(
A,\,
A,\,
A,\,
0,\,
0
).
}
\]

---

## 5. LTG numerical target under EXP-100 normalization

Under the KMS-normalized benchmark,

\[
A
=
\frac{\zeta_{\rm LTG}\hbar c}
{2\pi m_{\eta'}}.
\]

For

\[
\zeta_{\rm LTG}=0.825,
\]

\[
\boxed{
A\simeq0.02705\ {\rm fm}.
}
\]

Thus at a spatial length \(L\),

\[
\boxed{
\frac{\Delta\chi_t}{\chi_t}
\simeq
\frac{\Delta\Sigma}{\Sigma}
\simeq
-\frac{0.02705\ {\rm fm}}{L}.
}
\]

The sign follows the particular EXP-104 transfer convention and should be checked against the final curved-background microscopic derivation.

---

## 6. Important limitation

The equal-slope relation follows from combining:

- the light-quark Ward identity;
- GMOR;
- the assumption that the anomalous finite-size effect is represented by the same leading shift of the condensate/topological amplitude.

It does not prove that real 4D QCD has such a \(1/L\) correction.

---

## Terminal classification

### Original ghost mechanism closer to Branch A or B?

\[
\boxed{\text{BRANCH B / CHIRAL CO-SHIFT IS THE NATURAL READING}.}
\]

### EXP-105 ratio as primary test

\[
\boxed{\text{DOWNGRADED}.}
\]

### Stronger prospective test

\[
\boxed{
A_\chi\simeq A_\Sigma\simeq A_{M_\pi^2F_\pi^2},
\qquad
A_{R_\chi}\simeq A_{b_2}\simeq0.
}
\]
