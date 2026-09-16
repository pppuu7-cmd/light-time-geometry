# EXP-026 — Frame-invariant differential scalar charge

## Objective

Turn the toy-model mass-source discriminator from EXP-025 into a quantity that survives Jordan/Einstein frame redefinitions and connects directly to equivalence-principle / fifth-force observables.

The key idea is to compare **two species**, so any universal conformal rescaling cancels.

## 1. Scalar charge of a particle species

In the 4D Einstein frame let the canonically normalized radion/modulus be `varphi` and let the physical mass of species `A` be

\[
m_A(\varphi).
\]

Define its dimensionless scalar charge

\[
\boxed{
\alpha_A
\equiv
M_{\rm Pl}\frac{\partial\ln m_A}{\partial\varphi}.
}
\]

A light radion produces an additional scalar force whose strength depends on these charges.

## 2. Why an individual scalar charge is frame-sensitive

Suppose a field/frame transformation rescales every matter mass by the same scalar-dependent factor,

\[
m_A\rightarrow e^{F(\varphi)}m_A.
\]

Then

\[
\alpha_A
\rightarrow
\alpha_A
+M_{\rm Pl}F'(\varphi).
\]

Therefore an individual `alpha_A` contains a universal convention-dependent piece associated with where the conformal factor is placed.

## 3. Differential scalar charge is frame robust

For two species `A` and `B`, define

\[
\boxed{
\Delta\alpha_{AB}
\equiv
\alpha_A-\alpha_B.
}
\]

Under the same universal conformal rescaling,

\[
\Delta\alpha_{AB}
\rightarrow
(\alpha_A+C)-(\alpha_B+C)
=\Delta\alpha_{AB}.
\]

Thus

\[
\boxed{
\Delta\alpha_{AB}
\text{ is invariant under a universal matter conformal rescaling.}
}
\]

This is the appropriate observable-level version of the LTG mass-source discriminator.

## 4. Relation to mass-ratio variation

Because

\[
\ln\frac{m_A}{m_B}
=\ln m_A-\ln m_B,
\]

we have

\[
\boxed{
M_{\rm Pl}
\frac{\partial}{\partial\varphi}
\ln\frac{m_A}{m_B}
=\Delta\alpha_{AB}.
}
\]

Therefore differential scalar charge is directly the sensitivity of a dimensionless mass ratio to the radion.

This is explicitly frame-safe because the common conformal factor cancels from the ratio.

## 5. Insert the mixed LTG/KK toy model

In EXP-025, in the inherited/Jordan parametrization,

\[
m_A^2=m_{H,A}^2+m_{KK,A}^2,
\]

with

\[
m_{KK,A}\propto b^{-1}
\]

and `m_H,A` assumed independent of `b`.

Define the hidden fraction

\[
\boxed{
f_A
\equiv
\frac{m_{KK,A}^2}{m_A^2}.
}
\]

Then

\[
\boxed{
\frac{\partial\ln m_A}{\partial\ln b}
=-f_A.
}
\]

For the canonical radion convention used in EXP-018,

\[
\varphi
=\sqrt{\frac32}M_{\rm Pl}\ln b,
\]

so

\[
M_{\rm Pl}\frac{\partial\ln b}{\partial\varphi}
=\sqrt{\frac23}.
\]

The nonuniversal part of the scalar charge is therefore

\[
\alpha_A^{\rm nonuniv}
=-\sqrt{\frac23}\,f_A.
\]

Taking the difference cancels any universal frame contribution:

\[
\boxed{
\Delta\alpha_{AB}
=-\sqrt{\frac23}
\left(f_A-f_B\right).
}
\]

This is the cleanest frame-robust source-discriminator equation found so far in the project.

## 6. Physical meaning

If

\[
f_A=f_B,
\]

then the two masses respond identically to the radion and their ratio is insensitive to it at this order:

\[
\Delta\alpha_{AB}=0.
\]

If

\[
f_A\neq f_B,
\]

then

\[
\frac{m_A}{m_B}
\]

changes with the radion and the species generally feel different scalar forces.

Thus a nonuniversal hidden-momentum contribution creates exactly the kind of composition dependence tested by equivalence-principle experiments and precision clocks.

## 7. Weak-equivalence-principle connection

