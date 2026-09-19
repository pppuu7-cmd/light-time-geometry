# EXP-114 — Local-covariant EFT no-go for a linear-H QCD vacuum term

## Objective

Determine whether the key EXP-100 scaling

\[
\rho_{\rm top}
\sim
H\Lambda_{\rm QCD}^3
\]

could arise from an ordinary local generally covariant low-energy effective action of a gapped QCD sector.

---

## 1. Local covariant derivative expansion

After integrating out massive degrees of freedom on a smooth background, an ordinary local gravitational effective action has schematic form

\[
W_{\rm local}[g]
=
\int d^4x\sqrt{-g}
\left[
-\rho_0
+
a_1R
+
a_2R^2
+
a_3R_{\mu\nu}R^{\mu\nu}
+
a_4R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
+
\cdots
\right].
\]

The coefficients contain powers/logarithms of QCD scales.

There is no local generally covariant scalar built only from a smooth metric that is linear in one derivative of the scale factor.

Curvature starts at two derivatives.

---

## 2. de Sitter specialization

For four-dimensional de Sitter,

\[
R=12H^2,
\]

\[
R_{\mu\nu}R^{\mu\nu}
=
36H^4,
\]

\[
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
=
24H^4.
\]

Therefore an analytic local curvature expansion generates

\[
\boxed{
\Delta\rho_{\rm local}
=
b_1\Lambda_{\rm QCD}^2H^2
+
b_2H^4
+
b_3\frac{H^6}{\Lambda_{\rm QCD}^2}
+\cdots,
}
\]

not

\[
H\Lambda_{\rm QCD}^3.
\]

### Result 114A

\[
\boxed{
H\Lambda_{\rm QCD}^3
\text{ cannot arise from the ordinary analytic local metric EFT.}
}
\]

---

## 3. Possible escape routes

A term linear in \(H\) can arise only if at least one local-EFT assumption fails.

Examples:

1. a genuinely nonlocal functional of the metric;
2. dependence on global topology or finite manifold size;
3. a state-dependent horizon/global contribution;
4. a boundary/extrinsic-curvature term;
5. a nonanalytic invariant such as \(\sqrt{R}\), which itself signals nonlocal/nonanalytic infrared physics;
6. an additional preferred timelike structure.

The Veneziano/deformed-QCD mechanism explicitly claims the first two types of infrared/topological physics.

---

## 4. Why the H^2 alternative does not solve the hierarchy

Suppose instead ordinary local QCD generated

\[
\rho_X
=
b\Lambda_{\rm QCD}^2H^2.
\]

Friedmann closure gives

\[
3\bar M_P^2H^2
=
b\Lambda_{\rm QCD}^2H^2.
\]

For \(H\ne0\),

\[
\boxed{
3\bar M_P^2
=
b\Lambda_{\rm QCD}^2.
}
\]

This is false by the enormous Planck/QCD hierarchy unless

\[
b\sim M_P^2/\Lambda_{\rm QCD}^2
\]

is itself huge.

Thus the ordinary \(H^2\) curvature response does not dynamically generate a tiny nonzero de Sitter scale.

### Result 114B

The special linear-in-\(H\) nonlocal scaling is not a cosmetic detail.

It is exactly what permits the QCD/Planck hierarchy to solve for a tiny nonzero \(H\).

---

## 5. Odd-versus-even H diagnostic

A useful conceptual discriminator is

\[
\boxed{
\text{local analytic curvature response}
\Rightarrow
\text{even powers of }H
}
\]

for exact de Sitter,

while

\[
\boxed{
\text{EXP-100 topological response}
\Rightarrow
\text{leading odd/nonanalytic }H.
}
\]

Therefore a successful microscopic calculation must explicitly show how locality/analyticity is evaded.

---

## 6. Consequence for the covariant coefficient

EXP-113 wrote

\[
\rho_{\rm top}^{\rm dS}
=
\mathcal C_{\rm dS}
H
\frac{X_{\rm QCD}}{m_{\eta'}}.
\]

EXP-114 shows that

\[
\mathcal C_{\rm dS}
\]

cannot be extracted from ordinary local heat-kernel/curvature coefficients.

It belongs to a nonlocal/global part of the QCD effective action,

\[
\boxed{
W_{\rm top}^{\rm nonlocal}[g,\mathcal M,\theta].
}
\]

---

## Terminal classification

### Linear-H term from ordinary local covariant QCD EFT

\[
\boxed{\text{NO-GO}.}
\]

### Linear-H term from nonlocal/topological sector

\[
\boxed{\text{POSSIBLE / MUST BE COMPUTED}.}
\]

### Significance

A future derivation of

\[
\mathcal C_{\rm dS}\simeq0.263
\]

would constitute evidence for precisely the nonlocal topological physics on which the QCD-KMS hierarchy mechanism relies.
