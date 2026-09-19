# EXP-048 — Does event-horizon causality dynamically select HL = 1?

## Objective

EXP-046 found the conditional de Sitter closure

\[
HL=1,
\qquad
c=1,
\qquad
\Gamma/H=3,
\qquad
w=-1.
\]

This experiment asks the next decisive question:

> Does the future event-horizon geometry itself dynamically drive \(x\equiv HL\) toward 1, or is \(x=1\) merely a boundary condition once de Sitter is already assumed?

---

## 1. Event-horizon kinematics

Define the future event horizon

\[
L(t)
=
a(t)
\int_t^\infty
\frac{dt'}{a(t')}.
\]

Differentiating gives

\[
\boxed{
\dot L=HL-1.
}
\]

Define

\[
x\equiv HL.
\]

Using the e-fold variable

\[
N=\ln a,
\]

we have

\[
x'
\equiv
\frac{dx}{dN}
=
\frac{\dot x}{H}.
\]

Now

\[
\dot x
=
\dot H L+H\dot L.
\]

Therefore

\[
x'
=
x\frac{\dot H}{H^2}
+x-1.
\]

Define

\[
\epsilon
\equiv
-\frac{\dot H}{H^2},
\]

so

\[
\boxed{
x'
=
x(1-\epsilon)-1.
}
\]

Using

\[
q=-1-\frac{\dot H}{H^2}
=
\epsilon-1,
\]

this becomes

\[
\boxed{
x'=-qx-1.
}
\]

---

## 2. de Sitter test

For exact de Sitter,

\[
q=-1,
\qquad
\epsilon=0.
\]

Then

\[
\boxed{
x'=x-1.
}
\]

The fixed point is

\[
x_*=1.
\]

Linearize:

\[
x=1+\delta.
\]

Then

\[
\delta'=\delta.
\]

Therefore

\[
\delta(N)
=
\delta_0e^N.
\]

So, treated as a local first-order evolution equation,

\[
\boxed{
x=1
}
\]

is not a forward-time stable attractor.

### Result 048A

The local differential identity for the event horizon does **not** dynamically attract generic \(HL\) toward 1.

---

## 3. Why exact de Sitter still has HL = 1

For constant \(H\),

\[
\dot L=HL-1.
\]

The general local solution is

\[
L(t)
=
H^{-1}
+
C e^{Ht}.
\]

But the true event horizon is not defined by an arbitrary local initial condition.

It is defined by the future boundary integral

\[
L(t)
=
a(t)
\int_t^\infty\frac{dt'}{a(t')}.
\]

That future boundary condition removes the growing mode:

\[
C=0.
\]

Hence

\[
\boxed{
L=H^{-1}
}
\]

is selected nonlocally.

### Result 048B

\[
\boxed{
HL=1
}
\]

in de Sitter is a **global future-boundary selection**, not a local dynamical attractor of \(\dot L=HL-1\).

This is conceptually important for LTG.

---

## 4. Generic accelerating power-law universe

Take

\[
a(t)\propto t^p,
\qquad
p>1.
\]

Then

\[
H=\frac{p}{t}.
\]

The event horizon is

\[
L
=
a(t)\int_t^\infty\frac{dt'}{a(t')}
=
\frac{t}{p-1}.
\]

Therefore

\[
\boxed{
HL
=
\frac{p}{p-1}
>1.
}
\]

The deceleration parameter is

\[
q
=
-\frac{p-1}{p}.
\]

Hence

\[
\boxed{
HL=-\frac1q.
}
\]

Only in the limit

\[
p\to\infty
\]

does

\[
q\to-1,
\qquad
HL\to1.
\]

Thus cosmic acceleration alone does not imply \(HL=1\).

### Result 048C

\[
\boxed{
\ddot a>0
\not\Rightarrow
HL=1.
}
\]

The value \(HL=1\) specifically identifies the de Sitter causal limit among this family.

---

## 5. Consequence for the HDE pressure relation

EXP-045 obtained

\[
w_X
=
-\frac13-\frac{2}{3HL}.
\]

For generic accelerated power-law expansion,

\[
HL>1,
\]

so

\[
-1<w_X<-\frac13.
\]

Only at

\[
HL=1
\]

does

\[
w_X=-1.
\]

Therefore the pressure becomes exactly vacuum-like only at the de Sitter causal boundary.

---

## 6. Consequence for LTG novelty

EXP-046 appeared to fix

\[
HL=1,
\quad
c=1,
\quad
\Gamma/H=3.
\]

EXP-048 clarifies the logical status:

1. \(HL=1\) is not produced by local event-horizon kinematics;
2. it is selected by the future causal boundary of de Sitter;
3. \(c=1\) and \(\Gamma/H=3\) are then conditional consequences;
4. a genuine LTG law must explain why the global causal boundary selects the de Sitter branch.

Thus the active problem is sharpened from

\[
\text{derive }HL=1
\]

to

\[
\boxed{
\text{derive a global future-boundary / causal consistency condition
that selects the de Sitter branch}.
}
\]

---

## 7. Candidate forms for the next gate

A legitimate next gate may use a truly global quantity rather than another local operator.

Candidates include:

### A. Horizon entropy extremization

\[
S_H
=
\frac{A_H}{4G}.
\]

Ask whether a generalized entropy condition

\[
\frac{dS_{\rm gen}}{dt}\ge0,
\qquad
\frac{dS_{\rm gen}}{dt}\to0
\]

selects

\[
\dot H\to0.
\]

### B. Causal-diamond stationarity

Construct a dimensionless functional

\[
\mathcal C[\mathcal D]
\]

from a causal diamond \(\mathcal D\), its null boundary, area, expansion and matter flux, then test whether

\[
\delta\mathcal C=0
\]

forces de Sitter closure.

### C. Null-expansion consistency

Use the null congruence expansion \(\theta\) and Raychaudhuri equation,

\[
\frac{d\theta}{d\lambda}
=
-\frac12\theta^2
-\sigma_{\mu\nu}\sigma^{\mu\nu}
-R_{\mu\nu}k^\mu k^\nu
\]

for hypersurface-orthogonal null congruences.

Ask whether a global regularity / finite-horizon condition selects a stationary null boundary with a fixed relation to \(H\).

These are global-causal questions and are qualitatively different from the already exhausted local LTG branch.

---

## 8. Terminal classification

### Does the event horizon itself locally drive HL -> 1?

\[
\boxed{\text{NO}.}
\]

**ANALYTIC FAIL AS A LOCAL ATTRACTOR.**

### Is HL = 1 nevertheless selected in exact de Sitter?

\[
\boxed{\text{YES}.}
\]

**GLOBAL BOUNDARY PASS.**

### Does this establish an LTG dynamical principle?

\[
\boxed{\text{NO, not yet}.}
\]

The missing law is precisely the global causal selection of the de Sitter boundary.

## Final consequence

The pressure-sign hypothesis and the global-causal branch now meet at the same point:

\[
\boxed{
\text{global causal selection}
\to
HL=1
\to
p=-\rho
}
\]

but the first arrow remains the unsolved LTG problem.
