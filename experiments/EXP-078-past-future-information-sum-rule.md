# EXP-078 — Past-to-future causal-information sum rule

## Objective

Use the exact dynamical LTG relation

\[
\frac{d\ln\mathcal N}{d\ln a}=3(1+w_{\rm eff})
\]

to derive a global past-to-future constraint and test whether a Planck-scale initial causal cell plus a finite de Sitter endpoint gives an independently predictive relation.

---

## 1. Integrate the LTG evolution law

Integrating between \(a_i\) and \(a_f\),

\[
\ln\left(\frac{\mathcal N_f}{\mathcal N_i}\right)
=
3\int_{a_i}^{a_f}
(1+w_{\rm eff})\,d\ln a.
\]

Therefore

\[
\boxed{
\mathcal N_f
=
\mathcal N_i
\exp\left[
3\int_{a_i}^{a_f}
(1+w_{\rm eff})\,d\ln a
\right].
}
\]

Call this the:

\[
\boxed{
\text{LTG causal-information sum rule}.
}
\]

---

## 2. Planck causal-cell normalization

For a flat apparent horizon,

\[
\mathcal N
=
\frac{c^5}{2G\hbar H^2}.
\]

Define the Planck Hubble/frequency scale

\[
H_P
=
\sqrt{\frac{c^5}{G\hbar}}
=
t_P^{-1}.
\]

At

\[
H_i=H_P,
\]

one gets

\[
\boxed{
\mathcal N_i=\frac12.
}
\]

Equivalently, a horizon of radius

\[
R_i=\ell_P
\]

has

\[
A_i=4\pi\ell_P^2
\]

and therefore

\[
A_i/(8\pi\ell_P^2)=1/2.
\]

This corrects the informal \(O(1)\) Planck-cell language to the precise LTG normalization.

---

## 3. Future de Sitter endpoint

For an asymptotic de Sitter scale \(H_*\),

\[
\mathcal N_*
=
\frac12
\left(
\frac{H_P}{H_*}
\right)^2.
\]

Thus the sum rule gives

\[
\boxed{
\int_{a_P}^{\infty}
(1+w_{\rm eff})\,d\ln a
=
\frac23
\ln\left(
\frac{H_P}{H_*}
\right)
}
\]

provided the future endpoint exists and \(H\to H_*>0\).

This is a direct relation among:

- the Planck causal scale;
- the full enthalpy-weighted expansion history;
- the future de Sitter scale.

---

## 4. Representative late-time benchmark

Using

\[
H_*
\simeq
H_0\sqrt{\Omega_\Lambda}
\]

with the representative values already used in earlier LTG gates,

\[
H_0\simeq2.1843\times10^{-18}\ {\rm s^{-1}},
\qquad
\Omega_\Lambda\simeq0.685,
\]

gives

\[
H_*
\simeq1.8078\times10^{-18}\ {\rm s^{-1}}.
\]

With

\[
H_P\simeq1.8549\times10^{43}\ {\rm s^{-1}},
\]

the future LTG count is

\[
\boxed{
\mathcal N_*
\simeq5.26\times10^{121}.
}
\]

The required integrated weighted expansion is

\[
\boxed{
\int
(1+w_{\rm eff})\,d\ln a
\simeq93.66.
}
\]

Equivalently,

\[
\boxed{
\ln\left(\frac{\mathcal N_*}{\mathcal N_P}\right)
\simeq280.97.
}
\]

These values are a consistency benchmark, not an LTG prediction, because the late scale was used as input.

---

## 5. Finite-information future criterion

Take

\[
a_f\to\infty.
\]

A finite nonzero future information capacity,

\[
0<\mathcal N_\infty<\infty,
\]

requires

\[
\boxed{
\int^{\infty}
(1+w_{\rm eff})\,d\ln a
<\infty.
}
\]

On a nonphantom branch,

\[
1+w_{\rm eff}\ge0,
\]

this means the cumulative enthalpy-weighted expansion must converge.

For a smooth asymptotic state, this requires

\[
\boxed{
w_{\rm eff}\to-1
}
\]

sufficiently rapidly.

Thus finite future causal information capacity provides a global integrability form of the de Sitter-endpoint condition.

---

## 6. Constant-w examples

### \(w>-1\) forever

If

\[
w=\text{constant}>-1,
\]

then

\[
\int^\infty(1+w)d\ln a=\infty
\]

and hence

\[
\boxed{
\mathcal N_\infty=\infty.
}
\]

No finite de Sitter information capacity exists.

### \(w=-1\)

If

\[
w=-1,
\]

then

\[
\mathcal N=\text{constant}.
\]

### Phantom \(w<-1\)

Then

\[
\mathcal N
\]

decreases and can approach zero as \(H\) diverges toward a big-rip-type singularity.

---

## 7. Is the sum rule new physics?

No.

It is the integrated form of the exact flat-FLRW Einstein identity from EXP-064.

Therefore it is a strong global checksum, not an independent law.

Its value is conceptual:

\[
\boxed{
\text{future horizon information}
=
\text{initial causal information}
\times
e^{\text{integrated enthalpy history}}.
}
\]

---

## 8. Potential use as a boundary test

If future \(H_*\) were not inserted but independently predicted by a microscopic boundary rule, the sum rule would constrain the entire admissible \(w_{\rm eff}(a)\) history.

Conversely, if:

1. \(\mathcal N_i\) were fixed microscopically;
2. \(w_{\rm eff}(a)\) were independently known from matter physics;
3. no late \(H\) information were used;

then the sum rule would predict \(\mathcal N_f\).

At present those independence conditions are not satisfied strongly enough to claim a new prediction.

---

## Terminal classification

### Global past-future relation

\[
\boxed{
\ln(\mathcal N_f/\mathcal N_i)
=
3\int(1+w_{\rm eff})d\ln a
}
\]

**ANALYTIC PASS.**

### Finite future capacity criterion

\[
\boxed{
\int^\infty(1+w_{\rm eff})d\ln a<\infty
}
\]

**ANALYTIC PASS.**

### Independent LTG prediction

**NOT YET.**
