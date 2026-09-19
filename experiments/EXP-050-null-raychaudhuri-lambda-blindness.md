# EXP-050 — Null Raychaudhuri test: can null geometry fix the de Sitter scale?

## Objective

Test the second candidate left by EXP-048:

\[
\text{null-congruence regularity}
\stackrel{?}{\Longrightarrow}
HL=1
\quad\text{or}\quad
H=H_*.
\]

This is a particularly sharp gate because LTG has emphasized null geometry as the light sector.

---

## 1. Null Raychaudhuri equation

For a hypersurface-orthogonal null congruence with tangent \(k^\mu\),

\[
\frac{d\theta}{d\lambda}
=
-\frac12\theta^2
-\sigma_{\mu\nu}\sigma^{\mu\nu}
-R_{\mu\nu}k^\mu k^\nu.
\]

The cosmological-constant Einstein equation is

\[
R_{\mu\nu}
-\frac12Rg_{\mu\nu}
+\Lambda g_{\mu\nu}
=
8\pi G T_{\mu\nu}.
\]

Contract with the null vector twice.

Since

\[
g_{\mu\nu}k^\mu k^\nu=0,
\]

all metric-proportional terms vanish:

\[
-\frac12R\,g_{\mu\nu}k^\mu k^\nu=0,
\]

\[
\Lambda g_{\mu\nu}k^\mu k^\nu=0.
\]

Therefore

\[
\boxed{
R_{\mu\nu}k^\mu k^\nu
=
8\pi G T_{\mu\nu}k^\mu k^\nu.
}
\]

The cosmological constant is invisible to the local null-focusing contraction.

---

## 2. de Sitter versus Minkowski

In exact de Sitter,

\[
R_{\mu\nu}
=
3H^2g_{\mu\nu}.
\]

Hence for every null vector,

\[
\boxed{
R_{\mu\nu}k^\mu k^\nu=0.
}
\]

In Minkowski,

\[
R_{\mu\nu}=0,
\]

so again

\[
\boxed{
R_{\mu\nu}k^\mu k^\nu=0.
}
\]

Thus the local null Raychaudhuri source cannot distinguish

\[
H=0
\]

from

\[
H>0
\]

inside the family of vacuum Einstein spaces.

### Result 050A

\[
\boxed{
\text{local null focusing is blind to the cosmological constant.}
}
\]

This is an analytic no-go for deriving the de Sitter scale from local null Raychaudhuri data alone.

---

## 3. Vacuum energy is null-silent

A vacuum-energy stress tensor is

\[
T_{\mu\nu}^{\rm vac}
=
-\rho_{\rm vac}g_{\mu\nu}.
\]

Then

\[
\boxed{
T_{\mu\nu}^{\rm vac}k^\mu k^\nu=0.
}
\]

So the null energy flux seen by the Raychaudhuri equation is identical for all values of \(\rho_{\rm vac}\).

This means a local null-only principle cannot determine the absolute vacuum-energy density.

It can constrain matter components with nonzero

\[
T_{kk},
\]

but it is blind to the metric-proportional part.

---

## 4. Stationary null boundary is not enough

Suppose one requires a shear-free stationary null surface,

\[
\theta=0,
\qquad
\sigma_{\mu\nu}=0.
\]

Raychaudhuri gives

\[
R_{\mu\nu}k^\mu k^\nu=0.
\]

But every Einstein space satisfying

\[
R_{\mu\nu}=\Lambda_{\rm eff}g_{\mu\nu}
\]

passes this null condition for arbitrary \(\Lambda_{\rm eff}\).

Therefore

\[
\boxed{
\theta=0
}
\]

does not fix

\[
H,
\qquad
L,
\qquad
HL.
\]

A length/area/global boundary datum must be added.

---

## 5. Consequence for the pressure-sign branch

The vacuum-like pressure condition

\[
p=-\rho
\]

corresponds to

\[
T_{\mu\nu}\propto g_{\mu\nu}.
\]

Exactly this component is invisible under

\[
T_{\mu\nu}k^\mu k^\nu.
\]

Therefore there is a structural separation:

\[
\boxed{
\text{null focusing}
\text{ detects } \rho+p,
}
\]

whereas

\[
\boxed{
\text{vacuum pressure / cosmological constant}
\text{ resides in the metric-proportional sector.}
}
\]

This is highly relevant to LTG: the pure null sector cannot by itself measure the absolute vacuum-energy offset.

---

## 6. What additional information can break the degeneracy?

At least one non-null/global datum is needed, for example:

1. horizon area
   \[
   A\sim H^{-2};
   \]
2. horizon entropy
   \[
   S\sim A/G;
   \]
3. a timelike observer's static-patch acceleration/temperature;
4. a causal-diamond volume;
5. a global boundary condition fixing the event-horizon size;
6. a nonlocal quantum/global entropy functional.

This agrees with EXP-048: the unresolved physics must be global rather than another local null equation.

---

## 7. Terminal classification

### Can local null Raychaudhuri regularity select de Sitter rather than Minkowski?

\[
\boxed{\text{NO}.}
\]

**ANALYTIC FAIL.**

### Can it determine the cosmological constant or \(H_*\)?

\[
\boxed{\text{NO}.}
\]

**NULL-BLINDNESS NO-GO.**

### Can it still constrain departures from vacuum-like behavior?

\[
\boxed{\text{YES}.}
\]

It detects

\[
T_{kk}
\]

and hence focusing from components with

\[
\rho+p\ne0.
\]

### LTG consequence

A theory based only on local light/null congruences cannot determine the vacuum-energy scale.

The surviving route requires

\[
\boxed{
\text{null structure}
+
\text{global area/entropy/causal-volume data}.
}
\]

## Prior-art anchors

- Raychaudhuri equation and null-focusing theorems.
- Einstein equation: the cosmological-constant term vanishes under contraction with a null vector.
- Vacuum energy is therefore invisible to local \(T_{kk}\) data.
