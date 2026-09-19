# EXP-047 — Quantum trace-anomaly pressure-sign branch

## Objective

Test whether quantum geometric backreaction can realize the pressure-sign hypothesis:

\[
\rho>0,
\qquad
p:+\to-
\]

without requiring negative photon energy.

This gate focuses on the trace channel already isolated in EXP-036.

---

## 1. Isotropic stress and the trace

For an isotropic stress tensor in the \((-+++)\) convention,

\[
T^\mu{}_\mu=-\rho+3p.
\]

Therefore

\[
\boxed{
p=\frac{\rho+T}{3}
}
\]

where

\[
T\equiv T^\mu{}_\mu.
\]

The pressure becomes negative when

\[
T<-\rho.
\]

A vacuum-like equation of state

\[
p=-\rho
\]

requires

\[
\boxed{
T=-4\rho.
}
\]

Thus a sufficiently negative geometry-induced trace can change the pressure sign while the energy density remains positive.

---

## 2. de Sitter symmetry

In a de Sitter-invariant vacuum, maximal symmetry constrains the renormalized expectation value to the form

\[
\langle T_{\mu\nu}\rangle
=
C\,g_{\mu\nu}.
\]

Then

\[
\rho=-C,
\qquad
p=C,
\]

so

\[
\boxed{
p=-\rho.
}
\]

The trace is

\[
T=4C=-4\rho.
\]

Therefore any de Sitter-invariant quantum contribution with

\[
C<0
\]

has

\[
\rho>0,
\qquad
p<0.
\]

This realizes the user's pressure-sign idea at the quantum effective-stress level.

---

## 3. Standard 4D conformal-anomaly estimate

Under the standard covariant trace-anomaly framework,

\[
\langle T^\mu{}_\mu\rangle
=
\frac{1}{(4\pi)^2}
\left(
c_{\rm A} C_{\mu\nu\rho\sigma}^2
-
a_{\rm A} E_4
+
b\,\Box R
\right).
\]

For a free spin-1 conformal field, the standard Euler-anomaly coefficient is

\[
a_{\rm A}=\frac{31}{180}.
\]

In exact de Sitter,

\[
C_{\mu\nu\rho\sigma}=0,
\qquad
\Box R=0,
\qquad
E_4=24H^4.
\]

Hence the standard anomaly branch gives

\[
T_{\rm anom}
=
-\frac{31}{120\pi^2}H^4.
\]

By de Sitter symmetry,

\[
\rho_{\rm anom}
=
-\frac14T_{\rm anom}
=
\boxed{
\frac{31}{480\pi^2}H^4
}
\]

and

\[
\boxed{
p_{\rm anom}
=
-\rho_{\rm anom}.
}
\]

Thus, in the standard anomaly treatment,

\[
\boxed{
\rho_{\rm anom}>0,
\qquad
p_{\rm anom}<0
}
\]

even though no individual photon needs negative energy.

This is a direct quantum-field realization of a sign change in the system's geometric response rather than in photon energy.

---

## 4. Magnitude test against late-time dark energy

Observed late-time dark-energy density is of order

\[
\rho_{\rm DE}
\sim
3M_{\rm Pl}^2H_0^2.
\]

The anomaly contribution scales as

\[
\rho_{\rm anom}
\sim
H_0^4.
\]

Therefore

\[
\frac{\rho_{\rm anom}}{\rho_{\rm DE}}
=
\frac{31}{1440\pi^2}
\frac{H_0^2}{M_{\rm Pl}^2}.
\]

Using

\[
\hbar H_0
\simeq
1.44\times10^{-33}\ {\rm eV},
\]

and

\[
M_{\rm Pl}
\simeq
2.435\times10^{27}\ {\rm eV},
\]

gives

\[
\boxed{
\frac{\rho_{\rm anom}}{\rho_{\rm DE}}
\simeq
7.6\times10^{-124}.
}
\]

