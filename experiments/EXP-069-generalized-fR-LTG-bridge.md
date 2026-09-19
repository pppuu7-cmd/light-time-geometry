# EXP-069 — Generalized LTG bridge in constant-curvature f(R) gravity

## Objective

EXP-068 showed that the raw Einstein-gravity formula is not an exact universal quantum identity.

Test whether its core survives in a broader classical/effective gravity theory when area entropy is replaced by Wald entropy and Misner-Sharp energy by the corresponding generalized horizon energy.

Use vacuum metric \(f(R)\) gravity at a constant-curvature de Sitter fixed point.

---

## 1. Constant-curvature f(R) setup

Take the gravitational action

\[
I
=
\frac{c^3}{16\pi G}
\int d^4x\sqrt{-g}\,f(R)
\]

with no matter for the fixed-point test.

Let

\[
R=R_0=\text{const},
\]

and define

\[
\boxed{
F_0
\equiv
f'(R_0).
}
\]

The vacuum constant-curvature field equation in four dimensions reduces to

\[
\boxed{
F_0R_0=2f(R_0).
}
\]

For de Sitter,

\[
R_0=\frac{12}{L^2},
\]

with horizon radius \(L\).

---

## 2. Wald entropy

For metric \(f(R)\) gravity, the stationary horizon Wald entropy is

\[
\boxed{
S_W
=
\frac{k_BF_0A c^3}{4G\hbar}.
}
\]

For the de Sitter horizon,

\[
A=4\pi L^2.
\]

Therefore

\[
\boxed{
\frac{S_W}{2\pi k_B}
=
\frac{F_0A}{8\pi\ell_P^2}.
}
\]

Thus the geometric term is no longer bare area but the Wald-weighted area.

---

## 3. Generalized Misner-Sharp horizon energy

For constant \(F_0\), the generalized horizon energy reduces to the Einstein expression rescaled by \(F_0\):

\[
\boxed{
E_{\rm eff}
=
\frac{F_0c^4L}{2G}.
}
\]

Use the light-crossing time

\[
\tau_L=\frac{L}{c}.
\]

Then

\[
\frac{E_{\rm eff}\tau_L}{\hbar}
=
\frac{F_0c^3L^2}{2G\hbar}.
\]

Since

\[
\frac{F_0A}{8\pi\ell_P^2}
=
\frac{F_0(4\pi L^2)c^3}{8\pi G\hbar}
=
\frac{F_0c^3L^2}{2G\hbar},
\]

we obtain

\[
\boxed{
\frac{E_{\rm eff}\tau_L}{\hbar}
=
\frac{S_W}{2\pi k_B}.
}
\]

### Result 069A

The LTG energy-time-information bridge survives exactly at the constant-curvature \(f(R)\) fixed point when the correct Wald entropy and generalized horizon energy are used.

---

## 4. Euclidean action

The Euclidean de Sitter four-sphere has

\[
V_4
=
\frac{8\pi^2}{3}L^4.
\]

Using

\[
R_0=\frac{12}{L^2},
\]

this is

\[
V_4
=
\frac{384\pi^2}{R_0^2}.
\]

The Euclidean on-shell action is

\[
I_E
=
-\frac{c^3}{16\pi G}
f(R_0)V_4.
\]

Use the fixed-point equation

\[
f(R_0)=\frac12F_0R_0.
\]

Then

\[
I_E
=
-\frac{c^3}{16\pi G}
\frac12F_0R_0
\frac{384\pi^2}{R_0^2}.
\]

Therefore

\[
\boxed{
I_E
=
-\frac{12\pi c^3F_0}{GR_0}.
}
\]

Now the Wald entropy is

\[
\frac{S_W}{k_B}
=
\frac{F_0A c^3}{4G\hbar}.
\]

Since

\[
A
=
4\pi L^2
=
\frac{48\pi}{R_0},
\]

we get

