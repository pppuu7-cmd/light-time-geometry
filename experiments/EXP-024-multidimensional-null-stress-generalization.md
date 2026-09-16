# EXP-024 — Generalization to k hidden spatial dimensions

## Objective

Determine which LTG relations are genuinely structural and which are artifacts of having exactly one extra spatial dimension.

Generalize the null-lift kinetic construction from 5D to

\[
D=4+k
\]

spacetime dimensions: one time coordinate, three visible spatial coordinates, and `k` hidden spatial coordinates.

## 1. Higher-dimensional null shell

In a local orthonormal frame let

- `p` be the magnitude of visible 3-momentum;
- `q_a`, `a=1,...,k`, be the physical hidden momenta.

A massless higher-dimensional mode obeys

\[
\boxed{
E^2
=p^2c^2
+c^2\sum_{a=1}^k q_a^2.
}
\]

Define the effective 4D rest mass by

\[
\boxed{
m^2c^2
=\sum_{a=1}^k q_a^2.}
\]

Then the 4D observer sees the ordinary massive dispersion relation

\[
\boxed{E^2=p^2c^2+m^2c^4.}
\]

Thus hidden **momentum magnitude**, not a particular fifth component, is the structural quantity generating 4D mass.

## 2. Proper-time complementarity remains unchanged

For every effective 4D mode,

\[
\frac{v^2}{c^2}
=\frac{p^2c^2}{E^2},
\]

and

\[
\left(\frac{d\tau}{dt}\right)^2
=\frac{m^2c^4}{E^2}
=\frac{c^2\sum_a q_a^2}{E^2}.
\]

Therefore

\[
\boxed{
\frac{v^2}{c^2}
+
\left(\frac{d\tau}{dt}\right)^2
=1
}
\]

independent of the number of hidden dimensions.

## 3. Arbitrary kinetic distribution

Let `f(p,q_a)` denote an arbitrary positive phase-space distribution that is isotropic in the three visible directions.

The energy density is

\[
\rho
=\int d\Gamma\, f E.
\]

Visible pressure per visible direction is

\[
P
=\int d\Gamma\, f\frac{p^2c^2}{3E}.
\]

For hidden direction `a`,

\[
P_a
=\int d\Gamma\, f\frac{q_a^2c^2}{E}.
\]

Define total internal pressure

\[
\boxed{P_I\equiv\sum_{a=1}^kP_a.}
\]

Using the higher-dimensional null shell,

\[
p^2c^2+c^2\sum_aq_a^2=E^2,
\]

we obtain exactly

\[
\boxed{3P+P_I=\rho.}
\]

This is independent of `k`.

## 4. 4D trace equals minus total internal pressure

The effective 4D kinetic trace is

\[
T_{(4)}=-\rho+3P.
\]

Therefore

\[
\boxed{T_{(4)}=-P_I.}
\]

If the complete parent higher-dimensional stress is traceless, this is the dimensional split

\[
T^A{}_A
=T^\mu{}_{\mu}
+\sum_aT^a{}_a
=0.
\]

Hence the one-extra-dimension identity from EXP-015/016 generalizes exactly:

\[
\boxed{
\text{effective 4D massive trace}
=-\text{total hidden pressure}.
}
\]

## 5. Proper-time fraction equals total hidden-pressure fraction

Define

\[
\chi\equiv\frac{P_I}{\rho}.
\]

Then

\[
P_I
=\int d\Gamma\,fE
\frac{c^2\sum_aq_a^2}{E^2}.
\]

Using the effective mass/proper-time relation,

\[
\boxed{
\chi
=\left\langle
\left(\frac{d\tau}{dt}\right)^2
\right\rangle_E.
}
\]

Thus the central LTG stress interpretation is not special to 5D:

\[
\boxed{
\frac{P_I}{\rho}
=-\frac{T_{(4)}}{\rho}
=\left\langle
\left(\frac{d\tau}{dt}\right)^2
\right\rangle_E.
}
\]

## 6. Equation-of-state domain is dimension independent

Again,

\[
3P+P_I=\rho
\]

gives

\[
w_4\equiv P/\rho
=\frac{1-\chi}{3}.
\]

Since

\[
0\le\chi\le1,
\]

we retain

\[
\boxed{0\le w_4\le1/3.}
\]

Therefore the acceleration/dark-energy no-go of EXP-021 is not an artifact of one hidden dimension.

It applies to any positive-energy on-shell massless parent gas whose 4D mass is simply the magnitude of hidden spatial momentum.

## 7. Fully isotropic higher-dimensional radiation

