# EXP-017 — Null-stress redistribution, proper-time fraction, and geometric shear

## Objective

Test whether conversion from a 4D massless/zero-mode sector into massive KK modes produces a universal increase of visible space, or whether higher-dimensional Einstein gravity predicts a more precise geometric response.

The key inputs are the robust kinetic identities from EXP-016:

\[
3P+P_\psi=\rho,
\]

\[
\chi\equiv\frac{P_\psi}{\rho}
=\left\langle\left(\frac{d\tau}{dt}\right)^2\right\rangle_E,
\]

so that

\[
P=\frac{\rho}{3}(1-\chi).
\]

## 1. Homogeneous 5D geometry

Take

\[
dS_5^2=-c^2dt^2+a(t)^2d\mathbf{x}^2+b(t)^2d\psi^2,
\]

and define

\[
H=\frac{\dot a}{a},
\qquad
H_b=\frac{\dot b}{b}.
\]

For a diagonal stress tensor

\[
T^A{}_B=
\operatorname{diag}(-\rho,P,P,P,P_\psi),
\]

the flat 5D Einstein equations include

\[
\boxed{3H^2+3HH_b=\kappa_5^2\rho,}
\]

\[
-2\dot H-\dot H_b-3H^2-2HH_b-H_b^2
=\kappa_5^2P,
\]

and

\[
\boxed{-3\dot H-6H^2=\kappa_5^2P_\psi.}
\]

## 2. Mean expansion and anisotropy variables

Define the full four-spatial-dimensional volume expansion

\[
\boxed{\Theta=3H+H_b}
\]

and the visible/internal expansion difference

\[
\boxed{\Delta=H-H_b.}
\]

Then

\[
H=\frac{\Theta+\Delta}{4},
\qquad
H_b=\frac{\Theta-3\Delta}{4}.
\]

The Hamiltonian constraint becomes

\[
\boxed{
\Theta^2-\Delta^2
=\frac{8}{3}\kappa_5^2\rho.
}
\]

This is already important: at a fixed instantaneous total energy density, the constraint depends on total expansion and shear/anisotropy, not directly on how the pressure is partitioned between visible and hidden directions.

## 3. Pressure difference sources anisotropy

Subtract the hidden-direction Einstein equation from a visible-direction Einstein equation. The result simplifies exactly to

\[
\boxed{
\dot\Delta+\Theta\Delta
=\kappa_5^2(P-P_\psi).
}
\]

Now insert

\[
P=\frac{\rho}{3}(1-\chi),
\qquad
P_\psi=\rho\chi.
\]

Then

\[
P-P_\psi
=\frac{\rho}{3}(1-4\chi),
\]

so

\[
\boxed{
\dot\Delta+\Theta\Delta
=\frac{\kappa_5^2\rho}{3}
(1-4\chi).
}
\]

Using EXP-016,

\[
\boxed{
\chi
=\left\langle
\left(\frac{d\tau}{dt}\right)^2
\right\rangle_E.
}
\]

Therefore the proper-time/hidden-pressure fraction directly controls the **source of geometric anisotropy** between visible expansion and internal expansion.

## 4. Isotropic-stress point

The anisotropy source vanishes when

\[
P=P_\psi.
\]

For a 5D-null ensemble this occurs at

\[
\boxed{\chi=\frac14.}
\]

Then

\[
P=P_\psi=\frac{\rho}{4},
\]

which is precisely isotropic radiation pressure in four spatial dimensions.

For a monoenergetic 4D effective massive mode,

\[
\chi=\left(\frac{mc^2}{E}\right)^2=\frac14
\]

implies

\[
E=2mc^2,
\]

\[
\gamma=2,
\]

and

\[
\boxed{v=\frac{\sqrt3}{2}c.}
\]

This is not a new universal constant; it is simply the point at which a null momentum distribution has equal pressure per spatial dimension across the three visible plus one hidden directions.

## 5. Mean-volume focusing

For a traceless 5D null kinetic stress,

\[
T^A{}_A=0,
\]

so the 5D Einstein equation gives

\[
R_{00}=\kappa_5^2\rho
\]

in the chosen conventions.

Using

