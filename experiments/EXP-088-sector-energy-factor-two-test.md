# EXP-088 — Entropy detailed balance versus quasi-local energy: the de Sitter factor-of-two test

## Objective

Check whether the sector-transition ratio of EXP-087 can be reproduced by treating the positive Misner-Sharp horizon energy as an ordinary thermal energy in a Boltzmann factor.

This is a consistency test of the physical meaning of the unified LTG formula.

---

## 1. Conditional horizon spectrum

Let

\[
\mathcal N_n=\alpha n.
\]

For de Sitter,

\[
R_n
=
\sqrt{2\alpha n}\,\ell_P.
\]

The positive quasi-local horizon energy is

\[
\boxed{
E_n
=
E_P
\sqrt{\frac{\alpha n}{2}}.
}
\]

The Gibbons-Hawking thermal energy is

\[
\boxed{
k_BT_n
=
\frac{E_P}
{2\pi\sqrt{2\alpha n}}.
}
\]

---

## 2. Adjacent energy gap

For large \(n\),

\[
\Delta E_n
=
E_{n+1}-E_n
\approx
\frac{dE}{dn}.
\]

Therefore

\[
\Delta E_n
\approx
\frac{\alpha E_P}
{2\sqrt{2\alpha n}}.
\]

Divide by the horizon thermal energy:

\[
\boxed{
\frac{\Delta E_n}{k_BT_n}
\to
\pi\alpha.
}
\]

So an ordinary Boltzmann factor based only on \(E_{\rm MS}\) would give a neighboring suppression of order

\[
e^{-\pi\alpha}.
\]

---

## 3. Entropy detailed balance

But the actual horizon entropy difference is

\[
\frac{\Delta S}{k_B}
=
2\pi\alpha.
\]

Thus dS detailed balance gives

\[
\boxed{
\frac{\Gamma_+}{\Gamma_-}
=
e^{2\pi\alpha},
}
\]

which contains twice the exponent obtained from the naive quasi-local-energy gap.

### Result 088A

\[
\boxed{
\Delta S/k_B
=
2\,\Delta E_{\rm MS}/(k_BT)
}
\]

in the large-\(n\) neighboring-level limit.

---

## 4. Why this is not a contradiction

De Sitter horizon thermodynamics is not an ordinary fixed-volume mechanical system.

For the positive Misner-Sharp/apparent-horizon energy,

\[
E_{\rm MS}=T_HS_H,
\]

not

\[
E=2T S
\]

or the standard extensive Euler relation of an ordinary gas.

The horizon first law contains pressure/work and sign-convention subtleties.

EXP-065 already showed that the positive Misner-Sharp energy is not identical to the canonical internal energy inferred from the Euclidean de Sitter partition function.

Therefore:

\[
\boxed{
\text{sector detailed balance must be based on the full gravitational entropy/action,
not a naive Boltzmann factor using }E_{\rm MS}.
}
\]

---

## 5. Consequence for LTG

The unified equality

\[
E_{\rm geom}\tau
=
\frac{\hbar}{2\pi}\frac{S}{k_B}
\]

does not mean that \(E_{\rm geom}\) can be inserted as an ordinary transition Hamiltonian energy with no work term.

This prevents a false derivation of the sector rates.

### Result 088B

The correct transition variable is the full causal/gravitational action or entropy difference.

The positive quasi-local energy is one member of the structural LTG identity but not by itself the transition free energy.

---

## Terminal classification

### Naive thermal-sector model based on Misner-Sharp gaps

\[
\boxed{\text{FAIL}.}
\]

### Entropy/action detailed balance

\[
\boxed{\text{CONSISTENT}.}
\]

### LTG interpretation

The transition law must remain gravitational/action based, not ordinary-particle Boltzmann dynamics.
