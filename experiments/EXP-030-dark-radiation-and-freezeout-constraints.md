# EXP-030 — Dark-radiation and freeze-out constraints on the benchmark

## Objective

Apply the first unavoidable cosmological observable to EXP-029.

The minimal benchmark contains a massless zero mode even after the first KK states become heavy. If that zero mode survives to recombination, it behaves as dark radiation and contributes to the effective relativistic energy density `N_eff`.

At the same time, annihilation of the massive modes can heat the remaining zero mode. This creates a concrete correlation between the null↔timelike conversion history and late-time dark radiation.

## 1. Dark-radiation contribution of one real massless scalar

For a decoupled real bosonic zero mode at temperature `T_h`,

\[
\rho_0=\frac{\pi^2}{30}T_h^4
\]

in natural units.

One effective Standard-Model neutrino species has

\[
\rho_{\nu,1}
=\frac78\frac{\pi^2}{15}T_\nu^4.
\]

Therefore

\[
\boxed{
\Delta N_{\rm eff}
=\frac{\rho_0}{\rho_{\nu,1}}
=\frac47\left(\frac{T_h}{T_\nu}\right)^4.
}
\]

Using

\[
T_\nu=(4/11)^{1/3}T_\gamma
\]

after electron-positron annihilation, and defining

\[
\xi_\gamma\equiv T_h/T_\gamma,
\]

we have

\[
\boxed{
\Delta N_{\rm eff}
=\frac47\left(\frac{11}{4}\right)^{4/3}\xi_\gamma^4
\simeq2.20\,\xi_\gamma^4.
}
\]

Thus the hidden temperature, not only the KK mass scale, is an observable model parameter.

## 2. Current observational scale

Modern CMB+BAO analyses constrain `N_eff` to remain close to the Standard-Model value. The precise central value and uncertainty are dataset/model dependent; current combinations typically constrain extra radiation at the level of order a few tenths rather than allowing an entire fully thermalized extra neutrino-like sector without consequence.

As an **illustrative conservative benchmark**, if one requires

\[
\Delta N_{\rm eff}\lesssim0.3,
\]

then

\[
\boxed{
\xi_\gamma
\lesssim
\left(\frac{0.3}{2.20}\right)^{1/4}
\approx0.61.
}
\]

This number is not adopted as a universal latest bound; it is a useful benchmark because published `N_eff` constraints vary with the cosmological dataset and parameter extension.

## 3. Hidden entropy conservation

If the hidden sector is decoupled from the visible sector, its comoving entropy is conserved while internal reactions remain adiabatic:

\[
\boxed{s_h a^3=\mathrm{const}.}
\]

Therefore

\[
T_h a\,g_{*s,h}^{1/3}=\mathrm{const}.
\]

If the hidden relativistic degrees of freedom change from `g_before` to `g_after`, the remaining radiation is heated relative to pure `a^{-1}` redshifting:

\[
\boxed{
T_{h,after}
=T_{h,before}
\left(\frac{g_{before}}{g_{after}}\right)^{1/3}
}
\]

at equal scale factor across the entropy-transfer idealization.

## 4. Heating by the first KK pair

At temperatures well above the first KK mass, the truncated benchmark has effectively

- one real zero mode;
- the `+1` and `-1` modes, together equivalent to two real degrees of freedom.

Thus schematically

\[
g_{*s,h}^{high}\simeq3.
\]

After the massive modes annihilate away in equilibrium,

\[
g_{*s,h}^{low}\simeq1.
\]

The zero-mode temperature is therefore heated by

\[
\boxed{
\frac{T_{h,low}}{T_{h,adiabatic}}
=3^{1/3}.
}
\]

Because radiation density scales as `T^4`, the corresponding dark-radiation density is enhanced by

\[
\boxed{3^{4/3}}
\]

relative to a hypothetical history without this entropy release.

### F-030A

**Efficient annihilation of the timelike KK sector back into the null zero mode increases, rather than decreases, the late dark-radiation temperature.**

This is an important cosmological memory of the conversion process.

## 5. Visible-sector entropy dilution

The hidden-to-visible temperature ratio is also affected by entropy release in the visible plasma.

If the sectors decouple at some early epoch `dec`, then later

\[
\boxed{
\frac{T_h}{T_{vis}}
\propto
\left(\frac{g_{*s,h}^{dec}}{g_{*s,h}}
\right)^{1/3}
\left(\frac{g_{*s,vis}}{g_{*s,vis}^{dec}}
\right)^{1/3}.
}
\]

Thus early decoupling can make the hidden sector colder because many visible degrees of freedom subsequently annihilate and heat the visible bath.

The final `Delta N_eff` therefore depends on **both** hidden and visible entropy histories.