For a sufficiently light scalar whose range exceeds the experimental scale, a generic scalar-tensor force between a source `E` and test body `A` has a strength controlled schematically by

\[
\alpha_E\alpha_A.
\]

For two test bodies `A` and `B`, the differential acceleration scales, for small scalar corrections, like

\[
\boxed{
\eta_{AB}
\sim
\alpha_E\,\Delta\alpha_{AB},
}
\]

up to composition, finite-range, screening, and normalization details.

Substituting the LTG/KK toy relation,

\[
\boxed{
\eta_{AB}
\sim
-\sqrt{\frac23}\,
\alpha_E\,(f_A-f_B).
}
\]

This does **not** give a universal direct bound on `f_A-f_B` because the source charge `alpha_E`, radion mass/range, screening, and realistic nuclear composition are model dependent.

## 8. Experimental scale

The MICROSCOPE mission's final titanium/platinum result found no weak-equivalence-principle violation and constrained the Eotvos parameter at the `10^-15` scale.

Therefore a long-range radion with order-unity source coupling cannot tolerate an order-unity nonuniversality in hidden mass fractions.

Conversely, a model can evade this test by, for example,

- making the radion sufficiently massive/short ranged;
- stabilizing it strongly;
- making its source coupling very small;
- arranging nearly universal hidden fractions;
- invoking screening, if consistently realized.

These are standard scalar-tensor escape routes and must be treated quantitatively in a concrete model.

## 9. Clock/mass-ratio connection

Because

\[
\Delta\alpha_{AB}
=M_{\rm Pl}\partial_\varphi\ln(m_A/m_B),
\]

any time- or environment-dependent radion field can induce changes in dimensionless frequency or mass ratios.

Thus clock comparisons and free-fall experiments probe complementary aspects of the same source-sensitive scalar coupling.

This matches the standard dilaton/moduli phenomenology literature: light scalars generically produce both variation of effective constants and equivalence-principle violations when their couplings are composition dependent.

## 10. What has become observable?

The original LTG quantity

\[
mc^2d\tau/\hbar
\]

was frame robust but source blind.

The new differential quantity

\[
\boxed{
\Delta\alpha_{AB}
=M_{\rm Pl}\partial_\varphi\ln(m_A/m_B)
}
\]

is both

- dimensionless;
- insensitive to a universal frame rescaling;
- source sensitive;
- experimentally meaningful.

This is a genuine improvement in the **diagnostic formulation**, even though the physics remains standard radion/dilaton phenomenology.

## 11. Results

### F-026A

**The single-species hidden fraction is parametrization dependent, but the differential scalar charge between two species is frame robust under universal conformal rescaling.**

### F-026B

**In the minimal mixed-mass toy model,**

\[
\boxed{
\Delta\alpha_{AB}
=-\sqrt{\frac23}(f_A-f_B).
}
\]

### F-026C

**The same quantity controls both radion sensitivity of the dimensionless mass ratio and composition-dependent fifth-force effects.**

### F-026D

**Existing equivalence-principle tests strongly disfavor a light, gravitational-strength radion with strongly nonuniversal hidden-mass fractions.**

### F-026E

**This remains standard scalar-tensor/moduli phenomenology; it is a discriminator of hidden-momentum mass, not yet an LTG-specific prediction.**

## 12. Next gate

The project has now found a measurable parameter but not a unique predicted value.

To become a distinct theory, LTG would need to predict at least one of:

1. the hidden fractions `f_A` for real species;
2. the radion mass/range;
3. the coupling `alpha_E`;
4. a relation among `f_A`, particle quantum numbers, and the phase integer;
5. a new universal cancellation or nonzero pattern for `Delta alpha_AB`.

Without such a prediction, the framework remains an interpretation/parameterization of standard extra-dimensional scalar phenomenology.

## Literature anchors

- Damour & Donoghue, *Phenomenology of the Equivalence Principle with Light Scalars*, arXiv:1007.2790.
- Damour & Donoghue, *Equivalence Principle Violations and Couplings of a Light Dilaton*, arXiv:1007.2792.
- MICROSCOPE Collaboration, final WEP test, arXiv:2209.15487 / Phys. Rev. Lett. 129, 121102 (2022).
