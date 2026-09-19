# EXP-055 — Four-volume conjugacy and topological scale-selection no-go

## Objective

Continue EXP-054 by testing two ways to turn the global action count into a genuine prediction:

1. cosmological constant / spacetime four-volume conjugacy;
2. topological quantization on the Euclidean de Sitter manifold.

The required success criterion is strict:

\[
\text{derive }H_*\text{ or }N
\]

without inserting the observed cosmological scale.

---

## 1. Cosmological constant as a global variable

In unimodular formulations of gravity, the cosmological constant can appear as a global integration constant rather than as a fixed local coupling.

A conjugate global variable is related to spacetime four-volume.

Schematically, the cosmological term in the action is

\[
I_\Lambda
=
-\frac{\Lambda}{8\pi G}V_4
\]

in natural units, up to signature/convention choices.

Thus

\[
\boxed{
\Lambda
\leftrightarrow
\frac{V_4}{8\pi G}
}
\]

forms a global action-conjugate pair in unimodular formulations.

This is established prior art.

---

## 2. Euclidean de Sitter four-volume count

For Euclidean de Sitter \(S^4\),

\[
V_4
=
\frac{24\pi^2}{\Lambda^2}.
\]

Therefore the magnitude of the cosmological-term action is

\[
\frac{\Lambda V_4}{8\pi G}
=
\frac{3\pi}{G\Lambda}.
\]

But EXP-054 found

\[
N
=
\frac{3\pi}{G\Lambda}.
\]

Hence

\[
\boxed{
N
=
\frac{\Lambda V_4}{8\pi G\hbar}
}
\]

with \(\hbar\) restored.

So the same global count can be written as:

\[
\boxed{
N
=
\frac{S_{\rm dS}}{k_B}
=
\frac{|I_E|}{\hbar}
=
\frac{\Lambda V_4}{8\pi G\hbar}.
}
\]

### Result 055A

Four-volume conjugacy gives a fourth exact representation of the same dimensionless quantity.

It does **not** independently determine the quantity.

---

## 3. Quantum uncertainty does not select the mean Lambda

If \(\Lambda\) and a four-volume variable are canonically conjugate in a chosen unimodular quantization, one expects a schematic uncertainty relation of the form

\[
\Delta\Lambda\,\Delta V_4
\sim
G\hbar
\]

up to convention-dependent numerical factors.

For a very large four-volume, this can make the cosmological constant sharply defined.

But a small uncertainty

\[
\Delta\Lambda
\]

does not determine the expectation value

\[
\langle\Lambda\rangle.
\]

Thus four-volume conjugacy can explain why a global \(\Lambda\) may behave as a sharply defined constant for a huge universe, but it does not explain why its value is small and positive.

### Result 055B

\[
\boxed{
\text{conjugacy can constrain fluctuations, not the mean scale.}
}
\]

The initial/global state still has to select the mean value.

---

## 4. Topological quantization on S4

The Euclidean de Sitter manifold is topologically

\[
S^4.
\]

Its Euler characteristic is

\[
\boxed{
\chi(S^4)=2.
}
\]

In four dimensions the Gauss-Bonnet-Chern theorem gives

\[
\chi
=
\frac{1}{32\pi^2}
\int d^4x\sqrt g\,
E_4,
\]

where

\[
E_4
=
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
-4R_{\mu\nu}R^{\mu\nu}
+R^2.
\]

For the round \(S^4\),

\[
\boxed{
\int d^4x\sqrt g\,E_4
=
64\pi^2.
}
\]

Crucially, this is independent of the sphere radius \(L\).

### Result 055C

Topology provides a genuine integer:

\[
\boxed{\chi=2}
\]

but it is blind to the de Sitter scale.

Thus pure topology alone cannot determine

\[
H_*,
\qquad
\Lambda,
\qquad
N\sim H_*^{-2}.
\]

---

## 5. Adding a Gauss-Bonnet topological action does not fix L

Suppose one adds in four dimensions

\[
I_{\rm GB}
=
\alpha
\int d^4x\sqrt g\,E_4.
\]

For a closed four-manifold,

\[
I_{\rm GB}
=
32\pi^2\alpha\,\chi.
\]

On \(S^4\),

\[
I_{\rm GB}
=
64\pi^2\alpha.
\]

Because the integral is topological, its variation does not determine the radius of the round \(S^4\) in ordinary four-dimensional gravity.

Thus even if the topological contribution to a quantum phase were quantized, it would only label a sector.

It would not determine the continuous geometric scale.

### Result 055D

\[
\boxed{
\text{topological integer}
\not\Rightarrow
\text{vacuum curvature scale}.
}
\]

---

## 6. Combined no-go

We now have two complementary failures:

### Action / four-volume side

Sensitive to the scale, but continuous:

\[
N\propto\Lambda^{-1}.
\]

### Topology side

Quantized/discrete, but scale blind:

\[
\chi=2.
\]

The missing object must possess both properties simultaneously:

\[
\boxed{
\text{global + quantized + scale-sensitive}.
}
\]

This is a much sharper criterion than "find a global invariant."

---

## 7. Candidate class that meets the structural criterion

A compact gauge flux through a nontrivial cycle can be:

- global;
- quantized;
- energy carrying;
- capable of contributing a vacuum-like stress tensor.

In four spacetime dimensions, a four-form field strength is the minimal concrete example.

This motivates EXP-056:

> test whether quantized four-form flux can fix the vacuum scale without arbitrary continuous parameters, and whether it naturally realizes the LTG pressure-sign branch.

---

## 8. Terminal classification

### Lambda-four-volume conjugacy

**GLOBAL STRUCTURE PASS / SCALE-PREDICTION FAIL.**

### Quantum uncertainty of Lambda

**FLUCTUATION CONTROL POSSIBLE / MEAN VALUE NOT FIXED.**

### Pure topology

**DISCRETENESS PASS / SCALE SENSITIVITY FAIL.**

### Strongest surviving criterion

A successful LTG global invariant must be

\[
\boxed{
\text{global}
+
\text{quantized}
+
\text{scale-sensitive}
}
\]

and must derive a physical scale without using \(H_*\) or \(\Lambda\) as an input.

## Prior-art anchors

- Henneaux-Teitelboim / unimodular gravity: cosmological constant as a global integration constant with four-volume-related conjugate variable.
- Modern unimodular-gravity reviews emphasize that solving the cosmological-constant problem requires a global four-volume constraint or initial-state input.
- Gauss-Bonnet-Chern theorem: the Euler number of \(S^4\) is topological and independent of its radius.
