# LTG Research Status v12 — causal information balance and quantum relative-entropy completion through EXP-076

## Executive result

The project attempted to derive a genuine LTG law rather than another static identity.

The strongest result is a two-layer structure.

### Local / causal-quantum layer

For a causal region with causal timescale \(\tau_c\), generalized information count

\[
\mathcal N_{\rm gen}
=
\frac{S_{\rm gen}}{2\pi k_B},
\]

and modular/causal energy transfer \(\Delta Q_{\rm mod}\), the natural quantum balance is

\[
\boxed{
\frac{\tau_c\Delta Q_{\rm mod}}{\hbar}
=
\Delta\mathcal N_{\rm gen}
+
\frac{D_{\rm grav}}{2\pi},
\qquad
D_{\rm grav}\ge0.
}
\]

In controlled QFT/modular settings,

\[
D_{\rm grav}
\to
D(\rho\Vert\sigma),
\]

the quantum relative entropy.

At first order,

\[
D=O(\epsilon^2),
\]

so

\[
\boxed{
\frac{\tau_c\,\delta Q_{\rm mod}}{\hbar}
=
\delta\mathcal N_{\rm gen}
}
\]

is recovered as the reversible entanglement-first-law limit.

### Global / selection layer

The local law does **not** select:

\[
H,
\qquad
\Lambda,
\qquad
n,
\qquad
\mathcal N(a).
\]

A genuinely LTG-specific global boundary/state-selection rule is still missing.

---

## EXP-070 — exact Einstein causal information / enthalpy law

For the flat-FLRW apparent horizon,

\[
\mathcal N
=
\frac{c^5}{2G\hbar H^2}.
\]

Einstein-FLRW dynamics gives

\[
\boxed{
\hbar\dot{\mathcal N}
=
3V_H(\varepsilon+p)
=
3(E_H+pV_H).
}
\]

Equivalently, for the horizon heat flux,

\[
\boxed{
\hbar H\dot{\mathcal N}
=
\dot Q_H.
}
\]

Using

\[
T_H=\frac{\hbar H}{2\pi k_B},
\qquad
S_H=2\pi k_B\mathcal N,
\]

this is exactly

\[
\dot Q_H=T_H\dot S_H.
\]

**Classification: exact PASS / equivalent to Friedmann-Clausius dynamics.**

---

## EXP-071 — logarithmic quantum entropy correction

Using

\[
S
=
\frac{\pi}{GH^2}
+
\alpha\ln\left(\frac{4\pi}{GH^2}\right)
\]

and the equilibrium causal balance gives

\[
\boxed{
\dot H
=
-\frac{4\pi G(\rho+p)}
{1+\alpha GH^2/\pi}.
}
\]

Integrating with matter conservation yields

\[
\boxed{
H^2
+
\frac{\alpha G}{2\pi}H^4
=
\frac{8\pi G}{3}\rho+C.
}
\]

This maps to known entropy-corrected cosmology and is Planck-suppressed for order-unity \(\alpha\).

**Classification: modified dynamics PASS / LTG novelty FAIL.**

---

## EXP-072 — f(R) causal-balance residual

For

\[
F=df/dR
\]

and Wald information

\[
\mathcal N_W
=
\frac{F}{2G\hbar H^2},
\]

the exact \(f(R)\) background equation gives

\[
\boxed{
\hbar\dot{\mathcal N}_W
-
3V_H(\rho_m+p_m)
=
\frac{\ddot F}{2GH^3}.
}
\]

Thus define

\[
\boxed{
\mathfrak R_{\rm LTG}
=
\frac{\ddot F}{2GH^3}.
}
\]

For Einstein gravity,

\[
F=1
\Rightarrow
\mathfrak R_{\rm LTG}=0.
\]

The dimensionless residual is

\[
\boxed{
\frac{\ddot F}{FH^2}
=
\alpha_M'
+\alpha_M^2
-\epsilon_H\alpha_M.
}
\]

For luminal scalar-tensor propagation,

\[
\frac{d_L^{GW}}{d_L^{EM}}
=
\frac{M_*(0)}{M_*(z)},
\qquad
F=M_*^2.
\]

Therefore the residual is in principle testable with standard sirens plus expansion-history data.

**Classification: measurable LTG packaging / prior-art ingredients.**

---

## EXP-073 — Causal Information Balance conjecture

A candidate LTG postulate was formulated:

\[
\boxed{
\delta Q
=
\frac{\hbar}{\tau_c}d\mathcal N_{\rm gen}.
}
\]

For flat FLRW,

\[
\boxed{
\hbar H\dot{\mathcal N}_{\rm gen}
=
\dot Q_H.
}
\]

