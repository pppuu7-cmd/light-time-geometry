# LTG Research Status v2 — after EXP-038

## Confirmed structural core

The project has converged on the following exact standard-physics structure.

### 1. Tangent/cotangent dual norms

For timelike motion,

\[
-g_{\mu\nu}dx^\mu dx^\nu=c^2d\tau^2,
\]

while on the massive mass shell,

\[
-g^{\mu\nu}p_\mu p_\nu=m^2c^2.
\]

The same metric/inverse-metric pair therefore defines the invariant proper-time norm and invariant mass norm on dual spaces.

### 2. Light is the null boundary

For ideal massless propagation,

\[
g(dx,dx)=0,
\qquad d\tau=0,
\qquad p^2=0,
\qquad m=0.
\]

Light is not literally the negative of time. It is the null-balance sector of the same Lorentzian causal geometry.

### 3. Exact SR projection identity

For an on-shell free particle in a local inertial frame,

\[
\frac{d\tau}{dt}=\frac{mc^2}{E},
\qquad
\frac{v}{c}=\frac{pc}{E},
\]

so

\[
\left(\frac{v}{c}\right)^2+
\left(\frac{d\tau}{dt}\right)^2=1.
\]

### 4. Classical kinetic trace theorem

For an isotropic on-shell particle ensemble,

\[
\chi_\tau
\equiv
\left\langle\left(\frac{d\tau}{dt}\right)^2\right\rangle_E
=1-3w,
\]

and

\[
-T_{\rm kin}=\varepsilon\chi_\tau.
\]

Combined with Einstein gravity,

\[
\boxed{
R-4\Lambda
=\frac{8\pi G}{c^4}\varepsilon\chi_\tau
}
\]

for the stated classical kinetic sector.

EXP-034 verified this dynamically for null-to-massive conversion and found no residual beyond standard GR + kinetic theory:

\[
\Delta_{\rm LTG}=0.
\]

### 5. Quantum boundary of the proper-time theorem

The classical identity is not universal in QFT because trace anomalies and other non-kinetic contributions can make

\[
\langle T^\mu{}_{\mu}\rangle\neq0
\]

even when the fundamental fields are massless.

Therefore the broader object is the stress trace / scale-breaking sector, not particle mass alone.

Define schematically

\[
\chi_{\rm scale}
\equiv
-\frac{\langle T\rangle}{\varepsilon}.
\]

For the ordinary classical particle sector,

\[
\chi_{\rm scale}=\chi_\tau,
\]

but this equality need not hold for a general quantum state.

### 6. Dimensional transmutation

A classically scale-free theory can generate a dynamical invariant scale through quantum running,

\[
\beta(g)\neq0
\to
\Lambda_{\rm dyn}.
\]

If massive composites form,

\[
M_n\sim C_n\Lambda_{\rm dyn},
\]

then they acquire timelike worldlines and proper-time phase

\[
\Phi_n=-\frac{M_nc^2}{\hbar}\tau.
\]

Thus timelike clock scales can emerge without an explicit elementary mass parameter.

### 7. Quantum one-particle trace/mass bridge

For a stable one-particle state, the forward matrix element of the total conserved energy-momentum tensor is normalized by translation symmetry. With project signature `(-,+,+,+)`, its reduced trace satisfies schematically

\[
\langle P|T^\mu{}_{\mu}|P\rangle_{\rm red}=-2M^2
\]

in natural units.

The same mass fixes the Compton clock rate

\[
\omega_C=Mc^2/\hbar.
\]

Therefore there is a quantum-level bridge

\[
\boxed{
\text{total EMT trace}
\leftrightarrow
M^2
\leftrightarrow
\omega_C^2
\leftrightarrow
\text{proper-time phase}.
}
\]

## What has been falsified or demoted

The following strong claims are not supported:

1. **"Mass creates spacetime geometry."** False as stated: vacuum and radiation geometries exist.
2. **"Light literally converts into time."** Unsupported; light is the null sector, while proper time is the timelike norm.
3. **"Any creation of massive particles causes extra expansion beyond GR."** EXP-034 gives `Delta_LTG = 0` for ordinary on-shell conversion.
4. **"The Ricci trace is uniquely a measure of massive-particle proper time."** False in full QFT because of trace anomalies and other quantum contributions.
5. **"Coordinate-momentum reciprocity is unique to LTG."** False; Born reciprocity/Born geometry and curved-momentum-space frameworks already explore this territory.

## Strongest current interpretation

The project now supports the following hierarchy:

\[
\boxed{
\text{causal/Lorentzian geometry}
\to
\begin{cases}
\text{null sector: zero proper-time norm},\\
\text{timelike sector: nonzero proper-time norm},
\end{cases}}
\]

while invariant scale generation gives

\[
\boxed{
\text{invariant scale}
\to
\text{mass/clock scales and/or stress trace},
}
\]

and the stress tensor then sources spacetime geometry through Einstein gravity.

Mass is therefore not the universal creator of geometry. It is one particularly direct realization of a scale-bearing timelike sector.

## Novelty status

**No distinct LTG dynamical law has yet survived.**

The project has produced a coherent synthesis and several exact bridge identities, but every tested local dynamical relation through EXP-038 is contained in established SR/GR/QFT/KK/phase-space physics.

## Sharp next question

The remaining nontrivial possibility is upstream of mass itself:

> Can causal/null geometry determine or constrain the value of a dynamically generated quantum scale, rather than merely responding to the resulting stress tensor?

A positive answer would require a parameter-reducing relation between a geometric/causal invariant and an RG/symmetry-breaking scale that is not already curvature-induced symmetry breaking, horizon thermality, gravitational dimensional transmutation, or standard effective field theory.

That is the correct next novelty gate.
