# EXP-045 — Pressure-sign reversal under geometric response

## Objective

Test the refined hypothesis:

> The sign change need not occur in photon energy. Photon energy may remain positive while the response of the system to cosmological geometry changes sign, primarily through an effective pressure.

The gate distinguishes:

1. equilibrium photon pressure;
2. geometry-defined total effective pressure;
3. bulk-viscous pressure;
4. gravitational particle-creation pressure;
5. horizon/global-causal pressure.

The central question is whether

\[
\rho>0
\]

can coexist with a geometry-driven transition

\[
p_{\rm eff}>0
\to
p_{\rm eff}=0
\to
p_{\rm eff}<0
\]

without requiring negative photon energy.

---

## 1. Minimal photon gas: no sign reversal

For freely propagating equilibrium radiation,

\[
p_\gamma=\frac13\rho_\gamma,
\qquad
\rho_\gamma>0.
\]

Therefore

\[
w_\gamma=\frac{p_\gamma}{\rho_\gamma}=\frac13
\]

and ordinary FLRW redshift gives

\[
\rho_\gamma\propto a^{-4}.
\]

So the equilibrium pressure of the same free photon gas remains positive.

### Result 045A

\[
\boxed{
\text{free positive-energy photons}
\not\Rightarrow
p_\gamma<0
}
\]

under ordinary FLRW expansion.

The pressure-sign hypothesis therefore requires an effective/system-level stress rather than the equilibrium Maxwell pressure alone.

---

## 2. Purely geometric effective pressure

In flat FLRW, define an effective source by rewriting the Einstein equations as

\[
\rho_{\rm eff}=3M_{\rm Pl}^2H^2,
\]

\[
p_{\rm eff}
=
-M_{\rm Pl}^2(2\dot H+3H^2).
\]

Hence

\[
\boxed{
w_{\rm eff}
=
\frac{p_{\rm eff}}{\rho_{\rm eff}}
=
-1-\frac{2\dot H}{3H^2}.
}
\]

Equivalently, with the deceleration parameter

\[
q=-1-\frac{\dot H}{H^2},
\]

one has

\[
\boxed{
w_{\rm eff}=\frac{2q-1}{3}.
}
\]

This immediately shows a pressure-sign transition while

\[
\rho_{\rm eff}=3M_{\rm Pl}^2H^2>0.
\]

### Benchmarks

Radiation-like geometry:

\[
\dot H=-2H^2
\quad\Rightarrow\quad
w_{\rm eff}=\frac13.
\]

Matter-like geometry:

\[
\dot H=-\frac32H^2
\quad\Rightarrow\quad
w_{\rm eff}=0.
\]

Pressure becomes negative when

\[
\dot H>-\frac32H^2
\]

or

\[
q<\frac12.
\]

Accelerated expansion requires

\[
w_{\rm eff}<-\frac13
\]

or

\[
\dot H>-H^2
\]

or

\[
q<0.
\]

de Sitter:

\[
\dot H=0
\quad\Rightarrow\quad
w_{\rm eff}=-1.
\]

### Result 045B

The sign of effective pressure can change while the effective energy density remains strictly positive:

\[
\boxed{
\rho_{\rm eff}>0,
\qquad
p_{\rm eff}:\ +\to0\to-.
}
\]

This is mathematically exact at the FLRW effective-fluid level.

However, this relation by itself is a rewriting of the geometry. It does not identify the microphysical mechanism that causes the transition.

---

## 3. Bulk-viscous realization

For an imperfect radiation fluid,

\[
p_{\rm eff}=p_\gamma+\Pi,
\]

with Eckart-type bulk pressure

\[
\Pi=-3\zeta H,
\qquad
\zeta\ge0.
\]

Then

\[
p_{\rm eff}
=
\frac{\rho}{3}-3\zeta H,
\]

so

\[
w_{\rm eff}
=
\frac13-\frac{3\zeta H}{\rho}.
\]

Define

\[
\Xi\equiv\frac{3\zeta H}{\rho}.
\]

Then

\[
w_{\rm eff}=\frac13-\Xi.
\]

The thresholds are:

