# EXP-093 — Finite total Hilbert capacity and the late de Sitter scale

## Objective

EXP-089 showed that exact detailed balance on an unbounded entropy tower drives

\[
n\to\infty,
\qquad
\Lambda\to0^+.
\]

Test the minimal alternative:

\[
\boxed{
\dim\mathcal H_{\rm tot}=D_{\rm tot}<\infty.
}
\]

Assume the q-ary LTG sectors of EXP-090 are effective accessible subspaces with

\[
\dim\mathcal H_n=q^n.
\]

---

## 1. Maximum sector

Because

\[
q^n\le D_{\rm tot},
\]

the sector index is bounded by

\[
\boxed{
n\le
n_{\max}
=
\left\lfloor
\frac{\ln D_{\rm tot}}{\ln q}
\right\rfloor.
}
\]

If the largest sector saturates the total capacity,

\[
q^{n_{\max}}
\simeq
D_{\rm tot},
\]

then

\[
\boxed{
n_{\max}\ln q
\simeq
\ln D_{\rm tot}.
}
\]

---

## 2. Late horizon scale

EXP-090 gives the q-ary de Sitter spectrum

\[
H_n^2
=
\frac{\pi c^5}
{G\hbar\,n\ln q}.
\]

At the maximum sector,

\[
H_*^2
=
\frac{\pi c^5}
{G\hbar\,n_{\max}\ln q}.
\]

Using

\[
n_{\max}\ln q
\simeq
\ln D_{\rm tot},
\]

we obtain

\[
\boxed{
H_*^2
=
\frac{\pi c^5}
{G\hbar\ln D_{\rm tot}}.
}
\]

Equivalently,

\[
\boxed{
\Lambda_*
=
\frac{3\pi c^3}
{G\hbar\ln D_{\rm tot}}.
}
\]

### Result 093A

A finite total Hilbert-space capacity selects a finite minimum positive curvature if the entropy-detailed-balance dynamics saturates the largest accessible sector.

---

## 3. q cancels

The endpoint depends only on

\[
\ln D_{\rm tot},
\]

not on the microscopic q-ary factorization.

Therefore:

\[
\boxed{
\text{the late de Sitter scale is insensitive to whether the elementary information unit is binary, ternary, etc.}
}
\]

provided the same total Hilbert dimension is reached.

This separates:

- microscopic sector bookkeeping \(q\);
- global capacity \(D_{\rm tot}\).

---

## 4. Relation to de Sitter entropy

The maximal entropy is

\[
S_{\max}
=
k_B\ln D_{\rm tot}.
\]

But de Sitter entropy is

\[
\frac{S_{\rm dS}}{k_B}
=
\frac{\pi c^5}
{G\hbar H_*^2}.
\]

Therefore Result 093A is exactly

\[
\boxed{
S_{\max}=S_{\rm dS}.
}
\]

### Result 093B

The finite-capacity endpoint is not a new formula.

It is the finite-state interpretation of de Sitter entropy.

---

## 5. Detailed-balance endpoint

For a finite tower

\[
1\le n\le n_{\max},
\]

the equilibrium weights satisfy

\[
P_n\propto q^n.
\]

Therefore the late distribution is strongly concentrated near

\[
n_{\max}.
\]

Thus finite total capacity plus detailed balance gives a thermodynamic mechanism that populates the largest-capacity sector.

But the numerical value

\[
D_{\rm tot}
\]

remains an input.

---

## 6. Prior-art boundary

The possibility that de Sitter entropy counts a finite number of physical states has a substantial literature, including finite-dimensional de Sitter quantum models and recent arguments that finite causal-diamond entropy should correspond to finite physical-state number.

This is not settled universally in quantum gravity, but it is established as a serious research program.

### Classification

\[
\boxed{
\text{FINITE-CAPACITY SELECTION: STRUCTURAL PASS / PRIOR-ART INTERPRETATION}.
}
\]

---

## 7. Remaining problem

The cosmological-constant problem is now equivalent to

\[
\boxed{
\text{what microscopic/global principle fixes }D_{\rm tot}?
}
\]

The q-ary transition law cannot answer this.

A genuine LTG advance requires deriving

\[
D_{\rm tot}
\]

from an earlier/global causal structure without using \(H_*\) or \(\Lambda_*\) as input.
