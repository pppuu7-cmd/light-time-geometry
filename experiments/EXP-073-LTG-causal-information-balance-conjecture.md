# EXP-073 — LTG Causal Information Balance Conjecture and falsifiable standard-siren law

## Objective

Formulate the first LTG statement in the project that is:

1. not merely an algebraic identity;
2. reduces to the exact Einstein result;
3. has a clear microscopic interpretation;
4. can be falsified observationally.

This is a **candidate LTG law**, not an established theorem.

---

## 1. Three starting principles

### Principle A — complete generalized information

For a causal horizon/diamond, define

\[
\boxed{
\mathcal N_{\rm gen}
=
\frac{S_{\rm gen}}{2\pi k_B},
}
\]

where \(S_{\rm gen}\) includes all gravitational and quantum entropy assigned to the causal boundary/state.

The crucial word is **complete**.

The entropy must be defined independently of the desired cosmological equations.

### Principle B — causal temperature

Associate the causal timescale

\[
\tau_c
\]

with the horizon/diamond temperature

\[
\boxed{
k_BT_c
=
\frac{\hbar}{2\pi\tau_c}.
}
\]

For a flat FLRW apparent horizon,

\[
\tau_c=H^{-1}.
\]

### Principle C — no hidden entropy channel

If \(S_{\rm gen}\) is complete, there is no additional untracked internal entropy-production term outside \(\mathcal N_{\rm gen}\).

The physical energy crossing the causal boundary satisfies the ordinary balance relation

\[
\delta Q=T_c\,dS_{\rm gen}.
\]

This is the nontrivial LTG assumption.

---

## 2. Derive the candidate law

Using

\[
S_{\rm gen}=2\pi k_B\mathcal N_{\rm gen},
\]

we have

\[
dS_{\rm gen}
=
2\pi k_B\,d\mathcal N_{\rm gen}.
\]

Then

\[
\delta Q
=
\frac{\hbar}{2\pi k_B\tau_c}
(2\pi k_B\,d\mathcal N_{\rm gen}).
\]

Therefore

\[
\boxed{
\delta Q
=
\frac{\hbar}{\tau_c}
d\mathcal N_{\rm gen}.
}
\]

Equivalently,

\[
\boxed{
\hbar\dot{\mathcal N}_{\rm gen}
=
\tau_c\,\dot Q.
}
\]

For flat FLRW,

\[
\tau_c=H^{-1},
\]

so

\[
\boxed{
\hbar H\dot{\mathcal N}_{\rm gen}
=
\dot Q_H.
}
\]

Call this the:

\[
\boxed{
\textbf{LTG Causal Information Balance (CIB) law}.
}
\]

---

## 3. Einstein limit

For

\[
\mathcal N_{\rm gen}
\to
\mathcal N_{\rm LTG}
=
\frac{A}{8\pi\ell_P^2},
\]

EXP-070 proved exactly that

\[
\hbar H\dot{\mathcal N}_{\rm LTG}
=
\dot Q_H.
\]

Therefore CIB has the correct Einstein limit.

---

## 4. Why this is not automatically a tautology

If one defines \(S_{\rm gen}\) retrospectively from the gravitational field equations, CIB is empty.

For CIB to have physical content:

1. \(S_{\rm gen}\) must come from an independently specified microscopic/quantum state;
2. \(\dot Q\) must be independently defined from non-gravitational energy flux;
3. the equality must then be tested.

This separates LTG from ordinary "derive an entropy that reproduces Friedmann" constructions.

Recent work on modified-gravity horizon thermodynamics explicitly emphasizes the ambiguity of choosing entropy-production terms merely to retrofit the known field equations.

CIB forbids that post-hoc freedom.

---

## 5. First falsifiable truncation: Wald f(R)

Suppose the semiclassical generalized information is approximated by the Wald term,

\[
\mathcal N_{\rm gen}
\approx
\mathcal N_W
=
\frac{F}{2G\hbar H^2}.
\]

Use matter heat flux only.

EXP-072 gives

\[
\hbar\dot{\mathcal N}_W
-
3V_H(\rho_m+p_m)
=
\frac{\ddot F}{2GH^3}.
\]

Therefore CIB predicts

\[
\boxed{
\ddot F=0
}
\]

within this controlled truncation.

This is a genuine restriction on generic \(f(R)\)/scalar-tensor background evolution.

### Result 073A — testable LTG truncation

\[
\boxed{
F(t)=F_0+\dot F_0(t-t_0).
}
\]

The effective Planck mass squared must be linear in Jordan-frame cosmic time over the regime in which the Wald truncation of \(S_{\rm gen}\) is valid.

---

