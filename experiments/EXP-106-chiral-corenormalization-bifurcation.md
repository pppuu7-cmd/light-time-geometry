# EXP-106 — Chiral co-renormalization bifurcation of the proposed lattice isolator

## Objective

EXP-105 proposed

\[
R_\chi(L)
=
\frac{\chi_t(L)}
{M_\pi^2(L)F_\pi^2(L)}
\]

as a way to suppress ordinary chiral finite-volume effects while retaining an anomalous topological \(1/L\) term.

This gate checks whether that is universally true.

---

## 1. Chiral Ward-identity baseline

For two approximately degenerate light flavors,

\[
\chi_t
\simeq
\frac14 M_\pi^2F_\pi^2
\]

at leading chiral order.

Equivalently, with

\[
M_\pi^2F_\pi^2
\simeq
2m_q\Sigma,
\]

one has

\[
\chi_t
\simeq
\frac12m_q\Sigma.
\]

Therefore \(\chi_t\) and the GMOR product probe the same leading chiral amplitude.

---

## 2. Branch A — topological-contact-only finite-size effect

Suppose the anomalous effect changes only the non-dispersive topological contact amplitude,

\[
\chi_t(L)
=
\chi_t(\infty)
\left[
1-\frac{A_\chi}{L}
\right],
\]

while

\[
M_\pi^2(L)F_\pi^2(L)
=
M_\pi^2(\infty)F_\pi^2(\infty)
+
O(e^{-m_\pi L}).
\]

Then

\[
\boxed{
\frac{R_\chi(L)}{R_\chi(\infty)}
=
1-\frac{A_\chi}{L}
+\cdots.
}
\]

In this branch EXP-105 is a good signal isolator.

---

## 3. Branch B — common chiral-amplitude renormalization

Suppose instead

\[
\Sigma(L)
=
\Sigma_\infty
\left[
1-\frac{A_\Sigma}{L}
\right]
+\cdots.
\]

Then GMOR implies

\[
M_\pi^2F_\pi^2(L)
=
M_\pi^2F_\pi^2(\infty)
\left[
1-\frac{A_\Sigma}{L}
\right]
+\cdots.
\]

If the same amplitude controls \(\chi_t\),

\[
\chi_t(L)
=
\chi_t(\infty)
\left[
1-\frac{A_\Sigma}{L}
\right]
+\cdots.
\]

Therefore

\[
\boxed{
R_\chi(L)
=
R_\chi(\infty)
+
O(L^{-2},e^{-m_\pi L}).
}
\]

### Result 106A

A common \(1/L\) renormalization of the chiral condensate removes the anomalous signal from the ratio proposed in EXP-105.

Thus

\[
\boxed{
R_\chi
\text{ is not a universal LTG isolator.}
}
\]

---

## 4. What the original ghost/topological proposal fixes

The Veneziano-ghost construction isolates a non-dispersive topological sector and its mixing with the \(\eta'\).

It does not provide a controlled physical-4D finite-volume calculation of the simultaneous leading \(1/L\) shifts of

- \(\chi_t\);
- \(M_\pi\);
- \(F_\pi\);
- \(\Sigma\);
- \(m_{\eta'}\).

Therefore Branch A versus Branch B cannot presently be chosen from the original proposal alone.

---

## 5. Robust lattice strategy

Do not fit only \(R_\chi\).

Prospectively measure the vector of finite-volume slopes

\[
\boxed{
\mathbf A
=
(
A_\chi,\,
A_{M_\pi^2F_\pi^2},\,
A_\Sigma,\,
A_{b_2},\,
A_{\eta'}
).
}
\]

Then classify:

### Contact-sector branch

\[
A_\chi\ne0,
\qquad
A_{M_\pi^2F_\pi^2}\simeq0,
\qquad
A_{b_2}\simeq0.
\]

### Common-chiral-amplitude branch

\[
A_\chi
\simeq
A_{M_\pi^2F_\pi^2}
\simeq
A_\Sigma,
\]

with the ratio \(R_\chi\) approximately stationary.

### Theta-shape-deformation branch

\[
A_{b_2}\ne0.
\]

In the last case the simple common-amplitude mapping of EXP-104 fails.

---

## 6. Stronger model-independent combination

The lattice test should first establish whether any continuum-stable power-law sector exists.

Only after the slope pattern is classified should a cosmological mapping be applied.

This prevents the analysis from choosing an observable after seeing which quantity happens to show a \(1/L\) drift.

---

## Terminal classification

### EXP-105 ratio as universal detector

\[
\boxed{\text{FAIL}.}
\]

### EXP-105 ratio under contact-only hypothesis

\[
\boxed{\text{VALID CONDITIONALLY}.}
\]

### Required next measurement

\[
\boxed{
(A_\chi,A_{M_\pi^2F_\pi^2},A_\Sigma,A_{b_2},A_{\eta'})
}
\]

rather than a single susceptibility ratio.
