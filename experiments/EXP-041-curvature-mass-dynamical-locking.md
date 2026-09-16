# EXP-041 — Curvature–mass dynamical locking test

## Objective

Test whether a curvature-sensitive scale-free scalar can dynamically approach a fixed mass/geometry ratio, even though a universal algebraic law `m^2 proportional R` failed in EXP-039/040.

The key distinction is:

- **algebraic law:** mass is always locally fixed by curvature;
- **dynamical locking:** evolution drives a broad set of initial conditions toward a common ratio.

A true LTG novelty candidate would require the attractor ratio to be more universal than an arbitrary function of microscopic couplings.

## 1. Minimal dynamical model

Use natural units and the scalar equation in an approximately FLRW/de Sitter background,

\[
\ddot\phi+3H\dot\phi+\xi R\phi+\lambda\phi^3=0,
\]

with

\[
R\simeq12H^2
\]

for a spatially flat quasi-de Sitter phase.

The effective potential is

\[
V_{\rm eff}(\phi)
=\frac12\xi R\phi^2
+\frac\lambda4\phi^4.
\]

Assume

\[
\lambda>0,
\qquad
\xi R<0,
\]

so a broken-phase minimum exists.

## 2. Fixed point

The stationary nonzero solution obeys

\[
\xi R\phi+\lambda\phi^3=0,
\]

hence

\[
\boxed{
\phi_*^2=-\frac{\xi R}{\lambda}
=-\frac{12\xi}{\lambda}H^2.
}
\]

If a matter field obtains mass through

\[
m=y|\phi|,
\]

then at the fixed point

\[
\boxed{
\frac{m_*^2}{H^2}
=-\frac{12y^2\xi}{\lambda}.
}
\]

Similarly,

\[
\boxed{
\frac{m_*^2}{|R|}
=\frac{y^2|\xi|}{\lambda}.
}
\]

Thus a dimensionless geometry/mass ratio can indeed become constant dynamically.

## 3. Stability

Write

\[
\phi=\phi_*+\delta\phi.
\]

The effective curvature of the potential at the broken minimum is

\[
V''(\phi_*)
=\xi R+3\lambda\phi_*^2.
\]

Using

\[
\lambda\phi_*^2=-\xi R,
\]

we obtain

\[
\boxed{
V''(\phi_*)=-2\xi R>0.
}
\]

The linearized perturbation equation is

\[
\delta\ddot\phi
+3H\delta\dot\phi
+(-2\xi R)\delta\phi=0.
\]

For `H > 0` and `-2 xi R > 0`, Hubble friction damps a broad range of perturbations toward the minimum.

Therefore the ratio above can be an attractor with respect to initial conditions.

## 4. What is and is not universal

The attractor removes sensitivity to the initial field value and velocity, but its value is

\[
\boxed{
\mathcal Q_*
\equiv\frac{m_*^2}{H^2}
=-\frac{12y^2\xi}{\lambda}.
}
\]

Hence the fixed ratio depends explicitly on the microscopic couplings

\[
y,\quad\xi,\quad\lambda.
\]

Different theories give different attractor ratios.

Thus

\[
\boxed{
\text{initial-condition universality}
\neq
\text{parameter universality}.
}
\]

This is the central result of EXP-041.

## 5. Backreaction does not automatically solve the problem

In the fully coupled theory with action schematically

\[
S=\int d^4x\sqrt{-g}
\left[
\frac12(M_P^2-\xi\phi^2)R
-\frac12(\partial\phi)^2
-\frac\lambda4\phi^4
\right],
\]

the scalar contributes to the Friedmann equations and the effective gravitational coupling is field dependent.

Solving the full fixed-point conditions changes numerical coefficients and may create additional branches, but the equations still contain the same dimensionless couplings.

Absent a new symmetry or fixed-point principle, any constant ratio remains a function of those couplings.

Therefore gravitational backreaction can create self-consistent scaling solutions but does not by itself generate a parameter-free LTG prediction.

## 6. Connection to clock rate

At the attractor,

\[
\omega_C=m_*
\]

in natural units, so

\[
\boxed{
\frac{\omega_C}{H}
=\sqrt{-\frac{12y^2\xi}{\lambda}}.
}
\]

This gives exactly the type of clock/geometry locking sought by LTG:

\[
\text{Compton clock rate}
\propto
\text{cosmological expansion rate}.
\]

But the proportionality factor is not fixed by geometry alone.

## 7. Loss of locking after the geometric phase

If the background later evolves toward

\[
R\to0
\]

and the model has no separate persistent scale, then

\[
\phi_*\to0,
\qquad
m_*\to0.
\]

Thus the dynamical attractor does not solve the vacuum-memory no-go of EXP-040.

A persistent late-time mass still requires dimensional transmutation, a separate condensate, explicit symmetry breaking, or another memory mechanism.

## 8. Result

### EXP-041A

Curvature-coupled field dynamics can produce an attractor with a constant dimensionless ratio `m/H` or `m^2/R`.

### EXP-041B

The attractor can erase initial-condition dependence.

### EXP-041C

The attractor value remains an explicit function of microscopic couplings. No coupling-independent LTG constant appears.

### EXP-041D

Without a second scale/memory mechanism, the mass still disappears when the curvature trigger disappears.

## 9. Status of the geometry-generates-mass route

The route is now strongly constrained:

\[
\boxed{
\text{geometry can trigger, temporarily induce, or dynamically lock a mass scale,}
}
\]

but

\[
\boxed{
\text{geometry alone has not fixed a persistent universal particle mass.}
}
\]

Every tested mechanism is standard curvature-induced field dynamics and remains coupling dependent.

## 10. Next conceptual gate

To obtain a genuinely parameter-reducing law, one needs a principle that fixes the dimensionless couplings or selects a special fixed point.

Candidate sources include:

1. an RG fixed point determining coupling ratios;
2. an enhanced symmetry at a critical point;
3. topological quantization;
4. a consistency condition joining causal geometry and quantum phase.

Among these, an RG fixed-point test is the least arbitrary and has substantial prior art. The next experiment should ask whether a fixed point can make `omega_C/H` universal, and whether such behavior is already standard asymptotic-safety / conformal-fixed-point physics.
