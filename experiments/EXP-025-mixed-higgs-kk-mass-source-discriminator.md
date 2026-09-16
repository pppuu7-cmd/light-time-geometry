# EXP-025 — Mixed Higgs/ordinary mass + hidden-momentum mass

## Objective

The previous experiments treated the effective 4D mass as if it arose entirely from hidden momentum. Realistic particle physics does not permit that identification for the known Standard-Model spectrum in the minimal model.

This experiment asks a sharper question:

> If a particle has both an ordinary 4D/Higgs-like mass contribution and a KK hidden-momentum contribution, can geometry distinguish the two sources even though ordinary proper time sees only the total mass?

## 1. Minimal mixed mass spectrum

Take a 5D field whose 4D zero mode has a mass `m_H` from a mechanism independent of the compact momentum, together with one compact circle.

At tree level the KK tower has the standard form

\[
\boxed{
m_n^2
=m_H^2+m_{KK,n}^2,
}
\]

where

\[
\boxed{
m_{KK,n}
=\frac{|n|\hbar}{cbR_0}.}
\]

This is the familiar extra-dimensional spectrum

\[
m_n^2=m_0^2+n^2/R_{\rm phys}^2
\]

in ordinary particle-physics units.

## 2. Proper time sees the total mass

The effective 4D dispersion relation is

\[
E^2=p^2c^2+m_n^2c^4.
\]

Therefore

\[
\boxed{
\left(\frac{d\tau}{dt}\right)^2
=\frac{m_n^2c^4}{E^2}
=\frac{(m_H^2+m_{KK}^2)c^4}{E^2}.
}
\]

The ordinary proper-time phase is

\[
\boxed{
d\Phi
=\frac{m_nc^2}{\hbar}d\tau.}
\]

It contains only the physical total mass `m_n`; by itself it does not say which fraction came from Higgs/Yukawa physics and which from hidden momentum.

## 3. Hidden pressure sees only the hidden-momentum component

For the same on-shell excitation, the internal-direction pressure fraction is determined by the physical hidden momentum:

\[
\boxed{
\frac{P_I}{\rho}
=\frac{m_{KK}^2c^4}{E^2}
}
\]

for a monoenergetic mode, and by the corresponding energy-weighted average for a distribution.

The 4D kinetic trace, however, depends on the **total** mass:

\[
\boxed{
-\frac{T_{(4)}}{\rho}
=\frac{m_n^2c^4}{E^2}
=\left(\frac{d\tau}{dt}\right)^2.
}
\]

Therefore the old pure-null-parent identity

\[
T_{(4)}=-P_I
\]

no longer holds once a genuinely non-hidden mass contribution is added.

Instead,

\[
\boxed{
-\frac{T_{(4)}}{\rho}
-
\frac{P_I}{\rho}
=
\frac{m_H^2c^4}{E^2}.
}
\]

## 4. Proper-time fraction splits into two source fractions

Define

\[
\chi_\tau
\equiv
\left(\frac{d\tau}{dt}\right)^2,
\]

\[
\chi_{KK}
\equiv
\frac{m_{KK}^2c^4}{E^2},
\]

and

\[
\chi_H
\equiv
\frac{m_H^2c^4}{E^2}.
\]

Then

\[
\boxed{\chi_\tau=\chi_{KK}+\chi_H.}
\]

This gives the cleanest answer so far to the question "does proper time know where mass came from?"

### Answer

**No. Proper time knows the total timelike mass shell. Internal stress knows only the part of that mass shell produced by hidden momentum.**

## 5. A geometric mass-source discriminator

In the inherited/Jordan description of this toy model, assume `m_H` is independent of the compact scale `b`, while

\[
m_{KK}\propto b^{-1}.
\]

Then

\[
m^2=m_H^2+m_{KK}^2.
\]

Differentiate with respect to the internal scale:

\[
\frac{\partial\ln m}{\partial\ln b}
=
-\frac{m_{KK}^2}{m^2}.
\]

Define

\[
\boxed{
f_{KK}\equiv\frac{m_{KK}^2}{m^2}.}
\]

Then

\[
\boxed{
f_{KK}
=-\frac{\partial\ln m}{\partial\ln b}.}
\]

This quantity runs from

\[
f_{KK}=0
\]

for a purely non-geometric/Higgs-like mass to

\[
f_{KK}=1
\]

for a pure hidden-momentum mass.

This is a useful source discriminator **within the stated model**.

## 6. Radion response

For a small fluctuation of the compact scale,

