# EXP-042 — RG fixed point and clock/geometry universality test

## Objective

Test whether renormalization-group fixed points can remove the arbitrary-coupling problem found in EXP-041 and make a geometry/clock ratio genuinely universal.

## 1. Starting attractor relation

EXP-041 found, in a curvature-induced broken phase,

\[
\frac{\omega_C}{H}
=\sqrt{-\frac{12y^2\xi}{\lambda}}
\]

for the simple quasi-de Sitter benchmark.

The ratio is independent of initial conditions but depends on the running couplings

\[
y(\mu),\quad\xi(\mu),\quad\lambda(\mu).
\]

## 2. Fixed-point hypothesis

Suppose the coupled matter-gravity RG flow approaches a fixed point

\[
\beta_y(y_*,\xi_*,\lambda_*,\ldots)=0,
\]

\[
\beta_\xi(y_*,\xi_*,\lambda_*,\ldots)=0,
\]

\[
\beta_\lambda(y_*,\xi_*,\lambda_*,\ldots)=0.
\]

Then the attractor ratio would formally approach

\[
\boxed{
\mathcal Q_*
\equiv\left(\frac{\omega_C}{H}\right)_*
=\sqrt{-\frac{12y_*^2\xi_*}{\lambda_*}}.
}
\]

If all three fixed-point values were physically unique and the broken-phase solution existed, this would remove the freedom in the ratio inside that universality class.

## 3. Important first caveat: an exact fixed point is scale invariant

At an exact RG fixed point the dimensionless couplings stop running and the theory is scale invariant/conformal under suitable conditions.

An intrinsic particle mass scale cannot generally arise from the fixed point alone unless another scale is supplied by:

- the curved background (`H`, `R`);
- spontaneous breaking;
- a relevant deformation;
- finite temperature/density;
- boundary conditions.

Therefore a fixed point can determine **dimensionless ratios**, but it does not by itself generate a persistent dimensionful mass in flat spacetime.

## 4. Background-induced mass at the fixed point

If curvature supplies the temporary scale, the fixed-point couplings can yield

\[
m_*\propto H
\]

with a fixed coefficient.

This is a legitimate scaling solution:

\[
\boxed{
\text{RG fixed point}
+\text{geometric scale }H
\to
\text{fixed }m/H.
}
\]

But once

\[
H\to0,
\]

the mass again vanishes unless the RG trajectory leaves the fixed point or another order parameter retains a scale.

Thus the fixed point solves parameter-locking but not the vacuum-memory problem.

## 5. Leaving the fixed point introduces relevant parameters

A realistic theory with a persistent low-energy mass scale must flow away from the fixed point along one or more relevant directions.

Near a fixed point, a relevant deformation has the schematic form

\[
g_i(k)-g_{i,*}
\sim C_i\left(\frac{k}{k_0}\right)^{-\theta_i}
\]

with positive critical exponent `theta_i` under the chosen convention.

The coefficients `C_i` encode the RG trajectory.

These are integration constants / physical parameters that determine crossover scales.

Hence dimensional transmutation or crossover generically reintroduces at least one dimensionful scale

\[
\Lambda_{\rm cross}.
\]

Low-energy masses then have the form

\[
M_n
=\Lambda_{\rm cross}\,
F_n(\text{dimensionless trajectory data}).
\]

Therefore the fixed point does not automatically predict all masses from geometry alone.

## 6. Universality versus scheme/truncation dependence

Individual fixed-point coordinates such as

\[
y_*,\xi_*,\lambda_*
\]

need not be separately scheme independent in an approximate RG treatment.

Universal physical information is more robustly associated with:

- existence of the fixed point;
- number of relevant directions;
- critical exponents;
- genuinely observable amplitude ratios or S-matrix quantities.

Therefore the formal ratio

\[
-12y_*^2\xi_*/\lambda_*
\]

cannot be called a universal LTG prediction merely because it is built from fixed-point coordinates.

One must demonstrate scheme-independent observable meaning.

## 7. Prior-art classification

Gravity-matter fixed points, including nonminimal scalar couplings, Yukawa interactions, and quartic interactions, are already studied within asymptotic-safety and gauge-Yukawa fixed-point programs.

Those frameworks explicitly use RG fixed points to reduce the number of free parameters and constrain IR couplings.

Therefore the mechanism

\[
\text{gravity + RG fixed point}
\to
\text{predicted coupling ratios}
\]

is not unique to LTG.

## 8. Result

### EXP-042A

An RG fixed point can in principle turn the EXP-041 clock/geometry attractor from an initial-condition attractor into a coupling-space attractor.

### EXP-042B

At an exact fixed point, geometry may supply the only dimensionful background scale, yielding a temporary fixed ratio `m/H`.

### EXP-042C

Persistent flat-space masses require leaving the fixed point or adding symmetry-breaking/history data, reintroducing relevant trajectory parameters or a transmutation scale.

### EXP-042D

Fixed-point coordinates alone are not automatically scheme-independent observables.

### EXP-042E

The entire mechanism has established prior art in asymptotic-safety / interacting-fixed-point physics.

## 9. Consequence for the LTG novelty search

The sequence

\[
\boxed{
\text{geometry}
\to
\text{RG scale/fixed point}
\to
\text{mass/clock ratio}
}
\]

can be physically meaningful, but no LTG-specific law has emerged.

To become distinct, LTG would have to supply a new consistency condition that:

1. selects a particular RG trajectory or fixed point;
2. fixes a physical dimensionless observable;
3. follows from causal/null geometry rather than being imposed as an RG boundary condition.

## 10. Current endpoint

After EXP-034–042, every natural local route has mapped to known structures:

- Einstein + kinetic theory;
- canonical phase-space / Born reciprocity;
- conformal anomaly and dimensional transmutation;
- curvature-induced symmetry breaking;
- scalar-tensor backreaction;
- RG fixed points / asymptotic safety.

The project should therefore avoid adding arbitrary new local operators merely to force novelty.

The remaining genuinely distinct possibility would require a **global causal consistency principle** capable of selecting quantum scale data (RG trajectory, boundary condition, topological sector, or phase quantization) from geometry.

That is a qualitatively different research program and should be isolated as a new gate rather than mixed with the already-closed local-dynamics branch.
