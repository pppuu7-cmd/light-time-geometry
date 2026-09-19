# EXP-063 — Duality-fixed coupling as a parameter-free hierarchy seed

## Objective

EXP-062 showed that a 4D causal metric does not fix a dimensionless gauge coupling.

Test the strongest remaining symmetry-based loophole:

\[
\boxed{
\text{exact electric-magnetic duality}
\to
\text{self-dual coupling}
}
\]

and ask whether such a discretely fixed coupling can seed the huge hierarchy of EXP-060 without continuous tuning.

---

## 1. Complexified coupling and S-duality

Use the standard complex coupling

\[
\tau
=
\frac{\theta}{2\pi}
+
\frac{4\pi i}{g^2}.
\]

The S transformation acts as

\[
S:\quad
\tau\mapsto-\frac1\tau.
\]

A fixed point satisfies

\[
\tau=-\frac1\tau,
\]

so

\[
\tau^2=-1.
\]

In the upper half plane,

\[
\boxed{
\tau=i.
}
\]

For

\[
\theta=0,
\]

this gives

\[
\frac{4\pi}{g_{\rm SD}^2}=1
\]

and therefore

\[
\boxed{
g_{\rm SD}^2=4\pi,
\qquad
g_{\rm SD}=\sqrt{4\pi}.
}
\]

Thus an exact duality symmetry can indeed fix a continuous coupling to a discrete special value.

### Result 063A

\[
\boxed{
\text{symmetry-fixed dimensionless couplings exist}.
}
\]

This is established prior art in self-dual gauge theories, not an LTG result.

---

## 2. Other modular fixed point

The modular group also has the fixed point

\[
\tau=e^{i\pi/3}
=
\frac12+i\frac{\sqrt3}{2}
\]

under an appropriate modular transformation.

Then

\[
\frac{4\pi}{g^2}
=
\frac{\sqrt3}{2},
\]

so

\[
\boxed{
g^2
=
\frac{8\pi}{\sqrt3}.
}
\]

Again the coupling is fixed discretely by symmetry.

---

## 3. Feed the self-dual coupling into EXP-060

EXP-060 used

\[
n
=
\frac12
\exp\left(
\frac{2A}{g^2}
\right).
\]

Take the illustrative standard nonperturbative coefficient

\[
A=8\pi^2.
\]

### At tau = i

With

\[
g^2=4\pi,
\]

the exponent is

\[
\frac{2A}{g^2}
=
\frac{16\pi^2}{4\pi}
=
4\pi.
\]

Therefore

\[
\boxed{
n_{\tau=i}
=
\frac12e^{4\pi}
\approx1.43\times10^5.
}
\]

### At tau = exp(i pi/3)

With

\[
g^2=\frac{8\pi}{\sqrt3},
\]

the exponent is

\[
\frac{16\pi^2}{8\pi/\sqrt3}
=
2\pi\sqrt3.
\]

Therefore

\[
\boxed{
n_{\rm modular}
=
\frac12e^{2\pi\sqrt3}
\approx2.66\times10^4.
}
\]

These are large compared with unity but nowhere near

\[
10^{122}.
\]

### Result 063B

A standard self-dual coupling combined with a typical \(8\pi^2/g^2\)-type nonperturbative action does **not** generate the required cosmological hierarchy.

---

## 4. Required action coefficient at the self-dual point

To obtain

\[
n_*\sim10^{122}
\]

at

\[
g^2=4\pi,
\]

one requires

\[
\frac{2A}{4\pi}
\approx
\ln(2\times10^{122})
\approx281.6.
\]

Thus

\[
A
\approx
2\pi\times281.6
\approx1.77\times10^3.
\]

This is far larger than the illustrative coefficient

\[
8\pi^2\approx79.
\]

Therefore self-duality alone does not naturally solve the hierarchy problem in this benchmark.

---

## 5. Conceptual value of the result

EXP-063 demonstrates a key distinction.

### Coupling selection

Exact duality symmetry can remove continuous freedom:

\[
\boxed{
g\to g_{\rm SD}.
}
\]

### Hierarchy generation

Whether that selected value yields an enormous transmuted hierarchy depends on the nonperturbative coefficient and beta-function structure.

Thus the combined mechanism requires both:

\[
\boxed{
\text{duality selection}
+
\text{appropriate RG/nonperturbative dynamics}.
}
\]

Neither ingredient alone is enough.

---

## 6. Is causal geometry responsible for the self-dual point?

Not in the standard construction.

The self-dual value follows from an internal quantum duality acting on the coupling space.

The spacetime causal metric does not select

\[
\tau=i
\]

by itself.

To turn this into LTG-specific physics one would need a new argument that the light/time/global-causal structure enforces an electric-magnetic or more general modular self-duality.

No such derivation has been obtained.

### Result 063C

\[
\boxed{
\text{parameter-free coupling selection: possible by symmetry}
}
\]

but

\[
\boxed{
\text{causal-geometric origin of that symmetry: OPEN}.
}
\]

---

## 7. Relation to the original light-time duality intuition

This is conceptually suggestive because the original LTG intuition involved two dual sectors.

Electric-magnetic duality is a genuine example where

\[
\text{two descriptions}
\]

are exchanged and a special fixed point can remove coupling freedom.

But this is only an analogy unless LTG derives a concrete duality transformation on its own variables.

Therefore the project should not identify light/time duality with S-duality without an explicit map.

---

## 8. Terminal classification

### Can an exact duality fix a dimensionless coupling?

\[
\boxed{\text{YES}.}
\]

**PRIOR-ART PASS.**

### Does the standard self-dual coupling generate n ~ 10^122 with A = 8 pi^2?

\[
\boxed{\text{NO}.}
\]

**HIERARCHY FAIL FOR THE BENCHMARK.**

### Can LTG derive the needed duality from causal geometry?

\[
\boxed{\text{NOT YET}.}
\]

## Active next criterion

A viable parameter-free route must now supply either:

1. a different exact symmetry that fixes a smaller effective coupling;
2. a larger dynamically derived nonperturbative action coefficient;
3. a multi-stage exponential hierarchy;
4. an LTG-specific duality relation whose fixed point is derived from causal geometry.

Any such proposal must predict, not fit, the relevant dimensionless data.
