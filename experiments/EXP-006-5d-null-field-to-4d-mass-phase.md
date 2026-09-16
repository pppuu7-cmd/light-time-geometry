# EXP-006 — 5D massless field -> 4D mass and proper-time phase

## Question

EXP-004 showed, for the simplest 5D null lift,

\[
mc=|p_\psi|,
\qquad
c\,d\tau=|d\psi|.
\]

These relations suggest a stronger field-level statement:

> Can a four-dimensional massive quantum mode and its proper-time phase arise directly from a higher-dimensional massless field carrying momentum in the hidden direction?

This is a standard Kaluza-Klein idea, but it tests whether the LTG null/timelike connection survives quantization at the level of the wave equation rather than only classical worldlines.

---

## 1. Phase identity

Choose orientation so that

\[
p_\psi=mc,
\qquad
d\psi=c\,d\tau.
\]

Then

\[
\boxed{p_\psi d\psi=mc^2d\tau.}
\]

The usual relativistic proper-time action for a free massive particle is, up to sign convention,

\[
S_4=-mc^2\int d\tau.
\]

The associated quantum phase is

\[
\exp\left(-\frac{i}{\hbar}mc^2\tau\right).
\]

But the hidden-coordinate plane-wave phase is

\[
\exp\left(-\frac{i}{\hbar}p_\psi\psi\right).
\]

Using the null-lift relations,

\[
\boxed{
\frac{mc^2\tau}{\hbar}
=\frac{p_\psi\psi}{\hbar}
}
\]

for the corresponding displacement.

Thus the massive particle's proper-time phase can be reinterpreted as ordinary translation phase in the hidden direction.

This is a precise version of the idea that the "mass clock" may be a projection of deeper null geometry.

---

## 2. Field-level dimensional reduction

Take a flat 5D product spacetime with one spacelike hidden coordinate `psi`:

\[
dS_5^2=\eta_{\mu\nu}dx^\mu dx^\nu+d\psi^2.
\]

Let `Psi(x,psi)` be a massless 5D scalar satisfying

\[
\boxed{\Box_5\Psi=0.}
\]

Since

\[
\Box_5=\Box_4+\partial_\psi^2,
\]

use a separated mode

\[
\Psi(x,\psi)=\phi(x)e^{ik_\psi\psi}.
\]

Then

\[
\partial_\psi^2\Psi=-k_\psi^2\Psi,
\]

and the 5D massless equation becomes

\[
\boxed{(\Box_4-k_\psi^2)\phi=0.}
\]

The 4D Klein-Gordon equation for mass `m` is

\[
\left(\Box_4-\frac{m^2c^2}{\hbar^2}\right)\phi=0.
\]

Therefore

\[
\boxed{k_\psi=\frac{mc}{\hbar}},
\]

or

\[
\boxed{p_\psi=\hbar k_\psi=mc.}
\]

So a **massless 5D field mode with nonzero hidden momentum is exactly a massive 4D Klein-Gordon mode** in this simple product geometry.

The zero mode

\[
k_\psi=0
\]

remains massless in 4D.

---

## 3. Null/timelike sectors as modes of one deeper field

At the level of the higher-dimensional field:

\[
\boxed{
\text{same 5D massless field}
\begin{cases}
 k_\psi=0 &\to \text{4D massless mode},\\
 k_\psi\neq0 &\to \text{4D massive mode}.
\end{cases}
}
\]

This is stronger than saying that a photon worldline continuously turns into an electron worldline. It says that lower-dimensional massless and massive dispersion relations can arise as different momentum sectors of a common higher-dimensional massless theory.

That structural idea is established Kaluza-Klein physics and is not unique to LTG.

---

## 4. Compact hidden coordinate

If

\[
\psi\sim\psi+2\pi R,
\]

single-valued modes have

\[
k_\psi=\frac{n}{R},
\qquad n\in\mathbb Z.
\]

Hence

\[
\boxed{m_n=\frac{|n|\hbar}{Rc}.}
\]

The 4D mass spectrum is therefore geometric.

This also shows a major phenomenological constraint: a naive single compact dimension predicts a regular Kaluza-Klein tower, not the observed arbitrary Standard Model mass spectrum. Additional structure would be required.

---

## 5. Relation to the de Broglie/Compton clock

The proper-time phase frequency of a massive mode is

\[
\omega_C=\frac{mc^2}{\hbar}.
\]

Using

\[
k_\psi=\frac{mc}{\hbar},
\]

we obtain

\[
\boxed{\omega_C=c\,k_\psi.}
\]

Thus the Compton angular frequency is exactly `c` times the hidden spatial wave number in the minimal null lift.

Equivalently, when the null-lift relation gives `d psi = c d tau`,

\[
k_\psi d\psi=\omega_C d\tau.
\]

The 4D internal phase clock is therefore the dimensional-reduction image of higher-dimensional spatial phase.

---

## 6. Why this still does not prove a new physical dimension

There are two logically different statements:

### Mathematical statement
A massive 4D Klein-Gordon field can be obtained by Fourier reducing a massless 5D field with fixed hidden momentum.

**True and standard.**

### Physical statement
The hidden coordinate is a real fundamental dimension and observed rest mass/proper time are caused by motion in it.

**Not established by the mathematics alone.**

To promote the construction to a physical theory, LTG would need to specify:

- why the extra coordinate exists;
- its topology and metric dynamics;
- how Standard Model spin/gauge structure arises;
- why observed masses and couplings have their measured values;
- why Kaluza-Klein excitations have not appeared in existing experiments;
- how gravity reduces to observed 4D GR to high precision.

---

## EXP-006 result

The null-lift picture closes into a coherent classical+quantum triangle:

\[
\boxed{
P_5^2=0
\quad\Rightarrow\quad
p_4^2=-p_\psi^2=-m^2c^2
}
\]

\[
\boxed{
dS_5^2=0
\quad\Rightarrow\quad
d\psi=c\,d\tau
}
\]

\[
\boxed{
p_\psi d\psi=mc^2d\tau
}
\]

and

\[
\boxed{
\Box_5\Psi=0
\quad\Rightarrow\quad
\left(\Box_4-\frac{m^2c^2}{\hbar^2}\right)\phi=0.
}
\]

### Classification

**EXACT KNOWN DIMENSIONAL-REDUCTION STRUCTURE; VERY CLOSE TO LTG CORE INTUITION.**

No new physics has been isolated, but the research direction is now much sharper. Instead of postulating that "matter converts light into time," a mathematically coherent reformulation is:

> 4D null and timelike behavior may be different projections/momentum sectors of a deeper null geometry, with 4D rest mass and proper-time phase emerging from hidden-direction momentum and phase.

The remaining novelty question is whether LTG can derive a new invariant coupling between this null-lift structure and cosmological geometry that is not already ordinary Kaluza-Klein/radion physics.
