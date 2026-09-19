# EXP-085 — Controlled CFT causal-diamond test of area-extensive relative entropy

## Objective

EXP-083–084 require a gravitational relative-entropy residual with area scaling,

\[
D_{\rm grav}\sim A/\ell_P^2.
\]

Test whether ordinary local QFT in a causal diamond produces such scaling automatically.

Use the exact vacuum modular Hamiltonian of a ball in a four-dimensional conformal field theory.

---

## 1. Modular Hamiltonian of a CFT ball

For a ball of radius \(R\) in Minkowski vacuum, the modular Hamiltonian is

\[
\boxed{
K_B
=
2\pi
\int_{r<R}
d^3x\,
\frac{R^2-r^2}{2R}
T_{00}(x).
}
\]

This is an exact local modular Hamiltonian for the vacuum reduced to the ball.

---

## 2. Uniform small energy-density perturbation

Take a perturbation with approximately constant

\[
\delta\langle T_{00}\rangle
=
\delta\rho
\]

across the ball.

The geometric weight integral is

\[
\int_{r<R}
d^3x\,
\frac{R^2-r^2}{2R}
=
\frac{4\pi R^4}{15}.
\]

Therefore

\[
\boxed{
\delta\langle K_B\rangle
=
\frac{8\pi^2}{15}
R^4\delta\rho.
}
\]

By the entanglement first law,

\[
\boxed{
\delta S
=
\delta\langle K_B\rangle
}
\]

at first order.

### Result 085A

The ordinary local-QFT entropy response of a 4D causal diamond scales as

\[
\boxed{
\delta S\sim R^4\delta\rho,
}
\]

not universally as horizon area

\[
R^2.
\]

---

## 3. What density would be required for area scaling?

The LTG/gravitational target is

\[
\delta S_{\rm grav}
\sim
\frac{R^2}{G\hbar}.
\]

Set

\[
R^4\delta\rho
\sim
\frac{R^2}{G\hbar}.
\]

Then

\[
\boxed{
\delta\rho
\sim
\frac{1}{G\hbar R^2}.
}
\]

Restoring the conventional gravitational units gives precisely the curvature/critical-density scaling class

\[
\boxed{
\rho
\sim
\frac{1}{GR^2}.
}
\]

### Result 085B

Using ordinary local matter entropy to *derive* the holographic vacuum scale is circular:

\[
\text{area scaling}
\]

appears only if the perturbation density is already chosen to scale as

\[
1/(GR^2).
\]

---

## 4. Relative entropy begins at second order

For a nearby state,

\[
D(\rho\Vert\sigma)
=
\Delta\langle K\rangle-\Delta S.
\]

The first-order pieces cancel:

\[
D=O(\delta\rho^2).
\]

Its coefficient is determined by the quantum Fisher/Kubo-Mori metric and stress-tensor correlation functions.

Therefore no universal first-order area coefficient

\[
\eta
\]

comes from the matter CFT ball.

### Result 085C

The required area-extensive \(D_{\rm grav}\) is not a generic matter-QFT relative entropy.

---

## 5. Consequence for LTG

The microscopic source of

\[
D_{\rm grav}\propto A/\ell_P^2
\]

must involve specifically gravitational structures such as:

1. edge modes / boundary completion;
2. horizon microstates;
3. non-factorization constraints;
4. holographic code subspaces;
5. generalized entropy area terms;
6. a genuinely nonlocal gravitational state.

This narrows the theory target substantially.

---

## 6. Connection to entanglement-equilibrium gravity

Entanglement-equilibrium derivations combine:

- the matter modular-energy variation
  \[
  \delta S_{\rm matter}\sim R^4\delta\rho;
  \]
- the geometric area variation
  \[
  \delta A/G\hbar.
  \]

Their stationarity gives the Einstein equation.

Thus the fact that matter and geometric terms have different primitive scaling is not a defect; it is precisely what gravity balances.

LTG should therefore not try to identify the whole dark-energy area term with ordinary matter entanglement.

---

## 7. Terminal classification

### Ordinary local CFT relative entropy automatically area extensive

\[
\boxed{\text{NO}.}
\]

### Matter causal-diamond first law

\[
\boxed{
\delta S
=
\frac{8\pi^2}{15}R^4\delta\rho
}
\]

**CONTROLLED PASS.**

### LTG implication

\[
\boxed{
\text{the required area residual must be gravitational/boundary,
not generic local matter QFT.}
}
\]

## Active next gate

The remaining microscopic target is a gravitational boundary algebra whose relative entropy is finite and area extensive.

Candidate controlled settings include:

- semiclassical gravity with edge modes;
- holographic code subspaces where relative entropy has a bulk/boundary equality;
- de Sitter static-patch generalized entropy.

The test is whether any such setting fixes the coefficient \(\eta\) rather than merely allowing area scaling.
