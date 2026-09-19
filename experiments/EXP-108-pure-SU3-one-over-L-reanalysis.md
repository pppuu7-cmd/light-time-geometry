# EXP-108 — Reanalysis of the 2026 seven-volume pure-SU(3) susceptibility data for an anomalous 1/L tail

## Objective

Use an already published high-statistics lattice dataset as a preliminary, non-cosmological test of whether topological susceptibility shows a large \(1/L\) finite-size tail.

Dataset:

Stephan Dürr and Gianluca Fuwa,
*Topological susceptibility and excess kurtosis in SU(3) Yang-Mills theory*,
Phys. Rev. D 113, 054508 (2026).

The paper provides seven physical volumes at fixed \(\beta=6.1912\), Table IX, and fits the standard massive-theory exponential finite-volume form.

This is pure Yang-Mills, not physical \(N_f=2+1\) QCD, so it cannot directly determine the EXP-100 \(\eta'\)-normalized coefficient.

It can nevertheless test whether a simple \(1/L\) law dominates a controlled topological observable.

---

## 1. Published finite-volume data

For the fixed-\(\beta=6.1912\) ensembles:

\[
N=L/a
=
12,14,16,18,20,24,28,
\]

with

\[
\langle q_{\rm ren}^2\rangle
=
0.1911(17),
0.6689(38),
1.3482(63),
2.2154(81),
3.394(15),
7.019(25),
13.050(53).
\]

At fixed \(a\),

\[
\chi_t a^4
=
\frac{\langle q_{\rm ren}^2\rangle}{N^4}.
\]

Following the paper, use

\[
N\ge14
\]

for the principal finite-volume fit.

The physical lattice spacing is approximately

\[
a\simeq0.0655\ {\rm fm}
\]

using the paper's \(r_0/a=7.263\) and \(r_0\simeq0.4757\) fm.

---

## 2. Pure 1/L model

Fit

\[
\chi_t a^4
=
c+\frac{d}{N}.
\]

Using the published statistical errors as diagonal fit errors gives

\[
\boxed{
\chi^2\simeq543.96
\quad
\text{for }4\text{ dof}.
}
\]

### Result 108A

\[
\boxed{
\text{a pure }1/L
\text{ law as the sole finite-volume correction is decisively incompatible with these data.}
}
\]

This result is expected physically because the smallest retained boxes still show the ordinary glueball-mediated exponential correction.

---

## 3. Standard exponential model

Fit

\[
\chi_t a^4
=
c+b e^{-mN}.
\]

The re-fit gives approximately

\[
\boxed{
ma=0.902\pm0.085
}
\]

and

\[
\boxed{
\chi^2\simeq0.58
\quad
\text{for }3\text{ dof}.
}
\]

The published paper independently reports

\[
\boxed{
M_Ga=0.903(38)
}
\]

from its finite-volume analysis.

Thus the re-fit reproduces the published standard exponential behavior.

---

## 4. Add an anomalous 1/L tail on top of the known exponential

To avoid falsely forcing the anomalous term to explain ordinary finite-volume physics, fix the exponential mass to the published

\[
M_Ga=0.903
\]

and fit

\[
\boxed{
\chi_t a^4
=
c+\frac{d}{N}+b e^{-0.903N}.
}
\]

The result is

\[
d
=
(0.09\pm4.60)\times10^{-6}
\]

in the corresponding lattice normalization.

Write the power-law term as

\[
\chi_t(L)
=
\chi_\infty
\left(
1-\frac{A_{\rm YM}}{L}
\right)
+
\text{exponential}.
\]

Then

\[
\boxed{
A_{\rm YM}
=
(-0.0003\pm0.0142)\ {\rm fm}.
}
\]

A diagonal-error 95% interval is approximately

\[
\boxed{
-0.0281\ {\rm fm}
<
A_{\rm YM}
<
0.0276\ {\rm fm}.
}
\]

The fit quality remains excellent,

\[
\chi^2\simeq0.576
\]

for 3 dof.

### Result 108B

The central anomalous \(1/L\) coefficient in this pure-YM reanalysis is consistent with zero.

---

## 5. Comparison to the physical-QCD LTG target

EXP-104 predicts, conditionally for physical QCD,

\[
A_\chi^{N_f=2+1}
\simeq
0.02705\ {\rm fm}
\]

when the earlier cosmological matching value is used.

Numerically this lies about

\[
\boxed{
1.9\sigma
}
\]

from the pure-YM re-fit central value.

However this is **not** a direct exclusion because:

1. pure Yang-Mills has no physical \(\eta'\)/light-quark GMOR mapping;
2. the coefficient can depend on \(N_f\), quark masses and topology;
3. the data were not generated to isolate a sub-percent power-law tail;
4. correlations and continuum systematics are not fully reconstructed in this simple re-fit.

### Result 108C

\[
\boxed{
\text{published pure-YM data give a preliminary null result,
not a terminal test of EXP-100}.
}
\]

---

## 6. Important published observation

The authors themselves find that the standard working volume needs only a finite-volume correction factor of approximately

\[
1.0048(08)
\]

to reach the infinite-volume susceptibility, and their exponential fit yields a pseudoscalar glueball mass consistent with independent determinations.

This strongly supports conventional gapped finite-volume physics as the dominant effect in the measured range.

---

## 7. Appendix-volume cross-check

The same paper contains a second seven-volume series at a coarser lattice spacing extending to larger physical boxes.

Those data show mild cutoff effects and are not a continuum-matched determination of a tiny anomalous slope.

A simple power-law interpretation is therefore not used as a decisive LTG test.

The correct next step remains a dedicated physical-QCD, multi-spacing, matched-volume analysis.

---

## Terminal classification

### Pure 1/L as sole finite-volume law in published SU(3) data

\[
\boxed{\text{FAIL}.}
\]

### Additional small 1/L tail after standard exponential physics

\[
\boxed{\text{CONSISTENT WITH ZERO / CURRENT BOUND NOT DECISIVE}.}
\]

### Direct physical-QCD EXP-100 test

\[
\boxed{\text{STILL OPEN}.}
\]

## Reproducibility note

The numerical re-fit uses only the published Table IX values and quoted diagonal statistical errors. It is a project-side audit, not a replacement for the collaboration's correlated systematic analysis.