\[
\frac{S_W}{k_B}
=
\frac{12\pi c^3F_0}{G\hbar R_0}.
\]

Hence

\[
\boxed{
\frac{|I_E|}{\hbar}
=
\frac{S_W}{k_B}.
}
\]

### Result 069B

The Euclidean-action / entropy identity also survives at the constant-curvature \(f(R)\) fixed point.

---

## 5. Generalized common variable

Define

\[
\boxed{
\mathcal N_{f(R)}
\equiv
\frac{F_0A}{8\pi\ell_P^2}.
}
\]

Then all four terms coincide:

\[
\boxed{
\mathcal N_{f(R)}
=
\frac{F_0A}{8\pi\ell_P^2}
=
\frac{S_W}{2\pi k_B}
=
\frac{|I_E|}{2\pi\hbar}
=
\frac{E_{\rm eff}\tau_L}{\hbar}.
}
\]

This is the direct \(f(R)\) generalization of the Einstein LTG bridge.

---

## 6. What this means

The common-variable structure is not tied uniquely to the bare Einstein area law.

Its deeper ingredients are:

1. stationary causal horizon;
2. correct gravitational entropy functional;
3. correct quasi-local/effective energy;
4. Euclidean saddle thermodynamics.

Thus the more robust conceptual formula is

\[
\boxed{
\text{gravitational entropy}
\leftrightarrow
\text{Euclidean action}
\leftrightarrow
\text{generalized horizon energy}\times\text{causal time}.
}
\]

Bare geometric area is only the Einstein-gravity realization.

---

## 7. Non-equilibrium limitation

For general time-dependent \(f(R)\) cosmology,

\[
F=f'(R)
\]

can vary.

Then horizon thermodynamics generally contains an entropy-production term,

\[
dS
=
\frac{\delta Q}{T}
+
d_iS.
\]

So the simple equilibrium equality need not remain exact during arbitrary dynamical evolution.

EXP-069 is therefore a fixed-point / constant-curvature theorem, not a theorem for all modified-gravity cosmologies.

---

## 8. Quantum limitation

Even Wald entropy is a classical effective-action quantity.

Full quantum generalized entropy can include

\[
S_{\rm gen}
=
S_W
+
S_{\rm out}
+
S_{\rm loop}
+\cdots.
\]

Therefore the nonperturbative quantum version remains open.

The natural next object is

\[
\boxed{
\mathcal N_{\rm gen}
=
\frac{S_{\rm gen}}{2\pi k_B}.
}
\]

The challenge is to identify corresponding generalized action and energy-time variables beyond the stationary semiclassical saddle.

---

## 9. Terminal classification

### Einstein-only artifact?

\[
\boxed{\text{NO}.}
\]

The bridge survives a controlled \(f(R)\) generalization.

### Constant-curvature f(R) fixed point

\[
\boxed{\text{ANALYTIC PASS}.}
\]

### Generic dynamical modified gravity

\[
\boxed{\text{NOT YET}.}
\]

Entropy production and varying \(F\) obstruct the simple equilibrium identity.

### Full quantum gravity

\[
\boxed{\text{OPEN}.}
\]

## Strongest upgraded formula

At a constant-curvature \(f(R)\) de Sitter fixed point,

\[
\boxed{
\frac{F_0A}{8\pi\ell_P^2}
=
\frac{S_W}{2\pi k_B}
=
\frac{|I_E|}{2\pi\hbar}
=
\frac{E_{\rm eff}\tau_L}{\hbar}.
}
\]

This suggests that the durable LTG object is generalized horizon entropy/information rather than raw area.

## Prior-art anchors

- Metric \(f(R)\) horizon entropy is Wald entropy \(S_W=F A/(4G)\).
- Generalized Misner-Sharp energy in \(f(R)\) and scalar-tensor cosmology reduces to \(E=FR/(2G)\) at the apparent horizon under the relevant conditions.
- Modified-gravity horizon thermodynamics is generically non-equilibrium when \(F\) varies.
