# EXP-049 — Horizon-entropy stationarity as a de Sitter selector

## Objective

Test the first global-causal candidate left by EXP-048:

\[
\text{generalized / horizon entropy stationarity}
\stackrel{?}{\Longrightarrow}
\dot H\to0
\]

without assuming de Sitter in advance.

The goal is to distinguish three questions:

1. Does horizon entropy increase under ordinary energy conditions?
2. Does finite entropy saturation imply \(w_{\rm eff}\to-1\)?
3. Does entropy stationarity determine the nonzero asymptotic scale \(H_*\)?

---

## 1. Apparent-horizon entropy in flat FLRW

For spatially flat FLRW, the apparent-horizon radius is

\[
R_A=\frac1H.
\]

Its area is

\[
A_A=4\pi R_A^2=\frac{4\pi}{H^2}.
\]

Using the Bekenstein-Hawking entropy,

\[
S_A=\frac{A_A}{4G},
\]

gives

\[
\boxed{
S_A=\frac{\pi}{G H^2}.
}
\]

Differentiate:

\[
\boxed{
\dot S_A
=
-\frac{2\pi}{G}
\frac{\dot H}{H^3}.
}
\]

For flat FLRW in Einstein gravity,

\[
\dot H=-4\pi G(\rho+p).
\]

Therefore

\[
\boxed{
\dot S_A
=
\frac{8\pi^2}{H^3}(\rho+p).
}
\]

If the null energy condition holds,

\[
\rho+p\ge0,
\]

then

\[
\boxed{
\dot S_A\ge0.
}
\]

So horizon area/entropy is monotonic for the standard nonphantom branch.

### Result 049A

Horizon-entropy monotonicity is automatic under the standard FLRW equations plus the null energy condition. It is not an independent LTG law.

---

## 2. Stationarity condition

Assume an expanding state with finite nonzero

\[
H\to H_*>0.
\]

If the horizon entropy saturates,

\[
\dot S_A\to0,
\]

then

\[
\dot H\to0.
\]

Since

\[
w_{\rm eff}
=
-1-\frac{2\dot H}{3H^2},
\]

one obtains

\[
\boxed{
w_{\rm eff}\to-1.
}
\]

Equivalently,

\[
\rho+p\to0.
\]

Thus finite horizon-entropy saturation selects a vacuum-like effective equation of state.

### Result 049B

\[
\boxed{
H\to H_*>0
\quad+\quad
\dot S_A\to0
\Longrightarrow
w_{\rm eff}\to-1.
}
\]

This is an analytic pass for the pressure-sign branch.

---

## 3. Does entropy maximization fix \(H_*\)?

No.

For a de Sitter family,

\[
S_{\rm dS}(H)
=
\frac{\pi}{G H^2}.
\]

Different de Sitter radii have different entropies.

Entropy stationarity with respect to time says

\[
\dot H=0,
\]

but it does not determine which constant value of \(H\) is selected.

Indeed, within the de Sitter family,

\[
S_{\rm dS}\propto H^{-2},
\]

so lowering \(H\) increases the horizon entropy.

There is no finite preferred \(H_*>0\) from this formula alone.

### Result 049C

\[
\boxed{
\dot S_A\to0
}
\]

can fix the equation-of-state endpoint but **cannot fix the dark-energy scale**.

A separate global constraint is required to determine \(H_*\) or \(\Lambda\).

---

## 4. Important counterexample: no positive asymptotic de Sitter scale

If the universe has no positive asymptotic vacuum scale and instead

\[
H\to0,
\]

then

\[
R_A\to\infty,
\]

and

\[
S_A\to\infty.
\]

For a matter-dominated power law,

\[
a\propto t^{2/3},
\qquad
H=\frac{2}{3t},
\]

one has

\[
S_A\propto t^2.
\]

There is no finite entropy maximum.

Therefore the generalized idea

\[
\text{entropy always selects de Sitter}
\]

is too strong.

What is true is conditional:

\[
\boxed{
\text{if a finite horizon entropy maximum exists at }H_*>0,
\text{ its stationary endpoint is de Sitter-like.}
}
\]

---

## 5. Generalized entropy and Q-screens

A generalized entropy has schematic form

\[
S_{\rm gen}
=
\frac{A}{4G}
+
S_{\rm out}.
\]

Cosmological generalized-second-law constructions allow monotonic generalized entropy on suitable Q-screens without requiring an event horizon.

This is a broader law than de Sitter equilibration.

Hence

\[
\frac{dS_{\rm gen}}{dt}\ge0
\]

does not imply

\[
\frac{dS_{\rm gen}}{dt}\to0
\]

and does not by itself imply de Sitter.

The additional assumption of finite asymptotic entropy saturation is the key step.

---

## 6. Relation to cosmic no-hair

With a positive cosmological constant and ordinary matter satisfying appropriate energy conditions, large classes of expanding cosmologies are known to approach de Sitter behavior.

Then

\[
H\to H_\Lambda,
\qquad
\dot H\to0,
\]

and horizon entropy approaches a finite value.

Thus entropy saturation is consistent with cosmic no-hair, but it does not independently generate the positive cosmological constant.

---

## 7. Terminal classification

### Horizon entropy monotonicity

\[
\dot S_A\ge0
\]

**ANALYTIC PASS / PRIOR-ART MAPPED.**

### Finite entropy saturation implies vacuum-like pressure

\[
H_*>0,\quad
\dot S_A\to0
\Longrightarrow
w_{\rm eff}\to-1
\]

**ANALYTIC PASS.**

### Entropy principle fixes \(H_*\) or \(\Lambda\)

**FAIL.**

The magnitude remains undetermined.

### LTG consequence

Entropy gives a plausible **endpoint criterion** but not a **scale-selection law**.

The unresolved LTG problem remains:

\[
\boxed{
\text{what global causal datum fixes the finite horizon scale?}
}
\]

## Prior-art anchors

- Gibbons-Hawking horizon thermodynamics.
- Bousso & Engelhardt (2015), generalized second law for cosmology and Q-screens.
- Cosmic no-hair literature: positive-\(\Lambda\) expanding universes can asymptotically approach de Sitter.