In a Wald-only \(f(R)\) truncation this predicts

\[
\boxed{
\ddot F=0.
}
\]

Hence

\[
F(t)=F_0+\dot F_0(t-t_0)
\]

and the standard-siren ratio has the one-parameter form

\[
\boxed{
\frac{d_L^{GW}(z)}{d_L^{EM}(z)}
=
\left[
1-\gamma
\int_0^z
\frac{dz'}{(1+z')H(z')}
\right]^{-1/2},
}
\]

where

\[
\gamma=\dot F_0/F_0.
\]

This is falsifiable.

However EXP-074 showed that exact zero residual is too strong beyond the reversible/linearized quantum limit.

---

## EXP-074 — relative-entropy quantum completion

Quantum relative entropy gives

\[
\boxed{
D(\rho\Vert\sigma)
=
\Delta\langle K\rangle
-
\Delta s
\ge0.
}
\]

With causal temperature

\[
k_BT_c=\frac{\hbar}{2\pi\tau_c},
\]

physical modular energy

\[
\Delta Q_{\rm mod}
=
k_BT_c\Delta\langle K\rangle,
\]

and

\[
\Delta\mathcal N_q
=
\Delta s/(2\pi),
\]

one obtains exactly

\[
\boxed{
\frac{\tau_c\Delta Q_{\rm mod}}{\hbar}
-
\Delta\mathcal N_q
=
\frac{D(\rho\Vert\sigma)}{2\pi}
\ge0.
}
\]

At first order,

\[
D=O(\epsilon^2),
\]

so the CIB equality is recovered.

At second order,

\[
D
=
\frac12\epsilon^2\mathcal F_Q+\cdots,
\]

giving a positive correction controlled by quantum Fisher information / canonical energy in suitable gravitational settings.

**Classification: quantum completion FOUND / foundation is prior-art relative entropy / LTG normalization is synthetic.**

---

## EXP-075 — quantum focusing

For

\[
\mathcal N_{\rm gen}
=
S_{\rm gen}/(2\pi k_B),
\]

the quantum expansion is proportional to

\[
\frac1A
\frac{d\mathcal N_{\rm gen}}{d\lambda}.
\]

QFC-type structure therefore implies, schematically for homogeneous cuts,

\[
\boxed{
\frac{d}{d\lambda}
\left[
\frac1A
\frac{d\mathcal N_{\rm gen}}{d\lambda}
\right]
\le0.
}
\]

This supplies the null causal-evolution constraint on the same generalized LTG variable.

**Classification: causal quantum constraint FOUND / QFC prior art.**

---

## EXP-076 — relative-entropy minimization

The simplest selection rule

\[
\min D(\rho\Vert\sigma)
\]

gives

\[
D_{\min}=0
\]

when

\[
\rho=\sigma.
\]

This produces local entanglement equilibrium but does not choose among a family of equilibrium backgrounds with different cosmological scales.

Therefore:

\[
\boxed{
D=0
\not\Rightarrow
\text{unique }H,\Lambda,n.
}
\]

**Classification: local equilibrium PASS / global scale selection FAIL.**

---

## Strongest law now available

The best-supported LTG causal/quantum form is

\[
\boxed{
\frac{\tau_c\Delta Q_{\rm mod}}{\hbar}
=
\Delta\mathcal N_{\rm gen}
+
\frac{D_{\rm grav}}{2\pi},
\qquad
D_{\rm grav}\ge0,
}
\]

supplemented along null evolution by quantum-focusing constraints.

Interpretation:

\[
\boxed{
\text{causal action input}
=
\text{geometric/information change}
+
\text{quantum distinguishability}.
}
\]

This is the deepest current synthesis of:

- energy;
- causal/light time;
- generalized gravitational information;
- quantum relative entropy.

---

## Novelty status

The ingredients are established separately.

The current formula is therefore **not yet a newly discovered law of nature**.

Its value is that it identifies the exact object that any genuine LTG theory must control.

The remaining missing content is no longer local dynamics.

It is:

\[
\boxed{
\text{a global boundary/state-selection functional that chooses one causal history.}
}
\]

Such a rule must determine the reference-state family or a global invariant without inserting the observed late-time scale.

---

## Active next gate

Search for a global functional

\[
\mathfrak G[
\text{past boundary},
\text{future boundary},
\mathcal N_{\rm gen},
D_{\rm grav}
]
\]

whose extremization selects a unique causal history and that cannot be reduced to:

- ordinary relative-entropy minimization;
- generalized second law;
- Einstein/Friedmann equations;
- standard path-integral saddle weighting.

Until such a functional is found, LTG has a strong local causal/quantum synthesis but not an independent global dynamics.