Now impose the stronger condition that the parent radiation is isotropic across **all** `3+k` spatial dimensions.

Each spatial direction then carries the same pressure

\[
P_{\rm each}=\frac{\rho}{3+k}.
\]

The three visible directions therefore have

\[
\boxed{P=\frac{\rho}{3+k},}
\]

while total internal pressure is

\[
\boxed{P_I=\frac{k}{3+k}\rho.}
\]

Hence

\[
\boxed{\chi_{\rm iso}=\frac{k}{3+k}}
\]

and the effective 4D equation of state is

\[
\boxed{w_{4,\rm iso}=\frac{1}{3+k}.}
\]

Examples:

- `k=0`: `w=1/3`;
- `k=1`: `w=1/4`;
- `k=2`: `w=1/5`;
- `k=3`: `w=1/6`.

This is a clean observable consequence of **full higher-dimensional isotropy**, though not a new theoretical result.

## 8. Apparent dimension from an isotropic parent fluid

If a component were independently known to be a fully isotropic null gas in `3+k` spatial dimensions, then

\[
w=\frac{1}{3+k}
\]

could be inverted:

\[
\boxed{k=\frac1w-3.}
\]

This is not a generic method for measuring dimensions because the strong premise of higher-dimensional isotropy must first be justified.

Still, it gives a useful phenomenological benchmark.

## 9. Multi-dimensional compactification softens the charge–mass problem but does not remove it automatically

With multiple compact directions, 4D mass can depend on the norm

\[
m^2c^2
=\sum_a q_a^2,
\]

while a particular 4D gauge charge may depend on only one component or one linear combination of the hidden momenta.

Therefore particles can, in principle, have the same observed charge but different masses due to momentum in additional neutral/internal directions.

This shows that the charged-lepton no-go of EXP-023 is specifically a no-go for the **single-circle, single-momentum sole-origin model**, not for all higher-dimensional constructions.

But the price is additional compactification structure, extra towers, more moduli/gauge fields, and additional phenomenology.

### F-024A

**Multiple hidden dimensions can break the simple universal `m/|q|` relation.**

### F-024B

**They do so by adding new independent hidden momentum components, not by changing the basic null-lift mechanism.**

## 10. Phase generalization

Let the internal physical momentum vector be

\[
\mathbf q=(q_1,\ldots,q_k).
\]

The internal contribution to the canonical phase is

\[
dS_I=\sum_a p_a dy^a.
\]

For free geodesic propagation, internal velocity is parallel to internal momentum in the local orthonormal frame. Then along the trajectory the magnitude relation gives

\[
\boxed{|dS_I|=mc^2d\tau}
\]

up to orientation/sign conventions.

For a compact `k`-torus, momentum and winding become integer vectors,

\[
\mathbf n\in\mathbb Z^k,
\qquad
\mathbf w\in\mathbb Z^k,
\]

and closed-cycle phase is controlled by their lattice pairing

\[
\boxed{
\frac1\hbar\oint p_a dy^a
=2\pi\,\mathbf n\cdot\mathbf w.
}
\]

Thus the single-circle integer `nw` generalizes naturally to the standard torus momentum–winding pairing.

Again this is known compactification topology, not a new LTG quantum rule.

## 11. Strong structural statement

The most robust current LTG relation is therefore dimension-independent within the entire class of null higher-dimensional kinetic reductions:

\[
\boxed{
\underbrace{\left\langle v^2/c^2\right\rangle_E}_{3P/\rho}
+
\underbrace{\left\langle(d\tau/dt)^2\right\rangle_E}_{P_I/\rho}
=1.
}
\]

Equivalently,

\[
\boxed{
T_{(4)}=-P_I.
}
\]

This can be read as:

> what a 4D observer calls the massive/proper-time fraction is the fraction of the parent null stress carried in hidden spatial directions.

That statement survives replacing one hidden dimension by many.

## 12. Novelty status

### F-024C

**The hidden-pressure/proper-time interpretation is structural across arbitrary numbers of flat compact hidden dimensions.**

### F-024D

**Its robustness increases its value as a unifying interpretation, but not its novelty: it remains a consequence of the higher-dimensional null mass shell and kinetic stress tensor.**

## 13. Next target

The next useful extension is no longer "add dimensions." It is to include a realistic mass mechanism simultaneously with hidden momentum:

\[
E^2=p^2c^2+m_H^2c^4+m_{KK}^2c^4+\text{mixing},
\]

and determine whether the LTG proper-time/stress interpretation can separate the Higgs/Yukawa contribution from the geometric hidden-momentum contribution in any observable way.

That is the natural EXP-025.