## 6. Freeze-out equation in dimensionless variables

Define

\[
x\equiv\frac{m_1c^2}{T_h}
\]

and a yield with respect to hidden entropy,

\[
Y_1\equiv\frac{n_1}{s_h}.
\]

For standard radiation-dominated expansion and a slowly varying hidden/visible temperature ratio, the annihilation equation takes the standard form

\[
\boxed{
\frac{dY_1}{dx}
=-\frac{s_h\langle\sigma v\rangle}{Hx}
\left(Y_1^2-Y_{1,eq}^2\right),
}
\]

up to the precise convention for counting the `+1,-1` pair.

If

\[
\xi\equiv T_h/T_{vis}
\]

and visible radiation dominates the Hubble rate,

\[
H\simeq1.66\sqrt{g_{*,vis}}
\frac{T_{vis}^2}{M_{Pl}},
\]

while

\[
s_h=\frac{2\pi^2}{45}g_{*s,h}T_h^3.
\]

Then

\[
\boxed{
\frac{s_h}{Hx}
\simeq
0.264
\frac{g_{*s,h}}{\sqrt{g_{*,vis}}}
\xi^2
\frac{M_{Pl}m_1\langle\sigma v\rangle}{x^2}
}
\]

when the conventional non-reduced Planck mass and natural units are used.

The exact numerical coefficient changes with Planck-mass and pair-counting conventions, but the parameter dependence is robust.

## 7. Equilibrium yield

For a Maxwell-Boltzmann massive species of degeneracy `g_1`,

\[
n_{1,eq}
=\frac{g_1m_1^2T_h}{2\pi^2}K_2(x).
\]

Therefore

\[
\boxed{
Y_{1,eq}(x)
=\frac{45}{4\pi^4}
\frac{g_1}{g_{*s,h}}
x^2K_2(x).
}
\]

Freeze-out occurs parametrically when

\[
\boxed{
n_{1,eq}\langle\sigma v\rangle
\sim H.}
\]

Thus the relic abundance is controlled by the standard dimensionless combination involving

\[
M_{Pl}m_1\langle\sigma v\rangle
\]

and the hidden/visible temperature ratio.

## 8. Matter relic versus dark-radiation tension

The benchmark has two competing outcomes.

### Efficient annihilation

If the interaction is strong,

- the massive modes annihilate efficiently;
- their relic abundance is small;
- more entropy is transferred into the zero mode;
- dark radiation is comparatively hotter.

### Early freeze-out

If the interaction is weak,

- more massive KK relic survives;
- less entropy is returned to the zero mode;
- the late matter-like component is larger;
- the detailed zero-mode temperature history changes.

Therefore relic matter abundance and dark radiation are **correlated through the same conversion process**.

### F-030B

**The benchmark predicts a standard tradeoff between surviving timelike relic density and heating of the null radiation bath.**

This is physically meaningful but not LTG-specific; it is ordinary secluded-sector thermodynamics.

## 9. LTG variables in the Boltzmann history

The hidden proper-time/trace fraction is

\[
\chi_h(a)
=1-3w_h(a).
\]

It can be reconstructed from the numerical Boltzmann solution through

\[
\boxed{
\chi_h
=\frac{\rho_1-3P_1}{\rho_0+\rho_1}.
}
\]

Thus a single numerical evolution simultaneously provides

- the relic abundance;
- dark radiation;
- the equation of state;
- the LTG proper-time fraction.

This gives LTG a useful diagnostic variable but no extra equation.

## 10. Novelty test

Everything derived above follows from standard

- KK spectrum and selection rules;
- entropy conservation;
- thermal field theory;
- Boltzmann freeze-out;
- dark-radiation parameterization.

### F-030C

**The first quantitatively testable LTG benchmark remains fully equivalent to standard hidden KK cosmology.**

### F-030D

**Its value is now falsifiability: a chosen `(m_1, sigma v, xi)` point predicts both a massive relic and a dark-radiation contribution.**

## 11. Next experiment

Implement the dimensionless Boltzmann system numerically and scan benchmark values.

The first code should output

1. `Y_1(x)`;
2. `rho_1/rho_0`;
3. `w_h(x)`;
4. `chi_h(x)`;
5. approximate late relic density;
6. `Delta N_eff` from the surviving zero mode.

Then test whether any region simultaneously permits a significant timelike relic fraction and acceptable dark radiation without adding new ingredients.

## Data anchor

The 2025 Particle Data Group review of neutrinos in cosmology summarizes current `N_eff` constraints from several CMB/BAO combinations and shows explicitly that the numerical constraint is dataset and cosmological-model dependent. The benchmark therefore should scan `Delta N_eff` rather than hard-code a single universal bound.
