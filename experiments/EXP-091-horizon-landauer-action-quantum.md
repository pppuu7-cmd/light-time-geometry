# EXP-091 — Horizon Landauer action quantum

## Objective

Test whether the q-ary sector step of EXP-090 has a natural causal thermodynamic cost and whether the minimal binary sector \(q=2\) is selected by known information thermodynamics.

---

## 1. One q-ary entropy step

EXP-090 gives

\[
\boxed{
\Delta S
=
k_B\ln q.
}
\]

The de Sitter / causal horizon temperature is

\[
\boxed{
k_BT_H
=
\frac{\hbar H}{2\pi}.
}
\]

For a reversible information step,

\[
\Delta Q_{\rm rev}
=
T_H\Delta S.
\]

Therefore

\[
\boxed{
\Delta Q_{\rm rev}
=
\frac{\hbar H}{2\pi}\ln q.
}
\]

---

## 2. Multiply by causal time

For the horizon light/causal time

\[
\tau_H=H^{-1},
\]

we obtain

\[
\boxed{
\Delta Q_{\rm rev}\tau_H
=
\frac{\hbar}{2\pi}\ln q.
}
\]

But the LTG causal-action step from EXP-090 is exactly

\[
\Delta(E_{\rm geom}\tau_{\rm light})
=
\frac{\hbar}{2\pi}\ln q.
\]

Hence

\[
\boxed{
\Delta\mathcal A_{\rm causal}^{\rm rev}
=
T_H\Delta S\,\tau_H
=
\frac{\hbar}{2\pi}\ln q.
}
\]

### Result 091A — horizon Landauer action quantum

The q-ary LTG sector step is exactly the causal-time version of the reversible Landauer information cost evaluated at the horizon temperature.

---

## 3. Binary step

For

\[
q=2,
\]

\[
\boxed{
\Delta S=k_B\ln2
}
\]

and

\[
\boxed{
\Delta\mathcal A_{\rm bit}
=
\frac{\hbar\ln2}{2\pi}.
}
\]

This is the causal action associated with one bit at the horizon temperature over one horizon time.

---

## 4. Does Landauer select q=2?

No.

Landauer's principle for erasing a q-ary symbol gives

\[
Q_{\min}
=
k_BT\ln q.
\]

All integers

\[
q\ge2
\]

are allowed.

Binary encoding is the smallest nontrivial alphabet and therefore the smallest nonzero entropy/action step, but this is an economy/minimality statement, not a theorem of quantum gravity.

### Result 091B

\[
\boxed{
\text{Landauer fixes the cost for a chosen }q;
\text{ it does not select }q.
}
\]

---

## 5. Relation to the global causal action bound

EXP-077 gave

\[
\mathcal A_{\rm causal}
\ge
\hbar\Delta\mathcal N.
\]

For the q-ary sector variable,

\[
\Delta\mathcal N
=
\frac{\ln q}{2\pi}.
\]

Therefore

\[
\boxed{
\mathcal A_{\rm causal}
\ge
\frac{\hbar}{2\pi}\ln q
}
\]

for one elementary capacity step.

The reversible Landauer step saturates this bound.

### Result 091C

The global causal-action inequality and horizon Landauer thermodynamics are mutually consistent.

---

## 6. Novelty status

Landauer information cost and horizon temperature are established.

The exact LTG packaging

\[
\boxed{
\text{one q-ary capacity step}
\Longleftrightarrow
\Delta\mathcal A
=
\frac{\hbar}{2\pi}\ln q
}
\]

is a synthesis, not a new independent thermodynamic law.

---

## Terminal classification

### q-ary causal action quantum

**PASS.**

### Binary \(q=2\) as minimal nontrivial step

**PASS as minimality convention.**

### Binary \(q=2\) uniquely selected by physics

\[
\boxed{\text{FAIL}.}
\]

A microscopic algebra/topology/symmetry is still needed to fix \(q\).
