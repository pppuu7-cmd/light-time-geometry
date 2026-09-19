# EXP-103 — Cosmological self-consistency test of the rho_X proportional to H branch

## Objective

Even if EXP-102 were to confirm a real-QCD topological \(1/L\) term, EXP-100 would still need to pass a cosmological-dynamics test.

Test the minimal branch

\[
\boxed{
\rho_X=\mu^3 H
}
\]

in flat Einstein gravity with pressureless matter and separate conservation of the dark component.

Here

\[
\mu^3
\]

denotes the QCD-generated coefficient. Its absolute value does not affect the equation-of-state relation derived below.

---

## 1. Dark-energy continuity equation

Separate conservation gives

\[
\dot\rho_X
+
3H(1+w_X)\rho_X
=
0.
\]

Because

\[
\rho_X=\mu^3H,
\]

we have

\[
\dot\rho_X=\mu^3\dot H.
\]

Divide by

\[
\rho_X=\mu^3H.
\]

Then

\[
\boxed{
\frac{\dot H}{H^2}
=
-3(1+w_X).
}
\]

---

## 2. Raychaudhuri equation

For pressureless matter plus the \(X\) component,

\[
\dot H
=
-\frac{1}{2\bar M_P^2}
\left[
\rho_m+(1+w_X)\rho_X
\right].
\]

Using

\[
3\bar M_P^2H^2
=
\rho_m+\rho_X
\]

and

\[
\Omega_X
=
\frac{\rho_X}{3\bar M_P^2H^2},
\]

we obtain

\[
\boxed{
\frac{\dot H}{H^2}
=
-\frac32
\left(
1+w_X\Omega_X
\right).
}
\]

Equating with the continuity result yields

\[
-3(1+w_X)
=
-\frac32(1+w_X\Omega_X).
\]

Therefore

\[
2+2w_X
=
1+w_X\Omega_X
\]

and hence

\[
\boxed{
w_X
=
-\frac{1}{2-\Omega_X}.
}
\]

### Result 103A — parameter-free equation-of-state trajectory

Once \(\rho_X\propto H\) and separate conservation are assumed, the dark-energy equation of state is fixed.

The QCD coefficient changes the scale at which the component becomes important but not this functional relation.

---

## 3. Evolution of Omega_X

Since

\[
\Omega_X
=
\frac{\mu^3}{3\bar M_P^2H},
\]

we have

\[
\frac{d\ln\Omega_X}{d\ln a}
=
-\frac{\dot H}{H^2}.
\]

Using

\[
\frac{\dot H}{H^2}
=
-3(1+w_X)
\]

and the expression for \(w_X\),

\[
1+w_X
=
\frac{1-\Omega_X}{2-\Omega_X}.
\]

Therefore

\[
\boxed{
\Omega_X'
=
\frac{3\Omega_X(1-\Omega_X)}
{2-\Omega_X},
}
\]

where prime means

\[
d/d\ln a.
\]

Thus:

\[
\Omega_X\to0
\quad\Rightarrow\quad
w_X\to-\frac12
\]

at early times, while

\[
\Omega_X\to1
\quad\Rightarrow\quad
w_X\to-1
\]

at the future de Sitter endpoint.

---

## 4. Local CPL slope

Use

\[
w(a)
=
w_0+w_a(1-a).
\]

At

\[
a=1,
\]

\[
w_a
=
-
\left.
\frac{dw}{d\ln a}
\right|_0.
\]

Since

\[
\frac{dw}{d\Omega}
=
-\frac{1}{(2-\Omega)^2},
\]

we obtain

\[
\boxed{
w_a
=
\frac{3\Omega_{X0}(1-\Omega_{X0})}
{(2-\Omega_{X0})^3}.
}
\]

Therefore

\[
\boxed{
w_a>0
}
\]

for every

\[
0<\Omega_{X0}<1.
\]

For the previously used comparison value

\[
\Omega_{X0}=0.685,
\]

one gets

\[
\boxed{
w_0=-0.76046,
}
\]

\[
\boxed{
w_a^{\rm local}=+0.28467.
}
\]

The sign of the slope is independent of the QCD coefficient.

---

