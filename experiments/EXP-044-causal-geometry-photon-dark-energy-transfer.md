# EXP-044 — Can causal geometry derive photon-to-dark-energy transfer?

## Objective

Continue EXP-043 at the only surviving branch:

\[
\gamma \longrightarrow X,
\qquad
w_X\simeq -1,
\]

and ask whether the transfer term can be derived from geometry itself rather than inserted as an arbitrary phenomenological coupling.

The gate tests:

1. minimal Einstein-Maxwell theory;
2. local curvature couplings;
3. horizon / global-causal conversion;
4. a natural geometric infrared threshold \(E_*\sim\hbar H\);
5. a solvable interacting-fluid benchmark;
6. whether the global-horizon version is genuinely new or maps to known holographic dark energy.

---

## 1. Minimal Einstein-Maxwell gate

Start with

\[
S=
\int d^4x\sqrt{-g}
\left[
\frac{M_{\rm Pl}^2}{2}(R-2\Lambda)
-\frac14F_{\mu\nu}F^{\mu\nu}
\right].
\]

In conformal time,

\[
ds^2=a(\eta)^2
\left(
-d\eta^2+d\mathbf{x}^2
\right).
\]

For the Maxwell term in four spacetime dimensions,

\[
\sqrt{-g}\,g^{\mu\alpha}g^{\nu\beta}
\propto
a^4 a^{-2}a^{-2}
=
1.
\]

Therefore the free Maxwell action is conformally invariant in spatially flat FLRW.

The source-free Maxwell equations imply separate stress-energy conservation,

\[
\nabla_\mu T_{\rm EM}^{\mu\nu}=0.
\]

For homogeneous radiation,

\[
\dot\rho_\gamma+4H\rho_\gamma=0.
\]

Hence the geometric expansion term does not produce an independent exchange current:

\[
\boxed{Q^\nu_{\rm geom}=0}
\]

in minimal Einstein-Maxwell theory.

This is stronger than the EXP-043 sign argument: not only does \(E\) fail to cross zero, but standard FLRW geometry supplies no photon-to-vacuum conversion channel at all.

### Result 044A

\[
\boxed{
\text{minimal GR + Maxwell + FLRW}
\Rightarrow
Q^\nu=0.
}
\]

A nonzero transfer requires physics beyond the minimal system.

---

## 2. Why a local geometric coupling is not parameter-free

One can break the conformal result by adding terms such as

\[
-\frac14 I(\mathcal G)F_{\mu\nu}F^{\mu\nu},
\]

where \(\mathcal G\) denotes one or more curvature invariants, or higher-dimension terms such as

\[
\frac{\alpha}{M^2}
R_{\mu\nu}
F^{\mu\lambda}F^\nu{}_\lambda.
\]

But then the theory requires at least one of:

- a new function \(I\);
- a dimensionless coefficient \(\alpha\);
- a new scale \(M\);
- an additional field whose value determines \(I\).

Thus local geometry can mediate exchange only after adding new dynamical information.

For pure geometric-optics radiation the electromagnetic invariants satisfy, mode by mode,

\[
F_{\mu\nu}F^{\mu\nu}=0,
\qquad
F_{\mu\nu}\tilde F^{\mu\nu}=0,
\]

so the simplest scalar prefactor \(I(\mathcal G)F^2\) is especially weak as a direct radiation-to-scalar source on an ideal null wave. More general tensor couplings are possible, but are higher-order operators with free coefficients.

### Result 044B

Local curvature couplings do not give a unique LTG transfer law. They reintroduce arbitrary coupling data and map into known nonminimal electrodynamics / modified-gravity frameworks.

---

## 3. Horizon-crossing gate

Suppose the proposed conversion happens when radiation leaves a causal patch.

A cosmological event horizon for a comoving observer is

\[
R_{\rm eh}(t)
=
a(t)
\int_t^\infty\frac{dt'}{a(t')}.
\]

In asymptotic de Sitter,

\[
R_{\rm eh}\to H^{-1}.
\]

A flux-based source has the dimensional form

\[
Q_H
\sim
\frac{\text{energy crossing horizon}}{\text{horizon volume}}
\sim
C_H H\rho_\gamma,
\]

where \(C_H\) is dimensionless.

This reproduces the phenomenological structure

\[
Q=\Gamma H\rho_\gamma,
\]

but geometry alone has not yet fixed the coefficient.

There is also a deeper problem: an event horizon is observer/patch dependent and depends on the future expansion history. Turning a patch-dependent boundary flux directly into a local homogeneous stress tensor risks double counting and nonlocality.