So the standard free-Maxwell anomaly scale is roughly 123 orders of magnitude too small to explain present dark energy.

### Result 047A

The sign structure works:

\[
\boxed{
\rho>0,\quad p=-\rho.
}
\]

The late-time magnitude does not:

\[
\boxed{
\rho_{\rm anom}\ll\rho_{\rm DE}.
}
\]

---

## 5. Why the scaling mismatch is robust

The important comparison is

\[
H^4
\]

versus

\[
M_{\rm Pl}^2H^2.
\]

Their ratio is

\[
\sim
\frac{H^2}{M_{\rm Pl}^2}.
\]

At the present Hubble scale this is extraordinarily small.

Changing an order-unity anomaly coefficient cannot bridge the gap.

A viable late-time mechanism therefore needs at least one additional enhancement or scale, for example:

- a very large number of effective degrees of freedom;
- a nonlocal infrared enhancement;
- a new dynamical scale;
- horizon/global-causal physics producing \(M_{\rm Pl}^2H^2\) rather than \(H^4\);
- modified gravitational response.

This independently points back toward the global-causal/horizon branch of EXP-044/046.

---

## 6. Important renormalization caveat

The existence and interpretation of the conformal trace anomaly are standard results in covariant QFT in curved spacetime.

However, the detailed renormalized vacuum stress tensor of a Maxwell field in de Sitter space is technically subtle.

Recent work using a particular minimal adiabatic-subtraction prescription has argued for a vanishing massless Maxwell vacuum stress and no trace anomaly in that prescription, while the standard covariant anomaly literature obtains a nonzero geometric trace.

Therefore the Maxwell-specific numerical coefficient above should be classified as:

\[
\boxed{
\text{standard covariant-anomaly branch}
}
\]

rather than as a scheme-independent new LTG theorem.

The broader structural result is stronger than the Maxwell-specific coefficient:

\[
\boxed{
\text{quantum geometric stress can have }
\rho>0,\ p<0
}
\]

without negative particle energies.

---

## 7. Relation to EXP-036

EXP-036 established that

\[
T^\mu{}_\mu
\]

can be nonzero in a massless quantum sector because geometry/renormalization introduces a scale.

EXP-047 adds the pressure interpretation:

\[
\boxed{
T<-\rho
\Longrightarrow
p<0.
}
\]

At the de Sitter-symmetric point,

\[
\boxed{
T=-4\rho
\Longrightarrow
p=-\rho.
}
\]

Thus the trace channel is also a pressure-sign channel.

---

## 8. Terminal classification

### Can geometry change the effective pressure sign without negative photon energy?

\[
\boxed{\text{YES at the effective quantum-stress level.}}
\]

**STRUCTURAL PASS.**

### Does the standard free-Maxwell anomaly explain current dark energy?

\[
\boxed{\text{NO.}}
\]

**MAGNITUDE FAIL** by approximately \(10^{123}\).

### Does this establish a new LTG law?

\[
\boxed{\text{NO.}}
\]

The trace-anomaly route is established QFT-in-curved-spacetime physics and was already anticipated by EXP-036.

### What survives?

The viable target remains a mechanism that produces

\[
\boxed{
\rho>0,\quad p<0
}
\]

with the larger geometric scaling

\[
\boxed{
\rho\sim M_{\rm Pl}^2H^2
}
\]

rather than the local quantum-curvature scaling

\[
\rho\sim H^4.
\]

That again singles out global/horizon or genuinely nonlocal causal physics as the more promising LTG branch.

## Prior-art anchors

- Brown & Cassidy (1977), stress tensors and trace anomalies in conformally flat spacetime.
- Wald (1978), trace anomaly of conformally invariant quantum fields in curved spacetime.
- Shore (1980), conformal anomaly in massless QED.
- Koksma & Prokopec (2008), trace-anomaly effects in cosmology.
- Recent alternative adiabatic-regularization work on Maxwell fields in de Sitter should be treated as a live technical caveat rather than ignored.
