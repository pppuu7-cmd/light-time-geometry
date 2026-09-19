# EXP-110 — Existing full-QCD multi-volume sensitivity gap

## Objective

Check whether already-published dynamical-QCD volume comparisons are precise enough to test the EXP-109 correlated \(1/L\) target.

Use the JLQCD Möbius domain-wall study, which contains a matched-volume comparison at the same bare parameters.

---

## 1. Published matched-volume point

At

\[
\beta=4.17,
\qquad
m_{ud}=0.0035,
\qquad
m_s=0.04,
\]

the study compares:

\[
L/a=32
\]

and

\[
L/a=48.
\]

The lattice spacing is approximately

\[
a\simeq0.08\ {\rm fm},
\]

so the physical spatial lengths are approximately

\[
\boxed{
L_1\simeq2.56\ {\rm fm},
\qquad
L_2\simeq3.84\ {\rm fm}.
}
\]

The corresponding susceptibility estimates are

\[
\chi_t(L_1)
=
0.217(64)(14)\times10^{-5}
\]

and

\[
\chi_t(L_2)
=
0.282(34)(42)\times10^{-5}
\]

in lattice units.

The authors report these as mutually consistent and conclude that their finite-volume systematics are under control at their statistical precision.

---

## 2. LTG target size

The EXP-109 benchmark predicts

\[
\frac{\chi_t(L)}
{\chi_t(\infty)}
\simeq
1-\frac{A}{L},
\]

with

\[
A=0.02705\ {\rm fm}.
\]

The predicted relative difference between the two volumes is

\[
A
\left(
\frac1{L_1}-\frac1{L_2}
\right).
\]

Numerically,

\[
\boxed{
\left|
\frac{\chi_t(L_2)-\chi_t(L_1)}
{\chi_t}
\right|_{\rm LTG}
\simeq
0.00352
=
0.352\%.
}
\]

---

## 3. Published statistical sensitivity

Combining the quoted statistical and systematic errors in quadrature gives relative uncertainties of roughly

\[
\boxed{
30\%
}
\]

for the smaller volume and

\[
\boxed{
19\%
}
\]

for the larger one.

Thus the published volume comparison is approximately two orders of magnitude too imprecise to test a \(0.35\%\) LTG drift.

### Result 110A

\[
\boxed{
\text{existing matched full-QCD data are consistent with the LTG target
but not remotely precise enough to verify or exclude it}.
}
\]

---

## 4. Why this matters

The phrase "finite-volume effects are under control" in an ordinary hadron/QCD analysis does not mean that a sub-percent anomalous \(1/L\) contribution has been excluded.

The EXP-100 hypothesis lives below the precision goal of most existing zero-temperature topology studies.

---

## 5. Required sensitivity

For a two-volume comparison with a target fractional shift

\[
\delta\simeq0.35\%,
\]

a clean \(5\sigma\) pairwise test would require combined relative uncertainty

\[
\boxed{
\sigma_{\rm combined}
\lesssim0.07\%.
}
\]

A practical campaign should instead gain power from:

- many matched volumes;
- correlated scale setting;
- simultaneous fits to \(\chi_t,\Sigma,M_\pi,F_\pi,b_2\);
- multiple lattice spacings;
- the full \(1/L\) functional form.

---

## Terminal classification

### Existing full-QCD data

\[
\boxed{\text{INSUFFICIENT SENSITIVITY}.}
\]

### Existing-data falsification of EXP-100

\[
\boxed{\text{NO}.}
\]

### Dedicated lattice campaign still required

\[
\boxed{\text{YES}.}
\]
