# EXP-067 — Can de Sitter Euclidean/adiabatic periodicity derive the 8π area quantum?

## Objective

Test the conditional input used in the unified LTG integer formula,

\[
A_n=8\pi\ell_P^2n,
\]

specifically for a pure de Sitter cosmological horizon.

The goal is to determine whether the \(8\pi\) spacing can be derived uniquely from horizon periodicity / adiabatic invariance, rather than imported from the black-hole Bekenstein spectrum.

---

## 1. de Sitter horizon data

For a four-dimensional de Sitter horizon of radius

\[
R=\frac{c}{H},
\]

use the positive apparent-horizon Misner-Sharp scale

\[
E_{\rm MS}
=
\frac{c^4R}{2G}.
\]

The horizon angular frequency associated with the inverse Euclidean period is

\[
\omega_H
=
\frac{c}{R}
=
H.
\]

The Euclidean time period is

\[
\mathcal T_E
=
\frac{2\pi}{\omega_H}
=
\frac{2\pi R}{c}.
\]

---

## 2. Kunstatter-type adiabatic invariant

A common semiclassical quantization prescription uses

\[
I
=
\int
\frac{dE}{\omega}.
\]

Using

\[
dE_{\rm MS}
=
\frac{c^4}{2G}dR
\]

and

\[
\omega_H=\frac{c}{R},
\]

we obtain

\[
I
=
\int
\frac{c^4}{2G}dR
\frac{R}{c}
=
\frac{c^3R^2}{4G}.
\]

Since

\[
A=4\pi R^2,
\]

this becomes

\[
\boxed{
I
=
\frac{\hbar A}{16\pi\ell_P^2}.
}
\]

Impose Bohr-Sommerfeld/Kunstatter quantization,

\[
I=n\hbar.
\]

Then

\[
\boxed{
A_n
=
16\pi\ell_P^2n.
}
\]

### Result 067A

The simplest pure-de-Sitter adiabatic-invariant calculation gives a \(16\pi\ell_P^2\) spacing, not \(8\pi\ell_P^2\).

---

## 3. Independent literature check

A published calculation of the D-dimensional de Sitter horizon area spectrum using Padmanabhan horizon thermodynamics together with Hod/Kunstatter/Maggiore methods finds

\[
\boxed{
A_n
=
16\pi\ell_P^2n
}
\]

in four-dimensional units.

The same work emphasizes that this spacing is twice the familiar \(8\pi\ell_P^2\) Schwarzschild result.

Other horizon-quantization prescriptions and Kerr-Newman-de-Sitter calculations can recover Bekenstein-type spacings.

Therefore the coefficient is method/horizon dependent in the semiclassical literature.

### Result 067B

\[
\boxed{
8\pi
\text{ is not a uniquely established de Sitter area quantum.}
}
\]

This is a direct novelty/robustness constraint on the LTG integer formula.

---

## 4. Consequence for the unified formula

The structural continuous identity

\[
\boxed{
\frac{S}{2\pi k_B}
=
\frac{E_{\rm geom}\tau_{\rm light}}{\hbar}
}
\]

remains exact for the spherical horizon definitions used by LTG.

For Euclidean de Sitter,

\[
\boxed{
\frac{|I_E|}{2\pi\hbar}
=
\frac{S}{2\pi k_B}
}
\]

also remains exact.

But if the de Sitter area spectrum is

\[
A_n=16\pi\ell_P^2n,
\]

then

\[
\frac{A_n}{8\pi\ell_P^2}=2n.
\]

Hence the LTG common variable is

\[
\boxed{
\mathcal N_{\rm LTG}=2n
}
\]

for this quantization prescription, not \(n\).

Equivalently,

\[
\frac{S_n}{2\pi k_B}
=
\frac{|I_{E,n}|}{2\pi\hbar}
=
\frac{E_{\rm geom}\tau_{\rm light}}{\hbar}
=
2n.
\]

---

## 5. Why the factor-of-two appears

The horizon thermodynamics is not identical to a simple mechanical oscillator.

For de Sitter, the first law includes a pressure-volume term,

\[
T\,dS=dE+P\,dV
\]

in the local horizon thermodynamic formulation.

Different quantization methods choose different combinations of:

- horizon energy;
- work terms;
- transition frequency;
- quasinormal-mode spacing;
- canonical action variable.

Therefore the integer normalization is sensitive to the quantization prescription.

This is not a small bookkeeping issue; it determines whether the common LTG variable equals \(n\), \(2n\), or another scaled integer.

---

## 6. Direct action-variable check

If one uses the Euclidean period itself to form

\[
J
=
\int \mathcal T_E\,dE,
\]

then

\[
J
=
\int
\frac{2\pi R}{c}
\frac{c^4}{2G}dR
=
\frac{\pi c^3R^2}{2G}.
\]

This is

\[
J
=
\frac{A c^3}{8G}.
\]

Bohr-Sommerfeld quantization in the form

\[
J=2\pi n\hbar
\]

again gives

\[
\boxed{
A_n=16\pi\ell_P^2n.
}
\]

So the factor-of-two result is reproduced by the direct period-integral benchmark.

---

## 7. Terminal classification

### Can pure de Sitter horizon periodicity uniquely derive

\[
A_n=8\pi\ell_P^2n?
\]

\[
\boxed{\text{NO}.}
\]

### Does a standard adiabatic-invariant route give a discrete area spectrum?

\[
\boxed{\text{YES}.}
\]

For the benchmark above,

\[
\boxed{
A_n=16\pi\ell_P^2n.
}
\]

### Does the continuous LTG common variable survive?

\[
\boxed{\text{YES}.}
\]

The exact horizon relation among area, entropy, Euclidean action and \(E_{\rm geom}\tau_{\rm light}\) survives.

### Is the identification

\[
\mathcal N_{\rm LTG}=n
\]

universal?

\[
\boxed{\text{NO}.}
\]

It is normalization/quantization-prescription dependent.

---

## 8. Updated strongest formula

The robust formula should therefore be written first in continuous form:

\[
\boxed{
\mathcal N_{\rm LTG}
\equiv
\frac{A}{8\pi\ell_P^2}
=
\frac{S}{2\pi k_B}
=
\frac{|I_E|}{2\pi\hbar}
=
\frac{E_{\rm geom}\tau_{\rm light}}{\hbar}.
}
\]

Only after choosing a specific quantum-area spectrum should one write

\[
\mathcal N_{\rm LTG}
=
\alpha n
\]

with a model-dependent integer normalization \(\alpha\).

Examples:

\[
\alpha=1
\]

for the conditional \(8\pi\) spectrum, while

\[
\alpha=2
\]

for the \(16\pi\) pure-de-Sitter adiabatic spectrum.

## Prior-art anchor

- A. López-Ortega (2009), *Area spectrum of the D-dimensional de Sitter spacetime*, Physics Letters B 682, 85-88, derives a de Sitter area spacing twice the Schwarzschild \(8\pi\) value using an adiabatic-invariant / quasinormal-mode approach.
