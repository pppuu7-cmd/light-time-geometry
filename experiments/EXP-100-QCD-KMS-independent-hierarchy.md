# EXP-100 — Independent QCD–KMS derivation of the 10^122 de Sitter information hierarchy

## Objective

Attempt the requested independent derivation of the LTG global capacity without using:

- \(H_0\);
- \(\Omega_\Lambda\);
- the observed dark-energy density;
- the previously inferred \(D_{\rm tot}\).

Use only:

1. low-energy QCD parameters;
2. the Planck scale;
3. a causal-horizon temperature normalization;
4. Einstein/Friedmann self-consistency.

This is a **conditional microscopic derivation** because the required 4D QCD finite-size coefficient is not yet derived from first principles.

---

## 1. QCD topological vacuum-energy input

The Veneziano-ghost / QCD-topological proposal gives a finite-curvature vacuum contribution of the form

\[
\rho_X
\simeq
2c_{\rm top}
\frac{H}{m_{\eta'}}
\left|
m_q\langle\bar q q\rangle
\right|.
\]

The important structural point is

\[
\boxed{
\rho_X\propto H\times\text{QCD}^3.
}
\]

The coefficient \(c_{\rm top}\) encodes the finite-size/topology response and is expected to be dimensionless and order unity in the underlying proposal.

---

## 2. Causal/KMS normalization

A de Sitter or trapping horizon has temperature

\[
\boxed{
k_BT_H
=
\frac{\hbar H}{2\pi}.
}
\]

Independent ghost-dark-energy literature has explicitly generalized the QCD vacuum contribution to be proportional to the Hawking temperature on the trapping horizon rather than to a bare Hubble scale.

Implement that causal normalization by associating the finite infrared inverse length with

\[
\boxed{
L_{\rm KMS}^{-1}
=
\frac{H}{2\pi}.
}
\]

Write the remaining microscopic finite-size coefficient as

\[
\zeta.
\]

Then

\[
\boxed{
\rho_X
=
\zeta
\frac{H}{\pi m_{\eta'}}
X_{\rm QCD},
}
\]

where

\[
X_{\rm QCD}
\equiv
\left|
m_q\langle\bar q q\rangle
\right|.
\]

No cosmological value of \(H\) is inserted here.

---

## 3. Express the QCD factor through GMOR

In the two-light-flavor chiral benchmark,

\[
(m_u+m_d)
|\langle\bar q q\rangle|
\simeq
f_\pi^2m_\pi^2.
\]

Using

\[
m_q\simeq\frac{m_u+m_d}{2},
\]

gives

\[
\boxed{
X_{\rm QCD}
\simeq
\frac12
f_\pi^2m_\pi^2.
}
\]

Therefore

\[
\boxed{
\rho_X
=
\zeta
\frac{Hf_\pi^2m_\pi^2}
{2\pi m_{\eta'}}.
}
\]

---

## 4. Close the system with de Sitter Friedmann dynamics

Use the reduced Planck mass

\[
\bar M_P^2
=
\frac{1}{8\pi G}
\]

and the vacuum-dominated Friedmann equation

\[
\boxed{
H^2
=
\frac{\rho_X}
{3\bar M_P^2}.
}
\]

Substitute the QCD expression:

\[
H^2
=
\frac{1}{3\bar M_P^2}
\zeta
\frac{Hf_\pi^2m_\pi^2}
{2\pi m_{\eta'}}.
\]

Besides the trivial solution \(H=0\), the nonzero self-consistent solution is

\[
\boxed{
H_{\rm QCD-KMS}
=
\zeta
\frac{f_\pi^2m_\pi^2}
{6\pi m_{\eta'}\bar M_P^2}.
}
\]

This is the key result.

The Hubble/de Sitter scale is now generated from microscopic QCD plus gravity.

No \(H_0\) or \(\Lambda_{\rm obs}\) appears on the right-hand side.

---

## 5. Numerical benchmark with no cosmological input

Use representative low-energy values

\[
f_\pi=92.07\ {\rm MeV},
\]

\[
m_\pi=134.9768\ {\rm MeV},
\]

\[
m_{\eta'}=957.78\ {\rm MeV},
\]

\[
\bar M_P=2.435\times10^{18}\ {\rm GeV}.
\]

For

\[
\zeta=1,
\]

the predicted curvature scale is

\[
\boxed{
H_{\rm QCD-KMS}
\simeq
2.19\times10^{-18}\ {\rm s^{-1}}.
}
\]

This number was obtained without using a cosmological expansion measurement.

---

## 6. Independent LTG capacity prediction

For de Sitter,

\[
\boxed{
\ln D_{\rm tot}
=
\frac{S_{\rm dS}}{k_B}
=
\frac{8\pi^2\bar M_P^2}{H^2}.
}
\]

Substituting the independently generated QCD-KMS \(H\) gives

\[
\boxed{
\ln D_{\rm tot}^{\rm QCD-KMS}
\simeq
2.25\times10^{122}
\qquad
(\zeta=1).
}
\]

Thus

\[
\boxed{
D_{\rm tot}^{\rm QCD-KMS}
=
\exp\left(
2.25\times10^{122}
\right).
}
\]

This is the first LTG route in which the exponent of the global Hilbert capacity lands at order \(10^{122}\) without inserting the late cosmological scale.

### Result 100A

\[
\boxed{
\text{independent order-}10^{122}
\text{ hierarchy: PASS conditionally}.
}
\]

---

## 7. Required microscopic coefficient for the previous LTG benchmark

EXP-096 inferred from the representative late de Sitter benchmark

\[
\left(
\ln D_{\rm tot}
\right)_{\rm benchmark}
=
3.3072\times10^{122}.
\]

Since

\[
H\propto\zeta
\]

and therefore

\[
\ln D\propto\zeta^{-2},
\]

the value required to match that benchmark is

\[
\boxed{
\zeta_{\rm match}
=
\sqrt{
\frac{2.2491}{3.3072}
}
\simeq
0.825.
}
\]

This is an order-unity coefficient.

No exponentially small or finely tuned new parameter is required.

---

## 8. Why this is not yet a proof

The derivation depends on four nontrivial assumptions.

### A. 4D Veneziano/QCD finite-size response

The original QCD-topological proposal derives the linear finite-size effect by analogy with controlled 2D calculations.

A complete first-principles 4D finite-volume computation of the coefficient is still missing.

### B. KMS/trapping-horizon identification

The factor

\[
H/(2\pi)
\]

is physically motivated by the horizon temperature and has precedent in ghost-dark-energy work, but identifying it with the precise finite-size scale entering the QCD topological susceptibility is an LTG-specific closure assumption.

### C. GMOR mapping

The reduction

\[
X_{\rm QCD}
\simeq
\frac12f_\pi^2m_\pi^2
\]

is a leading chiral benchmark and carries convention/flavor corrections.

### D. Cosmological viability

Simple QCD ghost-dark-energy cosmologies have known phenomenological problems, including difficulty producing a robust matter-dominated epoch in some formulations.

Therefore reproducing the magnitude is not sufficient.

---

## 9. Falsifiable microscopic target

The derivation isolates one exact quantity that can in principle be computed independently:

\[
\boxed{
\zeta_{\rm 4D\,QCD}.
}
\]

A lattice/finite-volume/topological calculation should determine the leading infrared correction

\[
\Delta\epsilon_{\rm vac}
=
\zeta_{\rm 4D\,QCD}
\frac{H}{\pi m_{\eta'}}
X_{\rm QCD}
+\cdots.
\]

LTG requires approximately

\[
\boxed{
\zeta_{\rm 4D\,QCD}\simeq0.8
}
\]

to match the earlier de Sitter benchmark.

This is now a genuine independent microscopic test.

---

## 10. Terminal classification

### Uses observed cosmological \(H\) or \(\Lambda\) as input

\[
\boxed{\text{NO}.}
\]

### Generates the \(10^{122}\) order independently

\[
\boxed{\text{YES, conditionally}.}
\]

### Exact first-principles prediction

\[
\boxed{\text{NOT YET}.}
\]

### Missing calculation

\[
\boxed{
\text{derive }\zeta_{\rm 4D\,QCD}
\text{ from finite-volume/topological QCD}.
}
\]
