# EXP-082 — Positive relative-entropy residual cannot be locally extensive if it sources late vacuum energy

## Objective

Try to use the positive irreversibility action from EXP-077,

\[
\mathcal A_{\rm irr}
=
\frac{\hbar}{2\pi}D_{\rm tot},
\qquad
D_{\rm tot}\ge0,
\]

as a possible positive vacuum-energy source.

Test whether an additive local relative-entropy residual can reproduce the observed infrared scaling

\[
\rho_\Lambda\sim \frac{1}{GL^2}.
\]

---

## 1. Effective vacuum-action identification

As a hypothesis, identify the global irreversible action with an effective vacuum action over a four-volume:

\[
\boxed{
\frac{\hbar}{2\pi}D_{\rm tot}
=
\rho_XV_4.
}
\]

Then

\[
\boxed{
\rho_X
=
\frac{\hbar D_{\rm tot}}
{2\pi V_4}.
}
\]

Because

\[
D_{\rm tot}\ge0,
\]

this route automatically gives

\[
\boxed{
\rho_X\ge0.
}
\]

Thus relative entropy solves the **sign** problem if this identification is valid.

---

## 2. Additive local residual

Suppose the region contains

\[
N_4=\frac{V_4}{\ell_P^4}
\]

microscopic cells and the total relative entropy is additive:

\[
D_{\rm tot}
=
\sum_{j=1}^{N_4}d_j,
\qquad
d_j\ge0.
\]

Assume a stationary local distribution with finite nonzero mean

\[
\langle d_j\rangle=\mu>0.
\]

Then by ordinary law-of-large-numbers scaling,

\[
D_{\rm tot}
\sim
\mu N_4.
\]

Therefore

\[
\rho_X
\sim
\frac{\hbar \mu N_4}
{2\pi N_4\ell_P^4}
=
\boxed{
\frac{\hbar\mu}
{2\pi\ell_P^4}.
}
\]

This is a microscopic/Planckian density independent of the cosmic scale \(L\).

### Result 082A

A positive additive local relative-entropy density produces a constant UV-scale vacuum density, not the desired IR scale.

---

## 3. Zero-mean escape is impossible for nonnegative local terms

For signed random action increments one can have

\[
\langle\delta I\rangle=0
\]

and rms growth

\[
\sqrt{N_4}.
\]

But for

\[
d_j\ge0,
\]

the condition

\[
\langle d_j\rangle=0
\]

implies

\[
d_j=0
\]

almost surely.

Thus local positive relative entropy cannot use an ordinary central-limit cancellation to obtain \(\sqrt{N_4}\) growth.

### Result 082B

\[
\boxed{
\text{positivity removes the simple Poisson-cancellation route}.
}
\]

---

## 4. What scaling is required?

To obtain

\[
\rho_X
\sim
\frac{\hbar}{\ell_P^2L^2},
\]

with

\[
V_4\sim L^4,
\]

the total residual must scale as

\[
D_{\rm tot}
\sim
\frac{L^2}{\ell_P^2}.
\]

That is:

\[
\boxed{
D_{\rm tot}
\sim
\text{area in Planck units},
}
\]

not four-volume in Planck units.

Equivalently,

\[
\boxed{
D_{\rm tot}
\sim
\mathcal N_{\rm horizon}.
}
\]

This is the crucial scaling requirement.

---

## 5. Consequence

If a positive LTG quantum residual sources an infrared vacuum term, it cannot be a sum of independent bulk-cell entropy productions with order-unity mean.

It must be one of:

1. boundary-extensive;
2. strongly nonlocal;
3. correlated so that effective independent degrees of freedom scale as area;
4. constrained by a holographic code/subregion algebra;
5. a single global relative entropy rather than an extensive local sum.

### Result 082C

\[
\boxed{
\text{positive sign}
+
\text{correct late-time magnitude}
\Rightarrow
\text{holographic/nonlocal residual}.
}
\]

---

## 6. Relation to the original LTG picture

This result strongly favors the evolved LTG architecture:

\[
\text{causal boundary information}
\]

rather than

\[
\text{local energy stored uniformly in spacetime}.
\]

It also explains why the literal "energy of every piece of space" picture repeatedly failed.

The required vacuum-scale object is global/boundary-like.

---

## 7. Terminal classification

### Relative entropy can enforce positive effective vacuum action

**SIGN PASS, conditionally.**

### Independent additive bulk residual gives correct IR scale

\[
\boxed{\text{FAIL}.}
\]

### Required residual scaling

\[
\boxed{
D_{\rm tot}\propto A/\ell_P^2.
}
\]

**DERIVED NECESSITY under the effective-vacuum-action hypothesis.**

## Active next gate

Test the boundary-extensive case explicitly.

If

\[
D_{\rm grav}
=
\eta\frac{A}{\ell_P^2},
\]

derive the resulting vacuum-density coefficient, compare it with holographic dark energy, and determine whether any independent causal/quantum principle fixes \(\eta\).
