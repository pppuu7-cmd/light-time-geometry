# EXP-058 — Can semiclassical path-integral weighting select the horizon quantum number?

## Objective

EXP-057 obtained the conditional spectrum

\[
A_n=8\pi\ell_P^2n
\]

and therefore

\[
\frac{S_n}{k_B}=2\pi n,
\]

\[
|I_{E,n}|=2\pi n\hbar,
\]

\[
E_{\rm geom}\tau_{\rm light}=n\hbar,
\]

\[
H_n^2=\frac{c^5}{2G\hbar n}.
\]

The remaining problem is state selection:

\[
\boxed{
\text{why one particular }n?
}
\]

Test whether a simple semiclassical gravitational path-integral weight has a finite preferred \(n\).

---

## 1. Euclidean de Sitter action on the conditional spectrum

EXP-054 gives

\[
I_E=-\hbar N.
\]

EXP-057 gives

\[
N=2\pi n.
\]

Therefore

\[
\boxed{
I_{E,n}
=
-2\pi n\hbar.
}
\]

The standard formal Euclidean saddle factor is

\[
e^{-I_E/\hbar}.
\]

Substituting the de Sitter saddle gives

\[
\boxed{
W_n
\propto
e^{2\pi n}.
}
\]

This grows monotonically with \(n\).

Hence there is no finite maximum.

### Result 058A

Under the naive Euclidean saddle weight,

\[
\boxed{
n\to\infty
}
\]

is favored rather than a finite large \(n\).

Since

\[
H_n^2\propto \frac1n,
\]

this is the familiar tendency toward the smallest positive curvature / \(\Lambda\to0^+\), not a prediction of a specific finite cosmological scale.

---

## 2. Opposite-sign weighting also fails to select a finite large n

Some quantum-cosmology boundary prescriptions / contour choices effectively reverse the relevant exponential preference.

If the weighting were instead schematically

\[
W_n\propto e^{-2\pi n},
\]

then it would monotonically prefer

\[
\boxed{
n=n_{\min}.
}
\]

That corresponds to Planckian/high curvature, not a finite huge late-time level.

Thus either pure exponential sign gives an endpoint of the spectrum:

\[
n\to\infty
\]

or

\[
n\to n_{\min}.
\]

Neither gives a finite interior optimum.

### Result 058B

\[
\boxed{
\text{a pure }e^{\pm2\pi n}\text{ weighting cannot select a finite large }n.
}
\]

---

## 3. A finite preferred n requires extra structure

To obtain a finite stationary level

\[
n_*
\]

one needs a nontrivial measure or correction,

\[
W(n)
=
\mu(n)e^{\pm2\pi n},
\]

with

\[
\frac{d}{dn}\ln W(n_*)=0.
\]

Therefore

\[
\boxed{
\frac{d}{dn}\ln\mu(n_*)
=
\mp2\pi.
}
\]

A finite selection requires additional state-counting, matter, topology, boundary, or quantum-correction structure whose \(n\)-dependence competes with the classical action.

This is new input unless derived independently.

---

## 4. Entropy degeneracy does not solve the problem

A horizon entropy

\[
S_n/k_B=2\pi n
\]

corresponds formally to a degeneracy

\[
g_n\sim e^{2\pi n}.
\]

This has the same monotonic exponential structure.

Therefore simply saying

\[
\text{"more states at larger horizon area"}
\]

does not select a finite \(n\).

It strengthens the large-\(n\) tendency.

A selection rule needs a competing constraint, not just degeneracy.

---

## 5. Euclidean-gravity caveat

The Euclidean gravitational path integral is not mathematically straightforward.

Its conformal-factor instability and contour dependence mean that the naive saddle weight should not be promoted to a fundamental probability law without specifying a contour / boundary-state prescription.

Recent work continues to treat these contour and phase issues as nontrivial.

Therefore EXP-058 should be read as a no-go for the **simplest weighting argument**, not as a complete theorem about quantum cosmology.

---

## 6. Connection to the active LTG problem

The project has now separated three logically different steps:

### Step 1 — quantize the allowed scales

Conditional area quantization can give

\[
H_n^2\propto1/n.
\]

### Step 2 — assign amplitudes to the allowed levels

A semiclassical path integral supplies a weighting, but the simplest exponential form is monotonic.

### Step 3 — select the occupied state

This remains unsolved.

A successful LTG mechanism must provide a finite-\(n\) selection principle from causal/global information.

---

## 7. Candidate mechanisms left after this no-go

A finite interior \(n_*\) could arise from:

1. a past-future boundary amplitude with competing early and late terms;
2. a matter/radiation contribution to the full causal-patch action;
3. a topological multiplicity that decreases at large \(n\);
4. a flux/area matching constraint;
5. a microcanonical global constraint rather than canonical/exponential weighting;
6. a transition dynamics among neighboring levels with detailed balance and a finite stationary distribution.

These are state-selection mechanisms, not merely quantization rules.

---

## 8. Terminal classification

### Does conditional area quantization discretize the vacuum scale?

**YES, conditionally.**

### Does the simplest Euclidean action weight select a finite level?

\[
\boxed{\text{NO}.}
\]

### Does reversing the exponential sign solve it?

\[
\boxed{\text{NO}.}
\]

### Strongest conclusion

\[
\boxed{
\text{quantization is not state selection}.
}
\]

A genuine LTG prediction now requires a global finite-\(n\) selection mechanism.

## Prior-art anchors

- Gibbons-Hawking Euclidean de Sitter action.
- Hartle-Hawking / tunneling quantum-cosmology boundary-condition literature gives different exponential preferences.
- Euclidean quantum gravity has a conformal-factor / contour problem, so no unique naive probability measure should be assumed.
