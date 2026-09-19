# EXP-068 — Quantum-correction robustness of the unified LTG formula

## Objective

Test whether the current LTG common-variable identity

\[
\frac{A}{8\pi\ell_P^2}
=
\frac{S}{2\pi k_B}
=
\frac{|I_E|}{2\pi\hbar}
=
\frac{E_{\rm geom}\tau_{\rm light}}{\hbar}
\]

can be exact in quantum gravity, or whether it is only a leading semiclassical relation.

---

## 1. Semiclassical area law

At leading Einstein-gravity order,

\[
S_{\rm BH}
=
\frac{k_BA}{4\ell_P^2}.
\]

Therefore

\[
\boxed{
\frac{S_{\rm BH}}{2\pi k_B}
=
\frac{A}{8\pi\ell_P^2}.
}
\]

This is the first equality in the LTG chain.

---

## 2. Generic quantum correction

Quantum fields and quantum-gravity fluctuations generically produce corrections of schematic form

\[
\boxed{
\frac{S}{k_B}
=
\frac{A}{4\ell_P^2}
+
\alpha\ln\left(\frac{A}{\ell_P^2}\right)
+
\beta
+
O\left(\frac{\ell_P^2}{A}\right).
}
\]

The coefficient \(\alpha\) is generally theory- and field-content-dependent.

Then

\[
\frac{S}{2\pi k_B}
=
\frac{A}{8\pi\ell_P^2}
+
\frac{\alpha}{2\pi}
\ln\left(\frac{A}{\ell_P^2}\right)
+
\frac{\beta}{2\pi}
+\cdots.
\]

Therefore

\[
\boxed{
\frac{S}{2\pi k_B}
\neq
\frac{A}{8\pi\ell_P^2}
}
\]

beyond leading order unless all corrections vanish or the geometric side is correspondingly generalized.

### Result 068A

The simple LTG area-information equality is **not an exact universal quantum identity**.

It is a leading semiclassical Einstein-gravity relation.

---

## 3. Define a quantum discrepancy

Define

\[
\boxed{
\Delta_{\rm qLTG}
\equiv
\frac{S}{2\pi k_B}
-
\frac{A}{8\pi\ell_P^2}.
}
\]

At one-loop/logarithmic order,

\[
\boxed{
\Delta_{\rm qLTG}
=
\frac{\alpha}{2\pi}
\ln\left(\frac{A}{\ell_P^2}\right)
+
\frac{\beta}{2\pi}
+\cdots.
}
\]

This gives a clean way to state the limitation of the classical unified formula.

For macroscopic horizons,

\[
A\gg\ell_P^2,
\]

the correction is subleading relative to the leading area term, even though the logarithm can be large.

---

## 4. Euclidean action also receives quantum corrections

The semiclassical partition function has schematic form

\[
Z
\sim
e^{-I_E^{\rm cl}/\hbar}
Z_{\rm 1-loop}
Z_{\rm higher}.
\]

Thus

\[
-\ln Z
=
\frac{I_E^{\rm cl}}{\hbar}
-
\ln Z_{\rm 1-loop}
+\cdots.
\]

The entropy derived from the full partition function therefore includes loop corrections.

Hence the classical identity

\[
\frac{|I_E^{\rm cl}|}{\hbar}
=
\frac{S_{\rm cl}}{k_B}
\]

does not imply

\[
\frac{|I_E^{\rm cl}|}{\hbar}
=
\frac{S_{\rm quantum}}{k_B}.
\]

The effective action itself must be corrected consistently.

### Result 068B

The action-information equality can survive only in a generalized effective-action sense; it is not exact if one side is kept classical while the other includes quantum corrections.

---

## 5. Energy-time side

The classical quasi-local horizon energy is

\[
E_{\rm MS}
=
\frac{c^4R}{2G}
\]

in Einstein gravity.

Then

\[
\frac{E_{\rm MS}\tau}{\hbar}
=
\frac{A}{8\pi\ell_P^2}.
\]

If the gravitational effective action contains higher-curvature terms or quantum backreaction, then:

- the field equations change;
- the horizon entropy becomes Wald/generalized entropy rather than simply \(A/4G\hbar\);
- the appropriate quasi-local energy can also change.

Therefore the simple classical \(E_{\rm MS}\tau\) term need not remain equal to the full quantum entropy count.

### Result 068C

The full four-way LTG equality is best regarded as a **semiclassical Einstein-horizon identity**, not a nonperturbative quantum-gravity theorem.

---

## 6. Generalized route

A more robust future formulation would replace the raw area term by generalized gravitational entropy,

\[
S_{\rm grav}
=
S_{\rm Wald}
+
S_{\rm quantum/out}
+\cdots.
\]

Then define

\[
\boxed{
\mathcal N_{\rm gen}
\equiv
\frac{S_{\rm gen}}{2\pi k_B}.
}
\]

The research question becomes whether one can derive generalized counterparts

\[
\mathcal N_{\rm gen}
\stackrel{?}{=}
\frac{|I_{\rm eff}|}{2\pi\hbar}
\stackrel{?}{=}
\frac{E_{\rm eff}\tau_{\rm causal}}{\hbar}
\]

for a controlled class of quantum/effective gravitational theories.

This would be a genuinely stronger theorem than the current Einstein-level formula.

---

## 7. Implication for area quantization

If entropy is corrected,

\[
S_n
=
2\pi k_B n
\]

does not automatically imply the simple equally spaced area spectrum

\[
A_n=8\pi\ell_P^2n.
\]

Instead the area levels would satisfy an implicit corrected relation,

\[
\frac{A_n}{4\ell_P^2}
+
\alpha\ln\left(\frac{A_n}{\ell_P^2}\right)
+\cdots
=
2\pi n.
\]

Hence even if entropy/action were exactly quantized, the area spacing would generally cease to be exactly constant.

### Result 068D

\[
\boxed{
\text{quantized information/action}
\not\Rightarrow
\text{exactly equally spaced area}
}
\]

once quantum corrections are included.

---

## 8. Terminal classification

### Classical / semiclassical Einstein horizon formula

\[
\boxed{\text{PASS}.}
\]

### Exact universal quantum formula with raw area

\[
\boxed{\text{FAIL}.}
\]

### Possibility of a generalized entropy/effective-action LTG formula

\[
\boxed{\text{OPEN}.}
\]

This is now the more defensible route if LTG is to move beyond a semiclassical synthesis.

## Prior-art anchors

- Quantum and entanglement entropy calculations generically produce logarithmic corrections to horizon area laws.
- de Sitter entropy also receives one-loop/logarithmic corrections in quantum treatments.
- In higher-derivative gravity, horizon entropy is generalized from Bekenstein-Hawking area to Wald-type entropy.
