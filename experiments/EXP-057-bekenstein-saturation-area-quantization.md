# EXP-057 — Bekenstein-bound saturation and conditional horizon-area quantization

## Objective

Re-examine the exact LTG bridge from EXP-052,

\[
E_{\rm geom}\tau_{\rm light}
=
\frac{\hbar}{2\pi}\frac{S_H}{k_B},
\]

and ask:

1. Is this relation already known as an entropy bound saturation?
2. If horizon area is quantized, does the LTG bridge become an integer action law?
3. Does that integer determine the cosmological scale?

---

## 1. Bekenstein bound

For a system of total energy \(E\) contained within radius \(R\), the Bekenstein bound is

\[
\boxed{
S
\le
\frac{2\pi k_BER}{\hbar c}.
}
\]

For the horizon compactness energy

\[
E_{\rm geom}(R)
=
\frac{c^4R}{2G},
\]

the right-hand side becomes

\[
\frac{2\pi k_B}{\hbar c}
\frac{c^4R}{2G}
R
=
\frac{\pi k_Bc^3R^2}{G\hbar}.
\]

But the Bekenstein-Hawking entropy of a spherical horizon is

\[
S_H
=
\frac{k_BAc^3}{4G\hbar}
=
\frac{\pi k_Bc^3R^2}{G\hbar}.
\]

Therefore

\[
\boxed{
S_H
=
\frac{2\pi k_BE_{\rm geom}R}{\hbar c}.
}
\]

So the EXP-052 relation is exactly the saturation of the Bekenstein bound by a horizon-scale self-gravitating system.

### Result 057A

The LTG energy-time-entropy identity is physically correct but has established prior art:

\[
\boxed{
\text{EXP-052 bridge}
=
\text{Bekenstein-bound saturation at a horizon}.
}
\]

This clarifies its meaning.

---

## 2. Write the bound in light-time form

Use

\[
\tau_{\rm light}
=
\frac{R}{c}.
\]

Then saturation gives

\[
S_H
=
\frac{2\pi k_BE_{\rm geom}\tau_{\rm light}}{\hbar}.
\]

Therefore

\[
\boxed{
E_{\rm geom}\tau_{\rm light}
=
\frac{\hbar}{2\pi}\frac{S_H}{k_B}.
}
\]

Thus the LTG bridge is the action form of the Bekenstein/holographic saturation condition.

---

## 3. Conditional Bekenstein area spectrum

Bekenstein's original semiclassical area-quantization proposal is

\[
\boxed{
A_n
=
8\pi\ell_P^2 n,
\qquad
n\in\mathbb N,
}
\]

with

\[
\ell_P^2
=
\frac{G\hbar}{c^3}.
\]

Important caveat:

- equal area spacing is a long-standing semiclassical proposal;
- the coefficient \(8\pi\) is not universally accepted across all quantization schemes;
- extending a black-hole area spectrum unchanged to a pure cosmological de Sitter horizon is an additional hypothesis.

The following results are therefore conditional.

---

## 4. Entropy becomes an integer action count

If

\[
A_n=8\pi\ell_P^2n,
\]

then

\[
\frac{S_n}{k_B}
=
\frac{A_n}{4\ell_P^2}
=
\boxed{
2\pi n.
}
\]

EXP-054 found

\[
\frac{|I_E|}{\hbar}
=
\frac{S}{k_B}.
\]

Therefore

\[
\boxed{
|I_E|
=
2\pi n\hbar.
}
\]

This is exactly the action quantization form that was **not** justified by path-integral phase periodicity alone in EXP-054.

The logical direction is now clear:

\[
\boxed{
\text{area quantization}
\Rightarrow
\text{entropy quantization}
\Rightarrow
\text{Euclidean action quantization}.
}
\]

Not the reverse.

---

## 5. Energy-time action becomes n hbar

Using the EXP-052 bridge,

\[
E_{\rm geom}\tau_{\rm light}
=
\frac{\hbar}{2\pi}
\frac{S}{k_B},
\]

and

\[
S/k_B=2\pi n,
\]

we obtain

\[
\boxed{
E_{\rm geom}\tau_{\rm light}
=
n\hbar.
}
\]

This is the cleanest conditional quantized LTG relation obtained so far.

