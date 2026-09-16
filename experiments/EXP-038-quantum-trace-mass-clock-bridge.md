# EXP-038 — Quantum one-particle trace–mass–clock bridge

## Objective

Generalize the classical LTG chain beyond a kinetic gas and ask whether a stable quantum one-particle state carries an exact relation between:

- invariant mass;
- proper-time/Compton phase rate;
- the forward matrix element of the full energy-momentum tensor trace.

This is especially important after EXP-036/037, because the mass of a composite state can arise partly or mostly from quantum dynamics and trace anomaly rather than an explicit elementary mass term.

## 1. Convention

Use metric signature

\[
(-,+,+,+)
\]

and, for the field-theory matrix-element formulas in this note, temporarily use natural units `c = hbar = 1` unless restoring units explicitly.

Use standard relativistic one-particle normalization

\[
\langle P'|P\rangle
=2P^0(2\pi)^3\delta^3(\mathbf P'-\mathbf P).
\]

## 2. Forward energy-momentum-tensor normalization

Translation invariance fixes the zero-momentum-transfer normalization of the total conserved energy-momentum tensor.

For a stable one-particle state, after suppressing spin labels or averaging over them when appropriate, the forward matrix element has the reduced form

\[
\boxed{
\langle P|T^{\mu\nu}(0)|P\rangle_{\rm red}
=2P^\mu P^\nu
}
\]

where `red` means that the standard state-normalization delta-function structure is not being written explicitly.

For composite particles this is the statement that the total gravitational form factor multiplying the momentum flow is normalized at zero momentum transfer.

## 3. Take the trace

With the project signature,

\[
P^2=P_\mu P^\mu=-M^2
\]

in natural units.

Therefore

\[
\boxed{
\langle P|T^\mu{}_{\mu}(0)|P\rangle_{\rm red}
=2P^2=-2M^2.
}
\]

Equivalently, the invariant mass is fixed by the total forward trace coefficient:

\[
\boxed{
M^2
=-\frac12
\langle P|T^\mu{}_{\mu}|P\rangle_{\rm red}.
}
\]

This statement concerns the **total renormalized EMT**. A decomposition of the trace into quark masses, gluon anomaly, scalar terms, etc. is a separate and potentially scheme-dependent question.

## 4. Connect to the proper-time clock rate

For a stable massive particle, the free proper-time phase is

\[
\Phi=-\frac{Mc^2}{\hbar}\tau.
\]

Define the Compton angular frequency

\[
\boxed{
\omega_C\equiv\frac{Mc^2}{\hbar}.
}
\]

Restoring units in the trace relation gives a reduced forward trace proportional to `-2 M^2 c^2` with momentum written in physical units.

Hence

\[
\boxed{
\omega_C^2
=-\frac{c^2}{2\hbar^2}
\langle P|T^\mu{}_{\mu}|P\rangle_{\rm red}.
}
\]

Thus the same invariant mass determines both:

1. the frequency with which quantum phase accumulates per unit proper time;
2. the forward scalar trace carried by the complete one-particle state.

## 5. Structural interpretation

This gives a quantum analogue of the classical EXP-033 identity.

### Classical kinetic form

\[
-T=\varepsilon\chi_\tau.
\]

### Quantum one-particle form

\[
\boxed{
-T_{\rm fwd}
\propto M^2
\propto\omega_C^2.
}
\]

The two equations are not identical objects: one refers to a coarse-grained stress tensor of an ensemble, the other to a forward operator matrix element of a normalized one-particle state. But both connect the timelike invariant mass to the scalar trace sector.

## 6. Composite mass and anomaly

For a composite state such as a hadron, the total mass `M` can persist even in limits where explicit constituent masses are small.

The renormalized trace may contain terms schematically of the form

\[
T^\mu{}_{\mu}
=\sum_i (1+\gamma_{m_i})m_i\bar\psi_i\psi_i
+\frac{\beta(g)}{2g}F^a_{\rho\sigma}F_a^{\rho\sigma}
+\cdots.
\]

The forward matrix element of the **sum** is constrained by the physical pole mass of the state.

Therefore the quantum-generated scale discovered in EXP-037 is not merely parallel to mass generation: in a stable one-particle state, the total trace matrix element and the physical mass are tied by Poincare/translation symmetry.

## 7. Revised LTG chain

The strongest quantum-compatible chain now becomes

\[
\boxed{
\text{scale generation / symmetry breaking}
\to
\text{nonzero total EMT trace}
\leftrightarrow
M^2
\leftrightarrow
\omega_C^2
}
\]

for a stable one-particle state, while spacetime propagation satisfies

\[
\boxed{
M>0
\to
\text{timelike mass shell}
\to
 d\tau>0
\to
\Phi=-\omega_C\tau.
}
\]

This is a much sharper quantum version of the original statement that mass, proper time, and geometry are related.

## 8. Gravity caveat

The forward matrix element of `T^{mu nu}` does **not** by itself equal a local classical stress tensor at a spacetime point.

To obtain a local gravitational field one must specify a localized quantum state/wavepacket and a gravity prescription, for example the semiclassical equation

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}
\langle T_{\mu\nu}\rangle.
\]

Therefore it would be incorrect to directly substitute the plane-wave forward matrix element into the local Ricci scalar equation without handling normalization/localization.

What is exact is the mass/trace normalization of the one-particle state.

## 9. Result

### EXP-038A

A stable one-particle quantum state obeys an exact total-EMT forward normalization whose trace is fixed by its invariant mass squared.

### EXP-038B

The same mass fixes its proper-time Compton phase rate.

Therefore the project now has a quantum-level bridge

\[
\boxed{
\text{total EMT trace}
\leftrightarrow
M^2
\leftrightarrow
\omega_C^2
\leftrightarrow
\text{proper-time phase}
}
\]

that does not rely on a dilute classical gas approximation.

### EXP-038C

This is still established QFT/Poincare-symmetry structure, not a new LTG law.

## 10. What is genuinely new as an organizational insight

The earlier LTG language treated rest mass as if it were necessarily an elementary input.

EXP-036–038 show a more general hierarchy:

\[
\boxed{
\text{invariant scale}
\to
\text{total trace structure}
\to
\text{physical mass}
\to
\text{proper-time clock rate}
}
\]

where the invariant scale can be explicit or quantum generated.

This makes the `light/time` contrast secondary to a deeper distinction between scale-free/null sectors and scale-bearing/timelike excitations.

## 11. Next test

The remaining possible novelty is no longer an unspecified relation among `m`, `tau`, and `R`; standard theory already supplies several exact bridges.

A genuinely new LTG principle would have to explain or constrain **why a particular scale is generated**.

The sharp next question is therefore:

> Can causal/null geometry itself determine a renormalization or symmetry-breaking scale, rather than merely responding to the stress tensor after that scale has been generated?

That is a much stronger and riskier hypothesis and should be tested against known curvature-induced symmetry breaking, horizon scales, gravitational dimensional transmutation, and ordinary RG running before proposing a new law.
