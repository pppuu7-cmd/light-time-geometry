# EXP-104 — Prospective theta-dependent mapping from lattice susceptibility to the LTG QCD-KMS coefficient

## Objective

Turn EXP-102 into a genuinely prospective lattice test.

The QCD-KMS branch requires a finite-size vacuum-energy correction

\[
\Delta\rho_{\rm vac}(L)
=
\frac{\zeta_{\rm LTG}}{\pi m_{\eta'}L}
X_{\rm QCD}
+
O(L^{-2}),
\]

with

\[
X_{\rm QCD}
\simeq
\frac12 f_\pi^2m_\pi^2.
\]

A lattice calculation cannot infer \(\zeta_{\rm LTG}\) from an arbitrary post-hoc finite-volume observable.

We therefore derive the mapping to the theta-dependent free energy before any fit.

---

## 1. General identifiability problem

Write the finite-size correction to the QCD vacuum energy as

\[
\Delta{\cal E}(\theta,L)
=
\frac{1}{L}
\left[
C_0
+
\frac{C_2}{2}\theta^2
+
\frac{C_4}{4!}\theta^4
+\cdots
\right]
+
O(L^{-2}).
\]

The cosmological branch is controlled by

\[
\boxed{
C_0
=
\frac{\zeta_{\rm LTG}X_{\rm QCD}}
{\pi m_{\eta'}}.
}
\]

But the topological susceptibility measures

\[
\chi_t(L)
=
\left.
\frac{\partial^2{\cal E}(\theta,L)}
{\partial\theta^2}
\right|_{\theta=0},
\]

so

\[
\boxed{
\chi_t(L)-\chi_t(\infty)
=
\frac{C_2}{L}
+\cdots.
}
\]

Therefore:

\[
\boxed{
C_2
\text{ does not determine }
C_0
\text{ without a microscopic theta-shape relation}.
}
\]

### Result 104A — identifiability no-go

A generic \(1/L\) effect in \(\chi_t\) is not enough to determine the gravitationally relevant vacuum-energy coefficient.

The theta dependence must be specified prospectively.

---

## 2. Deformed-QCD benchmark supplies a theta-shape relation

In controlled deformed Yang-Mills/QCD, the topological vacuum energy has the form

\[
{\cal E}_{\rm dQCD}(\theta)
=
-\frac{N_c\zeta_{\rm mon}}{L_c}
\cos\left(
\frac{\theta}{N_c}
\right)
\]

on the lowest branch.

The finite-size correction modifies the monopole fugacity,

\[
\boxed{
\zeta_{\rm mon}({\mathbb L})
=
\zeta_{\rm mon}(\infty)
\left[
1-\frac{1}{2m_W{\mathbb L}}
+O({\mathbb L}^{-2})
\right].
}
\]

Because the same amplitude multiplies the entire theta potential, the vacuum energy and all theta derivatives acquire the same fractional \(1/{\mathbb L}\) correction.

In particular,

\[
\boxed{
\frac{\chi_t({\mathbb L})}
{\chi_t(\infty)}
=
1-\frac{1}{2m_W{\mathbb L}}+\cdots.
}
\]

This is the controlled toy-model precedent for the transfer rule below.

---

## 3. Minimal physical-QCD transfer hypothesis

Preregister the physical-QCD analogue:

\[
\boxed{
{\cal E}_{\rm top}(\theta,L)
=
\left[
1-\epsilon_L
\right]
{\cal E}_{\rm top}(\theta,\infty)
+
O(L^{-2},e^{-m_\pi L}),
}
\]

where

\[
\boxed{
\epsilon_L
=
\frac{\zeta_{\rm LTG}}
{2\pi m_{\eta'}L}.
}
\]

At leading chiral order,

\[
{\cal E}_{\rm top}(0,\infty)
\simeq
-f_\pi^2m_\pi^2
=
-2X_{\rm QCD}.
\]

Therefore the finite-size shift at theta zero is

\[
\Delta\rho_{\rm vac}(L)
=
-\epsilon_L{\cal E}_{\rm top}(0,\infty)
\]

which gives exactly

\[
\boxed{
\Delta\rho_{\rm vac}(L)
=
\frac{\zeta_{\rm LTG}}
{\pi m_{\eta'}L}
X_{\rm QCD}.
}
\]

Thus the same transfer hypothesis reproduces EXP-100 by construction and fixes the theta dependence prospectively.

---

## 4. Direct susceptibility prediction

Differentiate twice with respect to theta.

Because the entire topological amplitude is rescaled,

\[
\boxed{
\chi_t(L)
=
\chi_t(\infty)
\left[
1-
\frac{\zeta_{\rm LTG}}
{2\pi m_{\eta'}L}
\right]
+
O(L^{-2},e^{-m_\pi L}).
}
\]

Therefore

\[
\boxed{
\zeta_{\rm LTG}
=
-2\pi m_{\eta'}
\lim_{L\to\infty}
L
\left[
\frac{\chi_t(L)}
{\chi_t(\infty)}
-1
\right].
}
\]

This is the desired prospective

\[
\boxed{
C_1\longrightarrow\zeta_{\rm LTG}
}
\]

mapping.

In conventional lattice units with \(m_{\eta'}\) in MeV and \(L\) in fm,

\[
\boxed{
\frac{\chi_t(L)}{\chi_t(\infty)}-1
=
-
\frac{
\zeta_{\rm LTG}\,\hbar c
}{
2\pi m_{\eta'}L
}.
}
\]

---

## 5. Sign prediction

For the positive vacuum-energy shift required by EXP-100,

\[
\zeta_{\rm LTG}>0.
\]

Therefore

\[
\boxed{
\chi_t(L)<\chi_t(\infty)
}
\]

at finite \(L\).

The model predicts a **negative susceptibility tail** approaching the infinite-volume value from below.

This sign is inherited from the deformed-QCD mechanism: finite size lowers the topological fugacity/contact amplitude while making the negative vacuum energy less negative.

---

## 6. Numerical slope target

With

\[
m_{\eta'}=957.78\ {\rm MeV},
\]

\[
\hbar c=197.32698\ {\rm MeV\,fm},
\]

and

\[
\zeta_{\rm LTG}=0.825,
\]

define

\[
\boxed{
A_\chi
\equiv
\frac{\zeta_{\rm LTG}\hbar c}
{2\pi m_{\eta'}}
=
0.02705\ {\rm fm}.
}
\]

Then

\[
\boxed{
\frac{\chi_t(L)}{\chi_t(\infty)}
=
1-\frac{0.02705\ {\rm fm}}{L}
+\cdots.
}
\]

Predicted deficits are:

| L [fm] | fractional shift in \(\chi_t\) |
|---:|---:|
| 2.5 | \(-1.082\%\) |
| 3 | \(-0.902\%\) |
| 4 | \(-0.676\%\) |
| 5 | \(-0.541\%\) |
| 6 | \(-0.451\%\) |
| 8 | \(-0.338\%\) |

These are the direct lattice targets.

---

## 7. Higher theta cumulants

Write the theta-dependent free energy as

\[
f(\theta)
=
\frac12\chi_t\theta^2
\left[
1+b_2\theta^2+b_4\theta^4+\cdots
\right].
\]

If the finite-size effect is a pure common-amplitude rescaling, then every unnormalized theta cumulant receives the same factor,

\[
c_{2n}(L)
=
(1-\epsilon_L)c_{2n}(\infty)+\cdots.
\]

Therefore normalized shape coefficients satisfy

\[
\boxed{
b_2(L)
=
b_2(\infty)
+
O(L^{-2},e^{-m_\pi L}),
}
\]

and similarly for higher normalized \(b_{2n}\).

### Result 104B — null-control prediction

The minimal EXP-100 transfer hypothesis predicts:

\[
\boxed{
\chi_t:
\text{ nonzero }1/L\text{ tail},
}
\]

but

\[
\boxed{
b_2:
\text{ no leading }1/L\text{ tail}.
}
\]

This is a strong signal-plus-null-control pair.

---

## 8. What if b2 has a 1/L term?

Then the finite-size topological effect changes not only the amplitude but also the theta shape.

In that case,

\[
C_0,\ C_2,\ C_4,\ldots
\]

are independent microscopic coefficients.

A susceptibility fit alone cannot recover the cosmological \(C_0\).

The correct observable becomes the full finite-volume theta free-energy function.

Even then, an additive theta-independent \(C_0/L\) remains invisible to theta derivatives unless a microscopic action relates it to the theta-dependent coefficients.

### Result 104C

The deformed-QCD-inspired amplitude factorization is not optional bookkeeping.

It is the exact extra hypothesis that makes EXP-100 lattice-falsifiable through \(\chi_t\).

---

## 9. Terminal classification

### Generic lattice observable to cosmological zeta mapping

\[
\boxed{\text{NO-GO without a theta-shape model}.}
\]

### Deformed-QCD-inspired amplitude transfer

\[
\boxed{\text{PROSPECTIVE MAPPING DERIVED}.}
\]

### Direct target

\[
\boxed{
\chi_t(L)/\chi_t(\infty)
=
1-
\zeta_{\rm LTG}/(2\pi m_{\eta'}L)+\cdots.
}
\]

### Null control

\[
\boxed{
b_2(L)
=
b_2(\infty)+O(L^{-2},e^{-m_\pi L}).
}
\]

## Scientific status

This gate does not prove the \(1/L\) effect exists in physical QCD.

It converts the hypothesis into a specific, non-post-hoc lattice signature.