\[
\frac{\delta m}{m}
=-f_{KK}\frac{\delta b}{b}.
\]

Thus the sensitivity of a particle mass to the radion is proportional to the fraction of its mass-squared carried by hidden momentum.

This immediately gives a physical distinction:

- standard proper-time phase measures `m`;
- radion response measures the `b`-dependent part of `m`;
- comparing them can infer `f_KK` in the toy model.

## 7. Species dependence and equivalence-principle pressure

Suppose two species `A` and `B` have different hidden fractions:

\[
f_{KK,A}\neq f_{KK,B}.
\]

Then a common radion fluctuation produces

\[
\frac{\delta m_A}{m_A}
\neq
\frac{\delta m_B}{m_B}.
\]

A light dynamical radion would therefore couple nonuniversally to the species and generically produce composition-dependent fifth-force/equivalence-principle phenomenology.

This makes experimental constraints conceptually transparent:

\[
\boxed{
\text{large hidden-mass fraction}
\Rightarrow
\text{large radion sensitivity unless the radion is stabilized/decoupled.}
}
\]

This is standard scalar–tensor/extra-dimensional phenomenology, not a new LTG force.

## 8. General ensemble version

For a distribution of species/modes,

\[
-\frac{T_{(4)}}{\rho}
=\left\langle
\frac{m_H^2+m_{KK}^2}{E^2/c^4}
\right\rangle_E,
\]

while

\[
\frac{P_I}{\rho}
=\left\langle
\frac{m_{KK}^2}{E^2/c^4}
\right\rangle_E.
\]

Therefore

\[
\boxed{
-\frac{T_{(4)}+P_I}{\rho}
=\left\langle
\frac{m_H^2c^4}{E^2}
\right\rangle_E.
}
\]

The mismatch between the 4D trace and hidden pressure measures the non-hidden part of the mass shell in this simplified additive model.

## 9. Relation to Standard-Model masses

EXP-023 showed that hidden momentum alone cannot reproduce the simplest observed charged-lepton mass/charge pattern.

EXP-025 therefore supplies the more realistic interpretation:

\[
\boxed{
\text{physical mass}^2
=
\text{ordinary/Higgs-like contribution}^2
+
\text{geometric KK contribution}^2
}
\]

at tree level in the simplest mixed model.

The known particle masses may then be dominated by the ordinary sector while a small KK fraction remains possible in a model-dependent extension.

## 10. Is this new?

No. The spectrum

\[
m_n^2=m_0^2+n^2/R^2
\]

is standard in universal-extra-dimension and related KK models.

The derivative

\[
-\partial\ln m/\partial\ln b
\]

is simply the scalar/radion sensitivity of the mass.

### F-025A

**Proper time is source blind: it responds to total mass.**

### F-025B

**Hidden pressure is source selective: it responds only to hidden momentum.**

### F-025C

**In the minimal additive toy model, the logarithmic radion sensitivity exactly equals the KK fraction of mass-squared:**

\[
\boxed{
f_{KK}=-\partial\ln m/\partial\ln b.}
\]

### F-025D

**This provides a concrete experimental discriminator in principle, but it is standard radion/KK phenomenology rather than a new LTG prediction.**

## 11. Important frame/model caveat

The exact split into `m_H` and `m_KK`, and the simple derivative above, is clearest in the inherited/Jordan parametrization where the assumed non-KK mass is `b` independent.

After Weyl transformation to the Einstein frame, field normalizations can move radion dependence between masses and couplings. A realistic Higgs sector propagating in the higher-dimensional bulk may itself carry `b` dependence.

Therefore `f_KK` should be regarded as a clean toy-model source fraction, while actual observables must be formulated through physical scalar couplings and dimensionless ratios.

## 12. Next target

EXP-026 should ask whether the source decomposition has a **frame-invariant observable form**.

A natural candidate is a differential scalar charge between two species,

\[
\alpha_A-\alpha_B,
\qquad
\alpha_A\equiv M_{\rm Pl}\frac{\partial\ln m_A}{\partial\varphi},
\]

because a universal conformal rescaling cancels from the difference.

If this differential charge is proportional to differences in hidden-mass fraction, then equivalence-principle experiments give a direct constraint on nonuniversal LTG/KK mass content.

## Literature anchor

Tree-level universal-extra-dimension spectra have the standard quadrature form

\[
m_{(n)}=\sqrt{m_0^2+(n/R)^2},
\]

with further bulk, boundary, and radiative corrections in realistic models.
