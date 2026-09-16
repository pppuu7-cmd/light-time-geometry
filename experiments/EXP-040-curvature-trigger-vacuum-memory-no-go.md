# EXP-040 — Curvature trigger and vacuum-memory no-go

## Objective

Test whether the viable `geometry -> phase transition -> persistent mass` idea from EXP-039 can work in the smallest classically scale-free scalar model, and determine exactly what additional ingredient is required for vacuum memory.

## 1. Minimal scale-free curvature-coupled scalar

Use natural units for clarity and consider

\[
V(\phi,R)
=\frac{\lambda}{4}\phi^4
+\frac{\xi}{2}R\phi^2,
\qquad \lambda>0.
\]

There is no explicit mass parameter.

The stationary condition is

\[
\frac{\partial V}{\partial\phi}
=\phi\left(\lambda\phi^2+\xi R\right)=0.
\]

Therefore the extrema are

\[
\phi=0
\]

and, when

\[
\xi R<0,
\]

\[
\boxed{
v^2(R)=-\frac{\xi R}{\lambda}.
}
\]

## 2. Geometry can induce a temporary broken phase

If the background curvature has the sign required by `xi R < 0`, the origin is unstable and the field acquires a nonzero expectation value.

A Yukawa-coupled fermion would have

\[
m_f(R)=y|v(R)|,
\]

so

\[
\boxed{
m_f^2(R)=\frac{y^2|\xi|}{\lambda}|R|
}
\]

for the appropriate sign branch.

Thus geometry can indeed create a temporary mass/clock scale.

The corresponding Compton frequency is

\[
\omega_C(R)=m_f(R)
\]

in natural units, and the ratio

\[
\boxed{
\frac{m_f^2}{|R|}=\frac{y^2|\xi|}{\lambda}
}
\]

is constant only because it is fixed by the microscopic couplings.

It is not universal.

## 3. No persistent memory in the minimal model

Now let the cosmological curvature relax toward zero:

\[
R\to0.
\]

Then

\[
v^2(R)\to0,
\]

and therefore

\[
\boxed{
m_f(R)\to0.}
\]

The minimal model has no nonzero vacuum scale once the geometric trigger disappears.

Hence

\[
\boxed{
\text{curvature trigger alone}
\not\Rightarrow
\text{persistent mass memory}.
}
\]

This is an analytic no-go, not a numerical accident.

## 4. Why the failure is inevitable by dimensional analysis

The classical model contains only:

- dimensionless couplings `lambda`, `xi`, `y`;
- the background curvature scale `R`.

Therefore any dynamically induced mass in a static/quasi-static background must have the schematic form

\[
m^2=|R|\,F(\lambda,\xi,y,\ldots).
\]

If the only dimensionful input `R` vanishes, dimensional analysis forces the induced classical mass to vanish as well.

Thus a persistent nonzero mass in the flat-space limit requires either:

1. a second dimensionful scale;
2. quantum dimensional transmutation;
3. a topological/nonlocal scale;
4. a metastable state whose decay/history carries additional data;
5. explicit breaking through a mass parameter.

## 5. Add quantum dimensional transmutation

Suppose loop effects generate a nonzero scale `Lambda_dyn` and an effective potential of Coleman-Weinberg type,

\[
V_{\rm q}(\phi)
\sim
A\phi^4
\left[
\ln\left(\frac{\phi^2}{\Lambda_{\rm dyn}^2}\right)-C
\right].
\]

Then the total potential

\[
V_{\rm eff}(\phi,R)
=\frac{\xi}{2}R\phi^2+V_{\rm q}(\phi)
\]

can use curvature to alter which minimum is preferred while the nonzero scale of the minimum is fundamentally supplied by `Lambda_dyn`.

After

\[
R\to0,
\]

a nonzero minimum can remain:

\[
\boxed{
v\sim C_v\Lambda_{\rm dyn}\neq0.
}
\]

Then

\[
m_f=yv
\]

persists.

## 6. Causal interpretation

The logical chain becomes

\[
\boxed{
\text{quantum dynamics generates a possible scale}
}
\]

plus

\[
\boxed{
\text{geometry changes the effective vacuum landscape}
}
\]

leading to

\[
\boxed{
\text{phase selection / transition}
\to
\text{persistent vacuum scale}
\to
\text{mass and proper-time clock}.
}
\]

Thus geometry may act as a **selector or trigger**, but in the minimal persistent model it is not the sole creator of the scale.

## 7. Backreaction

Once the field settles at `v`, its stress tensor changes and therefore the geometry responds:

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
=8\pi G\,T_{\mu\nu}^{\rm eff}.
\]

The full structure is a feedback loop:

\[
\boxed{
R(t)
\to
V_{\rm eff}(\phi,R)
\to
v(t)
\to
m(t),T_{\mu\nu}(t)
\to
R(t).
}
\]

This is self-consistent curved-spacetime field theory, not yet a new LTG equation.

## 8. Parameter-reduction test

In the purely curvature-induced adiabatic phase,

\[
\frac{m_f^2}{|R|}
=\frac{y^2|\xi|}{\lambda}.
\]

The candidate dimensionless ratio is therefore controlled by arbitrary couplings.

With dimensional transmutation,

\[
\frac{m_f}{\Lambda_{\rm dyn}}
=yC_v
\]

is again controlled by couplings/nonperturbative constants.

No coupling-independent LTG ratio emerges automatically.

## 9. Result

### EXP-040A

Curvature can induce a broken phase and temporary mass scale in a classically scale-free scalar model.

### EXP-040B

The minimal `lambda phi^4 + xi R phi^2` theory has **no vacuum memory**: all induced masses vanish as `R -> 0`.

### EXP-040C

Persistent mass requires an additional scale-generating/history-bearing ingredient.

### EXP-040D

Once that ingredient is added, the construction maps to known dimensional-transmutation / curvature-induced symmetry-breaking physics, and the resulting ratios remain coupling dependent.

## 10. Consequence for LTG

The idea that geometry alone continuously converts a null/scale-free world into fixed particle masses does not survive the flat-space and dimensional-analysis tests.

The strongest viable causal interpretation is instead:

\[
\boxed{
\text{causal geometry may trigger/select a vacuum,
while quantum dynamics supplies a persistent invariant scale.}
}
\]

This is physically coherent but known in broad form.

## 11. Next experiment

A remaining possibility is **dynamical locking** rather than algebraic proportionality:

- `R` and the order parameter evolve together;
- the coupled system might possess an attractor;
- a dimensionless ratio could approach a fixed value independent of part of the initial data.

The next test should write the coupled FLRW + scalar equations and determine whether any attractor ratio such as

\[
\mathcal Q=\frac{m^2}{H^2}
\]

or

\[
\mathcal Q_R=\frac{m^2}{|R|}
\]

is universal or merely a function of couplings.
