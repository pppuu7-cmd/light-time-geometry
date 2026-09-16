# Light-Time Geometry (LTG)

Exploratory theoretical-physics research project investigating whether the familiar distinction between null and timelike motion can support a nontrivial dynamical interpretation linking radiation, mass, proper time, and spacetime geometry.

## Scientific status

LTG is a hypothesis-development and falsification project, not an established theory. The starting observations are standard relativity; any claim of new physics must survive explicit equivalence checks against special relativity, general relativity, relativistic quantum mechanics/QFT, and standard cosmology.

## Core question

Can the mass-shell relation

\[
E^2=p^2c^2+m^2c^4
\]

be embedded in a mathematically consistent structure in which the null (`m = 0`, `d\tau = 0`) and timelike (`m > 0`, `d\tau > 0`) sectors arise as physically meaningful regimes of a deeper object, rather than merely as a re-labelling of standard relativistic kinematics?

A stronger exploratory question is whether the emergence of nonzero proper time can be coupled to a change in spacetime geometry or cosmological scale without contradicting known conservation laws and observations.

## Working principles

1. **Recover known physics first.** Any candidate construction must reproduce standard special relativity in the appropriate limit.
2. **Separate identity from novelty.** Rewriting a known equation in new variables does not count as new physics.
3. **Try to falsify the idea.** Each step must include conditions under which the hypothesis would be rejected.
4. **Track assumptions explicitly.** No physical interpretation is accepted merely because an algebraic parameterization exists.
5. **Demand an observable difference.** A viable LTG extension must eventually produce at least one testable result not already implied by standard theory.

## Initial decomposition

For exploratory purposes define

\[
Q_s \equiv pc, \qquad Q_\tau \equiv mc^2,
\]

so that

\[
E^2 = Q_s^2 + Q_\tau^2.
\]

At this stage `Q_s` and `Q_tau` are only bookkeeping variables. The first task is to determine whether assigning them "null/spatial" and "timelike/proper-time" interpretations adds any invariant content or merely restates the standard hyperbolic geometry of four-momentum.

## Research gates

### Gate A — Kinematic equivalence
Determine whether the proposed light/time decomposition is exactly equivalent to rapidity, four-velocity, or four-momentum parameterizations already present in special relativity.

### Gate B — Dynamical content
If Gate A leaves room for additional structure, formulate a Lorentz-covariant dynamical law rather than an interpretation only.

### Gate C — Geometry coupling
Test whether a new variable can consistently couple to `g_{mu nu}` while respecting the Bianchi identity and local stress-energy conservation.

### Gate D — Cosmology
Only after A-C, test homogeneous/isotropic reductions against the Friedmann equations, radiation/matter scaling, and observational constraints.

### Gate E — Distinct prediction
Identify a falsifiable prediction that differs from GR/QFT without violating established precision tests.

## Repository map

- `hypothesis/` — definitions, assumptions, conjectures, falsification criteria.
- `theory/` — derivations and equivalence checks against established physics.
- `experiments/` — analytic and numerical tests.
- `results/` — confirmed identities, falsified variants, and open questions.

## First experiment

`EXP-001` asks the narrowest useful question:

> Does the decomposition `E^2 = (pc)^2 + (mc^2)^2`, together with proper-time kinematics, contain any invariant degree of freedom beyond ordinary special relativity?

If the answer is no, that result is recorded rather than hidden; the project then moves to the smallest possible extension that could introduce genuinely new content.
