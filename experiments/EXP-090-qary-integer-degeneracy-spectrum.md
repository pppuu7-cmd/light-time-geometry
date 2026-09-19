# EXP-090 — Integer-degeneracy sector quantization and the q-ary LTG spectrum

## Objective

Test whether the LTG sector label can be interpreted literally as a finite Hilbert-space capacity.

The previous conditional spectrum used

\[
S_n/k_B=2\pi\alpha n.
\]

If a sector has a finite number of microstates,

\[
g_n=\dim\mathcal H_n,
\]

then

\[
S_n=k_B\ln g_n
\]

requires \(g_n\) to be an integer.

This gate imposes that requirement exactly.

---

## 1. Exact multiplicative degeneracy

Assume each elementary capacity step multiplies the number of states by an integer

\[
q\ge2.
\]

Then

\[
\boxed{
g_n=q^n.
}
\]

Therefore

\[
\boxed{
\frac{S_n}{k_B}=n\ln q.
}
\]

This is the Bekenstein-Mukhanov-type degeneracy structure.

---

## 2. Area spectrum

Using the Bekenstein-Hawking relation

\[
\frac{S_n}{k_B}
=
\frac{A_n}{4\ell_P^2},
\]

we obtain

\[
\boxed{
A_n
=
4\ell_P^2\,n\ln q.
}
\]

Thus exact finite-state degeneracy prefers a logarithmic-integer area quantum,

\[
\boxed{
\Delta A
=
4\ell_P^2\ln q,
}
\]

rather than forcing the semiclassical \(8\pi\ell_P^2\) spacing.

---

## 3. Unified q-ary LTG formula

For stationary de Sitter,

\[
\frac{|I_E|}{\hbar}
=
\frac{S}{k_B}
\]

and

\[
\frac{E_{\rm geom}\tau_{\rm light}}{\hbar}
=
\frac{1}{2\pi}\frac{S}{k_B}.
\]

Therefore

\[
\boxed{
\frac{A_n}{4\ell_P^2\ln q}
=
\frac{S_n}{k_B\ln q}
=
\frac{|I_{E,n}|}{\hbar\ln q}
=
\frac{2\pi E_{\rm geom}\tau_{\rm light}}
{\hbar\ln q}
=
n.
}
\]

### Result 090A

This is the cleanest LTG integer formula if the integer is required to count exact finite-state multiplicative capacity.

The previous formula with

\[
A_n=8\pi\ell_P^2n
\]

is recovered only if one formally chooses

\[
\ln q=2\pi,
\]

i.e.

\[
q=e^{2\pi},
\]

which is not an integer.

Therefore the \(8\pi\) spectrum and exact finite Hilbert-space degeneracy cannot both be literal exact statements.

---

## 4. Cosmological scale spectrum

For a de Sitter horizon,

\[
A_n
=
\frac{4\pi c^2}{H_n^2}.
\]

Equating to the q-ary area spectrum gives

\[
\frac{4\pi c^2}{H_n^2}
=
4\ell_P^2n\ln q.
\]

Therefore

\[
\boxed{
H_n^2
=
\frac{\pi c^5}
{G\hbar\,n\ln q}.
}
\]

Equivalently,

\[
\boxed{
\Lambda_n
=
\frac{3\pi c^3}
{G\hbar\,n\ln q}.
}
\]

Again the large-scale problem becomes selection of the occupied level \(n\) and the microscopic alphabet size \(q\).

---

## 5. Detailed balance

For adjacent sectors,

\[
\Delta S
=
k_B\ln q.
\]

Therefore de Sitter detailed balance gives

\[
\boxed{
\frac{\Gamma_{n\to n+1}}
{\Gamma_{n+1\to n}}
=
e^{\Delta S/k_B}
=
q.
}
\]

This is conceptually cleaner than a noninteger ratio \(e^{2\pi\alpha}\).

The direction ratio is now exactly the state-multiplicity ratio.

---

## 6. Minimal binary sector

The smallest nontrivial exact capacity multiplier is

\[
\boxed{
q=2.
}
\]

Then each step adds one bit:

\[
\boxed{
\Delta S=k_B\ln2.
}
\]

The corresponding area quantum is

\[
\boxed{
\Delta A=4\ell_P^2\ln2.
}
\]

And detailed balance becomes

\[
\boxed{
\Gamma_+/\Gamma_-=2.
}
\]

This binary choice is minimal but is **not derived uniquely** by causal geometry.

---

## 7. Prior-art boundary

The logic

\[
\text{equally spaced area}
+
S=\ln(\text{integer degeneracy})
\]

leading to exponentially degenerate levels and logarithmic-integer spacing is Bekenstein-Mukhanov prior art.

Some algebraic black-hole models specifically obtain binary degeneracy.

LTG's contribution is to insert this exact microstate-counting normalization into the broader geometry-information-action-energy-time identity.

---

## 8. Terminal classification

### Exact finite Hilbert-space interpretation of \(S_n\)

\[
\boxed{\text{requires integer degeneracy}.}
\]

### \(8\pi\) spectrum plus exact finite degeneracy

\[
\boxed{\text{INCOMPATIBLE as literal exact statements}.}
\]

### q-ary unified formula

\[
\boxed{\text{ANALYTIC PASS / PRIOR-ART QUANTIZATION FOUNDATION}.}
\]

### Unique \(q\)

\[
\boxed{\text{NOT DERIVED}.}
\]

## Active next gate

Test whether the causal temperature and generalized action cost select the minimal binary \(q=2\) through a Landauer-type principle, or whether \(q\) remains arbitrary.
