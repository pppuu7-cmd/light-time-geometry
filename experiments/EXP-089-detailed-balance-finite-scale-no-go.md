# EXP-089 — Detailed-balance sector chain and finite-cosmological-scale no-go

## Objective

Given EXP-087, test whether entropy detailed balance can by itself select a finite late LTG sector.

Use a birth-death chain over

\[
n=1,2,\dots
\]

with neighboring transition rates satisfying

\[
\frac{\Gamma_{n\to n+1}}
{\Gamma_{n+1\to n}}
=
e^{2\pi\alpha}.
\]

---

## 1. Detailed-balance stationary weights

For a reversible Markov chain, detailed balance requires

\[
P_n^{\rm eq}\Gamma_{n\to n+1}
=
P_{n+1}^{\rm eq}
\Gamma_{n+1\to n}.
\]

Therefore

\[
\frac{P_{n+1}^{\rm eq}}
{P_n^{\rm eq}}
=
\frac{\Gamma_{n\to n+1}}
{\Gamma_{n+1\to n}}
=
e^{2\pi\alpha}.
\]

Hence

\[
\boxed{
P_n^{\rm eq}
\propto
e^{2\pi\alpha n}
=
e^{S_n/k_B}.
}
\]

This is the expected microstate-counting equilibrium weight.

---

## 2. Infinite tower

If

\[
n\in\mathbb N
\]

has no upper endpoint,

\[
\sum_{n=1}^\infty
e^{2\pi\alpha n}
\]

diverges.

Therefore the equilibrium distribution cannot be normalized.

### Result 089A

\[
\boxed{
\text{entropy-only detailed balance on an unbounded capacity tower has no finite equilibrium.}
}
\]

The chain is biased toward

\[
n\to\infty,
\]

equivalently

\[
H\to0,
\qquad
\Lambda\to0^+.
\]

---

## 3. Finite maximum capacity

Suppose instead

\[
1\le n\le n_{\max}.
\]

Then

\[
P_n^{\rm eq}
=
\frac{e^{2\pi\alpha n}}
{\sum_{m=1}^{n_{\max}}e^{2\pi\alpha m}}.
\]

Because

\[
e^{2\pi\alpha}\gg1
\]

for the tested spectra, the equilibrium is exponentially concentrated at

\[
\boxed{
n=n_{\max}.
}
\]

Thus a finite late de Sitter scale can be selected only if the global theory already supplies a maximum capacity.

### Result 089B

\[
\boxed{
\text{finite de Sitter selection}
\Longleftrightarrow
\text{finite maximum capacity}
}
\]

for the pure entropy-detailed-balance sector chain.

---

## 4. Relation to the cosmological constant

Under the conditional sector spectrum,

\[
H_n^2
=
\frac{c^5}
{2G\hbar\alpha n}.
\]

Therefore

\[
\boxed{
H_*^2
=
\frac{c^5}
{2G\hbar\alpha n_{\max}}.
}
\]

Equivalently,

\[
\boxed{
\Lambda_*
=
\frac{3c^3}
{2G\hbar\alpha n_{\max}}.
}
\]

The cosmological-constant problem has therefore been sharpened to:

\[
\boxed{
\text{what fixes }n_{\max}?
}
\]

This is stronger than asking which state is preferred once the allowed Hilbert space is already specified.

---

## 5. Barrier prefactors cannot fix equilibrium if detailed balance remains exact

Let

\[
\Gamma_{n\to n+1}
=
\gamma_{n+1/2}e^{+\pi\alpha},
\]

\[
\Gamma_{n+1\to n}
=
\gamma_{n+1/2}e^{-\pi\alpha}.
\]

Any positive symmetric prefactor

\[
\gamma_{n+1/2}
\]

cancels from the detailed-balance ratio.

Therefore barriers can make the evolution arbitrarily slow but do not change

\[
P_n^{\rm eq}\propto e^{S_n/k_B}.
\]

### Result 089C

\[
\boxed{
\text{barrier physics controls timescales, not the entropy-selected endpoint,
as long as detailed balance remains exact.}
}
\]

---

## 6. How to obtain a finite interior peak

At least one assumption must change:

1. the capacity tower terminates at finite \(n_{\max}\);
2. detailed balance is broken by terminals/driving;
3. additional sector weights oppose the entropy growth;
4. the entropy spacing stops growing linearly;
5. transitions cease before equilibrium and cosmic time/history matters.

All are new physical inputs.

---

## 7. Terminal classification

### Transition direction ratio

**FIXED by entropy spacing.**

### Absolute transition time

**UNFIXED.**

### Finite equilibrium on an unbounded tower

\[
\boxed{\text{FAIL}.}
\]

### Finite late de Sitter state under exact detailed balance

Requires

\[
\boxed{
n_{\max}<\infty
}
\]

or another nonequilibrium/global ingredient.

## Strongest consequence

The missing LTG law is now even narrower:

\[
\boxed{
\text{derive a finite maximum generalized-information capacity}
}
\]

or derive a controlled violation of equilibrium detailed balance.

Without that, sector thermodynamics drives the theory toward ever larger horizon capacity and \(\Lambda\to0^+\).