\[
R_{00}
=-3(\dot H+H^2)-(\dot H_b+H_b^2),
\]

we obtain

\[
\boxed{
\dot\Theta
=-\frac14\Theta^2
-\frac34\Delta^2
-\kappa_5^2\rho.
}
\]

The pressure-partition variable `chi` does **not** appear directly. It affects `Theta` indirectly by sourcing `Delta`, whose square increases focusing.

This is the 5D Raychaudhuri structure specialized to the present homogeneous geometry.

## 6. Consequence for the original LTG intuition

The minimal 5D null model therefore does **not** support the simple universal statement

\[
\text{more mass/proper time}\Rightarrow\text{more total spatial volume}.
\]

Instead it predicts the more precise chain

\[
\boxed{
\text{massless} \to \text{massive KK conversion}
\Rightarrow
P_\psi\uparrow
\Rightarrow
P-P_\psi\ \text{changes}
\Rightarrow
\Delta=H-H_b\ \text{is sourced}
\Rightarrow
\text{expansion is redistributed between dimensions}.
}
\]

The total higher-dimensional volume expansion is constrained primarily by total energy and shear, while the visible/internal split is controlled by directional pressure.

## 7. EXP-014 pair conversion in this language

For incoming 4D zero modes dominated by visible propagation,

\[
\chi\approx0,
\qquad
P_\psi\approx0.
\]

Producing an approximately 4D-rest KK pair `+n,-n` gives

\[
\chi\approx1,
\qquad
P_\psi\approx\rho,
\qquad
P\approx0.
\]

Thus the process transfers stress from visible momentum to hidden momentum while keeping net hidden momentum zero.

In the idealized limits,

\[
P-P_\psi:
\qquad
\frac{\rho}{3}
\longrightarrow
-\rho.
\]

The anisotropy source therefore changes sign.

## 8. Geometric reconstruction of the proper-time fraction

The anisotropy equation can be inverted:

\[
1-4\chi
=\frac{3(\dot\Delta+\Theta\Delta)}{\kappa_5^2\rho}.
\]

Hence

\[
\boxed{
\chi
=\frac14\left[
1-
\frac{3(\dot\Delta+\Theta\Delta)}{\kappa_5^2\rho}
\right].
}
\]

For the kinetic null sector this is also

\[
\boxed{
\left\langle
\left(\frac{d\tau}{dt}\right)^2
\right\rangle_E
=\frac14\left[
1-
\frac{3(\dot\Delta+\Theta\Delta)}{\kappa_5^2\rho}
\right].
}
\]

This is a direct equation relating the effective proper-time fraction to higher-dimensional geometric anisotropy.

It is not new physics: it is a rearrangement of 5D Einstein plus the KK/null stress identity. But it is the strongest explicit geometry–proper-time equation found so far in LTG.

## 9. Scientific status

### F-017A

**Mass/proper-time emergence is naturally interpreted as directional stress redistribution rather than creation of total spacetime volume.**

### F-017B

**The hidden-pressure/proper-time fraction sources the visible/internal shear through**

\[
\dot\Delta+\Theta\Delta
=\frac{\kappa_5^2\rho}{3}(1-4\chi).
\]

### F-017C

**The total volume expansion has no direct linear `chi` source for a traceless 5D null kinetic fluid; `chi` affects it indirectly through shear.**

### F-017D

**The naive hypothesis `matter creation directly expands space` is falsified in this minimal form. The refined hypothesis `massive-mode creation redistributes higher-dimensional expansion through directional stress` survives.**

## 10. Next gate

The next experiment should reduce the `(Theta, Delta, chi)` system to the 4D Einstein frame and ask which combinations are invariant observables.

Particular targets:

1. express the radion and 4D Hubble rate in terms of `Theta` and `Delta`;
2. determine whether the reconstructed `chi` is frame independent or merely a 5D/Jordan variable;
3. identify a dimensionless observable involving 4D expansion, radion evolution, and the KK phase invariant from EXP-013;
4. compare with standard scalar–tensor cosmology and fifth-force/varying-constant bounds.

If all such observables reduce to standard radion/scalar–tensor quantities, LTG should be classified as a coherent geometric reinterpretation at this level.
