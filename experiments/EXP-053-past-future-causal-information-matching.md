# EXP-053 — Past-future causal information matching and scale selection

## Objective

Continue the global-causal proposal from EXP-049–051.

Ask whether the missing late-time vacuum scale \(H_*\) can be fixed by matching an early causal boundary to a future de Sitter horizon through a finite information/entropy budget.

---

## 1. Future de Sitter entropy as a scale equation

For a future de Sitter horizon,

\[
L_*=\frac{c}{H_*}.
\]

The horizon entropy is

\[
S_*
=
\frac{k_B A_*c^3}{4G\hbar}
=
\frac{\pi k_B c^5}{G\hbar H_*^2}.
\]

Define the dimensionless horizon information capacity

\[
N_*
\equiv
\frac{S_*}{k_B}.
\]

Then

\[
\boxed{
N_*
=
\frac{\pi c^5}{G\hbar H_*^2}.
}
\]

Invert:

\[
\boxed{
H_*^2
=
\frac{\pi c^5}{G\hbar N_*}.
}
\]

This is important:

> if a global causal principle uniquely fixes \(N_*\), then it uniquely fixes the asymptotic de Sitter scale.

So information capacity can mathematically replace \(\Lambda\) as the unknown global datum.

---

## 2. Present-scale magnitude

Using a representative asymptotic value

\[
H_*
\sim
H_0\sqrt{\Omega_\Lambda},
\]

one gets approximately

\[
\boxed{
N_*
\sim3.3\times10^{122}.
}
\]

Thus the observed late-time curvature scale corresponds to a causal-horizon information capacity of order

\[
10^{122}
\]

in natural entropy units.

---

## 3. Naive early-late entropy equality

A Planck-radius causal surface has

\[
L=\ell_P.
\]

Its Bekenstein-Hawking entropy is

\[
\frac{S_P}{k_B}
=
\pi.
\]

Therefore the simplest equality

\[
S_{\rm early}
=
S_{\rm future}
\]

between one Planck causal cell and the late de Sitter horizon would require

\[
\pi
\sim
10^{122},
\]

which is impossible.

### Result 053A

\[
\boxed{
\text{one-cell early entropy conservation}
\not\Rightarrow
\text{observed late de Sitter scale}.
}
\]

Simple equality is ruled out.

---

## 4. Generalized second law points in the opposite direction

The relevant cosmological entropy laws are monotonicity statements,

\[
\Delta S_{\rm gen}\ge0,
\]

not conservation laws.

Therefore a huge growth

\[
S_{\rm early}\ll S_{\rm future}
\]

is not itself problematic.

This means the desired global matching principle cannot simply be

\[
S_{\rm past}=S_{\rm future}.
\]

It must instead specify something like:

- a maximum information capacity;
- a number of independent boundary degrees of freedom;
- a covariant entropy bound;
- a global path-integral/state-counting condition;
- a topological or phase constraint.

---

## 5. Information-budget reformulation

Suppose some microscopic theory supplies a finite global integer or dimensionless number

\[
N_{\rm global}.
\]

If the future de Sitter horizon saturates that capacity,

\[
N_*=N_{\rm global},
\]

then

\[
\boxed{
H_*
=
\sqrt{
\frac{\pi c^5}{G\hbar N_{\rm global}}
}.
}
\]

This would solve the scale-selection gap exactly.

But unless the early/boundary theory predicts

\[
N_{\rm global},
\]

the reformulation merely renames the free parameter:

\[
\Lambda
\longleftrightarrow
N_{\rm global}^{-1}.
\]

### Result 053B

Finite information capacity can **parameterize** the dark-energy scale but does not explain it unless \(N_{\rm global}\) is independently derived.

---

## 6. Relation to the energy-time-area bridge

EXP-052 gives

\[
E_{\rm geom}\tau
=
\frac{\hbar}{2\pi}N.
\]

At the future de Sitter horizon,

\[
E_*
=
\frac{c^5}{2GH_*},
\]

\[
\tau_*=\frac1{H_*},
\]

so

\[
\boxed{
E_*\tau_*
=
\frac{\hbar}{2\pi}N_*.
}
\]

Thus the late vacuum curvature scale can equivalently be described by:

- horizon radius \(L_*\);
- Hubble scale \(H_*\);
- quasi-local energy \(E_*\);
- light-crossing time \(\tau_*\);
- entropy/information capacity \(N_*\).

These are not independent once a de Sitter causal patch is specified.

The unsolved quantity is the one global number selecting the patch size.

---

## 7. Comparison with known causal-entropy ideas

The idea that a positive cosmological constant corresponds to a finite observable entropy/information capacity is established in de Sitter holography and causal entropy-bound literature.

Causal-entropic approaches have also attempted to use entropy production in causal diamonds to constrain the observed cosmological constant.

Therefore an LTG novelty claim cannot be just

\[
\Lambda\leftrightarrow N^{-1}.
\]

It must derive \(N\) from the project's light/time/global-causal structure without anthropic weighting or a fitted parameter.

---

## 8. Terminal classification

### Does future causal information capacity fix H if N is known?

\[
\boxed{\text{YES}.}
\]

**ALGEBRAIC PASS.**

### Does a simple past-future entropy equality provide N?

\[
\boxed{\text{NO}.}
\]

**FAIL.**

### Does current LTG derive N from the hot early universe?

\[
\boxed{\text{NOT YET}.}
\]

### Active next gate

Search for a dimensionless global invariant that can determine

\[
N_{\rm global}
\]

from both boundaries.

Candidate classes:

1. a past-future causal-diamond action;
2. a quantized global phase/winding number;
3. an integrated null-boundary entropy/flux relation;
4. a topological invariant;
5. a finite Hilbert-space/state-counting rule.

The criterion is strict:

\[
\boxed{
N_{\rm global}
\text{ must be derived, not fitted.}
}
\]

## Prior-art anchors

- Gibbons-Hawking de Sitter entropy.
- Bousso covariant entropy bounds and N-bound.
- Causal entropic principle approaches to the cosmological constant.
- de Sitter holography / finite-information interpretations.
