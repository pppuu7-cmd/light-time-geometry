# LTG Research Status v17 — microscopic audit of the QCD hierarchy branch through EXP-121

## Executive result

The QCD route to the huge de Sitter information hierarchy has now been audited deeply enough to separate:

1. what is mathematically exact;
2. what is demonstrated in controlled toy models;
3. what is currently testable in physical QCD;
4. what remains a genuinely new microscopic assumption.

The key scientific correction is:

\[
\boxed{
\text{the specific independent }10^{122}\text{ match is not yet robust.}
}
\]

What is robust is the following narrower statement:

\[
\boxed{
\text{a nonlocal QCD response of order }
H\Lambda_{\rm QCD}^{3}
\text{ would naturally generate an enormous }
10^{120\text{--}122}
\text{ de Sitter information hierarchy.}
}
\]

The exact late scale depends on a dimensionless curved-background topological-response coefficient that has not yet been calculated in real 4D QCD.

---

## 1. Preferred normalization: theta-potential amplitude

To eliminate flavor and GMOR convention ambiguity, define

\[
\boxed{
B_\theta
\equiv
-\epsilon_\theta(0)>0.
}
\]

For two approximately degenerate light flavors at leading chiral order,

\[
B_\theta
\simeq
f_\pi^2m_\pi^2.
\]

The physically clean curved-background response is

