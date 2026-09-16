# EXP-014 — Dynamical zero-mode → massive-pair transition

## Objective

Construct an explicit interacting model in which 4D massless/null modes convert into 4D massive/timelike modes while preserving 5D covariance, energy-momentum conservation, and hidden momentum conservation.

This is the closest direct test so far of the original LTG intuition that a lightlike sector can dynamically feed a massive/proper-time sector.

## 1. Interacting 5D massless field

Take a real 5D scalar on a compact circle,

\[
S=\int d^4x\,d\psi\,\sqrt{-G}\left[
-\frac12G^{AB}\partial_A\Phi\partial_B\Phi
-\frac{\lambda_5}{4!}\Phi^4
\right],
\]

with

\[
\psi\sim\psi+2\pi R_0.
\]

There is no explicit 5D mass term.

For a flat or slowly varying compactification background,

\[
\Phi(x,\psi)
=\frac{1}{\sqrt{2\pi R_0}}
\sum_{n\in\mathbb Z}
\phi_n(x)e^{in\psi/R_0},
\]

with the reality condition

\[
\phi_{-n}=\phi_n^*.
\]

## 2. 4D masses

The hidden gradient produces

\[
m_n=\frac{|n|\hbar}{cbR_0}.
\]

Therefore

\[
n=0\Rightarrow m_0=0,
\]

while

\[
n\neq0\Rightarrow m_n>0.
\]

In the WKB/geometric-optics limit the `n=0` mode has a null 4D mass shell and `n != 0` modes have timelike 4D mass shells.

## 3. Interaction selection rule

Substitute the mode expansion into the quartic interaction and integrate over the compact coordinate. The hidden integral gives

\[
\int_0^{2\pi R_0}d\psi\,
\exp\left[
\frac{i(n_1+n_2+n_3+n_4)\psi}{R_0}
\right]
\propto
\delta_{n_1+n_2+n_3+n_4,0}.
\]

Thus every interaction vertex obeys

\[
\boxed{
n_1+n_2+n_3+n_4=0.
}
\]

This is conservation of the hidden translation momentum.

## 4. Massless → massive pair conversion

The process

\[
0+0\rightarrow n+(-n)
\]

satisfies the selection rule because

\[
0+0=n+(-n).
\]

Thus two zero modes can, provided enough center-of-mass energy is available, scatter into a pair of opposite hidden momenta.

The 4D threshold is

\[
\boxed{
\sqrt{s}\ge2m_n c^2.
}
\]

The initial 4D modes are massless; the final 4D modes are massive.

Yet the total hidden momentum remains zero:

\[
p_{\psi,\rm tot}^{\rm in}=0
=p_{\psi,\rm tot}^{\rm out}.
\]

No hidden momentum is created from nothing; equal and opposite components are generated.

## 5. Geometric interpretation

For each outgoing mode,

\[
m_nc=\frac{|p_\psi|}{b}>0,
\]

so its 4D projection is timelike and admits nonzero proper time.

The conversion can therefore be summarized as

\[
\boxed{
(0,0)_{\rm hidden\ momentum}
\rightarrow
(+p_\psi,-p_\psi)
}
\]

which a 4D observer describes as

\[
\boxed{
\text{massless/null energy}
\rightarrow
\text{massive/timelike pair}.
}
\]

This is a much more precise statement than "light turns into time." The deeper 5D description is redistribution of energy into opposite hidden momentum sectors.

## 6. Proper-time phase after production

Each outgoing mode satisfies

\[
m_nc^2d\tau=|p_\psi d\psi|.
\]

Thus the interaction creates two 4D excitations for which a proper-time phase exists:

\[
d\phi_C
=\frac{m_nc^2}{\hbar}d\tau.
\]

Before the collision, the `n=0` external modes have no corresponding massive Compton phase; after the collision, the `+n` and `-n` sectors do.

This supplies an explicit dynamical realization of a null-to-timelike transition at the 4D level.

## 7. Stress-energy and geometry

If the produced massive modes later become nonrelativistic, their coarse-grained equation of state changes from radiation-like toward matter-like:

\[
P/\rho: \quad 1/3\rightarrow0.
\]

Their contribution to the stress-energy trace becomes nonzero:

\[
T=-\rho+3P.
\]

Because their masses depend on `b`, they also source the radion/internal metric through the same reduced action.

The full structural chain is therefore

\[
\boxed{
\text{zero-mode interaction}
\rightarrow
\pm p_\psi
\rightarrow
m_{4D}>0
\rightarrow
d\tau>0
\rightarrow
T\neq0\ (\text{nonrelativistic limit})
\rightarrow
\text{geometric/radion response}.
}
\]

Every arrow can arise from one interacting 5D variational principle.

## 8. Conservation-law result

This experiment resolves a conceptual problem in the original wording.

A free isolated massless mode cannot simply acquire nonzero hidden momentum if the compact direction is translationally symmetric. The conserved Noether charge forbids it.

But interactions may redistribute zero total hidden momentum into opposite nonzero values:

\[
0\rightarrow(+n)+(-n).
\]

Hence a viable null-to-timelike conversion mechanism naturally produces massive sectors in compensating hidden-momentum combinations.

## 9. Novelty status

KK number/momentum conservation and pair production of KK excitations are standard consequences of compact extra dimensions. In universal-extra-dimension models, the remnant KK parity is well known to enforce pair-production patterns.

Therefore this is not new physics by itself.

### F-014A

**A fully explicit, conservation-respecting 4D null-to-timelike transition exists in the interacting compact 5D model.**

### F-014B

**The transition is best interpreted as redistribution of energy into opposite hidden momenta, not conversion of a substance called light into a substance called time.**

### F-014C

**The same transition automatically creates the ingredients needed for a later trace/radion/geometric response.**

### F-014D

**The mechanism is known Kaluza–Klein interaction physics and therefore does not yet constitute an LTG novelty claim.**

## 10. Strongest current LTG statement

The project now has an explicit mathematical realization of the original intuition:

> A higher-dimensional massless/null theory can contain a 4D massless sector and 4D massive/timelike sectors. Interactions can transfer energy from zero hidden momentum into opposite nonzero hidden momenta, producing massive 4D excitations with proper-time phase while conserving the full higher-dimensional momentum. Those massive sectors then source geometry differently through their stress-energy and radion dependence.

The next question is whether the **backreaction during the conversion itself** enforces any invariant relation between the production of massive modes and visible expansion that is stronger than ordinary KK/GR dynamics.

That is the natural target for EXP-015.

## Literature anchor

The conservation of KK number (or its remnant KK parity after orbifolding) and consequent pair-production structure are standard features of compact extra-dimensional models; see, e.g., Hooper & Profumo, *Dark Matter and Collider Phenomenology of Universal Extra Dimensions*, arXiv:hep-ph/0701197.
