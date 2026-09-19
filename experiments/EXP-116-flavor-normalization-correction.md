# EXP-116 — Flavor-normalization correction and convention-independent theta-amplitude coefficient

## Objective

Audit the flavor normalization used in EXP-100, EXP-111, EXP-113 and EXP-115.

The original Urban-Zhitnitsky derivation first writes the final vacuum-energy formula for one light flavor,

\[
\rho_\Lambda
=
c\frac{2H}{m_{\eta'}}
|m_q\langle\bar q q\rangle|.
\]

For \(N_f\) degenerate flavors the later literature writes

\[
\boxed{
\rho_\Lambda
=
\frac{2N_f cH}{m_{\eta'}}
|m_q\langle\bar q q\rangle|.
}
\]

Some previous LTG bookkeeping mixed the one-flavor coefficient with a two-flavor GMOR substitution.

The purpose of this gate is to remove that ambiguity completely.

---

## 1. Define the physical theta-potential amplitude

Let

\[
\boxed{
B_\theta
\equiv
-\epsilon_\theta(0)
>0
}
\]

be the positive magnitude of the theta-dependent QCD vacuum potential at \(\theta=0\), after the same Minkowski subtraction used in the finite-size construction.

For \(N_f\) degenerate light quarks at leading chiral order,

\[
\epsilon_\theta(\theta)
=
-N_f X_q
\cos\left(\frac{\theta}{N_f}\right),
\]

where

\[
X_q
\equiv
|m_q\langle\bar q q\rangle|.
\]

Therefore

\[
\boxed{
B_\theta=N_fX_q.
}
\]

The topological susceptibility is

\[
\chi_t
=
\left.
\frac{\partial^2\epsilon_\theta}{\partial\theta^2}
\right|_{\theta=0}
=
\frac{X_q}{N_f},
\]

so

\[
\boxed{
B_\theta=N_f^2\chi_t
}
\]

for the equal-mass leading-order benchmark.

For physical unequal \(u,d,s\) masses, use the full measured/calculated theta potential rather than this simplified identity.

---

## 2. Define one convention-independent finite-size coefficient

Assume the finite-size topological effect rescales the complete theta-dependent amplitude at leading order:

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

The same coefficient produces the finite-size vacuum shift

\[
\boxed{
\Delta\rho_\theta(L)
=
\frac{\kappa_{\rm box}}
{m_{\eta'}L}
B_\theta.
}
\]

This is the clean observable definition of the coefficient.

---

## 3. Relation to the original ghost parameter c

The original paper parameterizes the ghost matrix element as

\[
\frac{\Delta\lambda_{YM}}{\lambda_{YM}}
=
-c\frac{1}{m_{\eta'}L}.
\]

Because the relevant susceptibility amplitude is quadratic in the ghost matrix element at the level of the leading variation,

\[
\frac{\Delta\chi_t}{\chi_t}
\simeq
-2c\frac{1}{m_{\eta'}L}.
\]

Therefore

\[
\boxed{
\kappa_{\rm box}=2c.
}
\]

For \(L=H^{-1}\),

\[
\Delta\rho_\theta
=
\kappa_{\rm box}
\frac{H}{m_{\eta'}}
B_\theta.
\]

Using

\[
B_\theta=N_fX_q,
\]

gives

\[
\boxed{
\rho_\Lambda
=
2N_f c
\frac{H}{m_{\eta'}}
X_q,
}
\]

which matches the multi-flavor formula.

### Result 116A

The flavor factor and the factor of two from the ghost-amplitude variation are both absorbed exactly by the invariant pair

\[
\boxed{
(B_\theta,\kappa).
}
\]

---

## 4. Relation to EXP-100 notation

For the two-degenerate-light-flavor GMOR benchmark,

\[
B_\theta
=
2X_q
\simeq
f_\pi^2m_\pi^2.
\]

EXP-100 wrote

\[
\rho_X
=
\zeta
\frac{Hf_\pi^2m_\pi^2}
{2\pi m_{\eta'}}.
\]

Therefore

\[
\boxed{
\kappa
=
\frac{\zeta}{2\pi}.
}
\]

The earlier benchmark

\[
\zeta_{\rm target}\simeq0.825
\]

therefore means

\[
\boxed{
\kappa_{\rm target}\simeq0.131.
}
\]

The original ghost parameter is then

\[
\boxed{
c_{\rm target}
=
\frac{\kappa_{\rm target}}{2}
\simeq0.066.
}
\]

This supersedes the \(c\simeq0.131\) identification written in EXP-111/113/115, which omitted the flavor/fractional-amplitude factor in that particular comparison.

---

## 5. Crucially, the direct lattice target is unchanged

The observable fractional-slope length is

\[
A_\chi
=
\frac{\kappa\hbar c}
{m_{\eta'}}.
\]

Thus the previous direct target

\[
\boxed{
A_\chi\simeq0.02705\ {\rm fm}
}
\]

is unchanged.

What changes is only the interpretation of that slope in terms of the historical coefficient \(c\):

\[
\boxed{
\frac{m_{\eta'}A_\chi}{\hbar c}
=
\kappa
=
2c.
}
\]

Therefore the EXP-104/108/109/110 lattice-signature calculations remain numerically valid.

---

## 6. Relation to the EXP-113 covariant coefficient

EXP-113 defined

\[
\rho_{\rm top}^{\rm dS}
=
\mathcal C_{\rm dS}
H
\frac{X_q}{m_{\eta'}}.
\]

For \(N_f\) degenerate flavors,

\[
B_\theta=N_fX_q,
\]

so

\[
\boxed{
\mathcal C_{\rm dS}
=
N_f\kappa_{\rm dS}.
}
\]

For the \(N_f=2\) benchmark,

\[
\boxed{
\mathcal C_{\rm dS,target}
\simeq0.263
}
\]

corresponds to

\[
\boxed{
\kappa_{\rm dS,target}
\simeq0.131.
}
\]

Thus the invariant cosmological target itself is unchanged.

---

## 7. Corrected hierarchy of coefficients

The clean hierarchy is now

\[
\boxed{
c_{\rm ghost}
\longrightarrow
\kappa=2c_{\rm ghost}
\longrightarrow
\mathcal C_{\rm dS}=N_f\kappa
}
\]

for the degenerate-flavor benchmark.

For \(N_f=2\),

\[
\boxed{
\mathcal C_{\rm dS}=4c_{\rm ghost}.
}
\]

---

## Terminal classification

### Previous lattice slope target

\[
\boxed{\text{UNCHANGED}.}
\]

### Previous \(10^{122}\) QCD-KMS benchmark

\[
\boxed{\text{UNCHANGED as a function of }\zeta.}
\]

### Historical coefficient mapping

\[
\boxed{\text{CORRECTED by a factor of two}.}
\]

### Preferred future notation

Use

\[
\boxed{
B_\theta,\qquad \kappa
}
\]

instead of \(N_f\)-dependent \(m_q\langle\bar q q\rangle\) conventions whenever possible.