\[
\boxed{
\rho_{\rm top}^{dS}
=
\kappa_{\rm dS}
\frac{H}{m_{\eta'}}
B_\theta.
}
\]

This is now the preferred LTG/QCD parameterization.

---

## 2. Flavor-normalization correction

The original Urban-Zhitnitsky formula for one flavor and later multi-flavor versions differ by explicit flavor factors.

The clean finite-size coefficient is

\[
\boxed{
\epsilon_\theta(\theta,L)
=
\left[
1-
\frac{\kappa_{\rm box}}
{m_{\eta'}L}
\right]
\epsilon_\theta(\theta,\infty)
+\cdots.
}
\]

Then

\[
\boxed{
\frac{\chi_t(L)}{\chi_t(\infty)}
=
1-
\frac{\kappa_{\rm box}}
{m_{\eta'}L}
+\cdots.
}
\]

The historical ghost coefficient satisfies, in the leading benchmark,

\[
\boxed{
\kappa_{\rm box}=2c_{\rm ghost}.
}
\]

For two degenerate light flavors,

\[
\boxed{
{\cal C}_{dS}
=
2\kappa_{\rm dS}.
}
\]

The previous direct lattice slope target remains unchanged:

\[
\boxed{
A_\chi
\simeq
0.02705\ {\rm fm}
}
\]

for the old late-scale benchmark.

The corrected dimensionless slope target is

\[
\boxed{
\kappa_{\rm box}
\simeq
0.131
}
\]

if the box-to-de-Sitter geometry transfer is unity.

---

## 3. EXP-104 — prospective theta mapping

A generic finite-size correction

\[
\Delta{\cal E}(\theta,L)
=
\frac1L
\left[
C_0+\frac12C_2\theta^2+\cdots
\right]
\]

has an identifiability problem:

- cosmology depends on \(C_0\);
- topological susceptibility measures \(C_2\).

Therefore a lattice susceptibility slope does not determine the cosmological vacuum-energy coefficient unless the theta dependence is specified microscopically.

Under a deformed-QCD-inspired common-amplitude hypothesis,

\[
\boxed{
\chi_t(L)/\chi_t(\infty)
=
1-\kappa_{\rm box}/(m_{\eta'}L)+\cdots.
}
\]

This makes the branch prospectively falsifiable.

---

## 4. EXP-106/109 — correlated Ward-identity signature

The original Veneziano-ghost proposal naturally links finite-size changes of

\[
\chi_t
\]

to changes of the chiral condensate through the Ward identity.

Thus the strongest physical-QCD signature is not an isolated susceptibility shift but approximately

\[
\boxed{
A_\chi
\simeq
A_\Sigma
\simeq
A_{M_\pi^2F_\pi^2},
}
\]

while

\[
\boxed{
A_{\chi/(M_\pi^2F_\pi^2)}
\simeq0.
}
\]

If the entire theta potential is only amplitude-rescaled, also

\[
\boxed{
A_{b_2}\simeq0.
}
\]

Therefore a dedicated lattice test should measure the slope vector, not a single ratio.

---

## 5. EXP-108 — published pure-SU(3) reanalysis

A seven-volume 2026 pure-Yang-Mills susceptibility dataset was re-fit.

A pure

\[
1/L
\]

finite-volume law gives approximately

\[
\boxed{
\chi^2\simeq544/4,
}
\]

and fails badly.

The ordinary exponential form gives

\[
ma\simeq0.902
\]

with excellent fit quality and reproduces the published glueball-scale result.

Allowing the published exponential contribution plus an additional \(1/L\) tail gives

\[
\boxed{
A_{\rm YM}
=
(-0.0003\pm0.0142)\ {\rm fm}.
}
\]

Thus:

\[
\boxed{
\text{dominant }1/L\text{ physics is ruled out in this pure-YM dataset;}
}
\]

but

\[
\boxed{
\text{a small additional tail at the full-QCD target scale is not decisively excluded.}
}
\]

Pure Yang-Mills does not supply the light-quark/\(\eta'\) mapping required by the QCD-dark-energy proposal.

---

## 6. EXP-110 — existing full-QCD sensitivity gap

Existing matched-volume full-QCD susceptibility data have percent-to-tens-of-percent uncertainties.

The LTG target between representative lattice volumes is only a few tenths of a percent.

Therefore currently located full-QCD datasets are not precise enough to provide a decisive pass/fail.

A dedicated multi-volume, multi-spacing physical-QCD calculation is required.

---

## 7. EXP-111/112 — exact 122 is normalization sensitive

The original finite-size proposal is naturally written in terms of a global length \(L\).

de Sitter provides several natural scales:

\[
H^{-1},
\qquad
\frac{\pi}{2H},
\qquad
\frac{\pi}{H},
\qquad
\frac{2\pi}{H}.
\]

The KMS circumference

\[
2\pi/H
\]

is an exact thermal-geometric fact, but controlled deformed-QCD Casimir calculations do not identify their large spatial finite-size scale with that thermal circumference.

Therefore:

\[
\boxed{
L_{\rm QCD}=2\pi/H
}
\]

is not derived.

The hierarchy is extremely sensitive to the effective coefficient because

\[
\ln D_{\rm tot}
\propto
\kappa^{-2}.
\]

Thus the exact decimal exponent \(122\) is not presently normalization robust.

---

## 8. EXP-113/117 — covariant microscopic target

Avoid arbitrary infrared lengths entirely.

Define

\[
\boxed{
\rho_{\rm top}^{dS}
=
\kappa_{\rm dS}
\frac{H}{m_{\eta'}}
B_\theta.
}
\]

Then Friedmann closure gives

\[
\boxed{
H_*
=
\kappa_{\rm dS}
\frac{B_\theta}
{3m_{\eta'}\bar M_P^2}.
}
\]

The LTG global capacity is

\[
\boxed{
\ln D_{\rm tot}
=
72\pi^2
\frac{
m_{\eta'}^2\bar M_P^6
}{
\kappa_{\rm dS}^2B_\theta^2
}.
}
\]

For the two-light-flavor benchmark, matching the previous late-scale comparison requires approximately

\[
\boxed{
\kappa_{\rm dS}\simeq0.131.
}
\]

The true predictive chain is

\[
\boxed{
\kappa_{\rm box}
\xrightarrow{{\cal T}_{\rm geom}}
\kappa_{\rm dS}.
}
\]

Both factors must be independently derived.

---

## 9. EXP-114 — local-EFT no-go

An ordinary analytic local generally covariant effective action of gapped QCD generates

\[
R\sim H^2,
\quad
R^2\sim H^4,
\quad\ldots
\]

not

\[
H\Lambda_{\rm QCD}^3.
\]

Therefore the required linear curvature response must be genuinely:

- nonlocal;
- global/topological;
- state dependent;
- boundary sensitive;
- or nonanalytic.

This is a strong diagnostic.

The mechanism cannot be replaced by an ordinary local curvature correction.

---

## 10. EXP-118 — Rindler support downgraded

A 2010 Rindler calculation argued that unphysical gauge/ghost modes produce extra horizon-sensitive vacuum energy.

A later complete canonical Maxwell quantization including Faddeev-Popov ghosts found exact cancellation of the nonphysical bulk thermal contributions and restored gauge invariance in 1+1 dimensions.

Therefore ordinary Rindler gauge-fixing ghosts do not provide independent evidence for a nonzero QCD de Sitter coefficient.

This does not refute the Veneziano contact term, which is a different topological/non-Abelian object.

Classification:

\[
\boxed{
\text{QCD branch survives, but Rindler support is removed from the evidence chain.}
}
\]

---

## 11. EXP-119 — controlled 2D support and its limit

The massive Schwinger model provides a controlled example in which a gapped gauge theory has topological/global finite-size sensitivity scaling as

\[
1/L.
\]

Thus power-law IR sensitivity is possible.

But the exact 2D work does not give a universal coefficient transporting a torus finite-size effect into real 4D QCD on de Sitter.

The literature on finite-temperature/finite-size Schwinger models also distinguishes the thermal circumference and the spatial length; physical quantities can depend on both separately.

Therefore:

\[
\boxed{
{\cal T}_{\rm geom}=1
}
\]

is not justified by the 2D analogy.

---

## 12. EXP-120 — covariant square-root-curvature alternative

A second conditional closure removes the arbitrary infrared-length choice by introducing

\[
\boxed{
S
=
\int\sqrt{-g}
\left[
\frac{\bar M_P^2}{2}R
-
\mu^3\sqrt{\frac{R}{12}}
\right],
}
\]

where

\[
\mu^3
=
\kappa_R
\frac{B_\theta}{m_{\eta'}}.
\]

This is the known functional class

\[
f(R)=R-2\alpha\sqrt R
\]

with a new QCD interpretation of the coefficient.

The nonzero constant-curvature solution is

\[
\boxed{
H_*
=
\frac{\mu^3}{4\bar M_P^2}
=
\kappa_R
\frac{B_\theta}
{4m_{\eta'}\bar M_P^2}.
}
\]

At the fixed point,

\[
f_R=\frac23>0,
\]

\[
f_{RR}>0,
\]

and

\[
\boxed{
m_s^2=12H_*^2>0.
}
\]

Thus the de Sitter point is stable under the standard scalaron criterion.

---

## 13. EXP-121 — observational risk of the square-root branch

The square-root model approaches GR at high curvature:

\[
F(R)=1-\alpha/\sqrt R\to1.
\]

But at the late de Sitter endpoint,

\[
\boxed{
F_*=2/3.
}
\]

Therefore it predicts substantial late-time running of the effective gravitational normalization and a cosmological-range scalaron.

It must pass:

- expansion-history data;
- growth;
- lensing;
- local/high-density tests;
- standard-siren GW damping.

Modern viable \(f(R)\) analyses show that these observables are highly sensitive to much smaller deviations from the GR limit in commonly studied models.

Thus the square-root branch is:

\[
\boxed{
\text{mathematically promising but observationally high-risk}.
}
\]

It is also nonanalytic at \(R=0\), so it should presently be treated as a late-time effective branch.

---

# Strongest current QCD result

The correct current statement is no longer

> QCD independently predicts \(10^{122}\).

It is:

\[
\boxed{
\text{if real QCD possesses a nonlocal topological curvature response }
\kappa_{\rm dS}=O(10^{-1}),
\text{ QCD + gravity naturally generate the required enormous late-time hierarchy.}
}
\]

For the simplest fluid/topological closure, the comparison target is

\[
\boxed{
\kappa_{\rm dS}\simeq0.131.
}
\]

For the covariant square-root-curvature closure, the corresponding coefficient is

\[
\boxed{
\kappa_R\simeq0.175.
}
\]

Neither is currently derived from first principles.

---

# Current decisive experiments

The QCD branch now has two clean independent tests.

## Microscopic flat-space gate

Measure

\[
\boxed{
\kappa_{\rm box}
=
-m_{\eta'}
\lim_{L\to\infty}
L
\left[
\chi_t(L)/\chi_t(\infty)-1
\right]
}
\]

together with correlated slopes of

\[
\chi_t,\quad
\Sigma,\quad
M_\pi^2F_\pi^2,\quad
b_2.
\]

## Curved-background gate

Compute directly

\[
\boxed{
\kappa_{\rm dS}
}
\]

or the nonanalytic square-root coefficient from

\[
W_{\rm top}[g,\theta]
\]

on de Sitter / Euclidean \(S^4\).

No hand-selected infrared length is allowed.

---

# Novelty status

The ingredients remain heavily connected to prior art:

- Veneziano/Kogut-Susskind topology;
- Schwinger-model finite-size effects;
- deformed-QCD topological Casimir effects;
- \(f(R)\) square-root gravity;
- horizon thermodynamics.

The LTG contribution is the systematic chain connecting them to:

\[
\boxed{
\text{QCD theta information}
\to
\text{nonlocal curvature response}
\to
H_*
\to
S_{\rm dS}
\to
D_{\rm tot}.
}
\]

This chain is now falsifiable and convention-clean, but not yet experimentally or microscopically verified.
