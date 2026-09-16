# EXP-034 — Dynamic null-to-mass curvature residual test

## Objective

Test the strongest LTG bridge during an explicit conversion of null energy into massive/timelike particles, and determine whether any geometric residual remains beyond standard relativistic kinetic theory plus Einstein gravity.

The experiment is deliberately minimal: it does not assume a new LTG coupling. A nonzero residual is allowed only if it follows from an independently stated principle.

## 1. Toy process

Consider a local center-of-momentum region containing an initially isotropic massless population `r`. A standard interaction converts part of its energy into a pair of identical massive particles `m`:

\[
r+r\longleftrightarrow m+m.
\]

The detailed matrix element is not needed for the kinematic/geometric identity below. We only require:

1. every external particle is on shell;
2. total four-momentum is conserved in each microscopic collision;
3. the produced distribution is isotropized on the coarse-graining scale used to define `P`;
4. the stress tensor is described by the ordinary kinetic expression.

Let the center-of-momentum energy of one collision be

\[
\sqrt{s}.
\]

Each outgoing massive particle has

\[
E_m=\frac{\sqrt{s}}{2},
\]

and

\[
p_m^2c^2=E_m^2-m^2c^4.
\]

Define

\[
\gamma\equiv\frac{E_m}{mc^2}=\frac{\sqrt{s}}{2mc^2},
\qquad
\beta^2=1-\frac{1}{\gamma^2}.
\]

The threshold is

\[
\sqrt{s}\ge2mc^2.
\]

## 2. Proper-time fraction of the produced pair

For each produced massive particle,

\[
\frac{d\tau}{dt}=\frac{mc^2}{E_m}=\frac1\gamma.
\]

Therefore

\[
\boxed{\left(\frac{d\tau}{dt}\right)^2=\frac1{\gamma^2}}
\]

and the null limit is recovered continuously for `gamma -> infinity`, while threshold production gives `gamma=1` and maximal proper-time fraction.

## 3. Convert a finite energy fraction

Let `epsilon` be the total local energy density during an effectively instantaneous conversion step, and let

\[
F\equiv\frac{\varepsilon_m}{\varepsilon},
\qquad 0\le F\le1
\]

be the fraction of energy carried by the newly produced massive sector immediately after isotropization.

The remaining massless sector has

\[
\varepsilon_r=(1-F)\varepsilon,
\qquad
P_r=\frac13\varepsilon_r.
\]

For a monoenergetic isotropic massive population,

\[
P_m=\frac13\varepsilon_m\beta^2.
\]

Hence

\[
P
=\frac{\varepsilon}{3}
\left[(1-F)+F\beta^2\right]
=\frac{\varepsilon}{3}
\left[1-\frac{F}{\gamma^2}\right].
\]

Therefore

\[
\boxed{
w\equiv\frac{P}{\varepsilon}
=\frac13\left(1-\frac{F}{\gamma^2}\right)
}
\]

and

\[
\boxed{
1-3w=\frac{F}{\gamma^2}.
}
\]

## 4. Dynamic proper-time fraction

The energy-weighted proper-time fraction of the total mixture is

\[
\chi_\tau
\equiv
\frac{1}{\varepsilon}
\sum_i\int E_i
\left(\frac{d\tau_i}{dt}\right)^2
f_i\,d^3p.
\]

The massless population contributes zero. The monoenergetic massive sector contributes `1/gamma^2` weighted by its energy fraction `F`. Thus

\[
\boxed{
\chi_\tau=\frac{F}{\gamma^2}.
}
\]

Comparing with the pressure calculation,

\[
\boxed{
\chi_\tau=1-3w.
}
\]

This is the explicit process-level realization of EXP-033.

## 5. Stress-energy trace computed independently

For the coarse-grained perfect-fluid stress tensor,

\[
T=-\varepsilon+3P.
\]

Using the expression above,

\[
T
=-\varepsilon\frac{F}{\gamma^2}.
\]

Therefore

\[
\boxed{
-T=\varepsilon\chi_\tau
=\varepsilon\frac{F}{\gamma^2}.
}
\]

The same result follows directly from the massive on-shell kinetic identity

\[
\varepsilon_m-3P_m
=\int\frac{m^2c^4}{E}f_m\,d^3p.
\]

Thus the result is independent of interpreting `chi_tau` first: the stress tensor itself gives the same scalar.

## 6. Geometric response

Einstein's trace equation is

\[
R-4\Lambda=-\frac{8\pi G}{c^4}T.
\]

Hence the post-conversion scalar curvature channel is

\[
\boxed{
R-4\Lambda
=\frac{8\pi G}{c^4}\,
\varepsilon\frac{F}{\gamma^2}
}
\]

or

\[
\boxed{
R-4\Lambda
=\frac{8\pi G}{c^4}\,\varepsilon\chi_\tau.
}
\]

