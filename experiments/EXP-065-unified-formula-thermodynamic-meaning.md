# EXP-065 — Thermodynamic meaning of the unified formula and horizon-level spacing

## Objective

Audit a subtle point in the unified formula:

\[
\frac{S}{2\pi k_B}
=
\frac{|I_E|}{2\pi\hbar}
=
\frac{E_{\rm geom}\tau_{\rm light}}{\hbar}.
\]

Ask whether the energy appearing in the \(E\tau\) term is the same thermodynamic energy that appears in the Euclidean de Sitter partition function.

Then, under the conditional area spectrum, compute the horizon energy-level spacing relative to the Gibbons-Hawking temperature.

---

## 1. de Sitter horizon quantities

For radius

\[
R=\frac{c}{H},
\]

the positive Misner-Sharp/apparent-horizon energy is

\[
\boxed{
E_{\rm MS}
=
\frac{c^4R}{2G}
=
\frac{c^5}{2GH}.
}
\]

The Gibbons-Hawking temperature is

\[
\boxed{
k_BT_H
=
\frac{\hbar H}{2\pi}
=
\frac{\hbar c}{2\pi R}.
}
\]

The entropy is

\[
\boxed{
S_H
=
\frac{\pi k_Bc^3R^2}{G\hbar}.
}
\]

Multiplying,

\[
T_HS_H
=
\frac{c^4R}{2G}
=
E_{\rm MS}.
\]

Hence

\[
\boxed{
E_{\rm MS}=T_HS_H.
}
\]

This is equivalent to the EXP-052 energy-time-entropy bridge.

---

## 2. Euclidean action uses a different thermodynamic energy convention

For Euclidean de Sitter,

\[
\frac{I_E}{\hbar}
=
-\frac{S_H}{k_B}.
\]

The semiclassical partition function is

\[
Z\sim e^{-I_E/\hbar}
=
e^{S_H/k_B}.
\]

Thus the canonical free energy is

\[
F
=
-k_BT_H\ln Z
=
-T_HS_H.
\]

Using

\[
T_HS_H=E_{\rm MS},
\]

we get

\[
\boxed{
F=-E_{\rm MS}.
}
\]

The canonical internal energy inferred from

\[
U=F+T_HS_H
\]

is then

\[
\boxed{
U=0
}
\]

for the pure de Sitter Euclidean saddle in this convention.

### Result 065A

The positive quantity

\[
E_{\rm geom}=E_{\rm MS}
\]

in the LTG \(E\tau\) term is **not** the same object as the canonical internal energy of the Euclidean de Sitter partition function.

Therefore the unified formula is a numerical/structural equality among differently interpreted quantities, not an identity asserting that one single thermodynamic energy appears everywhere.

This distinction is essential for avoiding overinterpretation.

---

## 3. Conditional horizon spectrum

Assume the Bekenstein-type area spectrum

\[
A_n
=
8\pi\ell_P^2n.
\]

Then

\[
R_n
=
\sqrt{2n}\,\ell_P.
\]

Define Planck time and energy

\[
t_P=\sqrt{\frac{\hbar G}{c^5}},
\qquad
E_P=\sqrt{\frac{\hbar c^5}{G}}.
\]

Then

\[
\boxed{
\tau_n
=
\frac{R_n}{c}
=
\sqrt{2n}\,t_P,
}
\]

\[
\boxed{
H_n
=
\frac{1}{\sqrt{2n}\,t_P},
}
\]

and

\[
\boxed{
E_n
=
E_{\rm MS}(R_n)
=
E_P\sqrt{\frac n2}.
}
\]

The exact action relation remains

\[
E_n\tau_n=n\hbar.
\]

---

## 4. Neighboring-level spacing

The positive quasi-local energy gap is

\[
\Delta E_n
=
E_{n+1}-E_n
=
\frac{E_P}{\sqrt2}
\left(
\sqrt{n+1}-\sqrt n
\right).
\]

The horizon thermal energy at level \(n\) is

\[
k_BT_n
=
\frac{E_P}{2\pi\sqrt{2n}}.
\]

Therefore

\[
\boxed{
\frac{\Delta E_n}{k_BT_n}
=
2\pi\sqrt n
\left(
\sqrt{n+1}-\sqrt n
\right)
}
\]

or equivalently

\[
\boxed{
\frac{\Delta E_n}{k_BT_n}
=
\frac{2\pi\sqrt n}{\sqrt{n+1}+\sqrt n}.
}
\]

For

\[
n\gg1,
\]

this approaches

\[
\boxed{
\Delta E_n
\approx
\pi k_BT_n.
}
\]

### Result 065B

Under the conditional \(8\pi\ell_P^2\) area spectrum, adjacent quasi-local horizon-energy levels are separated by a thermal-scale quantum of order the Gibbons-Hawking temperature.

This is a consistency-scale relation, not evidence that such transitions physically occur.

---

## 5. Entropy step

The conditional spectrum gives

\[
S_n=2\pi k_Bn.
\]

Therefore every step changes the entropy by

\[
\boxed{
\Delta S=2\pi k_B.
}
\]

In the large-\(n\) limit,

\[
T_n\Delta S
=
2\pi k_BT_n
\approx
2\Delta E_n.
\]

The factor of two is not a contradiction because the horizon first law includes gravitational work / sign conventions and the Misner-Sharp energy is not identical to the Euclidean canonical internal energy.

This again warns against treating all entries in the unified formula as one ordinary mechanical system.

---

## 6. Does thermal detailed balance select a huge n?

No state-selection rule follows from the level spacing alone.

A thermal transition model would require:

- a specified Hamiltonian;
- transition matrix elements;
- a bath/environment definition;
- the correct gravitational first-law sign and work terms.

The fact that

\[
\Delta E_n\sim k_BT_n
\]

only says that the conditional spectrum is thermodynamically natural in scale.

It does not select a finite large \(n\).

---

## 7. Terminal classification

### Unified formula as literal identity of one thermodynamic energy

\[
\boxed{\text{NO}.}
\]

The quantities have different physical roles.

### Numerical/structural equality

\[
\boxed{\text{YES}.}
\]

The horizon geometry links them exactly under the stated assumptions.

### Conditional adjacent-level gap

\[
\boxed{
\Delta E_n\to\pi k_BT_n
}
\]

for large \(n\).

**CONDITIONAL ANALYTIC PASS.**

### New state-selection mechanism

\[
\boxed{\text{NOT OBTAINED}.}
\]

## Consequence for LTG

The unified formula should be presented as a common dimensionless horizon variable, not as proof that entropy, Euclidean action and quasi-local energy are literally the same physical observable.
