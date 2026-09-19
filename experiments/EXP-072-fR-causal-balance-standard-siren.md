# EXP-072 — LTG causal-balance residual in f(R) gravity and a standard-siren observable

## Objective

Find a measurable quantity that vanishes in the exact Einstein LTG balance but is nonzero in a broader gravity theory.

Use metric \(f(R)\) gravity in the Jordan frame, with matter minimally coupled.

Work in natural units

\[
c=1
\]

while retaining \(\hbar\) explicitly in the LTG count.

Define

\[
F\equiv \frac{df}{dR}.
\]

---

## 1. Wald LTG count

For the flat apparent horizon,

\[
A=\frac{4\pi}{H^2}.
\]

The Wald entropy is

\[
S_W
=
\frac{F A}{4G\hbar}.
\]

Therefore

\[
\boxed{
\mathcal N_W
=
\frac{S_W}{2\pi}
=
\frac{F}{2G\hbar H^2}.
}
\]

Differentiate:

\[
\hbar\dot{\mathcal N}_W
=
\frac{1}{2G}
\left(
\frac{\dot F}{H^2}
-
\frac{2F\dot H}{H^3}
\right).
\]

---

## 2. f(R) Raychaudhuri equation

The second background equation is

\[
\boxed{
-2F\dot H
=
8\pi G(\rho_m+p_m)
+
\ddot F
-
H\dot F.
}
\]

The matter enthalpy inside the Hubble volume

\[
V_H=\frac{4\pi}{3H^3}
\]

is

\[
3V_H(\rho_m+p_m)
=
\frac{4\pi}{H^3}(\rho_m+p_m).
\]

Using the field equation,

\[
3V_H(\rho_m+p_m)
=
\frac{1}{2GH^3}
\left(
-2F\dot H-\ddot F+H\dot F
\right).
\]

Subtract this from \(\hbar\dot{\mathcal N}_W\).

The terms containing \(\dot H\) and \(H\dot F\) cancel exactly, leaving

\[
\boxed{
\hbar\dot{\mathcal N}_W
-
3V_H(\rho_m+p_m)
=
\frac{\ddot F}{2GH^3}.
}
\]

### Result 072A — LTG causal-balance residual

Define

\[
\boxed{
\mathfrak R_{\rm LTG}
\equiv
\hbar\dot{\mathcal N}_W
-
3V_H(\rho_m+p_m).
}
\]

Then

\[
\boxed{
\mathfrak R_{\rm LTG}
=
\frac{\ddot F}{2GH^3}.
}
\]

For Einstein gravity,

\[
F=1,
\]

so

\[
\boxed{
\mathfrak R_{\rm LTG}=0.
}
\]

---

## 3. Dimensionless form

Define the running-Planck-mass parameter

\[
\boxed{
\alpha_M
\equiv
\frac{d\ln F}{d\ln a}
=
\frac{\dot F}{HF}.
}
\]

Also define

\[
\epsilon_H
\equiv
-\frac{\dot H}{H^2},
\]

and prime as

\[
{}'=\frac{d}{d\ln a}.
\]

Then

\[
\frac{\ddot F}{FH^2}
=
\alpha_M'
+
\alpha_M^2
-
\epsilon_H\alpha_M.
\]

Normalize the residual by

\[
\hbar H\mathcal N_W
=
\frac{F}{2GH}.
\]

Then

\[
\boxed{
\frac{\mathfrak R_{\rm LTG}}
{\hbar\mathcal N_W}
\frac{1}{H}
=
\frac{\ddot F}{FH^2}
=
\alpha_M'
+
\alpha_M^2
-
\epsilon_H\alpha_M.
}
\]

This gives a dimensionless, background-level measure of failure of the Einstein LTG balance.

---

## 4. Gravitational-wave luminosity distance

For luminal scalar-tensor/Horndeski propagation with a running effective Planck mass,

\[
\boxed{
\frac{d_L^{\rm GW}(z)}
{d_L^{\rm EM}(z)}
=
\frac{M_*(0)}{M_*(z)}.
}
\]

For \(F=M_*^2\),

\[
\boxed{
\frac{F(z)}{F_0}
=
\left[
\frac{d_L^{\rm EM}(z)}
{d_L^{\rm GW}(z)}
\right]^2.
}
\]

Therefore standard sirens can reconstruct \(F(z)\) in this class of theories.

The expansion history provides \(H(z)\).

Hence the LTG residual is, in principle, independently observable from:

1. electromagnetic distance/redshift data;
2. gravitational-wave standard sirens;
3. expansion-history measurements.

### Result 072B

The LTG causal-balance residual can be mapped to an observable modified-gravity quantity.

This is a **testable packaging** of known Planck-mass-running physics.

---

## 5. Is the residual itself new physics?

No.

The ingredients are established:

- Wald entropy;
- \(f(R)\) background equations;
- running effective Planck mass;
- modified GW luminosity distance.

The cancellation producing

\[
\mathfrak R_{\rm LTG}
=
\ddot F/(2GH^3)
\]

is a useful LTG synthesis, but it is not yet a new law.

The new-law question is whether fundamental causal/quantum physics should require

\[
\boxed{
\mathfrak R_{\rm LTG}=0
}
\]

when the **complete** generalized entropy has been used.

That is formulated as a conjecture in EXP-073.

---

## Prior-art anchors

- Nonequilibrium \(f(R)\) horizon thermodynamics contains entropy-production / effective-coupling-evolution terms.
- Standard sirens probe a running effective Planck mass through \(d_L^{GW}/d_L^{EM}\).
