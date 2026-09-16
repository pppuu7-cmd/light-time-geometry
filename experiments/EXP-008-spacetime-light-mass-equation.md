# EXP-008 — Spacetime–light–mass equation

## Question

Can mass be added to the same mathematical structure that already contains space, time, and the invariant speed `c`, without inserting it by hand into the spacetime metric?

## 1. Why mass should not simply be inserted into the 4D interval

The 4D line element is

\[
ds^2=g_{\mu\nu}dx^\mu dx^\nu.
\]

It defines causal geometry: null, timelike, and spacelike separations. For a given spacetime geometry, this interval is universal and does not depend on the rest mass of the test particle.

Therefore an expression such as

\[
ds^2\to ds^2+f(m)
\]

has no justification in standard relativity and would generally make geometry particle-species dependent unless a new theory explains the modification.

The clean place for mass is the **mass-shell/action equation**, not an arbitrary addition to the metric.

## 2. Covariant master equation in 4D

For metric signature `(-,+,+,+)`, the relativistic Hamilton–Jacobi equation for a freely moving particle is

\[
\boxed{
g^{\mu\nu}\,\partial_\mu S\,\partial_\nu S+m^2c^2=0
}
\]

with

\[
p_\mu=\partial_\mu S.
\]

This equation already contains:

- **space and time** through the spacetime coordinates and metric `g_{mu nu}`;
- **light** through the invariant causal scale `c` and the null limit;
- **mass** through `m`.

### Massless limit

For

\[
m=0,
\]

we obtain

\[
\boxed{g^{\mu\nu}\partial_\mu S\partial_\nu S=0},
\]

which is the null/eikonal mass-shell condition.

### Massive sector

For

\[
m>0,
\]

we obtain

\[
g^{\mu\nu}p_\mu p_\nu=-m^2c^2,
\]

which is timelike.

Thus the same equation continuously distinguishes the lightlike and massive sectors.

## 3. Flat-spacetime form

In Minkowski spacetime,

\[
-\frac1{c^2}\left(\frac{\partial S}{\partial t}\right)^2
+|\nabla S|^2
+m^2c^2=0.
\]

Using

\[
E=-\frac{\partial S}{\partial t},
\qquad
\mathbf p=\nabla S,
\]

we recover

\[
\boxed{E^2=p^2c^2+m^2c^4}.
\]

So the familiar mass-shell relation is the flat-spacetime form of a single spacetime equation.

## 4. Direct space–time–light–mass identity for inertial motion

For a free massive particle,

\[
E=\gamma mc^2,
\qquad
\frac{d\tau}{dt}=\frac1\gamma=\frac{mc^2}{E}.
\]

Substituting into the interval identity gives

\[
\boxed{
\frac{|d\mathbf x|^2}{c^2dt^2}
+
\left(\frac{mc^2}{E}\right)^2
=1
}
\]

or equivalently

\[
\boxed{
|d\mathbf x|^2
+c^2\left(\frac{mc^2}{E}\right)^2dt^2
=c^2dt^2.
}
\]

This expression explicitly contains space `d x`, coordinate time `dt`, the invariant light speed `c`, and mass `m`.

However, it is exactly standard special relativity and is **not a new law**.

Its useful interpretation is

\[
\frac{mc^2}{E}=\frac{d\tau}{dt},
\]

so rest mass enters the normalized spatial/proper-time decomposition through the ratio of rest energy to total energy.

## 5. Proper-time action and mass phase

Along a timelike geodesic,

\[
dS=-mc^2d\tau.
\]

The corresponding semiclassical phase increment is

\[
\boxed{d\varphi=-\frac{mc^2}{\hbar}d\tau}.
\]

This gives a direct bridge

\[
\text{mass}\leftrightarrow\text{proper-time phase rate}.
\]

It is standard relativistic quantum mechanics, but it precisely formalizes the intuition that nonzero mass and nonzero proper time are deeply linked in the phase evolution of a massive state.

## 6. 5D null form of the same equation

Now use an independently defined fifth coordinate `psi` and metric

\[
dS_5^2=g_{\mu\nu}dx^\mu dx^\nu+b^2d\psi^2.
\]

The 5D **massless** Hamilton–Jacobi equation is

\[
\boxed{
G^{AB}\partial_A\mathcal S\partial_B\mathcal S=0.
}
\]

If

\[
\mathcal S(x,\psi)=S(x)+p_\psi\psi,
\]

then

\[
g^{\mu\nu}\partial_\mu S\partial_\nu S
+\frac{p_\psi^2}{b^2}=0.
\]

Identify

\[
\boxed{m_{\rm eff}^2c^2=\frac{p_\psi^2}{b^2}}.
\]

The 5D null equation becomes exactly

\[
\boxed{
g^{\mu\nu}\partial_\mu S\partial_\nu S+m_{\rm eff}^2c^2=0.
}
\]

Therefore a 4D massive Hamilton–Jacobi equation can be the projection of a higher-dimensional massless/null equation.

## 7. Candidate LTG master structure

The cleanest current form of the original intuition is therefore not a modified 4D interval but the pair

\[
\boxed{
G^{AB}P_AP_B=0
}
\]

and

\[
\boxed{
m_{\rm eff}c=\frac{|P_\psi|}{b}}.
\]

The observed 4D causal type then depends on hidden momentum:

\[
P_\psi=0
\quad\Rightarrow\quad
m_{\rm eff}=0
\quad\Rightarrow\quad
\text{4D null sector},
\]

while

\[
P_\psi\neq0
\quad\Rightarrow\quad
m_{\rm eff}>0
\quad\Rightarrow\quad
\text{4D timelike sector}.
\]

This gives one equation containing a deeper null/light structure whose 4D projections include space, time, and mass.

## 8. What is new and what is not

### Already known

- 4D Hamilton–Jacobi mass-shell equation;
- `m=0` null and `m>0` timelike sectors;
- KK identification of 4D mass with extra-dimensional momentum;
- 5D massless field reducing to 4D massive modes.

### Potential LTG question

The remaining nontrivial question is whether `b` or `P_psi` has a dynamical law tied to ordinary spacetime expansion in a way that produces a new dimensionless observable and is not equivalent to standard radion/KK theory.

## Result

**Yes: mass can be included in the same covariant mathematical structure as space, time, and light.**

The most conservative 4D equation is

\[
\boxed{
g^{\mu\nu}\partial_\mu S\partial_\nu S+m^2c^2=0.
}
\]

The most geometrically suggestive current LTG form is its 5D null lift

\[
\boxed{
G^{AB}\partial_A\mathcal S\partial_B\mathcal S=0,
\qquad
m_{\rm eff}^2c^2=\frac{p_\psi^2}{b^2}.
}
\]

At present these are known structures, not evidence for new physics. Their value for LTG is that they tell us exactly where a genuinely new dynamical ingredient would have to enter.