A photon being outside one observer's horizon remains an ordinary local future-directed photon for observers that can still meet it.

### Result 044C

\[
\boxed{
\text{horizon flux}
\Rightarrow
Q\sim H\rho_\gamma
}
\]

is dimensionally natural, but it does not by itself define a unique observer-independent covariant conversion law.

---

## 4. Natural infrared threshold \(E_*=\hbar H\)

If the hypothesis requires a finite geometric threshold before an effective sign/phase change, the simplest scale available from expansion is

\[
E_*=\hbar H.
\]

Using representative present values,

\[
H_0\simeq2.18\times10^{-18}\ {\rm s}^{-1},
\]

gives

\[
\boxed{
\hbar H_0
\simeq
1.44\times10^{-33}\ {\rm eV}.
}
\]

The mean energy of a \(T_0\simeq2.7255\ {\rm K}\) blackbody photon is

\[
\langle E_\gamma\rangle
\simeq
2.701\,k_BT_0
\simeq
6.34\times10^{-4}\ {\rm eV}.
\]

Thus

\[
\frac{\langle E_\gamma\rangle}{\hbar H_0}
\simeq
4.4\times10^{29}.
\]

If the far future is approximately de Sitter, a photon redshifts as \(E\propto a^{-1}\). Reaching \(E\sim\hbar H\) therefore needs approximately

\[
N
=
\ln
\left(
\frac{E_\gamma}{\hbar H}
\right)
\simeq68.3
\]

additional e-folds.

With \(H_\Lambda\simeq H_0\sqrt{\Omega_\Lambda}\), this is of order

\[
\boxed{
\Delta t\sim1.2\times10^{12}\ {\rm yr}
}
\]

for a present-day typical CMB photon.

This is an order-of-magnitude asymptotic-de-Sitter estimate, not an exact future prediction.

### Result 044D

If the geometric transition threshold is naturally \(E_*\sim\hbar H\), ordinary CMB photons are roughly \(10^{29}\) above it today.

Therefore this threshold cannot naturally explain why dark energy is important now. It would be a very-far-future transition for typical present photons.

---

## 5. Solvable interacting benchmark

Retain the phenomenological equations

\[
\dot\rho_\gamma+4H\rho_\gamma=-Q,
\]

\[
\dot\rho_X=Q
\]

for \(w_X=-1\), and choose

\[
Q=\Gamma H\rho_\gamma.
\]

Then

\[
\rho_\gamma(a)
=
\rho_{\gamma,i}
\left(\frac{a}{a_i}\right)^{-(4+\Gamma)},
\]

and

\[
\rho_X(a)
=
\rho_{X,i}
+
\frac{\Gamma}{4+\Gamma}
\rho_{\gamma,i}
\left[
1-
\left(\frac{a}{a_i}\right)^{-(4+\Gamma)}
\right].
\]

This proves that radiation can mathematically feed a component that tends to a constant density.

### Illustrative calibration from recombination

Set, only as a benchmark,

\[
a_i=(1+z_{\rm rec})^{-1},
\qquad
z_{\rm rec}\simeq1089,
\]

\[
\rho_X(a_i)=0,
\]

and use representative present density fractions

\[
\Omega_\Lambda\simeq0.685,
\qquad
\Omega_\gamma\simeq5.38\times10^{-5}.
\]

Then

\[
\frac{\rho_{X,0}}{\rho_{\gamma,0}}
\sim1.27\times10^4.
\]

Solving the exact background relation gives approximately

\[
\boxed{
\Gamma\simeq3.6\times10^{-8}.
}
\]

For a thermal spectrum, the modified scaling would be

\[
T_\gamma\propto a^{-(1+\Gamma/4)},
\]

so this illustrative value corresponds to an exponent shift of only

\[
\frac{\Gamma}{4}\simeq9.0\times10^{-9}.
\]

The important problem is not the smallness of the coupling. It is the boundary dependence.

For small \(\Gamma\),

\[
\rho_{X,0}
\approx
\frac{\Gamma}{4}
\rho_{\gamma,0}
a_i^{-4}.
\]

Therefore changing the start scale \(a_i\) changes the generated vacuum density by an enormous factor.

In the formal limit

\[
a_i\to0,
\]

the integral diverges.

### Result 044E

A photon-to-vacuum exchange law can reproduce a constant dark-energy density mathematically, but its magnitude is not predicted unless geometry also fixes:

1. when the interaction turns on;
2. the coefficient \(\Gamma\);
3. why the receiving sector has \(w_X=-1\).

