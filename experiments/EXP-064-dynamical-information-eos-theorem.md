# EXP-064 — Dynamical LTG information variable and equation-of-state theorem

## Objective

Test whether the common LTG horizon variable is merely a static algebraic rewriting or whether its evolution encodes cosmological dynamics.

Use the flat-FLRW apparent horizon

\[
R_A=\frac{c}{H}.
\]

Define

\[
\boxed{
\mathcal N_{\rm LTG}
\equiv
\frac{A_A}{8\pi\ell_P^2}
=
\frac{S_A}{2\pi k_B}
=
\frac{E_{\rm MS}\tau_A}{\hbar}
}
\]

with

\[
A_A=4\pi R_A^2,
\qquad
E_{\rm MS}=\frac{c^4R_A}{2G},
\qquad
\tau_A=\frac{R_A}{c}.
\]

Important: outside an equilibrium de Sitter saddle, the Euclidean-action equality

\[
|I_E|/(2\pi\hbar)=\mathcal N_{\rm LTG}
\]

is not automatically available. The dynamical theorem below uses only area, entropy and Misner-Sharp-energy/light-time terms.

---

## 1. Exact FLRW expression

Using

\[
\ell_P^2=\frac{G\hbar}{c^3},
\]

one obtains

\[
\boxed{
\mathcal N_{\rm LTG}
=
\frac{c^5}{2G\hbar H^2}.
}
\]

Thus the common horizon variable is exactly an inverse-Hubble-squared variable in flat FLRW.

---

## 2. Evolution equation

Differentiate:

\[
\frac{\dot{\mathcal N}}{\mathcal N}
=
-2\frac{\dot H}{H}.
\]

Since

\[
d\ln a=Hdt,
\]

we get

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}
=
-2\frac{\dot H}{H^2}.
}
\]

Define the Hubble slow-roll / deceleration variable

\[
\epsilon_H
\equiv
-\frac{\dot H}{H^2}.
\]

Then

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}
=
2\epsilon_H.
}
\]

---

## 3. Equation of state

For spatially flat Einstein-FLRW cosmology with total effective energy density \(\varepsilon\) and pressure \(p\),

\[
H^2
=
\frac{8\pi G}{3c^2}\varepsilon,
\]

\[
\dot H
=
-\frac{4\pi G}{c^2}(\varepsilon+p).
\]

Define

\[
w_{\rm eff}\equiv\frac{p}{\varepsilon}.
\]

Then

\[
-\frac{2\dot H}{H^2}
=
3(1+w_{\rm eff}).
\]

Therefore

\[
\boxed{
\frac{d\ln\mathcal N_{\rm LTG}}{d\ln a}
=
3(1+w_{\rm eff}).
}
\]

Equivalently,

\[
\boxed{
w_{\rm eff}
=
-1
+
\frac13
\frac{d\ln\mathcal N_{\rm LTG}}{d\ln a}.
}
\]

### Result 064A

The total effective equation of state can be reconstructed directly from the logarithmic growth rate of the LTG horizon-information variable.

This is an exact reparameterization of the flat-FLRW Einstein equations, not a new independent dynamical law.

---

## 4. Pressure-sign thresholds

The formula immediately gives sharp geometric-information thresholds.

### Radiation

\[
w=\frac13
\]

implies

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}=4.
}
\]

Thus

\[
\mathcal N\propto a^4.
\]

### Pressureless matter

\[
w=0
\]

implies

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}=3.
}
\]

Thus

\[
\mathcal N\propto a^3.
\]

### Negative pressure

\[
p<0
\quad\Longleftrightarrow\quad
w<0
\]

corresponds to

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}<3.
}
\]

### Accelerated expansion

\[
w<-\frac13
\]

corresponds to

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}<2.
}
\]

### de Sitter

\[
w=-1
\]

gives

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}=0,
}
\]

so

\[
\boxed{
\mathcal N=\text{const}.
}
\]

### Phantom branch

\[
w<-1
\]

would imply

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}<0,
}
\]

so the apparent-horizon information variable decreases.

---

## 5. Null-energy-condition interpretation

For the total effective fluid,

\[
\varepsilon+p\ge0
\]

is the null energy condition.

Using the Friedmann relation,

\[
\varepsilon+p\ge0
\quad\Longleftrightarrow\quad
\dot H\le0.
\]

Therefore

\[
\boxed{
\text{NEC}
\Longrightarrow
\dot{\mathcal N}_{\rm LTG}\ge0.
}
\]

Thus \(\mathcal N_{\rm LTG}\) is a monotonic geometric-information clock throughout the standard nonphantom branch.

### Result 064B

The monotonicity of the LTG variable is equivalent to apparent-horizon entropy growth under the NEC.

This is prior-art horizon thermodynamics written in the LTG normalization.

---

## 6. Direct relation to the user's pressure-sign hypothesis

The hypothesis was:

> the sign may change not in photon energy but in the system's response to geometry, especially pressure.

EXP-064 provides an exact geometric translation.

Photon energies can remain positive while the cosmic effective pressure changes sign at the point

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}=3.
}
\]

Acceleration begins at

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}=2.
}
\]

The de Sitter vacuum-like endpoint is

\[
\boxed{
\frac{d\ln\mathcal N}{d\ln a}=0.
}
\]

So the pressure sign is encoded in the **growth rate of geometric/information capacity**, not in a sign flip of particle energy.

---

## 7. Redshift form

Because

\[
a=(1+z)^{-1},
\]

we have

\[
\frac{d\ln\mathcal N}{d\ln a}
=
-\frac{d\ln\mathcal N}{d\ln(1+z)}.
\]

Hence

\[
\boxed{
w_{\rm eff}(z)
=
-1
-
\frac13
\frac{d\ln\mathcal N}{d\ln(1+z)}.
}
\]

Since

\[
\mathcal N(z)\propto H(z)^{-2},
\]

this contains no observational information beyond the expansion history \(H(z)\), but gives the unified LTG variable a direct dynamical interpretation.

---

## 8. Constant-w solutions

For constant \(w>-1\),

\[
H\propto a^{-\frac32(1+w)}.
\]

Therefore

\[
\boxed{
\mathcal N_{\rm LTG}
\propto
a^{3(1+w)}.
}
\]

This reproduces:

\[
\mathcal N\propto a^4
\quad
\text{for radiation},
\]

\[
\mathcal N\propto a^3
\quad
\text{for matter},
\]

and

\[
\mathcal N=\text{constant}
\quad
\text{for de Sitter}.
\]

---

## 9. Terminal classification

### Is the LTG common variable dynamically meaningful?

\[
\boxed{\text{YES}.}
\]

It exactly encodes \(H(t)\) and therefore the total equation of state in flat Einstein-FLRW cosmology.

### Is this independent new dynamics?

\[
\boxed{\text{NO}.}
\]

It is an exact reformulation of Friedmann dynamics / apparent-horizon thermodynamics.

### Does it sharpen the pressure-sign hypothesis?

\[
\boxed{\text{YES}.}
\]

The pressure sign and acceleration threshold become geometric-information growth thresholds.

## Strongest result

\[
\boxed{
w_{\rm eff}
=
-1
+
\frac13
\frac{d\ln\mathcal N_{\rm LTG}}{d\ln a}.
}
\]

A genuine LTG advance would require a new law for \(\mathcal N_{\rm LTG}(a)\) that is not merely equivalent to the Friedmann equations.
