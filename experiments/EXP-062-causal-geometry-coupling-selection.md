# EXP-062 — Can causal geometry fix a dimensionless microscopic coupling?

## Objective

Continue the active v9 gate:

\[
\text{global causal geometry}
\stackrel{?}{\Longrightarrow}
g_*.
\]

EXP-060 showed that if a dimensionless coupling is fixed, ordinary exponential dimensional transmutation can generate an enormous geometric hierarchy:

\[
H=H_Pe^{-A/g_*^2},
\qquad
n=\frac12e^{2A/g_*^2}.
\]

This experiment asks whether causal/horizon geometry itself can determine \(g_*\) without importing late-time \(H\), \(\Lambda\), or another arbitrary scale.

---

## 1. Four-dimensional effective-field-theory gate

Consider a gauge sector in curved spacetime,

\[
S_{\rm gauge}
=
-\frac{1}{4g^2}
\int d^4x\sqrt{-g}\,
F_{\mu\nu}F^{\mu\nu}.
\]

The coefficient

\[
\frac1{g^2}
\]

is a dimensionless Wilson coefficient.

General covariance fixes the tensor form of the operator but does not fix its coefficient.

Two theories can have the same background metric and causal structure while having different gauge coupling \(g\).

Therefore:

\[
\boxed{
g
\text{ is not determined by the Lorentzian metric or null cone alone.}
}
\]

### Result 062A

**LOCAL CAUSAL-GEOMETRY SELECTION OF \(g\): FAIL.**

This is an EFT parameter-independence result.

---

## 2. Does a horizon temperature fix g?

A de Sitter horizon provides

\[
T_{\rm dS}
=
\frac{\hbar H}{2\pi k_B}.
\]

This gives a natural renormalization scale

\[
\mu\sim H.
\]

Then the running coupling is evaluated as

\[
g(H).
\]

But the RG equation

\[
\frac{dg}{d\ln\mu}
=
\beta(g)
\]

requires a boundary condition.

For a one-coupling schematic beta function,

\[
\beta(g)=-bg^3+\cdots,
\]

one obtains

\[
\frac1{g^2(\mu)}
=
2b\ln\left(\frac{\mu}{\Lambda_{\rm dyn}}\right)
\]

up to conventions.

Geometry can choose the **scale at which to evaluate** the coupling,

\[
\mu\sim H,
\]

but not the RG integration constant

\[
\Lambda_{\rm dyn}.
\]

### Result 062B

\[
\boxed{
\text{horizon geometry can select an RG scale,
not an RG trajectory.}
}
\]

---

## 3. Fixed-point loophole

Suppose the matter-gravity system has a genuine RG fixed point

\[
\beta_i(g_*)=0.
\]

Then dimensionless couplings may approach fixed values.

This can reduce free parameters.

However EXP-042 already established:

1. fixed-point coordinates may be scheme/truncation dependent;
2. several fixed points or relevant directions may exist;
3. geometry alone does not choose the universality class / RG trajectory;
4. persistent infrared scales require relevant deformations or transmutation data.

Thus a fixed point can supply a candidate \(g_*\), but causal geometry has not selected it.

### Result 062C

**FIXED-POINT VALUE POSSIBLE / CAUSAL SELECTION NOT DERIVED.**

---

## 4. Extra-dimensional geometric loophole

In Kaluza-Klein-type compactification, a four-dimensional gauge coupling can arise from higher-dimensional geometry.

Schematically,

\[
g_4^{-2}
\sim
\frac{V_{\rm int}}{G_D}
\times
(\text{normalization factors}).
\]

Thus a dimensionless gauge coupling can indeed be geometrized.

But then it depends on:

- the compactification volume;
- topology;
- moduli;
- higher-dimensional gravitational normalization.

Unless those geometric moduli are themselves fixed, the coupling remains free.

### Result 062D

\[
\boxed{
\text{geometry can encode }g,
\text{ but only through extra geometric data beyond 4D causal structure.}
}
\]

This is prior art, not yet LTG novelty.

---

## 5. Holographic loophole

In gauge/gravity duality, boundary couplings / central charges can be related to bulk radii, flux integers and Newton constants.

This again demonstrates that dimensionless field-theory data may be encoded geometrically.

But the required information includes more than causal structure:

- flux numbers;
- compactification data;
- brane numbers;
- topology;
- boundary conditions.

So the correct lesson is not

\[
\text{geometry cannot determine couplings},
\]

but rather

\[
\boxed{
\text{causal metric alone cannot;
full quantum/global geometric data sometimes can.}
}
\]

---

## 6. Direct LTG self-consistency attempt

Combine the transmutation law

\[
H
=
H_Pe^{-A/g^2}
\]

with the de Sitter temperature

\[
k_BT_{\rm dS}
=
\frac{\hbar H}{2\pi}.
\]

Demanding that the generated infrared scale equal the horizon scale merely reproduces

\[
H=H.
\]

Equivalently,

\[
g^2
=
\frac{A}{\ln(H_P/H)}.
\]

This determines \(g\) only after \(H\) is known.

Therefore the naive "transmutation scale equals horizon scale" condition is circular.

### Result 062E

\[
\boxed{
\text{simple horizon/transmutation self-consistency does not select }g_*.
}
\]

---

## 7. What kind of geometry could select g?

EXP-062 sharpens the required input.

A successful geometric selection mechanism must contain **global quantum data beyond the metric**, for example:

1. an integer flux;
2. topology plus moduli stabilization;
3. a finite Hilbert-space dimension;
4. a boundary CFT consistency condition;
5. anomaly cancellation;
6. a quantized causal-boundary phase;
7. a compactification geometry with no continuous moduli.

Such a mechanism could yield

\[
g_*=f(\text{integers/topological data})
\]

without using the late cosmological scale.

Then EXP-060 could amplify \(g_*\) into the huge horizon hierarchy.

---

## 8. Terminal classification

### 4D metric/null cones fix a dimensionless gauge coupling

\[
\boxed{\text{NO}.}
\]

**EFT NO-GO.**

### Horizon temperature fixes the coupling

\[
\boxed{\text{NO}.}
\]

It fixes only a natural RG scale.

### RG fixed point can give a coupling value

\[
\boxed{\text{YES, conditionally}.}
\]

But the relevant fixed point / trajectory is not selected by causal geometry.

### Higher-dimensional/global quantum geometry can encode couplings

\[
\boxed{\text{YES}.}
\]

But it requires extra topological/flux/moduli data.

---

## 9. Active next gate

The project should no longer ask whether the 4D causal metric directly determines \(g_*\); it does not.

The narrower viable target is

\[
\boxed{
\text{global quantized geometric data}
\stackrel{?}{\Longrightarrow}
g_*.
}
\]

The next discriminating test should look for a **moduli-free compact/global construction** in which a dimensionless coupling is fixed solely by integers/topology, then ask whether EXP-060 transmutation yields a viable horizon hierarchy.

This preserves the no-free-continuous-parameter criterion.