\[
p_{\rm eff}=0
\quad\Longleftrightarrow\quad
\Xi=\frac13,
\]

\[
\ddot a>0
\quad\Longleftrightarrow\quad
w_{\rm eff}<-\frac13
\quad\Longleftrightarrow\quad
\Xi>\frac23,
\]

and

\[
w_{\rm eff}=-1
\quad\Longleftrightarrow\quad
\Xi=\frac43.
\]

Thus positive radiation energy can coexist with negative effective pressure if a sufficiently large nonequilibrium bulk stress is present.

But an exactly conformal, equilibrium Maxwell gas has no such bulk-viscous term generated merely by FLRW redshift. A nonzero \(\zeta\) requires interactions, nonconformality, nonequilibrium dynamics, or additional degrees of freedom.

### Result 045C

\[
\boxed{
\rho_\gamma>0,\quad
p_{\rm eff}<0
}
\]

is dynamically possible, but not in minimal free Maxwell theory.

---

## 4. Gravitational particle-creation pressure

For adiabatic cosmological particle creation, use the number balance

\[
\dot n+3Hn=n\Gamma.
\]

The creation pressure is

\[
\boxed{
p_c
=
-(\rho+p)\frac{\Gamma}{3H}.
}
\]

For radiation,

\[
p=\frac{\rho}{3},
\]

so

\[
p_{\rm eff}
=
p+p_c
=
\frac{\rho}{3}
-
\frac{4\rho}{3}\frac{\Gamma}{3H}.
\]

Therefore

\[
\boxed{
w_{\rm eff}
=
\frac13
-
\frac{4}{9}\frac{\Gamma}{H}.
}
\]

This gives three sharp thresholds.

### Pressure sign reversal

\[
w_{\rm eff}=0
\]

when

\[
\boxed{
\frac{\Gamma}{H}
=
\frac34.
}
\]

Thus

\[
\Gamma/H>\frac34
\]

gives negative effective pressure while \(\rho>0\).

### Acceleration threshold

\[
w_{\rm eff}<-\frac13
\]

requires

\[
\boxed{
\frac{\Gamma}{H}>\frac32.
}
\]

### Exact de Sitter-like point

\[
w_{\rm eff}=-1
\]

requires

\[
\boxed{
\frac{\Gamma}{H}=3.
}
\]

At this point,

\[
\Gamma=3H
\]

and the continuity equation becomes

\[
\dot\rho=0.
\]

Therefore positive-energy radiation plus sufficiently strong creation pressure can have

\[
\boxed{
\rho>0,
\qquad
p_{\rm eff}=-\rho,
\qquad
H=\mathrm{const}.
}
\]

This is precisely the pressure-sign mechanism suggested in the hypothesis: the sign changes in the effective response, not in the photon energy.

### Important directional sign result

If photons are being destroyed rather than created, then formally

\[
\Gamma<0.
\]

The creation-pressure term becomes positive:

\[
p_c>0.
\]

Therefore a process interpreted as

\[
\text{photons disappear into dark energy}
\]

does **not** by itself generate negative radiation pressure.

The negative-pressure branch corresponds instead to creation/backreaction or another nonequilibrium stress.

### Result 045D

The pressure-sign hypothesis is analytically viable.

For radiation,

\[
\boxed{
\Gamma=3H
\Rightarrow
w_{\rm eff}=-1
}
\]

without any negative photon energy.

But the coefficient \(\Gamma/H\) remains the missing dynamical law.

---

## 5. Global horizon sector: positive density, negative pressure

Consider holographic-type energy

\[
\rho_X
=
3c^2M_{\rm Pl}^2L^{-2},
\]

with the future event horizon

\[
L
=
a(t)\int_t^\infty\frac{dt'}{a(t')}.
\]

Then

\[
\dot L=HL-1.
\]

Assuming the horizon sector is separately conserved,

\[
\dot\rho_X+3H(1+w_X)\rho_X=0.
\]

Since

\[
\frac{\dot\rho_X}{\rho_X}
=
-2\frac{\dot L}{L},
\]

we obtain

\[
\boxed{
w_X
=
-\frac13-\frac{2}{3HL}.
}
\]

