# EXP-083 — Boundary-extensive relative entropy and holographic dark-energy mapping

## Objective

EXP-082 proved that a positive local bulk-extensive relative-entropy residual gives the wrong vacuum scale.

Test the required alternative:

\[
\boxed{
D_{\rm grav}
=
\eta
\frac{A}{\ell_P^2},
}
\]

where \(\eta\) is a dimensionless relative-entropy density per horizon Planck area.

Determine the induced vacuum-density scaling and whether it produces new LTG physics or maps to holographic dark energy (HDE).

Work in natural units \(c=1\) with \(\ell_P^2=G\hbar\).

---

## 1. Irreversibility action

From EXP-077,

\[
\boxed{
I_{\rm irr}
=
\frac{\hbar}{2\pi}D_{\rm grav}.
}
\]

Assume the global residual can be represented as an effective vacuum action over a causal four-volume

\[
V_4=C_4L^4.
\]

Let the horizon area be

\[
A=C_A L^2.
\]

Then

\[
\rho_X
\equiv
\frac{I_{\rm irr}}{V_4}
=
\frac{\hbar}{2\pi}
\frac{\eta C_A L^2/\ell_P^2}
{C_4L^4}.
\]

Using

\[
\ell_P^2=G\hbar,
\]

we obtain

\[
\boxed{
\rho_X
=
\frac{\eta C_A}{2\pi C_4}
\frac{1}{GL^2}.
}
\]

### Result 083A

A boundary-extensive positive quantum-information residual automatically generates the infrared scaling

\[
\boxed{
\rho_X\propto M_P^2L^{-2}.
}
\]

This is exactly the holographic-dark-energy scaling class.

---

## 2. Euclidean de Sitter / thermal-cell normalization

For the Euclidean \(S^4\),

\[
C_A=4\pi,
\qquad
C_4=\frac{8\pi^2}{3}.
\]

Then

\[
\boxed{
\rho_X
=
\frac{3\eta}{4\pi^2}
\frac{1}{GL^2}.
}
\]

The standard HDE parameterization is

\[
\rho_{\rm HDE}
=
\frac{3c_H^2}{8\pi G L^2}.
\]

Therefore

\[
\boxed{
c_H^2
=
\frac{2\eta}{\pi}.
}
\]

### Result 083B — information/HDE map

\[
\boxed{
\eta
=
\frac{\pi}{2}c_H^2.
}
\]

The HDE coefficient can be interpreted, within this hypothesis, as a relative-entropy density per horizon area.

---

## 3. Exact de Sitter normalization

For a pure de Sitter state with the horizon sector saturating the total critical density,

\[
c_H^2=1.
\]

Therefore

\[
\boxed{
\eta_{\rm dS}
=
\frac{\pi}{2}.
}
\]

So a microscopic quantum-boundary calculation yielding

\[
D_{\rm grav}
=
\frac{\pi}{2}
\frac{A}{\ell_P^2}
\]

would reproduce the exact de Sitter vacuum-action normalization in this convention.

This is a **target**, not a derived relative entropy.

---

## 4. Hubble-horizon test

Choose

\[
L=H^{-1}.
\]

Then

\[
\rho_X
=
\frac{3c_H^2H^2}{8\pi G}.
\]

The critical density is

\[
\rho_c
=
\frac{3H^2}{8\pi G}.
\]

Hence

\[
\boxed{
\Omega_X=c_H^2=\frac{2\eta}{\pi}.
}
\]

If \(\eta\) is constant, then

\[
\boxed{
\Omega_X=\text{constant}.
}
\]

Therefore a constant boundary relative-entropy density with the Hubble horizon cannot by itself produce the observed transition from radiation/matter domination to late dark-energy domination.

### Result 083C

\[
\boxed{
L=H^{-1}
+
\eta=\text{constant}
\Rightarrow
\text{standard Hubble-cutoff HDE problem}.
}
\]

This maps to known HDE prior art.

---

## 5. Future-event-horizon test

Take

\[
L
=
a(t)
\int_t^\infty
\frac{dt'}{a(t')}.
\]

Then

\[
\dot L=HL-1.
\]

For

\[
\rho_X\propto\eta L^{-2},
\]

separate conservation gives

\[
w_X
=
-1
-
\frac13
\frac{d\ln\rho_X}{d\ln a}.
\]

Therefore

\[
\boxed{
w_X
=
-\frac13
-
\frac{2}{3HL}
-
\frac13
\frac{d\ln\eta}{d\ln a}.
}
\]

For constant \(\eta\),

\[
\boxed{
w_X
=
-\frac13-\frac{2}{3HL},
}
\]

which is exactly the standard future-event-horizon HDE structure.

### Result 083D

The constant-\(\eta\) global-horizon branch is not new; it reproduces known HDE dynamics.

---

## 6. Where genuinely new LTG content could enter

The only new quantity in this reformulation is

\[
\boxed{
\eta(a)
\equiv
\frac{\ell_P^2}{A}
D_{\rm grav}(a).
}
\]

If LTG independently computes \(D_{\rm grav}\) from the quantum state, then it predicts:

\[
\boxed{
c_H^2(a)=\frac{2\eta(a)}{\pi}.
}
\]

This would replace the phenomenological HDE coefficient by a quantum-information observable.

That would be genuine new content.

---

## 7. Observable relation

For the Hubble-horizon version,

\[
\boxed{
\Omega_X(a)
=
\frac{2}{\pi}
\eta(a)
=
\frac{2\ell_P^2}{\pi A}
D_{\rm grav}(a).
}
\]

Thus measurements of the dark-energy fraction specify the boundary-relative-entropy density required by the model.

Conversely, an independent microscopic computation of \(D_{\rm grav}(a)\) would predict \(\Omega_X(a)\).

The crucial word is **independent**.

Using cosmological data to infer \(D_{\rm grav}\) is only a reparameterization.

---

## 8. Terminal classification

### Correct IR vacuum scaling

\[
\boxed{\text{PASS}.}
\]

### Positive sign

\[
\boxed{\text{PASS}}
\]

under the effective-vacuum-action identification because \(D_{\rm grav}\ge0\).

### Constant coefficient as new cosmology

\[
\boxed{\text{FAIL / HDE PRIOR ART}.}
\]

### New LTG opportunity

\[
\boxed{
\text{derive }
\eta(a)=\ell_P^2D_{\rm grav}/A
\text{ microscopically}.
}
\]

That is now a precise, falsifiable target.

## Prior-art boundary

Holographic dark energy already gives \(\rho\sim M_P^2L^{-2}\) with a dimensionless coefficient and known choices of IR cutoff.

LTG becomes distinct only if the coefficient and its evolution are calculated from independently defined causal quantum relative entropy rather than fitted.
