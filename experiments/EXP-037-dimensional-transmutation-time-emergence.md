# EXP-037 — Dimensional transmutation, composite mass, and proper-time emergence

## Objective

Follow the strongest refined LTG chain through a theory that is classically massless but generates a physical scale quantum mechanically.

This directly tests whether the conceptual sequence

\[
\text{scale-free}
\to
\text{generated scale}
\to
\text{mass}
\to
\text{proper-time phase}
\to
\text{stress trace}
\to
\text{curvature}
\]

can occur without inserting an explicit elementary rest mass by hand.

## 1. Start with a classically scale-free gauge sector

Consider schematically a four-dimensional gauge theory with no explicit mass parameter in the classical Lagrangian,

\[
\mathcal L
=-\frac14F^a_{\mu\nu}F_a^{\mu\nu}
+\text{massless matter terms}.
\]

The gauge coupling `g` is dimensionless in four spacetime dimensions.

At the classical level the theory can be scale invariant (subject to the detailed field content and improvement of the stress tensor).

There is no elementary Compton scale of the form

\[
\hbar/(mc)
\]

because no explicit `m` is present.

## 2. Renormalization generates a scale

Quantum mechanically, if

\[
\beta(g)\equiv\mu\frac{dg}{d\mu}\neq0,
\]

scale invariance is broken by renormalization.

A renormalization-group invariant dynamical scale can be defined schematically by

\[
\boxed{
\Lambda_{\rm dyn}
=\mu\exp\left[-\int^{g(\mu)}\frac{dg'}{\beta(g')}\right]
}
\]

with the precise convention depending on the theory and normalization.

This is dimensional transmutation: dimensionless coupling information is traded for a dimensionful invariant scale.

## 3. Composite masses can emerge from the dynamical scale

If the quantum theory develops a mass gap / bound states, their masses take the form

\[
\boxed{
M_n=C_n\frac{\hbar\Lambda_{\rm dyn}}{c}
}
\]

if `Lambda_dyn` is written as an inverse-length scale, or equivalently `M_n c^2 = C_n hbar omega_dyn` if it is represented as a frequency scale.

The dimensionless coefficients `C_n` are nonperturbative dynamical information.

The important LTG point is structural:

\[
\boxed{
\text{no explicit elementary mass}
\not\Rightarrow
\text{no massive timelike excitations}.
}
\]

A scale can arise dynamically first, with composite mass following from it.

## 4. Proper time appears at the composite level

Once a stable or sufficiently long-lived composite excitation has invariant mass `M_n`, its on-shell trajectory satisfies

\[
g^{\mu\nu}p_\mu p_\nu=-M_n^2c^2
\]

and therefore supports ordinary timelike proper time

\[
ds^2=-c^2d\tau^2.
\]

Its invariant phase is

\[
\boxed{
\Phi_n
=-\frac{M_nc^2}{\hbar}\int d\tau.
}
\]

Define its dynamically generated Compton time

\[
\boxed{
\tau_{C,n}
=\frac{\hbar}{M_nc^2}.
}
\]

Then

\[
\Phi_n=-\int\frac{d\tau}{\tau_{C,n}}.
\]

Thus a quantum-generated scale supplies the clock scale against which composite proper time accumulates phase.

## 5. The same quantum scale appears in the trace

The renormalized stress-energy trace contains the gauge trace anomaly schematically

\[
\boxed{
T^\mu{}_{\mu}
\supset
\frac{\beta(g)}{2g}
F^a_{\rho\sigma}F_a^{\rho\sigma}.
}
\]

Hence the same running that generates `Lambda_dyn` also makes the stress tensor trace nonzero.

This produces the structural chain

\[
\boxed{
\beta(g)\neq0
\to
\Lambda_{\rm dyn}
\to
\{M_n\}
\quad\text{and}\quad
T^\mu{}_{\mu}\neq0.
}
\]

The two descendants are not generally related by one elementary algebraic formula because the spectrum depends on nonperturbative coefficients and the trace depends on the quantum state/operators.

## 6. Geometry

Einstein's trace equation remains