## 6. Standard-siren prediction

For luminal scalar-tensor propagation,

\[
\frac{d_L^{GW}}{d_L^{EM}}
=
\sqrt{\frac{F_0}{F(z)}}.
\]

From

\[
F(t)
=
F_0+\dot F_0(t-t_0),
\]

and

\[
t(z)-t_0
=
-
\int_0^z
\frac{dz'}{(1+z')H(z')},
\]

define

\[
\gamma
\equiv
\frac{\dot F_0}{F_0}.
\]

Then

\[
\boxed{
\frac{d_L^{GW}(z)}
{d_L^{EM}(z)}
=
\left[
1
-
\gamma
\int_0^z
\frac{dz'}{(1+z')H(z')}
\right]^{-1/2}.
}
\]

This is a one-parameter shape prediction once \(H(z)\) is measured independently.

It is more restrictive than an arbitrary phenomenological \(\alpha_M(z)\).

### Differential form

Let

\[
r(z)
\equiv
\frac{d_L^{GW}}{d_L^{EM}},
\]

and use

\[
D\equiv\frac{d}{d\ln a}.
\]

Since

\[
F/F_0=r^{-2},
\]

we have

\[
\alpha_M=-2D\ln r.
\]

The CIB-Wald condition

\[
\ddot F=0
\]

becomes

\[
\boxed{
\alpha_M'
+
\alpha_M^2
-
\epsilon_H\alpha_M
=
0.
}
\]

Equivalently, with

\[
y\equiv D\ln r,
\]

\[
\boxed{
y'
-
2y^2
-
\epsilon_H y
=
0.
}
\]

This can be confronted with standard-siren and expansion-history data.

---

## 7. Late-time finite de Sitter consequence

If the universe approaches an eternal de Sitter state and the effective Planck mass remains finite,

\[
H\to H_*>0,
\qquad
F\to F_*<\infty,
\]

then

\[
\ddot F=0
\]

implies

\[
F=A+Bt.
\]

Finiteness as

\[
t\to\infty
\]

requires

\[
B=0.
\]

Therefore

\[
\boxed{
F\to\text{constant}
}
\]

and

\[
\boxed{
d_L^{GW}/d_L^{EM}\to1
}
\]

as the equilibrium endpoint is approached.

This is a concrete asymptotic prediction of the CIB-Wald truncation.

---

## 8. Critical caveat

The condition

\[
\ddot F=0
\]

is **not yet a fundamental theorem**.

It follows only if:

1. CIB is fundamental;
2. Wald entropy is already the complete generalized entropy over the tested regime;
3. matter heat flux is the correct independently defined \(\dot Q\);
4. no missing quantum/outside entropy contribution compensates the residual.

If

\[
S_{\rm gen}
=
S_W+S_{\rm out}+S_{\rm loop}+\cdots,
\]

then those additional terms modify the prediction.

Therefore observational failure of \(\ddot F=0\) would falsify the **Wald-truncated CIB**, not necessarily every possible generalized LTG law.

---

## 9. Novelty status

The ingredients of CIB are known separately:

- causal-horizon temperature;
- generalized entropy;
- Clausius balance;
- Wald entropy;
- standard-siren tests of Planck-mass running.

The potentially new LTG content is the **no-post-hoc-completion principle**:

> once \(S_{\rm gen}\) is specified independently and completely, the causal information balance must close with no arbitrary entropy-production function introduced merely to reproduce desired field equations.

This is a falsifiable methodological/physical postulate.

It becomes a new theory only when LTG supplies an independent microscopic formula for \(S_{\rm gen}\).

---

## 10. Current classification

### Exact Einstein limit

**PASS.**

### Independent quantum derivation of complete S_gen

**NOT YET.**

### Falsifiable Wald truncation

\[
\boxed{
\ddot F=0
}
\]

**NEW LTG CANDIDATE / TESTABLE / NOT YET ESTABLISHED.**

### Observable consequence

\[
\boxed{
\frac{d_L^{GW}}{d_L^{EM}}
=
\left[
1-\gamma
\int_0^z
\frac{dz'}{(1+z')H(z')}
\right]^{-1/2}
}
\]

in the Wald-truncated luminal scalar-tensor regime.

---

## Next decisive gate

Do not add freedom.

Attempt to derive the missing \(S_{\rm out}+S_{\rm loop}\) contribution from quantum focusing / relative entropy for a cosmological causal diamond.

Then ask whether the full CIB:

1. preserves \(\mathfrak R_{\rm LTG}=0\);
2. predicts a nonzero universal residual;
3. fails.

Only that calculation can promote CIB from an LTG conjecture into a quantum-causal theorem.
