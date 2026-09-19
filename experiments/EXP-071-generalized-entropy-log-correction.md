# EXP-071 — Generalized-entropy causal balance and logarithmic quantum correction

## Objective

Test the most direct quantum generalization of EXP-070:

\[
\boxed{
\hbar H\dot{\mathcal N}_{\rm gen}
=
\dot Q_H,
\qquad
\mathcal N_{\rm gen}
=
\frac{S_{\rm gen}}{2\pi k_B}.
}
\]

Determine whether a standard logarithmic quantum correction to horizon entropy produces new dynamics and whether those dynamics are already known.

Use natural units

\[
c=\hbar=k_B=1
\]

for the derivation.

---

## 1. Corrected entropy

Take

\[
S(H)
=
\frac{\pi}{GH^2}
+
\alpha
\ln\left(
\frac{4\pi}{GH^2}
\right)
+
\text{const}.
\]

The first term is the Bekenstein-Hawking entropy of the flat-FLRW apparent horizon.

The second is a generic logarithmic correction.

Define

\[
\mathcal N_{\rm gen}
=
\frac{S}{2\pi}.
\]

---

## 2. Apply causal balance

The apparent-horizon temperature is

\[
T_H=\frac{H}{2\pi}.
\]

The matter heat flux is

\[
\dot Q_H
=
\frac{4\pi}{H^2}
(\rho+p).
\]

The equilibrium causal balance is

\[
\dot Q_H=T_H\dot S.
\]

Differentiate the entropy:

\[
\frac{dS}{dH}
=
-\frac{2\pi}{GH^3}
-\frac{2\alpha}{H}.
\]

Hence

\[
\dot S
=
\left(
-\frac{2\pi}{GH^3}
-\frac{2\alpha}{H}
\right)\dot H.
\]

Then

\[
T_H\dot S
=
-\left(
\frac{1}{GH^2}
+
\frac{\alpha}{\pi}
\right)\dot H.
\]

Equating to the heat flux gives

\[
\frac{4\pi}{H^2}(\rho+p)
=
-\left(
\frac{1}{GH^2}
+
\frac{\alpha}{\pi}
\right)\dot H.
\]

Therefore

\[
\boxed{
\dot H
=
-\frac{4\pi G(\rho+p)}
{1+\frac{\alpha G}{\pi}H^2}.
}
\]

---

## 3. Integrate using matter conservation

Assume ordinary local conservation,

\[
\dot\rho+3H(\rho+p)=0.
\]

Then

\[
\frac{d(H^2)}{d\rho}
=
\frac{8\pi G/3}
{1+\frac{\alpha G}{\pi}H^2}.
\]

Integrating,

\[
\boxed{
H^2
+
\frac{\alpha G}{2\pi}H^4
=
\frac{8\pi G}{3}\rho
+
C.
}
\]

With constants restored, the correction is Planck-suppressed and schematically of order

\[
\ell_P^2H^4/c^2.
\]

### Result 071A

A logarithmic generalized-entropy correction generates an \(H^4\)-type correction to the Friedmann equation.

---

## 4. Novelty audit

Entropy-corrected Friedmann equations with logarithmic and inverse-area corrections have substantial prior art.

They have been derived using:

- apparent-horizon thermodynamics;
- entropic cosmology;
- loop/GUP-inspired entropy corrections;
- Padmanabhan-type emergent-space constructions.

Therefore EXP-071 does **not** produce an LTG-specific new law.

### Result 071B

\[
\boxed{
\text{generalized-entropy causal balance}
+
\text{standard log entropy correction}
}
\]

maps onto known entropy-corrected cosmology.

**PRIOR-ART MAPPED.**

---

## 5. Magnitude

The relative modification of the Raychaudhuri equation is governed by

\[
\frac{\alpha G}{\pi}H^2
\sim
\alpha(H/H_P)^2.
\]

At the present cosmic Hubble scale this is extraordinarily small for order-unity \(\alpha\).

Thus a local one-loop logarithmic correction cannot naturally explain present dark energy.

It becomes relevant only near very high curvature unless the coefficient or state dependence is enormous.

This matches the earlier EXP-047 anomaly-scale no-go.

---

## 6. Consequence

The simple route

\[
S_{\rm BH}
\to
S_{\rm BH}+\alpha\ln A
\]

does not create the required new LTG content.

The missing ingredient must be either:

1. a nonlocal/global contribution to \(S_{\rm gen}\);
2. a microscopic rule fixing a large state-dependent entropy term;
3. a new balance law rather than the equilibrium Clausius relation;
4. a relation involving independently observable gravitational degrees of freedom.

The next gate pursues item 4.

---

## Terminal classification

### Generalized entropy gives modified dynamics

**PASS.**

### New LTG dynamics

**FAIL / PRIOR ART.**

### Late-time dark energy from ordinary logarithmic correction

**MAGNITUDE FAIL for order-unity coefficient.**