\[
R-4\Lambda
=-\frac{8\pi G}{c^4}\langle T^\mu{}_{\mu}\rangle.
\]

Therefore quantum dimensional transmutation can activate the scalar-curvature trace channel even before describing matter as a dilute gas of massive on-shell particles.

This gives the broader path

\[
\boxed{
\text{quantum scale generation}
\to
\text{trace anomaly}
\to
\text{Ricci-scalar response}
}
\]

and, when massive composites exist,

\[
\boxed{
\text{quantum scale generation}
\to
\text{composite mass}
\to
\text{timelike proper-time phase}.
}
\]

## 7. Generalized trace/scale fraction

Define

\[
\boxed{
\chi_{\rm scale}
\equiv
-\frac{\langle T^\mu{}_{\mu}\rangle}{\varepsilon}
}
\]

for a state with positive reference energy density `epsilon`.

Then Einstein's trace equation becomes

\[
\boxed{
R-4\Lambda
=\frac{8\pi G}{c^4}\varepsilon\chi_{\rm scale}.
}
\]

### Classical on-shell particle gas

For the EXP-033 regime,

\[
\boxed{
\chi_{\rm scale}=\chi_\tau
=\left\langle\left(\frac{d\tau}{dt}\right)^2\right\rangle_E.
}
\]

### General quantum system

In general,

\[
\boxed{
\chi_{\rm scale}
=\chi_\tau
+\chi_{\rm anomaly}
+\chi_{\rm interaction/vacuum}
}
\]

as a schematic decomposition only; the pieces need not be separately unique or scheme independent in an arbitrary QFT.

The total trace and therefore the total `chi_scale` are the physically relevant quantities once a renormalized stress tensor is specified.

## 8. Important range test

For the classical massive/massless particle mixtures studied earlier,

\[
0\le\chi_\tau\le1.
\]

But `chi_scale` is more general.

For a perfect fluid,

\[
\chi_{\rm scale}=1-3w.
\]

Thus:

- ideal radiation: `w=1/3 -> chi_scale=0`;
- cold matter: `w=0 -> chi_scale=1`;
- vacuum-energy-like component: `w=-1 -> chi_scale=4`.

Therefore `chi_scale` cannot in general be interpreted as a probability or literal fraction of proper time. The interval `[0,1]` is special to the ordinary classical particle sector.

This sharply separates the successful LTG kinetic interpretation from the more general gravitational trace variable.

## 9. Result

### EXP-037A

A classically massless/scale-free theory can generate an invariant quantum scale through renormalization.

### EXP-037B

That generated scale can simultaneously support:

- a nonzero trace anomaly;
- a composite mass spectrum;
- timelike proper-time phases for massive bound states.

### EXP-037C

This provides a deeper standard-physics realization of the original LTG emergence intuition without requiring elementary mass as the first step.

### EXP-037D

No new LTG equation has appeared: the chain is standard renormalization-group/QFT physics plus Einstein gravity.

## 10. Revised conceptual hierarchy

The strongest hierarchy currently supported is

\[
\boxed{
\text{causal geometry}
\supset
\text{null/timelike kinematics}
}
\]

with

\[
\boxed{
\text{invariant scale generation}
\to
\text{mass/clock scales and/or trace}
}
\]

and

\[
\boxed{
\text{stress trace}
\to
\text{Ricci-scalar channel of geometry}.
}
\]

Rest mass is therefore one especially direct bridge between proper time and scale, but not the universal origin of geometric trace response.

## 11. Next novelty gate

The next useful question is whether LTG can impose a parameter-reducing relation between the two descendants of scale generation:

\[
\text{composite clock scale } M_n
\quad\text{and}\quad
\text{gravitational trace response }\langle T\rangle.
\]

Standard QFT does not reduce the entire nonperturbative spectrum to one local trace value. A genuinely new LTG principle would need to fix a dimensionless ratio or spectral relation that survives known QFT constraints.

Absent such a relation, the project should classify the scale-emergence branch as an interpretation/synthesis of established conformal anomaly, dimensional transmutation, and GR.