Using

\[
\Omega_X
=
\frac{\rho_X}{3M_{\rm Pl}^2H^2}
=
\frac{c^2}{H^2L^2},
\]

this becomes

\[
\boxed{
w_X
=
-\frac13
-
\frac{2}{3c}\sqrt{\Omega_X}.
}
\]

Thus

\[
\rho_X>0
\]

coexists naturally with

\[
p_X<0.
\]

In the dark-energy-dominated limit,

\[
\Omega_X\to1,
\]

and if

\[
c=1,
\]

then

\[
\boxed{
w_X\to-1.
}
\]

This is a clean example where the sign change is in the pressure/geometry response, not the energy density.

However, it is standard holographic-dark-energy structure and therefore not LTG novelty by itself.

---

## 6. Comparison of the mechanisms

### Same free photon

\[
E_\gamma>0,
\qquad
p_\gamma=\rho_\gamma/3>0.
\]

No pressure sign reversal.

### Imperfect / nonequilibrium radiation system

\[
E_\gamma>0,
\qquad
p_{\rm eff}=p_\gamma+\Pi.
\]

Pressure can become negative.

### Particle-creation backreaction

\[
E_\gamma>0,
\qquad
p_{\rm eff}
=
\frac{\rho}{3}
-
\frac{4\rho\Gamma}{9H}.
\]

Pressure becomes negative for \(\Gamma/H>3/4\), drives acceleration for \(\Gamma/H>3/2\), and becomes exactly vacuum-like for \(\Gamma/H=3\).

### Global causal/horizon sector

\[
\rho_X>0,
\qquad
w_X<0
\]

can emerge from the time dependence of the IR/horizon length \(L\).

---

## 7. Terminal classification

### Strict free-photon pressure flip

\[
\boxed{
\text{ordinary FLRW redshift}
\Rightarrow
p_\gamma:+\to-
}
\]

**ANALYTIC FAIL.**

### Effective system pressure flip

\[
\boxed{
\rho>0,
\qquad
p_{\rm eff}:+\to-
}
\]

**ANALYTIC PASS.**

### Radiation + creation-pressure realization

\[
\boxed{
\Gamma/H>\frac34
\Rightarrow
p_{\rm eff}<0
}
\]

and

\[
\boxed{
\Gamma/H=3
\Rightarrow
w_{\rm eff}=-1.
}
\]

**ANALYTIC PASS, BUT DYNAMICAL ORIGIN OF \(\Gamma\) NOT DERIVED.**

### Horizon-pressure realization

\[
\boxed{
\rho_X>0,
\qquad
w_X=
-\frac13-\frac{2}{3HL}<0
}
\]

**ANALYTIC PASS, BUT PRIOR-ART MAPPED TO HDE.**

---

## 8. New surviving LTG hypothesis

The strongest form of the user's idea is now

\[
\boxed{
\text{null/causal geometry}
\longrightarrow
\text{nonequilibrium or horizon response}
\longrightarrow
p_{\rm eff}<0
}
\]

while

\[
\boxed{
E_\gamma>0
}
\]

throughout.

The next discriminating question is whether causal/null geometry can uniquely derive either

\[
\boxed{
\Gamma/H
}
\]

or

\[
\boxed{
HL
}
\]

without inserting a free function or parameter.

A derivation of

\[
\Gamma/H=3
\]

or

\[
HL=1
\]

as a dynamical attractor from an LTG-specific global causal condition would be much more significant than a photon-energy sign reversal.

## Prior-art anchors

- P. W. R. Lima and J. A. S. Lima (2026), *Cosmic expansion driven by gravitational particle production: toward a complete cosmological scenario*, EPJC 86, 411. The adiabatic creation-pressure relation is \(p_c=-(\rho+p)\Gamma/(3H)\), and \(\Gamma=3H\) yields constant \(\rho\) and \(H\).
- W. Zimdahl and related relativistic nonequilibrium-fluid literature: particle creation can be represented by an effective negative pressure.
- S. Wang, Y. Wang and M. Li (2017), *Holographic dark energy*, Physics Reports 696, 1-57.
