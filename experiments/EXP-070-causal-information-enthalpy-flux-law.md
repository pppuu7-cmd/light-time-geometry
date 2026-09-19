# EXP-070 — Exact causal information / enthalpy flux law in Einstein-FLRW

## Objective

Derive the strongest dynamical law that follows exactly from the LTG common variable in flat Einstein-FLRW cosmology, and determine whether it is independent physics or a reformulation of horizon thermodynamics.

Define the apparent/Hubble horizon

\[
R_H=\frac{c}{H},
\]

with area

\[
A_H=4\pi R_H^2,
\]

volume

\[
V_H=\frac{4\pi}{3}R_H^3,
\]

and LTG horizon variable

\[
\boxed{
\mathcal N
=
\frac{A_H}{8\pi\ell_P^2}
=
\frac{c^5}{2G\hbar H^2}.
}
\]

Let \(\varepsilon\) denote total energy density and \(p\) total pressure.

---

## 1. Differentiate the LTG count

From

\[
\mathcal N
=
\frac{c^5}{2G\hbar H^2},
\]

we obtain

\[
\dot{\mathcal N}
=
-\frac{c^5}{G\hbar}
\frac{\dot H}{H^3}.
\]

For flat Einstein-FLRW,

\[
\dot H
=
-\frac{4\pi G}{c^2}
(\varepsilon+p).
\]

Therefore

\[
\hbar\dot{\mathcal N}
=
\frac{4\pi c^3}{H^3}
(\varepsilon+p).
\]

But

\[
V_H
=
\frac{4\pi c^3}{3H^3}.
\]

Hence

\[
\boxed{
\hbar\dot{\mathcal N}
=
3V_H(\varepsilon+p).
}
\]

Define the total energy inside the Hubble patch,

\[
E_H=\varepsilon V_H.
\]

Then

\[
\boxed{
\hbar\dot{\mathcal N}
=
3(E_H+pV_H).
}
\]

### Result 070A — LTG enthalpy-information law

\[
\boxed{
\hbar\dot{\mathcal N}
=
3\mathcal H_H,
\qquad
\mathcal H_H\equiv E_H+pV_H.
}
\]

The growth rate of the dimensionless horizon-information count, measured in energy units by \(\hbar\), equals three times the Hubble-patch enthalpy.

This is exact in flat Einstein-FLRW.

---

## 2. Horizon heat-flux form

The energy flux through the apparent horizon has magnitude

\[
\dot Q_H
=
A_H(\varepsilon+p)c.
\]

Since

\[
A_H
=
\frac{4\pi c^2}{H^2},
\]

we have

\[
\dot Q_H
=
\frac{4\pi c^3}{H^2}
(\varepsilon+p).
\]

Using Result 070A,

\[
H\hbar\dot{\mathcal N}
=
\frac{4\pi c^3}{H^2}
(\varepsilon+p).
\]

Therefore

\[
\boxed{
\hbar H\dot{\mathcal N}
=
\dot Q_H
}
\]

up to the chosen orientation sign convention for heat flow across the horizon.

### Result 070B — causal information-flux law

\[
\boxed{
\text{horizon energy scale }
(\hbar H)
\times
\text{information-growth rate }
(\dot{\mathcal N})
=
\text{energy flux}.
}
\]

---

## 3. Clausius derivation

The apparent-horizon temperature is

\[
\boxed{
T_H
=
\frac{\hbar H}{2\pi k_B}.
}
\]

The horizon entropy is

\[
S_H
=
2\pi k_B\mathcal N.
\]

Thus

\[
T_H\dot S_H
=
\frac{\hbar H}{2\pi k_B}
(2\pi k_B\dot{\mathcal N})
=
\hbar H\dot{\mathcal N}.
\]

Therefore

\[
\boxed{
\dot Q_H=T_H\dot S_H
}
\]

is precisely Result 070B.

### Classification

The LTG causal information-flux law is **exact but not independent new dynamics**.

It is the horizon Clausius/Friedmann relation in the LTG normalization.

---

## 4. Pressure interpretation

Result 070A gives

\[
\dot{\mathcal N}
=
\frac{3V_H}{\hbar}
(\varepsilon+p).
\]

Hence:

\[
\varepsilon+p>0
\Rightarrow
\dot{\mathcal N}>0,
\]

\[
\varepsilon+p=0
\Rightarrow
\dot{\mathcal N}=0,
\]

\[
\varepsilon+p<0
\Rightarrow
\dot{\mathcal N}<0.
\]

So the de Sitter/vacuum condition

\[
p=-\varepsilon
\]

is exactly the stationarity condition

\[
\boxed{
\dot{\mathcal N}=0.
}
\]

This strengthens the interpretation from EXP-064:

> pressure/enthalpy is the driver of geometric-information growth.

---

## 5. Why this matters for a new LTG law

The exact Einstein result suggests the generalized candidate

\[
\boxed{
\hbar H\dot{\mathcal N}_{\rm gen}
\stackrel{?}{=}
\dot Q_{\rm physical}
}
\]

with

\[
\mathcal N_{\rm gen}
=
\frac{S_{\rm gen}}{2\pi k_B}.
\]

If this equation remains valid when \(S_{\rm gen}\) is defined microscopically and independently of the gravitational field equations, it would become more than a reformulation.

That generalized statement is tested in subsequent gates.

---

## Terminal classification

### Einstein-FLRW law

\[
\boxed{
\hbar\dot{\mathcal N}
=
3(E+pV)
}
\]

and

\[
\boxed{
\hbar H\dot{\mathcal N}
=
\dot Q_H
}
\]

**ANALYTIC PASS.**

### Novel physical law

**NOT YET.**

The result is equivalent to standard Friedmann/horizon thermodynamics.

### New opportunity

Promote the exact Einstein relation to a generalized-entropy causal balance and test whether it imposes new observable constraints beyond GR.
