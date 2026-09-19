# EXP-084 — Can simple horizon quantum states fix the boundary residual coefficient eta?

## Objective

EXP-083 reduced the dark-energy problem to one microscopic quantity,

\[
\eta
=
\frac{\ell_P^2}{A}
D_{\rm grav}.
\]

A de Sitter normalization target is

\[
\eta_{\rm dS}=\frac{\pi}{2}
\]

within the chosen causal thermal-cell convention.

Test whether standard quantum-information states fix this coefficient automatically.

---

## 1. Finite horizon Hilbert-space benchmark

Assume a horizon Hilbert space of dimension

\[
d_H
=
\exp\left(
\frac{S_H}{k_B}
\right)
=
\exp\left(
\frac{A}{4\ell_P^2}
\right).
\]

Take the maximally mixed reference state

\[
\sigma
=
\frac{\mathbf 1}{d_H}.
\]

For a pure state

\[
\rho=|\psi\rangle\langle\psi|,
\]

the relative entropy is

\[
D(\rho\Vert\sigma)
=
\ln d_H.
\]

Therefore

\[
\boxed{
D(\rho\Vert\sigma)
=
\frac{A}{4\ell_P^2}.
}
\]

Thus

\[
\boxed{
\eta_{\rm pure/mix}
=
\frac14.
}
\]

### Result 084A

A canonical pure-versus-maximally-mixed horizon benchmark is area extensive but gives

\[
\eta=1/4,
\]

not the de Sitter target

\[
\eta=\pi/2.
\]

The ratio is

\[
\frac{\eta_{\rm dS}}
{\eta_{\rm pure/mix}}
=
2\pi.
\]

---

## 2. Mapped dark-energy coefficient

EXP-083 found

\[
c_H^2
=
\frac{2\eta}{\pi}.
\]

For

\[
\eta=\frac14,
\]

this gives

\[
\boxed{
c_H^2
=
\frac{1}{2\pi}
\approx0.159.
}
\]

Thus this simplest state pair does not produce a de Sitter-saturating horizon sector.

This is not an observational prediction because the state-pair identification is only a benchmark.

---

## 3. Nearby thermal states

Let

\[
\sigma=\rho_T
\]

be a thermal reference and

\[
\rho=\rho_{T+\delta T}
\]

a nearby state.

For a Gibbs family, relative entropy has the small-perturbation form

\[
D(\rho_{T+\delta T}\Vert\rho_T)
=
\frac12
\frac{C}{k_B}
\left(
\frac{\delta T}{T}
\right)^2
+
O\left(
(\delta T/T)^3
\right),
\]

where \(C\) is the heat capacity of the microscopic boundary system.

If

\[
\frac{C}{k_B}
=
c_A
\frac{A}{\ell_P^2},
\]

then

\[
\boxed{
\eta
=
\frac{c_A}{2}
\left(
\frac{\delta T}{T}
\right)^2
+\cdots.
}
\]

### Result 084B

For near-equilibrium quantum states, the area-density coefficient is state- and susceptibility-dependent.

It is not universal.

If \(c_A=O(1)\), achieving

\[
\eta\sim\pi/2
\]

requires an order-unity fractional mismatch, outside the strict linear near-equilibrium regime.

---

## 4. Can the 2pi KMS period fix the missing factor?

The numerical mismatch in Result 084A is exactly \(2\pi\), suggesting a tempting idea:

\[
\text{one full modular/KMS cycle}
\stackrel{?}{\Longrightarrow}
2\pi D.
\]

But quantum relative entropy is invariant under simultaneous unitary conjugation,

\[
D(U\rho U^\dagger\Vert U\sigma U^\dagger)
=
D(\rho\Vert\sigma).
\]

Ordinary modular flow of both states therefore does not accumulate a factor proportional to the modular period.

### Result 084C

\[
\boxed{
\text{the KMS }2\pi\text{ period does not by itself multiply relative entropy by }2\pi.
}
\]

The coefficient cannot be fixed by simply "going once around modular time."

---

## 5. Reverse relative entropy

For

\[
D(\sigma\Vert\rho)
\]

with \(\rho\) exactly pure and \(\sigma\) full rank, the relative entropy diverges because the support of \(\sigma\) is not contained in the support of \(\rho\).

Thus reversing the state order does not provide the desired finite coefficient.

---

## 6. What is required to predict eta?

A genuine prediction needs a microscopic specification of:

1. the horizon/diamond algebra;
2. the actual state \(\rho\);
3. the reference state \(\sigma\);
4. edge-mode/gravitational contributions;
5. the coarse-graining scale;
6. how the state pair evolves with cosmic time.

Only then is

\[
D_{\rm grav}(\rho\Vert\sigma)
\]

a calculable quantity.

### Result 084D

\[
\boxed{
\eta
\text{ is not fixed by generic quantum-information principles alone.}
}
\]

---

## 7. Terminal classification

### Area-extensive relative entropy is plausible

**PASS.**

### Universal coefficient

\[
\boxed{\text{FAIL}.}
\]

### Simplest finite-Hilbert-space benchmark

\[
\boxed{\eta=1/4.}
\]

### de Sitter target

\[
\boxed{\eta=\pi/2}
\]

remains un-derived.

## Active next gate

The next non-arbitrary route must derive the causal-boundary algebra/state pair.

A useful concrete target is to compute relative entropy for a controlled causal-diamond QFT state where the modular Hamiltonian is known exactly, then compare its area scaling with the required LTG coefficient.
