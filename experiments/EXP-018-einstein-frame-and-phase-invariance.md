# EXP-018 — Einstein-frame reduction and frame-invariant mass–time phase

## Objective

Reduce the strongest 5D LTG relations to the 4D Einstein frame and determine which quantities are genuine invariants rather than artifacts of the inherited 4D/Jordan parametrization.

The central questions are:

1. how do the visible Hubble rate, radion rate, and anisotropy variables transform?
2. how does the effective KK mass transform?
3. does the topological phase from EXP-013 survive the frame change?
4. can the proper-time/hidden-pressure fraction be reconstructed without an explicit factor of the compactification radius?

## 1. Jordan/inherited 4D frame

Start from

\[
dS_5^2
=g^{(J)}_{\mu\nu}dx^\mu dx^\nu
+b^2d\psi^2.
\]

For homogeneous cosmology,

\[
ds_J^2=-c^2dt_J^2+a_J^2d\mathbf x^2.
\]

Integrating the 5D Einstein-Hilbert term over the compact direction produces a 4D gravitational prefactor proportional to `b`.

To make the 4D Planck mass constant, define the Einstein-frame metric

\[
\boxed{g^{(E)}_{\mu\nu}=b\,g^{(J)}_{\mu\nu}.}
\]

Therefore

\[
\boxed{dt_E=\sqrt b\,dt_J,}
\]

and

\[
\boxed{a_E=\sqrt b\,a_J.}
\]

## 2. Hubble and radion rates

Define

\[
H_J=\frac{1}{a_J}\frac{da_J}{dt_J},
\qquad
H_b=\frac{1}{b}\frac{db}{dt_J}.
\]

Then

\[
\boxed{
H_E
=\frac{1}{\sqrt b}
\left(H_J+\frac12H_b\right).
}
\]

Define the Einstein-time logarithmic radion rate

\[
\boxed{
B_E\equiv\frac{d\ln b}{dt_E}
=\frac{H_b}{\sqrt b}.
}
\]

Hence

\[
H_J=\sqrt b\left(H_E-\frac12B_E\right),
\qquad
H_b=\sqrt b\,B_E.
\]

## 3. Mean expansion and anisotropy in Einstein variables

EXP-017 defined

\[
\Theta=3H_J+H_b,
\qquad
\Delta=H_J-H_b.
\]

Substituting the frame relations gives

\[
\boxed{
\Theta
=\sqrt b\left(3H_E-\frac12B_E\right),
}
\]

and

\[
\boxed{
\Delta
=\sqrt b\left(H_E-\frac32B_E\right).
}
\]

Define for convenience

\[
\mathcal T_E\equiv3H_E-\frac12B_E,
\qquad
\mathcal D_E\equiv H_E-\frac32B_E.
\]

Then

\[
\Theta=\sqrt b\,\mathcal T_E,
\qquad
\Delta=\sqrt b\,\mathcal D_E.
\]

## 4. Geometric reconstruction of the proper-time fraction

From EXP-017 and the 5D Hamiltonian constraint,

\[
\chi
=\frac14\left[
1-
8\frac{\dot\Delta_J+\Theta\Delta}
{\Theta^2-\Delta^2}
\right],
\]

where

\[
\chi
=\frac{P_\psi}{\rho}
=\left\langle
\left(\frac{d\tau}{dt}\right)^2
\right\rangle_E
\]

for the classical 5D-null kinetic sector.

Because

\[
\frac{d}{dt_J}=\sqrt b\frac{d}{dt_E},
\]

one finds

\[
\dot\Delta_J+\Theta\Delta
=b\left[
\dot{\mathcal D}_E
+3H_E\mathcal D_E
\right].
\]

Also,

\[
\Theta^2-\Delta^2
=b(\mathcal T_E^2-\mathcal D_E^2)
=2b(4H_E^2-B_E^2).
\]

The explicit `b` cancels, giving

\[
\boxed{
\chi
=\frac14\left[
1-
4\frac{
\dot{\mathcal D}_E+3H_E\mathcal D_E
}{4H_E^2-B_E^2}
\right],
}
\]

with

\[
\mathcal D_E=H_E-\frac32B_E.
\]

This is an important structural result: the proper-time/hidden-pressure fraction can be reconstructed from the Einstein-frame Hubble rate and radion rate without an explicit compactification scale.

It is not a purely metric 4D observable because `B_E` is an additional scalar/radion degree of freedom, but the formula is not an artifact of an explicit factor `b`.

## 5. KK mass in the Einstein frame

In the inherited/Jordan description,

\[
m_J
=\frac{|n|\hbar}{cbR_0}
\propto b^{-1}.
\]

A point-particle phase/action must be unchanged by a field redefinition:

\[
mc\int ds.
\]

Since

\[
ds_E=\sqrt b\,ds_J,
\]

we require

