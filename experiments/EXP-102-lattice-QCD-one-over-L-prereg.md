# EXP-102 — Preregistered lattice-QCD falsification test of the LTG QCD-KMS branch

## Objective

Design a direct numerical test of the one unresolved premise of EXP-100:

\[
\Delta\rho_{\rm top}(L)
=
\frac{\zeta}{\pi m_{\eta'}L}
X_{\rm QCD}
+
O(L^{-2})
+
O(e^{-m_\pi L}).
\]

The goal is not to fit cosmology.

The goal is to measure or exclude

\[
\boxed{
\zeta_{\rm 4D\,QCD}\simeq0.8
}
\]

in real QCD.

---

## 1. Ensembles

Use physical or near-physical

\[
N_f=2+1
\]

QCD.

At each lattice spacing \(a\), generate matched ensembles with the same:

- bare couplings;
- quark masses;
- action;
- temporal aspect ratio chosen to represent zero temperature;

and vary only the spatial physical size.

Target lengths:

\[
\boxed{
L=
2.5,\ 3,\ 4,\ 5,\ 6,\ 8\ {\rm fm}
}
\]

or the largest practical subset spanning at least a factor of two in \(L\).

Repeat at multiple lattice spacings to separate continuum and finite-volume effects.

---

## 2. Primary topological observables

Measure:

1. topological susceptibility
   \[
   \chi_t(L)=\langle Q^2\rangle/V_4;
   \]
2. fourth cumulant / \(b_2(L)\);
3. topological-sector partition-weight ratios when computationally feasible;
4. gradient-flow definitions at matched physical flow time.

The absolute vacuum energy is normalization dependent, so the most robust accessible test is the \(L\)-dependence of the \(\theta\)-dependent free energy,

\[
E(\theta,L)-E(0,L).
\]

A topological Casimir contribution must induce a consistent power-law signature in the \(\theta\)-dependent sector, not merely in an arbitrary additive vacuum constant.

---

## 3. Competing asymptotic models

Preregister three fits.

### Model E — standard gapped/ChPT behavior

\[
{\cal O}(L)
=
{\cal O}_\infty
+
C_E\,F_{\rm ChPT}(m_\pi L),
\]

with

\[
F_{\rm ChPT}
\sim
e^{-m_\pi L}
(m_\pi L)^{-p}
\]

at large \(L\).

### Model V — fixed-topology artifact

\[
{\cal O}(L)
=
{\cal O}_\infty
+
\frac{C_V}{V_4}
+
\cdots.
\]

### Model P — LTG/topological-Casimir candidate

\[
\boxed{
{\cal O}(L)
=
{\cal O}_\infty
+
\frac{C_1}{L}
+
\frac{C_2}{L^2}
+
C_EF_{\rm ChPT}(m_\pi L).
}
\]

The decisive parameter is

\[
C_1.
\]

---

## 4. Mapping to zeta

For the vacuum-energy form,

\[
C_1
=
\boxed{
\frac{\zeta X_{\rm QCD}}
{\pi m_{\eta'}}
}.
\]

Thus

\[
\boxed{
\zeta
=
\frac{\pi m_{\eta'} C_1}
{X_{\rm QCD}}.
}
\]

For \(\chi_t\) or another \(\theta\)-derivative observable, the mapping of \(C_1\) to \(\zeta\) must be derived from the same microscopic topological effective action **before looking at the lattice fit**.

Do not infer the map post hoc.

---

## 5. Numerical target

For

\[
\zeta=0.825,
\]

the predicted vacuum-energy correction is approximately

\[
\boxed{
\Delta\rho_{\rm top}(4\,{\rm fm})
\simeq
1.04\times10^6\ {\rm MeV}^4
}
\]

and

\[
\boxed{
\Delta\rho_{\rm top}(6\,{\rm fm})
\simeq
6.96\times10^5\ {\rm MeV}^4.
}
\]

The corresponding fourth-root scales are

\[
\boxed{
32.0\ {\rm MeV}
}
\]

and

\[
\boxed{
28.9\ {\rm MeV}.
}
\]

These numbers make the finite-volume hypothesis testable in principle.

---

## 6. Blind classification

Define the outcome before inspecting the result.

### PASS

A continuum-stable nonzero \(1/L\) coefficient is preferred over the standard exponential/\(1/V_4\) description and maps prospectively to

\[
0.5\lesssim\zeta\lesssim1.2.
\]

### TENSION

A \(1/L\) coefficient is present but yields

\[
0.1\lesssim|\zeta|<0.5
\]

or

\[
|\zeta|>1.2
\]

with stable significance.

### FAIL

The continuum result is consistent with

\[
\boxed{
|\zeta|<0.1
}
\]

at the preregistered confidence level, or the apparent \(1/L\) term disappears under continuum/volume/topology controls.

### PRE-SCIENCE FAIL

The ensembles do not reach a volume/continuum regime that separates

\[
1/L,\quad1/V_4,\quad e^{-m_\pi L}.
\]

---

## 7. Critical controls

The test must control:

- topology freezing;
- finite topological sampling;
- continuum extrapolation;
- aspect-ratio dependence;
- boundary conditions;
- gradient-flow scale;
- chiral finite-volume corrections;
- autocorrelation of \(Q\);
- fixed-sector \(1/V_4\) contamination.

A claimed \(1/L\) signal is invalid if it is attributable to any of these.

---

## 8. Why this test is decisive for LTG

EXP-100 uses no observed cosmological scale, but its hierarchy comes entirely from

\[
\rho_X\propto H\Lambda_{\rm QCD}^3.
\]

The proposed lattice gate tests the microscopic origin of that linear infrared dependence.

Therefore:

\[
\boxed{
\text{EXP-102 PASS}
\Rightarrow
\text{EXP-100 becomes a serious microphysical hierarchy candidate};
}
\]

\[
\boxed{
\text{EXP-102 FAIL}
\Rightarrow
\text{the QCD-KMS independent }10^{122}\text{ route is closed}.
}
\]

## Status

\[
\boxed{\text{PREREGISTERED TEST DESIGN; NOT YET EXECUTED}.}
\]
