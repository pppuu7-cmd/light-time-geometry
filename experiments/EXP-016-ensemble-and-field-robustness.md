# EXP-016 — Ensemble and field-theory robustness of the hidden-pressure identity

## Objective

Test whether the EXP-015 relation

\[
P_\psi/\rho=(d\tau/dt)^2
\]

is an artifact of a single-energy particle ensemble or survives more general distributions, interactions, field theory, radion evolution, and frame changes.

## 1. Arbitrary classical KK distribution

For KK mode `n`, let

\[
m_n=\frac{|n|\hbar}{cbR_0},
\qquad
E_n(p)=\sqrt{p^2c^2+m_n^2c^4}.
\]

Let `f_n(p)` be an arbitrary isotropic 3D phase-space distribution. Then

\[
\rho=\sum_n\int d^3p\,f_n(p)E_n,
\]

\[
P=\sum_n\int d^3p\,f_n(p)\frac{p^2c^2}{3E_n},
\]

and the hidden pressure is

\[
P_\psi=\sum_n\int d^3p\,f_n(p)\frac{m_n^2c^4}{E_n}.
\]

Using

\[
p^2c^2+m_n^2c^4=E_n^2,
\]

we obtain exactly

\[
\boxed{3P+P_\psi=\rho.}
\]

Therefore

\[
\boxed{T_{(4)}=-\rho+3P=-P_\psi.}
\]

This does **not** require a monokinetic ensemble.

## 2. Proper-time interpretation for a distribution

For each phase-space point,

\[
\left(\frac{d\tau}{dt}\right)^2
=\frac{m_n^2c^4}{E_n^2}.
\]

Therefore

\[
P_\psi
=\sum_n\int d^3p\,f_n E_n
\left(\frac{d\tau}{dt}\right)^2.
\]

Define the energy-weighted average

\[
\langle X\rangle_E
\equiv
\frac{1}{\rho}
\sum_n\int d^3p\,f_n E_n X.
\]

Then

\[
\boxed{
\frac{P_\psi}{\rho}
=\left\langle
\left(\frac{d\tau}{dt}\right)^2
\right\rangle_E.
}
\]

Similarly,

\[
\boxed{
\frac{3P}{\rho}
=\left\langle\frac{v^2}{c^2}\right\rangle_E.
}
\]

Hence

\[
\boxed{
\left\langle\frac{v^2}{c^2}\right\rangle_E
+
\left\langle
\left(\frac{d\tau}{dt}\right)^2
\right\rangle_E
=1.
}
\]

The LTG complementarity survives as an exact ensemble identity for collisionless/on-shell 5D-null KK particles.

## 3. Radion variation

If `b=b(t)`, then

\[
m_n(t)\propto b(t)^{-1}.
\]

At each instant the on-shell relation is still

\[
E_n^2=p^2c^2+m_n(t)^2c^4.
\]

Therefore the algebraic identity

\[
3P+P_\psi=\rho
\]

continues to hold instantaneously for the kinetic sector, provided the modes remain describable by the 5D massless shell and the compact direction remains well defined.

The distribution `f_n` will evolve, but the identity does not depend on its detailed shape.

## 4. Interactions

During an interaction, the **full** stress tensor generally contains potential/interaction contributions that are not captured by the kinetic phase-space expressions above.

Therefore EXP-015 should be interpreted carefully:

- before and after scattering, for asymptotic on-shell KK quanta, the identity is exact;
- during an interacting field configuration, `T_(4)=-P_psi` follows only if the full parent 5D stress tensor is traceless;
- a generic interaction need not preserve that condition.

For example, an arbitrary scalar self-interaction can introduce an explicit trace even when the bare 5D mass vanishes.

Thus the EXP-014 quartic model is a clean **mode-number/conversion** toy model, but its full local interacting stress should not automatically be called traceless.

## 5. Stronger field-theory condition

The geometrically robust field-theory statement is

\[
T^A{}_A
=T^\mu{}_{\mu}+T^\psi{}_{\psi}.
\]

Therefore, whenever the complete 5D theory/state obeys

\[
T^A{}_A=0,
\]

we have

\[
\boxed{
T^\mu{}_{\mu}
=-T^\psi{}_{\psi}.
}
\]

This is the field-theory generalization of the kinetic result.

A conformally improved massless scalar is an example where classical tracelessness can be imposed. In `D` dimensions the conformal curvature coupling is

\[
\xi_D=\frac{D-2}{4(D-1)},
\]

so in five dimensions

\[
\boxed{\xi_5=\frac{3}{16}.}
\]

For a truly conformal 5D theory on a smooth boundaryless spacetime, there is no local bulk Weyl anomaly in odd dimension; boundaries/defects can reintroduce anomaly terms.

## 6. Compactification and quantum interpretation

Compactification introduces a global length scale and a KK spectrum. The reduced 4D theory therefore contains masses and a nonzero 4D trace even when the parent local 5D conformal Ward identity is traceless.

The consistent interpretation is then

\[
\boxed{
\text{4D trace}
= -\text{internal stress}
}
\]

rather than "the 5D theory became massive."

The higher-dimensional parent can remain massless/conformal while the reduced theory contains a tower of massive states.

## 7. Frame dependence

After transforming the dimensionally reduced theory to a 4D Einstein frame, the radion is rescaled into the metric and matter couplings. Individual quantities called `rho`, `P`, `m`, and `T_(4)` change under the field redefinition.

Therefore

\[
P_\psi/\rho=(d\tau/dt)^2
\]

is best regarded as a transparent identity in the natural higher-dimensional/Jordan description of the KK kinetic sector, not as a frame-independent scalar equation in every reduced representation.

The more invariant structural statement is the higher-dimensional one:

\[
\boxed{T^A{}_A=0\Rightarrow T^\mu{}_{\mu}=-T^\psi{}_{\psi}.}
\]

## 8. Results

### F-016A

**The pressure complementarity `3P + P_psi = rho` is exact for arbitrary isotropic classical distributions of on-shell massless-5D KK modes.**

### F-016B

**The proper-time fraction generalizes to an energy-weighted ensemble average:**

\[
P_\psi/\rho
=\langle(d\tau/dt)^2\rangle_E.
\]

### F-016C

**Generic interactions can add trace contributions; the exact field-level identity requires a traceless parent 5D stress tensor.**

### F-016D

**The safest field-theory statement is `T_(4) = -T_psi^psi` whenever the parent 5D trace vanishes.**

### F-016E

**No new physics has yet been isolated; the relation is a robust dimensional-reduction identity rather than a new interaction law.**

## 9. Next target

The next experiment should use the 5D Einstein equations plus a conversion process to test whether shifting stress from the visible directions into `P_psi` imposes any frame-independent relation between

- massive-mode production;
- radion response;
- visible expansion;
- and the integrated topological phase from EXP-013.

If no such invariant survives reduction/frame transformations, the present LTG route should be classified as a coherent geometric reinterpretation of standard KK physics rather than a distinct theory.

## Literature anchors

- Odd-dimensional CFTs have no local bulk Weyl anomaly in the absence of boundaries; boundary contributions can exist: Fursaev & Solodukhin, arXiv:1601.06418; Solodukhin, arXiv:1510.04566.
- Higher-dimensional reductions and radion/frame transformations belong to standard KK/scalar–tensor physics.