\[
\boxed{m_E=\frac{m_J}{\sqrt b}.}
\]

Therefore

\[
\boxed{
m_E
=\frac{|n|\hbar}{cR_0}
\,b^{-3/2}.
}
\]

The same scaling follows directly by reducing a 5D scalar action and canonically normalizing its 4D kinetic term in the Einstein frame.

## 6. Canonical radion coupling

For ordinary 5D Einstein gravity reduced on a circle, the canonically normalized radion may be written, in the present convention, as

\[
\boxed{
\varphi
=\sqrt{\frac32}\,M_{\rm Pl}\ln b.
}
\]

Hence

\[
b
=\exp\left(
\sqrt{\frac23}\frac{\varphi}{M_{\rm Pl}}
\right).
\]

The Einstein-frame KK mass becomes

\[
\boxed{
m_E(\varphi)
=m_0\exp\left[
-\sqrt{\frac32}\frac{\varphi}{M_{\rm Pl}}
\right],
}
\]

where

\[
m_0=\frac{|n|\hbar}{cR_0}.
\]

Thus the dimensionless scalar coupling is order unity:

\[
\boxed{
M_{\rm Pl}\frac{d\ln m_E}{d\varphi}
=-\sqrt{\frac32}.
}
\]

This makes explicit why an unstabilized light radion would produce very strong scalar-tensor/fifth-force phenomenology. Stabilization or decoupling is required for realistic visible matter.

## 7. Frame invariance of the mass–proper-time phase

Proper time transforms as

\[
\boxed{d\tau_E=\sqrt b\,d\tau_J.}
\]

Mass transforms oppositely:

\[
m_E=m_J/\sqrt b.
\]

Therefore

\[
\boxed{
m_Ed\tau_E=m_Jd\tau_J.
}
\]

Multiplying by `c^2/hbar`,

\[
\boxed{
\frac{m_Ec^2d\tau_E}{\hbar}
=
\frac{m_Jc^2d\tau_J}{\hbar}.
}
\]

Hence the Compton/proper-time phase is unchanged by the Jordan–Einstein frame transformation.

For the compact winding result of EXP-013,

\[
\oint m_Jc^2d\tau_J=h|nw|,
\]

we therefore have

\[
\boxed{
\oint m_Ec^2d\tau_E
=
\oint m_Jc^2d\tau_J
=h|nw|.
}
\]

This is the strongest frame-robust relation found so far in LTG.

## 8. What is and is not invariant

### Not individually protected

- `b`;
- the numerical value of a dimensional mass `m`;
- `H_J` versus `H_E`;
- the split of the radion between metric and matter couplings.

These depend on field/frame conventions.

### Structurally protected

- the higher-dimensional null mass shell;
- integer hidden momentum/winding data;
- the action/phase integral `integral p_A dx^A`;
- the equality of hidden translation phase and 4D mass–proper-time phase;
- the existence of an additional radion degree of freedom after reduction.

## 9. Novelty result

The Einstein-frame reduction confirms that the strongest current LTG relations remain standard Kaluza–Klein/scalar–tensor physics.

However it also sharpens the project considerably:

### F-018A

**The dimensional statement `m ~ 1/b` is frame dependent and should not be treated as fundamental.**

### F-018B

**The phase element `m c^2 d tau / hbar` is frame invariant when mass and proper time are transformed consistently.**

### F-018C

**The winding relation**

\[
\oint mc^2d\tau=h|nw|
\]

**survives the Jordan–Einstein transformation exactly.**

### F-018D

**The proper-time/hidden-pressure fraction can be rewritten as a dimensionless combination of the Einstein-frame Hubble and radion rates, with explicit `b` cancellation.**

### F-018E

**An unstabilized KK mass sector carries an order-one radion coupling, confirming that realistic visible matter requires stabilization/decoupling.**

## 10. Current frontier

The project now has one particularly clean hierarchy of quantities:

\[
\boxed{
\text{frame-dependent: } b,\ m,\ H
}
\]

but

\[
\boxed{
\text{frame-robust: }
\frac{1}{\hbar}\int mc^2d\tau
=\frac{1}{\hbar}\int p_\psi d\psi
}
\]

with compact-cycle quantization

\[
\boxed{
\frac1\hbar\oint mc^2d\tau=2\pi nw.
}
\]

A genuine LTG novelty would now need to derive the integer/topological data `n,w`, or a new relation among them and 4D causal/curvature observables, rather than simply changing the radion Lagrangian.

## Literature anchors

- Standard dimensional reduction turns the extra metric component into a radion/scalar and admits Jordan/Einstein-frame descriptions.
- Scalar–tensor Einstein-frame transformations move scalar dependence between the metric and matter masses/couplings rather than removing the physical scalar degree of freedom.
- The present reduction remains within standard Kaluza–Klein/radion physics.