## 5. Comparison with current DESI direction

DESI DR2 cosmological analyses report that, within the phenomenological \(w_0w_a\)CDM parameterization and common data combinations, the favored dynamical-dark-energy region has

\[
\boxed{
w_0>-1,
\qquad
w_a<0.
}
\]

The simple \(\rho_X\propto H\) branch predicts the opposite sign,

\[
\boxed{
w_a>0.
}
\]

However, the 2026 DESI DR2 Lyman-alpha full-shape measurement shifted toward the standard \(\Lambda\)CDM prediction and explicitly notes that the current hints of evolving dark energy may weaken or require a more complex model.

### Result 103B

The minimal separately conserved \(\rho_X\propto H\) branch is **directionally in tension** with the principal DESI DR2 evolving-DE trend.

This is not yet a clean exclusion because:

- the evolving-DE evidence is dataset/model dependent;
- current 2026 Ly-alpha information has moved toward \(\Lambda\)CDM;
- a dedicated likelihood fit of this exact one-parameter trajectory has not been performed here.

---

## 6. Adiabatic sound speed

For a separately conserved barotropic effective component,

\[
c_a^2
=
\frac{\dot p_X}{\dot\rho_X}
=
w_X
-
\frac{w_X'}{3(1+w_X)}.
\]

Using the exact trajectory above,

\[
\boxed{
c_a^2
=
-\frac{2(1-\Omega_X)}
{(2-\Omega_X)^2}.
}
\]

Thus for

\[
0<\Omega_X<1,
\]

\[
\boxed{
c_a^2<0.
}
\]

It approaches zero only at the asymptotic de Sitter endpoint.

### Result 103C

The naive perfect-fluid realization has a negative adiabatic sound-speed squared, matching a known instability concern in the QCD-ghost dark-energy literature.

A microscopic non-fluid completion could modify the perturbation interpretation, but then the simple effective-fluid model is incomplete.

---

## 7. Exact background H(a)

The Friedmann equation is

\[
3\bar M_P^2H^2
=
\rho_{m0}a^{-3}
+
\mu^3H.
\]

Define

\[
H_\infty
=
\frac{\mu^3}{3\bar M_P^2}
\]

and

\[
H_m^2(a)
=
\frac{\rho_{m0}a^{-3}}
{3\bar M_P^2}.
\]

Then the positive branch is

\[
\boxed{
H(a)
=
\frac12
\left[
H_\infty
+
\sqrt{
H_\infty^2+4H_m^2(a)
}
\right].
}
\]

Thus the model has a fully fixed background trajectory once

\[
H_\infty
\]

and the matter density are specified.

The functional form resembles other square-root modified-expansion histories and can be tested directly against BAO/SN/CMB data rather than by fitting a generic \(w_0w_a\).

---

## 8. Interaction escape route

If the dark component exchanges energy with matter,

\[
\dot\rho_X
+
3H(1+w_X)\rho_X
=
-Q,
\]

then the rigid relation

\[
w_X=-1/(2-\Omega_X)
\]

changes.

Likewise, generalized ghost models containing

\[
\rho_X=\alpha H+\beta H^2
\]

have extra freedom.

But these modifications introduce additional dynamics/parameters beyond EXP-100's minimal independent closure.

Therefore they must be treated as new hypotheses rather than post-hoc repairs.

---

## Terminal classification

### Microscopic magnitude branch

Still conditional on EXP-102.

### Minimal background dynamics

\[
\boxed{
w_X=-1/(2-\Omega_X)
}
\]

**ANALYTIC PASS.**

### Current observational direction

\[
\boxed{
w_a>0
}
\]

is in directional tension with the principal DESI DR2 \(w_a<0\) preference, though the 2026 Lyman-alpha update reduces confidence in a simple evolving-DE interpretation.

### Perturbative fluid stability

\[
\boxed{
c_a^2<0
}
\]

for the naive separately conserved fluid.

**TENSION / KNOWN PROBLEM.**

## Overall consequence

Even a positive EXP-102 lattice result would not be enough.

The QCD-KMS branch would also need a viable microscopic perturbation theory and a dedicated fit of its exact \(H(a)\) trajectory to current cosmological data.
