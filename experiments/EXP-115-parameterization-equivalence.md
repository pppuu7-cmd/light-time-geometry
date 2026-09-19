# EXP-115 — Parameterization equivalence and the true microscopic coefficient

## Objective

Remove a misleading normalization ambiguity between the KMS notation of EXP-100 and the original Urban-Zhitnitsky-style notation.

Show which numerical coefficient is physically invariant.

---

## 1. Covariant response

Use the EXP-113 invariant form

\[
\boxed{
\rho_{\rm top}
=
\mathcal C_{\rm dS}
H
\frac{X_{\rm QCD}}{m_{\eta'}}.
}
\]

The late-scale benchmark requires

\[
\boxed{
\mathcal C_{\rm dS,target}
\simeq0.263.
}
\]

---

## 2. KMS notation

EXP-100 wrote

\[
\rho_{\rm top}
=
\zeta
\frac{H X_{\rm QCD}}
{\pi m_{\eta'}}.
\]

Therefore

\[
\boxed{
\zeta
=
\pi\mathcal C_{\rm dS}.
}
\]

For the target coefficient,

\[
\boxed{
\zeta_{\rm target}
\simeq0.825.
}
\]

---

## 3. Original-style notation

The original finite-manifold ghost parametrization can be written

\[
\rho_{\rm top}
=
2c
H
\frac{X_{\rm QCD}}{m_{\eta'}}.
\]

Therefore

\[
\boxed{
c
=
\frac{\mathcal C_{\rm dS}}{2}.
}
\]

For the same target,

\[
\boxed{
c_{\rm target}
\simeq0.131.
}
\]

Combining,

\[
\boxed{
\zeta
=
2\pi c.
}
\]

Thus

\[
0.825
\]

and

\[
0.131
\]

are the same physical target written in different conventions.

### Result 115A

The appearance of an order-unity \(\zeta\) after introducing the KMS \(2\pi\) factor is not independent evidence for the mechanism.

It is partly a reparameterization of the unknown infrared coefficient.

---

## 4. Flat-box susceptibility slope

For a flat large box, define

\[
\frac{\chi_t(L)}{\chi_t(\infty)}
=
1-\frac{A_\chi}{L}+\cdots.
\]

The natural dimensionless slope is

\[
\boxed{
c_{\rm box}
=
\frac{m_{\eta'}A_\chi}{\hbar c}.
}
\]

The EXP-104 target

\[
A_\chi\simeq0.02705\ {\rm fm}
\]

corresponds to

\[
\boxed{
c_{\rm box}\simeq0.131.
}
\]

This is numerically equal to the original-style target coefficient.

Hence the most transparent flat-space lattice target is not

\[
\zeta\simeq0.825
\]

but

\[
\boxed{
c_{\rm box}\simeq0.13.
}
\]

---

## 5. Geometry-transfer warning

The equality

\[
c_{\rm box}=c_{\rm dS}
\]

is not established.

A flat periodic box and the de Sitter static patch/Euclidean sphere have different global geometry.

Therefore the real predictive chain is

\[
\boxed{
c_{\rm box}
\xrightarrow{
\text{curved-geometry transfer}
}
\mathcal C_{\rm dS}
}
\]

and not a simple identity unless derived.

---

## Terminal classification

### True cosmological target

\[
\boxed{
\mathcal C_{\rm dS}\simeq0.263.
}
\]

### Equivalent original coefficient

\[
\boxed{
c\simeq0.131.
}
\]

### Equivalent EXP-100 coefficient

\[
\boxed{
\zeta\simeq0.825.
}
\]

### Independent significance of the 2pi factor

\[
\boxed{\text{NONE until the geometry transfer is derived}.}
\]
