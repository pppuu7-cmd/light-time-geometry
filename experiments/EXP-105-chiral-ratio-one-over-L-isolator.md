# EXP-105 — Chiral-ratio isolator for the LTG topological 1/L lattice signal

## Objective

The target signal from EXP-104 is sub-percent at realistic lattice volumes.

Standard chiral finite-volume effects can be larger and are mostly exponential in \(m_\pi L\).

Construct an observable that suppresses ordinary chiral finite-volume contamination while retaining the hypothesized anomalous topological \(1/L\) signal.

---

## 1. Standard chiral relation

For approximately degenerate light quarks, leading chiral perturbation theory gives

\[
\chi_t
\simeq
\frac14
M_\pi^2F_\pi^2
\]

up to higher-order and strange-quark corrections.

Lattice analyses with chiral fermions use the ratio

\[
\boxed{
R_\chi(L)
\equiv
\frac{\chi_t(L)}
{M_\pi^2(L)F_\pi^2(L)}
}
\]

because standard NLO finite-volume corrections largely cancel in this combination.

This is established lattice/chiral-EFT practice.

---

## 2. LTG anomalous-tail prediction

Under EXP-104,

\[
\chi_t(L)
=
\chi_t(\infty)
\left[
1-\frac{A_\chi}{L}
\right]
+\cdots
\]

with

\[
A_\chi
=
\frac{\zeta_{\rm LTG}\hbar c}
{2\pi m_{\eta'}}.
\]

Assume the ordinary pion observables retain their standard gapped finite-volume form,

\[
M_\pi(L)
=
M_\pi(\infty)
+
O(e^{-m_\pi L}),
\]

\[
F_\pi(L)
=
F_\pi(\infty)
+
O(e^{-m_\pi L}).
\]

Then

\[
\boxed{
\frac{R_\chi(L)}
{R_\chi(\infty)}
=
1-\frac{A_\chi}{L}
+
O(L^{-2},e^{-m_\pi L}).
}
\]

### Result 105A

The same anomalous \(1/L\) coefficient survives in the chiral-normalized ratio while standard NLO chiral finite-volume effects are strongly reduced.

---

## 3. Numerical target

For

\[
\zeta_{\rm LTG}=0.825,
\]

\[
A_\chi=0.02705\ {\rm fm}.
\]

Therefore

\[
\boxed{
R_\chi(L)/R_\chi(\infty)
=
1-\frac{0.02705\ {\rm fm}}{L}.
}
\]

Useful pairwise differences are:

### \(L=2.5\) fm versus \(8\) fm

\[
\boxed{
\Delta R/R
\simeq
0.744\%.
}
\]

### \(L=3\) fm versus \(6\) fm

\[
\boxed{
\Delta R/R
\simeq
0.451\%.
}
\]

### \(L=4\) fm versus \(8\) fm

\[
\boxed{
\Delta R/R
\simeq
0.338\%.
}
\]

These are small but not astronomically small.

---

## 4. Precision requirement

A clean pairwise \(5\sigma\) detection of the \(4\)-to-\(8\) fm difference alone would require a combined uncertainty of order

\[
\lesssim0.07\%
\]

on the ratio, which is much more precise than typical standalone determinations of \(\chi_t\).

Therefore a realistic test should use:

1. correlated matched-volume ensembles;
2. simultaneous multi-volume fitting;
3. common scale setting;
4. ratio observables;
5. continuum extrapolation;
6. the full expected \(1/L\) shape rather than one pairwise difference.

### Result 105B

The test is numerically difficult but not conceptually inaccessible.

A dedicated lattice campaign is required; existing generic topological-susceptibility datasets are not automatically decisive.

---

## 5. Signal-plus-null-control strategy

Fit simultaneously:

\[
R_\chi(L)
=
R_\infty
\left(
1-\frac{A_\chi}{L}
\right)
+
R_{\rm std}(L),
\]

and

\[
b_2(L)
=
b_{2,\infty}
+
b_{2,\rm std}(L).
\]

The EXP-104 amplitude-rescaling hypothesis requires:

\[
\boxed{
A_\chi>0
}
\]

with

\[
\boxed{
A_\chi
\simeq0.0271\ {\rm fm}
}
\]

for the benchmark,

while the leading anomalous coefficient of \(b_2\) is zero.

A simultaneous \(1/L\) drift in both \(R_\chi\) and \(b_2\) would falsify the simple amplitude-rescaling transfer even if some topological Casimir effect exists.

---

## 6. Stronger full-theta test

Modern lattice calculations can reconstruct the theta-dependent free energy from the topological-charge distribution.

For each volume, define

\[
f_L(\theta)
=
-\frac1{V_4}
\ln
\frac{Z_L(\theta)}
{Z_L(0)}.
\]

The amplitude-rescaling hypothesis predicts

\[
\boxed{
f_L(\theta)
=
\left(
1-\frac{A_\chi}{L}
\right)
f_\infty(\theta)
+
O(L^{-2},e^{-m_\pi L}).
}
\]

Therefore the ratio

\[
\boxed{
\frac{f_L(\theta)}
{f_\infty(\theta)}
}
\]

should be theta-independent at leading \(1/L\).

This is stronger than measuring \(\chi_t\) alone.

---

## 7. Terminal classification

### Best low-cost lattice discriminator

\[
\boxed{
R_\chi
=
\chi_t/(M_\pi^2F_\pi^2).
}
\]

### EXP-100 benchmark slope

\[
\boxed{
A_\chi
=
0.02705\ {\rm fm}.
}
\]

### Full-theta factorization test

\[
\boxed{
f_L(\theta)/f_\infty(\theta)
=
1-A_\chi/L
}
\]

at leading anomalous order.

### Existing-data verdict

No currently located physical zero-temperature multi-volume dataset is precise and controlled enough to claim either PASS or FAIL at the required sub-percent level.

## Active next gate

Search for or construct a real multi-volume zero-temperature dataset with matched physical parameters.

If unavailable, the next theoretical target is to derive whether the anomalous topological amplitude should also shift \(M_\pi\) or \(F_\pi\), which would determine how much of the \(1/L\) signal survives in \(R_\chi\).
