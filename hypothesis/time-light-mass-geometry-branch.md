# LTG research branch — time, light, mass, and geometry

## Motivation

This branch tests the intuition that light and time may be complementary manifestations of one underlying relativistic structure, while mass and geometry/space enter as the non-null sector develops.

The hypothesis must be stated carefully enough not to confuse a useful geometric reinterpretation with new physics.

## 1. The first exact structure: tangent-space Lorentz norm

Use metric signature `(-,+,+,+)`. For an infinitesimal displacement,

\[
ds^2=g_{\mu\nu}dx^\mu dx^\nu.
\]

For a timelike trajectory,

\[
ds^2=-c^2d\tau^2.
\]

In a local inertial frame,

\[
c^2d\tau^2=c^2dt^2-d\ell^2.
\]

Equivalently,

\[
\boxed{
\left(\frac{d\ell}{c\,dt}\right)^2+
\left(\frac{d\tau}{dt}\right)^2=1
}
\]

for timelike motion.

This gives two complementary normalized quantities in a chosen local inertial frame:

- propagation fraction: `d ell/(c dt)`;
- proper-time fraction: `d tau/dt`.

At rest,

\[
d\ell=0,\qquad d\tau=dt.
\]

In the null limit,

\[
d\ell=c\,dt,\qquad d\tau=0.
\]

### Important interpretation

Light is **not** literally the negative of time. The opposite signs belong to the temporal and spatial parts of the Lorentzian metric. Light is the **null balance condition** at which those contributions cancel:

\[
c^2dt^2-d\ell^2=0.
\]

Therefore a more precise version of the original intuition is:

> spatial propagation and proper-time accumulation are complementary projections of a Lorentzian interval, while light is the null boundary where the proper-time norm vanishes.

## 2. The dual exact structure: cotangent-space Lorentz norm

The inverse metric acts on four-momentum. For an on-shell particle,

\[
g^{\mu\nu}p_\mu p_\nu=-m^2c^2.
\]

In a local inertial frame,

\[
E^2=p^2c^2+m^2c^4.
\]

Hence

\[
\boxed{
\left(\frac{pc}{E}\right)^2+
\left(\frac{mc^2}{E}\right)^2=1.
}
\]

For a massive free particle,

\[
\frac{pc}{E}=\frac{v}{c},
\qquad
\frac{mc^2}{E}=\frac{d\tau}{dt}.
\]

Thus the coordinate-space and momentum-space decompositions coincide numerically:

\[
\boxed{
\frac{d\ell}{c\,dt}=\frac{pc}{E},
\qquad
\frac{d\tau}{dt}=\frac{mc^2}{E}.
}
\]

This is standard relativistic kinematics, but it gives the cleanest mathematical form found so far for the LTG intuition.

## 3. The proposed dual pairing

The metric produces two Lorentz norms:

### Tangent side

\[
\boxed{
\mathcal T^2\equiv -g_{\mu\nu}dx^\mu dx^\nu=c^2d\tau^2
}
\]

for timelike displacement.

### Cotangent side

\[
\boxed{
\mathcal M^2\equiv -g^{\mu\nu}p_\mu p_\nu=m^2c^2.
}
\]

This suggests the structural pairing

\[
\boxed{
\text{proper time} \leftrightarrow \text{rest mass}
}
\]

as the invariant magnitudes of the same Lorentzian geometry acting on tangent and cotangent spaces.

For a freely propagating massive particle,

\[
p_\mu=m u_\mu,
\qquad
u^\mu\equiv\frac{dx^\mu}{d\tau},
\]

so

\[
\boxed{
p_\mu dx^\mu=-mc^2d\tau
}
\]

with the chosen signature.

The action/phase therefore joins the two sides:

\[
S=-mc^2\int d\tau=\int p_\mu dx^\mu.
\]

This is an exact known identity, not a new LTG law.

## 4. Role map

The present branch assigns the following roles:

### Geometry `g`
Defines both the causal norm of spacetime displacements and the mass-shell norm of momenta.

### Space
Appears as the spatial component of `dx^mu`; increasing spatial propagation reduces proper-time accumulation relative to a chosen inertial coordinate time.

### Coordinate time `t`
Is one coordinate component and is frame dependent.

### Proper time `tau`
Is the invariant magnitude of a timelike spacetime displacement.

### Light
Is the null sector:

\[
g(dx,dx)=0.
\]

It defines the causal cone and the limiting balance `d ell = c dt`; it is not a second substance that must be converted into time.

### Mass
Is the invariant magnitude of a timelike four-momentum:

\[
-g^{-1}(p,p)=m^2c^2.
\]

Mass therefore plays on momentum space a role closely analogous to the role proper time plays on displacement space.

## 5. What the structure does NOT show

The following stronger claims do **not** follow from the equations above:

1. mass creates spacetime itself;
2. light is converted literally into time;
3. geometry exists only when mass exists;
4. space must expand whenever mass is created.

General relativity admits nontrivial geometry in vacuum, and radiation also carries stress-energy and gravitates. Therefore any claim that mass *creates* geometry or spatial volume requires an additional dynamical law and cannot be inferred from the Lorentz norms alone.

## 6. New hypothesis to test — dual-norm emergence

Define a tentative LTG hypothesis H3:

> There may exist a deeper phase-space structure in which the tangent-space invariant `c d tau` and the cotangent-space invariant `m c` are dual order parameters of the same underlying causal geometry, while the null sector is the simultaneous zero-norm boundary.

This is stronger than standard SR only if it predicts a relation beyond

\[
g(dx,dx)=-c^2d\tau^2,
\qquad
g^{-1}(p,p)=-m^2c^2,
\qquad
p_\mu dx^\mu=-mc^2d\tau.
\]

## 7. Falsification / novelty criteria

H3 is **interpretive only** if every proposed relation is algebraically reducible to:

- the Lorentzian interval;
- the mass-shell condition;
- `p_mu = m u_mu`;
- Hamilton-Jacobi theory;
- the standard worldline action.

H3 becomes a genuinely distinct theory only if at least one of the following survives:

1. a new invariant coupling tangent and cotangent norms;
2. a dynamical equation in which mass-generation changes geometry in a way not already contained in Einstein + QFT equations;
3. a protected relation between mass creation and spatial-volume evolution;
4. a measurable dimensionless observable not removable by field redefinition or choice of frame.

## 8. Immediate next test

Construct the most general local phase-space scalar at lowest derivative order from

\[
g_{\mu\nu},\quad dx^\mu,\quad p_\mu
\]

and test whether any invariant relation beyond the ordinary Lorentz norms and contraction `p_mu dx^mu` exists without adding a new field or preferred structure.

The branch should be rejected as a new theory if the invariant algebra closes completely on those standard quantities.
