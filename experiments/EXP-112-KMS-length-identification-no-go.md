# EXP-112 — KMS-length identification no-go for the QCD topological Casimir mechanism

## Objective

Test whether the geometric identification used in EXP-100,

\[
L_{\rm QCD}
=
\beta_{\rm dS}
=
\frac{2\pi}{H},
\]

can be derived from the controlled deformed-QCD topological Casimir mechanism.

---

## 1. Two distinct lengths in deformed QCD

The controlled deformed-QCD construction uses a compactified direction with a small circumference to make the gauge theory weakly coupled while preserving confinement/topological structure.

The topological Casimir test then introduces a **different, large spatial size** \(\mathbb L\) and finds

\[
\Delta E
\sim
\frac{1}{\mathbb L}
\]

instead of the ordinary massive-theory expectation

\[
e^{-m\mathbb L}.
\]

Thus the controlled result distinguishes:

\[
\boxed{
L_{\rm compact}
\neq
\mathbb L_{\rm Casimir}.
}
\]

The existence of a compact Euclidean circle does not imply that the large-distance topological Casimir scale is equal to its circumference.

---

## 2. de Sitter has several inequivalent natural lengths

For the four-dimensional static patch,

\[
ds^2
=
-(1-H^2r^2)dt^2
+
\frac{dr^2}{1-H^2r^2}
+
r^2d\Omega_2^2.
\]

The areal horizon radius is

\[
\boxed{
R_H=H^{-1}.
}
\]

On a constant-static-time slice, set

\[
r=H^{-1}\sin\chi.
\]

Then

\[
dl^2
=
H^{-2}
\left(
d\chi^2+\sin^2\chi\,d\Omega_2^2
\right),
\qquad
0\le\chi\le\frac{\pi}{2}.
\]

Therefore the proper radial distance from the center to the horizon is

\[
\boxed{
L_{\rm radial}
=
\frac{\pi}{2H}.
}
\]

A full geodesic scale across the corresponding \(S^3\)-type spatial geometry is of order

\[
\boxed{
L_{\rm spatial}
=
\frac{\pi}{H}.
}
\]

Euclidean regularity fixes the KMS period

\[
\boxed{
\beta_H
=
\frac{2\pi}{H}.
}
\]

Hence four equally natural geometric scales differ by factors

\[
1,\quad
\frac{\pi}{2},\quad
\pi,\quad
2\pi.
\]

---

## 3. The Euclidean thermal circle is not automatically the topological-Casimir spatial cycle

Euclidean de Sitter is the compact sphere \(S^4\).

The Euclidean static-patch time circle arises from the polar-angle-type coordinate required for smoothness at the horizon.

It is not automatically the same geometric object as a nontrivial spatial compactification length or the large spatial size \(\mathbb L\) used in the deformed-QCD Casimir calculation.

Therefore:

\[
\boxed{
\beta_H=2\pi/H
}
\]

is an exact thermal-geometric fact,

but

\[
\boxed{
L_{\rm topological\ Casimir}=\beta_H
}
\]

does not follow.

### Result 112A

\[
\boxed{
\text{KMS period does not uniquely determine the QCD topological finite-size length.}
}
\]

---

## 4. Numerical hierarchy consequence

Write generally

\[
L_{\rm IR}
=
\frac{\lambda_{\rm geom}}{H}.
\]

Then

\[
\rho_X
=
\frac{C_{\rm top}}{\lambda_{\rm geom}}
H
\frac{X_{\rm QCD}}{m_{\eta'}}.
\]

The cosmology depends only on

\[
\boxed{
C_{\rm eff}
=
\frac{C_{\rm top}}{\lambda_{\rm geom}}.
}
\]

Because

\[
\ln D_{\rm tot}\propto C_{\rm eff}^{-2},
\]

choosing

\[
\lambda_{\rm geom}=1
\]

versus

\[
2\pi
\]

changes the information count by a factor

\[
(2\pi)^2.
\]

That is large enough to move a benchmark from order \(10^{120}\) to order \(10^{122}\).

### Result 112B

The exact “122” agreement cannot be attributed to de Sitter KMS periodicity until the topological-QCD response to the curved geometry is derived.

---

## 5. Stronger formulation

The physically meaningful calculation should avoid introducing an arbitrary scalar length \(L_{\rm IR}\).

Instead compute the QCD topological effective action directly on the curved/global background,

\[
W_{\rm top}[g,\mathcal M,\theta].
\]

Then extract the finite-curvature vacuum response from

\[
\Delta\rho_{\rm top}
=
\frac{1}{\sqrt{-g}}
\frac{\delta W_{\rm top}}
{\delta g^{00}}
-
\left(
\text{Minkowski reference}
\right).
\]

This automatically includes:

- curvature;
- topology;
- boundary conditions;
- causal state;
- thermal/KMS structure;

without choosing a hand-made \(L\).

---

## Terminal classification

### \(L_{\rm QCD}=2\pi/H\) from deformed-QCD prior art

\[
\boxed{\text{NO}.}
\]

### KMS period itself

\[
\boxed{\text{EXACT GEOMETRIC FACT}.}
\]

### Identification of KMS period with the non-dispersive QCD finite-size scale

\[
\boxed{\text{EXTRA ASSUMPTION}.}
\]

## Active target

Compute a coordinate-independent de Sitter topological response coefficient directly from the curved QCD effective action.
