# EXP-054 — de Sitter action / entropy identity and phase-quantization gate

## Objective

Continue the active LTG gate from EXP-053:

\[
N_{\rm global}
\stackrel{?}{=}
\text{an invariant action / phase count of a complete causal history}.
\]

Test whether the on-shell gravitational action provides an independent prediction of the de Sitter information count, and whether a natural quantum phase condition quantizes that count.

---

## 1. Euclidean de Sitter saddle

Work first in natural units

\[
c=\hbar=1.
\]

Four-dimensional Euclidean de Sitter is a round \(S^4\) with

\[
L^2=\frac{3}{\Lambda}.
\]

For this Einstein space,

\[
R=4\Lambda.
\]

The four-volume of the round \(S^4\) is

\[
V_4(S^4)
=
\frac{8\pi^2}{3}L^4
=
\frac{24\pi^2}{\Lambda^2}.
\]

The Euclidean Einstein-Hilbert action is

\[
I_E
=
-\frac{1}{16\pi G}
\int d^4x\sqrt g\,(R-2\Lambda).
\]

Since

\[
R-2\Lambda=2\Lambda,
\]

one obtains

\[
\boxed{
I_E
=
-\frac{3\pi}{G\Lambda}.
}
\]

---

## 2. Exact action-entropy identity

The de Sitter horizon radius is

\[
L=\sqrt{\frac{3}{\Lambda}},
\]

so its area is

\[
A=4\pi L^2
=
\frac{12\pi}{\Lambda}.
\]

The Gibbons-Hawking entropy is

\[
S_{\rm dS}
=
\frac{k_B A}{4G\hbar}
\]

when constants are restored.

In natural units,

\[
\frac{S_{\rm dS}}{k_B}
=
\frac{A}{4G}
=
\frac{3\pi}{G\Lambda}.
\]

Therefore

\[
\boxed{
\frac{|I_E|}{\hbar}
=
\frac{S_{\rm dS}}{k_B}
\equiv N.
}
\]

This is an exact identity for the standard Euclidean de Sitter saddle.

### Result 054A

The proposed global action count exists:

\[
\boxed{
N
=
|I_E|/\hbar.
}
\]

But it is not independent of the horizon entropy count. It is exactly the same quantity.

Thus replacing

\[
N
\]

by

\[
|I_E|/\hbar
\]

does not yet explain the value of \(N\).

---

## 3. Connection to EXP-052

EXP-052 obtained, for a de Sitter/horizon scale,

\[
E_{\rm geom}\tau_{\rm light}
=
\frac{\hbar}{2\pi}N.
\]

Combining with

\[
|I_E|=\hbar N
\]

gives

\[
\boxed{
|I_E|
=
2\pi E_{\rm geom}\tau_{\rm light}.
}
\]

Hence the same dimensionless count appears in three forms:

\[
\boxed{
N
=
\frac{S_{\rm dS}}{k_B}
=
\frac{|I_E|}{\hbar}
=
2\pi\frac{E_{\rm geom}\tau_{\rm light}}{\hbar}.
}
\]

This is the strongest current LTG action-information bridge.

It links:

- geometry through horizon area;
- information through entropy;
- total gravitational action;
- energy;
- light-crossing time.

---

## 4. Does the path-integral phase quantize N?

A tempting hypothesis is

\[
e^{iI/\hbar}=1
\]

for a complete causal history, which would imply

\[
I=2\pi n\hbar.
\]

If one simply imposed

\[
|I_E|=2\pi n\hbar,
\]

then

\[
N=2\pi n.
\]

Using

\[
N=
\frac{\pi c^5}{G\hbar H^2},
\]

this would give

\[
\boxed{
H^2
=
\frac{c^5}{2G\hbar n}.
}
\]

So a huge integer \(n\) could parameterize a tiny late-time curvature.

However, this quantization condition is **not implied by the gravitational path integral**.

### Lorentzian issue

The factor

\[
e^{iI/\hbar}
\]

is invariant under shifting an action by \(2\pi n\hbar\), but that does not mean the physical on-shell action itself must be an integer multiple of \(2\pi\hbar\).

A quantization rule requires a genuine compact degree of freedom, gauge redundancy, winding, or topological consistency condition.

### Euclidean issue

For the Euclidean de Sitter saddle the semiclassical weight is

\[
e^{-I_E/\hbar},
\]

not a periodic phase.

Therefore Euclidean saddle-point consistency does not imply

\[
I_E=2\pi n\hbar.
\]

### Result 054B

\[
\boxed{
\text{naive action-phase quantization}
\not\Rightarrow
N=2\pi n.
}
\]

**CLASSIFICATION: FAIL without an additional compact/topological variable.**

---

## 5. Lorentzian complete-patch action problem

A future-eternal de Sitter static/causal patch has an infinite proper-time future.

A naive Lorentzian spacetime action integrated over the full eternal history is therefore not automatically a finite invariant number.

Obtaining the finite quantity

\[
|I_E|/\hbar=N
\]

uses the regular Euclidean saddle / horizon thermodynamic structure.

Therefore a proposal based on "the total Lorentzian action of all cosmic history" requires a regulator or a compact/global contour prescription.

### Result 054C

The finite action count is well defined for the Euclidean de Sitter saddle, but a naive full Lorentzian future history does not supply an automatically finite phase count.

---

## 6. What would make action quantization nontrivial?

A real prediction requires an independently quantized structure such as:

1. a compact global phase;
2. a topological winding number;
3. a quantized flux through a causal boundary;
4. a topological term whose coefficient and sector are fixed;
5. a finite-dimensional Hilbert-space rule that fixes the number of states.

Then one could obtain

\[
N=f(n_{\rm top})
\]

with

\[
n_{\rm top}\in\mathbb Z
\]

for a reason independent of the observed \(H\).

Without this step, the action identity is an exact reparameterization of the same de Sitter scale.

---

## 7. Terminal classification

### Does the Euclidean gravitational action reproduce the global information count?

\[
\boxed{\text{YES, exactly}.}
\]

**ANALYTIC PASS.**

### Is it independent information?

\[
\boxed{\text{NO}.}
\]

It is equal to the de Sitter entropy count.

### Does ordinary quantum phase periodicity quantize the count?

\[
\boxed{\text{NO}.}
\]

**NAIVE QUANTIZATION FAIL.**

### Surviving LTG statement

\[
\boxed{
\frac{S}{k_B}
=
\frac{|I_E|}{\hbar}
=
2\pi\frac{E_{\rm geom}\tau_{\rm light}}{\hbar}
}
\]

is an exact action-information-energy-time-geometry bridge.

The unresolved step remains the origin of the numerical value of this common dimensionless count.

## Prior-art anchors

- Gibbons-Hawking de Sitter entropy and Euclidean instanton action.
- Euclidean de Sitter on-shell action equals minus horizon entropy; the same structure extends to de Sitter black-hole instantons with the sum of horizon entropies.