Without those, the construction is a reparameterization, not an explanation.

---

## 6. Global causal energy maps to holographic dark energy

A different global-causal idea is to associate a vacuum-like energy density directly with a horizon/IR length \(L\):

\[
\boxed{
\rho_X
=
3c^2M_{\rm Pl}^2L^{-2}.
}
\]

This is the standard structural form of holographic dark energy (HDE).

If

\[
L=H^{-1},
\]

then

\[
\rho_X\propto M_{\rm Pl}^2H^2,
\]

which naturally has the order of the cosmological critical density. However, the simplest Hubble-horizon choice does not by itself give the required late-time accelerating equation of state.

The standard HDE construction instead often uses the future event horizon,

\[
L=R_{\rm eh},
\]

and introduces a free dimensionless parameter \(c\).

Thus the promising global-horizon descendant of the LTG intuition already has substantial prior art.

### Result 044F

\[
\boxed{
\text{global causal horizon}
\to
\rho_X\sim M_{\rm Pl}^2L^{-2}
}
\]

is physically meaningful, but it maps directly onto holographic-dark-energy territory unless LTG derives something stronger.

---

## 7. Observational discriminants

Any nonzero photon transfer generically threatens at least one of the assumptions behind the standard cosmic distance-duality relation,

\[
D_L=(1+z)^2D_A,
\]

namely photon-number conservation and ordinary null-geodesic propagation.

It can also modify the CMB temperature-redshift law

\[
T_{\rm CMB}(z)=T_0(1+z).
\]

Recent 2025-2026 distance-duality analyses remain broadly consistent with the standard relation, and the literature on CMB temperature evolution places strong constraints on appreciable photon creation/destruction.

Therefore an LTG photon-transfer model must predict these observables, not only the background Friedmann equation.

---

## 8. Terminal classification

### H1 — ordinary expansion itself converts photon energy into dark energy

\[
\boxed{
\text{FLRW expansion}
\to
\gamma\to X
}
\]

**FAIL in minimal Einstein-Maxwell theory.**

The exact minimal result is

\[
Q^\nu=0.
\]

### H2 — a horizon automatically converts lost photons into a local vacuum component

**NOT DERIVED.**

Dimensional analysis gives \(Q\sim H\rho_\gamma\), but coefficient, covariance, observer independence, and receiving equation of state are not fixed.

### H3 — conversion occurs when \(E_\gamma\sim\hbar H\)

**DISFAVORED AS AN EXPLANATION OF PRESENT DARK ENERGY.**

Typical present CMB photons are about \(4\times10^{29}\) above that geometric IR scale and would reach it only in the very far future in an asymptotic-de-Sitter estimate.

### H4 — a photon sector transfers energy to a separate \(w=-1\) component

**MATHEMATICALLY VIABLE BUT UNDERDETERMINED.**

The benchmark \(Q=\Gamma H\rho_\gamma\) works algebraically, but \(\Gamma\), the start time, and \(w_X\) are new inputs.

### H5 — dark energy is a global causal/horizon degree of freedom

**PHYSICALLY VIABLE AS A RESEARCH DIRECTION, BUT NOT YET NOVEL.**

The simplest realization maps to holographic dark energy.

---

## 9. The remaining LTG novelty gate

The hypothesis survives only in a sharper form:

\[
\boxed{
\text{global null/causal geometry}
\stackrel{?}{\Longrightarrow}
\left\{
L,\ c,\ Q^\mu,\ w_X
\right\}
}
\]

with no freely inserted dimensionless coupling and with an observational prediction beyond generic interacting or holographic dark-energy models.

A genuine LTG advance would need to derive at least one of the following:

1. the IR length \(L\) uniquely from causal/null geometry;
2. the coefficient \(c\) or \(\Gamma\) without fitting;
3. the receiving equation of state \(w_X\);
4. a unique relation between photon redshift and horizon entropy/information;
5. a dimensionless observable that distinguishes LTG from standard HDE/interacting-DE models.

That is the next scientifically discriminating gate.

## Prior-art anchors

- Leonard Parker's conformal-invariance result: conformally invariant free fields, including photons, are not produced by spatially flat FLRW expansion.
- Côté, Faraoni & Giusti (2019), *Revisiting the conformal invariance of Maxwell's equations in curved spacetime*, arXiv:1905.09968.
- Wang, Wang & Li (2017), *Holographic dark energy*, Physics Reports 696, 1-57.
- Recent 2025-2026 cosmic distance-duality tests remain broadly consistent with the standard photon-conserving relation.
