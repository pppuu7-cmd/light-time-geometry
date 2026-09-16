# EXP-013 — Topological mass–proper-time phase invariant

## Objective

Look for a relation that survives radion evolution and therefore is stronger than the dimensional statement `m ~ 1/b` by itself.

Use only the already established null-lift relations and compact-circle quantization.

## 1. Compact hidden direction

Take

\[
dS_5^2=g_{\mu\nu}dx^\mu dx^\nu+b(x)^2d\psi^2,
\]

with

\[
\psi\sim\psi+2\pi R_0.
\]

If the metric is independent of `psi`, the conjugate momentum is conserved:

\[
p_\psi=\frac{n\hbar}{R_0},\qquad n\in\mathbb Z.
\]

The 4D effective mass is

\[
\boxed{
m_n c=\frac{|p_\psi|}{b}
=\frac{|n|\hbar}{bR_0}.
}
\]

## 2. Proper time from the same null lift

For a 5D null trajectory whose 4D projection is timelike,

\[
0=dS_5^2=-c^2d\tau^2+b^2d\psi^2,
\]

hence

\[
\boxed{
c\,d\tau=b|d\psi|.
}
\]

## 3. Cancellation of the internal scale

Multiply the two relations:

\[
m_n c^2d\tau
=\frac{|p_\psi|}{b}\,b|d\psi|
=|p_\psi d\psi|.
\]

Thus

\[
\boxed{
m_n c^2d\tau=|p_\psi d\psi|.
}
\]

The compactification factor `b(x)` cancels **pointwise**. Therefore this relation survives slow or rapid variation of the radion as long as `psi` remains a cyclic direction and the null-lift relation remains valid.

This is stronger than either `m ~ 1/b` or `d tau ~ b d psi` separately.

## 4. One full hidden winding

For an oriented winding number `w`,

\[
\oint d\psi=2\pi wR_0.
\]

The hidden translation phase is

\[
\frac1\hbar\oint p_\psi d\psi
=2\pi nw.
\]

Therefore the magnitude of the accumulated 4D proper-time mass phase satisfies

\[
\boxed{
\frac1\hbar\oint m_n c^2d\tau
=2\pi|nw|.
}
\]

or equivalently

\[
\boxed{
\oint m_n c^2d\tau=h|nw|.
}
\]

For a single winding and the first nonzero KK mode,

\[
\boxed{
\Delta\tau_{\rm cycle}=\frac{h}{mc^2}.
}
\]

This last equation is **not** a universal proper-time quantum. It applies only to the specific compact hidden-cycle construction.

## 5. Interpretation

The ordinary 4D Compton/proper-time phase

\[
\phi_C=\frac1\hbar\int mc^2d\tau
\]

is exactly the hidden-direction translation phase in the minimal null lift.

The important new-to-this-project observation is not that KK phase quantization exists—it is standard—but that the pair

\[
m\propto b^{-1},\qquad d\tau\propto b
\]

forms a **radion-independent product**:

\[
\boxed{m\,d\tau\ \text{is protected against the explicit }b\text{ scaling}.}
\]

This provides a cleaner LTG invariant candidate than a varying mass alone.

## 6. Novelty test

The phase integral

\[
\oint p_\psi d\psi=2\pi n\hbar
\]

is ordinary quantization on a compact circle. The equality to the 4D proper-time phase follows from the standard null lift.

Therefore the result is not new physics by itself.

### F-013A

**A topologically quantized mass–proper-time phase exists in the compact null-lift model.**

### F-013B

**Its explicit radion dependence cancels exactly.**

### F-013C

**The invariant is known-equivalent to KK phase/momentum quantization, but it is the most robust compact equation found so far connecting mass and proper time.**

## 7. Next question

The next useful test is dynamical rather than kinematic:

> Can a 4D massless/zero-mode state convert into massive/timelike modes while preserving the conserved hidden momentum and 5D covariance?

On a compact circle the natural answer should be pair production into opposite KK numbers. EXP-014 tests this explicitly.