This gives a direct process-level map

\[
\boxed{
\text{null energy converted}
\to F
\to m>0
\to d\tau/dt>0
\to T\neq0
\to R-4\Lambda\neq0.
}
\]

## 7. Important energy dependence

The geometric trace response depends not only on how much energy becomes massive (`F`) but also on how relativistic the products are:

\[
\frac{R-4\Lambda}{(8\pi G/c^4)\varepsilon}
=\frac{F}{\gamma^2}.
\]

Two limiting cases are instructive.

### Threshold production

At

\[
\sqrt{s}=2mc^2,
\qquad \gamma=1,
\]

we have

\[
\chi_\tau=F,
\]

so all converted energy contributes maximally to the trace channel.

### Ultra-relativistic production

For

\[
\sqrt{s}\gg2mc^2,
\qquad\gamma\gg1,
\]

we have

\[
\chi_\tau\ll F.
\]

Thus creating particles with nonzero invariant mass does **not** immediately make the fluid strongly matter-like if those particles are highly relativistic. The relevant quantity is the timelike/proper-time fraction, not mass existence alone.

## 8. Post-production FLRW evolution

After production, suppose the massive particles free-stream collisionlessly in an FLRW background.

Their physical momentum redshifts as

\[
p(a)=p_*\frac{a_*}{a}.
\]

Therefore

\[
\gamma(a)
=\sqrt{1+\frac{p_*^2a_*^2}{m^2c^2a^2}}.
\]

For the massive component,

\[
\left(\frac{d\tau}{dt}\right)^2
=\frac{1}{\gamma(a)^2}
\]

increases monotonically toward unity as the particles cool.

Its number density scales as

\[
n_m\propto a^{-3},
\]

while its energy density is

\[
\varepsilon_m(a)=n_m(a)mc^2\gamma(a).
\]

The trace contribution is

\[
\boxed{
\varepsilon_m-3P_m
=\frac{\varepsilon_m}{\gamma(a)^2}
=\frac{n_mmc^2}{\gamma(a)}.
}
\]

Thus the scalar-curvature channel naturally strengthens relative to the massive component's own energy density as the produced particles transition from relativistic to nonrelativistic motion.

## 9. Define the LTG residual

Define

\[
\boxed{
\Delta_{\rm LTG}
\equiv
\left(R-4\Lambda\right)
-\frac{8\pi G}{c^4}\varepsilon\chi_\tau.
}
\]

Using only standard on-shell kinetic theory and Einstein gravity,

\[
\boxed{\Delta_{\rm LTG}=0}
\]

identically under the assumptions of this experiment.

No extra term is required by the null-to-mass conversion itself.

## 10. Result

### EXP-034A — Dynamic confirmation of the LTG bridge

The chain

\[
\text{null}\to\text{massive/timelike}\to\text{proper-time fraction}\to\text{stress trace}\to\text{Ricci scalar}
\]

holds dynamically for an explicit energy-conversion process.

The compact process-level identity is

\[
\boxed{
R-4\Lambda
=\frac{8\pi G}{c^4}\varepsilon\frac{F}{\gamma^2}.
}
\]

### EXP-034B — No new dynamical residual

For this entire class of ordinary on-shell 2-to-2 conversions,

\[
\boxed{\Delta_{\rm LTG}=0}
\]

unless an additional nonstandard coupling is inserted.

Therefore the currently established LTG bridge is a valid unifying reformulation of standard GR plus relativistic matter kinetics, not yet a distinct dynamical law.

## 11. What has now been proved within the stated assumptions

We can state a precise standard-physics theorem:

> For an isotropic ensemble of classical on-shell particles minimally coupled to Einstein gravity, the Ricci-scalar trace channel above the cosmological-constant contribution equals the total energy density multiplied by the energy-weighted squared proper-time rate:
>
> \[
> R-4\Lambda
> =\frac{8\pi G}{c^4}\varepsilon
> \left\langle\left(\frac{d\tau}{dt}\right)^2\right\rangle_E.
> \]

This identity remains valid while collisions convert massless and massive populations, provided the kinetic stress tensor description is applicable.

It is a theorem *inside standard GR + on-shell kinetic theory*, not a new fundamental law.

## 12. Next novelty gate

Since a local collision process produces no residual, the next useful question is not to add an arbitrary correction to Einstein's equation. Instead test whether the dual tangent/cotangent structure itself admits a deeper variational principle in phase space that:

1. treats the null boundary and timelike norm as phases of one dynamical object;
2. reproduces the standard bridge above in the low-energy limit;
3. fixes at least one otherwise-free parameter or observable;
4. is not equivalent to ordinary Hamiltonian mechanics on the cotangent bundle, Born reciprocity, doubly-special/relative-locality kinematics, or standard phase-space gravity.

That should be EXP-035.