It says that if the horizon area follows the Bekenstein \(8\pi\ell_P^2\) spectrum, then the product

\[
\text{horizon energy}
\times
\text{light-crossing time}
\]

is an integer quantum of action.

### Result 057B

\[
\boxed{
A_n=8\pi\ell_P^2n
\Longrightarrow
E_{\rm geom}\tau_{\rm light}=n\hbar.
}
\]

**CONDITIONAL ANALYTIC PASS.**

---

## 6. Conditional de Sitter curvature spectrum

For a de Sitter horizon,

\[
R=\frac{c}{H},
\]

and

\[
A=4\pi R^2
=
\frac{4\pi c^2}{H^2}.
\]

Set this equal to the conditional area spectrum:

\[
\frac{4\pi c^2}{H_n^2}
=
8\pi\ell_P^2n.
\]

Then

\[
H_n^2
=
\frac{c^2}{2\ell_P^2n}.
\]

Since

\[
\ell_P^2=\frac{G\hbar}{c^3},
\]

one obtains

\[
\boxed{
H_n^2
=
\frac{c^5}{2G\hbar\,n}.
}
\]

Equivalently,

\[
\boxed{
\Lambda_n
=
\frac{3c^3}{2G\hbar\,n}
}
\]

for the convention \(\Lambda=3H^2/c^2\).

So area quantization would discretize the cosmological constant.

---

## 7. Does this predict the observed scale?

No.

The integer

\[
n
\]

is not determined by the area spectrum itself.

A very small \(H\) simply corresponds to a very large \(n\).

Thus the continuous freedom

\[
H
\]

has become the discrete freedom

\[
n.
\]

This is progress in structure, but not scale selection.

### Result 057C

\[
\boxed{
\text{area quantization discretizes the vacuum scale
but does not select the occupied level}.
}
\]

The active problem becomes:

\[
\boxed{
\text{what global causal principle selects }n?
}
\]

---

## 8. Relation to EXP-056

EXP-056 found another global quantized scale-sensitive mechanism:

\[
f=nq
\]

for four-form flux.

The two branches have the same structural limitation.

### Four-form branch

\[
\text{integer }n
+
\text{charge spacing }q
\to
\Lambda_n.
\]

### Horizon-area branch

\[
\text{integer }n
+
\text{area quantum}
\to
H_n.
\]

In both cases, quantization exists but the state-selection rule remains missing.

The area branch is cleaner for LTG because the quantum is built from

\[
G,\hbar,c
\]

rather than a new flux charge \(q\), but its applicability to cosmological horizons is not established.

---

## 9. Strongest conditional synthesis

Under the Bekenstein area-spectrum hypothesis,

\[
\boxed{
\frac{A}{8\pi\ell_P^2}
=
\frac{1}{2\pi}\frac{S}{k_B}
=
\frac{1}{2\pi}\frac{|I_E|}{\hbar}
=
\frac{E_{\rm geom}\tau_{\rm light}}{\hbar}
=
n.
}
\]

This unifies:

- area;
- entropy;
- gravitational action;
- energy;
- light-crossing time;

into one integer.

This is the most compact mathematical realization yet of the LTG light-time-energy-geometry idea.

But it is conditional on a known semiclassical quantization proposal and does not determine the integer.

---

## 10. Terminal classification

### EXP-052 bridge as new identity

**NOT NOVEL:** it is Bekenstein-bound saturation.

### Conditional horizon area quantization

**PHYSICALLY MOTIVATED / NOT ESTABLISHED UNIVERSALLY.**

### Integer energy-time law

\[
E_{\rm geom}\tau_{\rm light}=n\hbar
\]

**CONDITIONAL PASS.**

### Cosmological scale prediction

**FAIL:** \(n\) is not selected.

## Next discriminating gate

Do not search for another way to write \(n\).

Search for a global causal state-selection principle that chooses one allowed integer level.

Possible tests:

1. semiclassical path-integral weighting over \(n\);
2. a past-future boundary transition amplitude;
3. flux/area matching between an early quantum boundary and future horizon;
4. a dynamical selection rule with stable transitions \(n\to n\pm1\).

A valid result must prefer a finite \(n\) without inserting the observed \(H\).
