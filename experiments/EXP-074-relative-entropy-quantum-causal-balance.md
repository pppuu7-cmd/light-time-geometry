# EXP-074 — Relative-entropy quantum completion of causal information balance

## Objective

EXP-073 proposed the reversible causal-information balance

\[
\frac{\tau_c\Delta Q}{\hbar}
=
\Delta\mathcal N.
\]

Test its quantum completion using an exact quantum-information identity rather than an arbitrary entropy-production term.

The key object is quantum relative entropy.

---

## 1. Relative entropy identity

Let \(\sigma\) be a reference state and \(\rho\) a perturbed state on a causal region.

Define the modular Hamiltonian

\[
K_\sigma=-\ln\sigma.
\]

The dimensionless von Neumann entropy is

\[
s(\rho)=-\mathrm{Tr}\,\rho\ln\rho.
\]

The relative entropy is

\[
\boxed{
D(\rho\Vert\sigma)
=
\Delta\langle K_\sigma\rangle
-
\Delta s
\ge0.
}
\]

This is an exact quantum-information identity.

---

## 2. Causal thermal normalization

For a causal diamond / horizon reference with modular temperature

\[
\boxed{
k_BT_c
=
\frac{\hbar}{2\pi\tau_c},
}
\]

define the physical modular-energy difference

\[
\boxed{
\Delta Q_{\rm mod}
\equiv
k_BT_c\,
\Delta\langle K_\sigma\rangle.
}
\]

Define the LTG-normalized entropy change

\[
\boxed{
\Delta\mathcal N_{\rm q}
\equiv
\frac{\Delta s}{2\pi}
=
\frac{\Delta S}{2\pi k_B}.
}
\]

Multiply the relative-entropy identity by \(1/(2\pi)\).

Since

\[
\frac{\tau_c\Delta Q_{\rm mod}}{\hbar}
=
\frac{\Delta\langle K_\sigma\rangle}{2\pi},
\]

we obtain

\[
\boxed{
\frac{\tau_c\Delta Q_{\rm mod}}{\hbar}
-
\Delta\mathcal N_{\rm q}
=
\frac{D(\rho\Vert\sigma)}{2\pi}.
}
\]

Therefore

\[
\boxed{
\frac{\tau_c\Delta Q_{\rm mod}}{\hbar}
\ge
\Delta\mathcal N_{\rm q}.
}
\]

### Result 074A — exact quantum causal-balance residual

The difference between dimensionless causal modular energy and entropy/information change is not arbitrary.

It is exactly relative entropy:

\[
\boxed{
\mathfrak D_{\rm LTG}
\equiv
\frac{\tau_c\Delta Q_{\rm mod}}{\hbar}
-
\Delta\mathcal N_{\rm q}
=
\frac{D(\rho\Vert\sigma)}{2\pi}
\ge0.
}
\]

---

## 3. Entanglement-first-law limit

Consider a one-parameter perturbation

\[
\rho(\epsilon)
=
\sigma+\epsilon\,\delta\rho+\cdots.
\]

Relative entropy has no linear term:

\[
D(\rho(\epsilon)\Vert\sigma)
=
O(\epsilon^2).
\]

Therefore at first order,

\[
\boxed{
\delta\langle K\rangle
=
\delta s.
}
\]

In LTG normalization,

\[
\boxed{
\frac{\tau_c\,\delta Q_{\rm mod}}{\hbar}
=
\delta\mathcal N_{\rm q}.
}
\]

Thus the reversible CIB equality is precisely the linearized entanglement-first-law limit.

### Result 074B

EXP-073's equality has a natural quantum interpretation:

\[
\boxed{
\text{CIB equality}
=
\text{first-order / reversible limit}.
}
\]

It should not be assumed exact for finite quantum departures from the reference state.

---

## 4. Second-order correction

The leading nonzero relative entropy is quadratic,

\[
D
=
\frac12
\epsilon^2
\mathcal F_Q
+
O(\epsilon^3),
\]

where \(\mathcal F_Q\) is the relevant quantum Fisher-information quadratic form, up to convention.

Hence

\[
\boxed{
\frac{\tau_c\Delta Q_{\rm mod}}{\hbar}
-
\Delta\mathcal N_{\rm q}
=
\frac{\epsilon^2}{4\pi}
\mathcal F_Q
+
O(\epsilon^3).
}
\]

This gives a definite sign:

\[
\boxed{
\text{finite quantum correction}
\ge0.
}
\]

It is controlled by state distinguishability, not a freely chosen phenomenological entropy-production coefficient.

---

## 5. Gravitational interpretation

In entanglement-equilibrium and holographic settings, relative entropy / its second variation is related to gravitational canonical energy.

At first order, generalized entropy variation plus the entanglement first law can yield the linearized semiclassical Einstein equation.

At second order, positivity of relative entropy becomes positivity of a gravitational canonical-energy functional in controlled settings.

Therefore the natural gravitational extension is schematically

\[
\boxed{
\text{causal modular-energy count}
-
\text{generalized information count}
=
\text{positive relative/canonical information}.
}
\]

This is much more constrained than introducing an arbitrary \(d_iS\).

---

## 6. Important limitation

The exact identity in Sections 1-4 is a QFT/modular-entropy theorem.

Replacing

\[
\mathcal N_{\rm q}
\]

by the full gravitational

\[
\mathcal N_{\rm gen}
=
\frac{S_{\rm gen}}{2\pi k_B}
\]

requires a controlled gravitational dictionary.

Examples where such dictionaries exist include:

- entanglement-equilibrium perturbation theory;
- holographic code subspaces / JLMS-type relations;
- semiclassical causal-diamond constructions.

It is **not** yet established as one universal nonperturbative cosmological identity.

---

## 7. Consequence for EXP-073

The exact zero-residual postulate

\[
\mathfrak R_{\rm LTG}=0
\]

is too strong as a universal quantum statement.

The better hierarchy is:

### Linearized equilibrium

\[
\boxed{
\mathfrak R_{\rm LTG}=0+O(\epsilon^2).
}
\]

### Finite quantum perturbation

\[
\boxed{
\mathfrak R_{\rm LTG}
\sim
\text{positive relative-entropy / canonical-energy term}.
}
\]

Thus the Wald-truncated prediction

\[
\ddot F=0
\]

from EXP-073 should be interpreted as a leading reversible approximation, not an exact full-quantum law.

---

## 8. Novelty status

Relative entropy positivity and the entanglement first law are established quantum-information physics.

The LTG contribution is the common causal normalization

\[
\frac{\tau_c Q}{\hbar}
\leftrightarrow
\mathcal N
\]

that places the classical horizon balance and quantum relative-entropy residual in one variable.

### Classification

\[
\boxed{
\text{QUANTUM COMPLETION FOUND / PRIOR-ART FOUNDATION / LTG SYNTHESIS}.
}
\]

It is not yet independent new physics.

---

## 9. Strongest candidate law after EXP-074

The scientifically defensible candidate is no longer a bare equality.

It is the **LTG quantum causal balance form**

\[
\boxed{
\frac{\tau_c\Delta Q_{\rm mod}}{\hbar}
=
\Delta\mathcal N_{\rm gen}
+
\mathcal D_{\rm grav},
\qquad
\mathcal D_{\rm grav}\ge0,
}
\]

where in controlled quantum-field settings

\[
\boxed{
\mathcal D_{\rm grav}
=
\frac{D(\rho\Vert\sigma)}{2\pi}.
}
\]

A genuinely new LTG theorem would require deriving the gravitational/generalized-entropy dictionary for \(\mathcal D_{\rm grav}\) in cosmology rather than assuming it.
