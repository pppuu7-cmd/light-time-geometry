# EXP-097 — Spectator-factor no-go for deriving the total Hilbert capacity from local causal data

## Objective

Test whether the current LTG local causal/quantum laws can determine the total global Hilbert-space dimension

\[
D_{\rm tot}=\dim\mathcal H_{\rm tot}.
\]

The active local LTG structure is

\[
\frac{\tau_c\Delta Q_{\rm mod}}{\hbar}
=
\Delta\mathcal N_{\rm gen}
+
\frac{D(\rho\Vert\sigma)}{2\pi}.
\]

---

## 1. Add an inaccessible spectator factor

Let the accessible causal theory live on

\[
\mathcal H_A.
\]

Now enlarge the global Hilbert space to

\[
\boxed{
\mathcal H_{\rm tot}
=
\mathcal H_A\otimes\mathcal K,
}
\]

where \(\mathcal K\) is a spectator factor that is completely inaccessible to all observables in the causal region.

Take the two states used in the local quantum balance to be

\[
\rho_A,\sigma_A
\]

and extend them by the same spectator state \(\tau_K\):

\[
\rho_{\rm tot}
=
\rho_A\otimes\tau_K,
\]

\[
\sigma_{\rm tot}
=
\sigma_A\otimes\tau_K.
\]

---

## 2. Relative entropy is invariant

Quantum relative entropy is additive under tensor products:

\[
D(\rho_A\otimes\tau_K\Vert
\sigma_A\otimes\tau_K)
=
D(\rho_A\Vert\sigma_A)
+
D(\tau_K\Vert\tau_K).
\]

Since

\[
D(\tau_K\Vert\tau_K)=0,
\]

we have

\[
\boxed{
D(\rho_{\rm tot}\Vert\sigma_{\rm tot})
=
D(\rho_A\Vert\sigma_A).
}
\]

Thus the LTG quantum residual does not see the spectator sector.

---

## 3. Accessible observables are unchanged

For any causal observable

\[
O_A,
\]

extend it as

\[
O_{\rm tot}=O_A\otimes \mathbf1_K.
\]

Then

\[
\mathrm{Tr}(\rho_{\rm tot}O_{\rm tot})
=
\mathrm{Tr}(\rho_AO_A).
\]

Hence:

- modular/causal energy measurements;
- local stress tensor;
- causal horizon observables;
- relative entropy inside the accessible algebra;

are unchanged by \(\mathcal K\).

---

## 4. But the total Hilbert dimension changes

The global dimension becomes

\[
\boxed{
D_{\rm tot}
=
D_A D_K,
}
\]

where

\[
D_K=\dim\mathcal K
\]

can be chosen arbitrarily.

Therefore infinitely many different values of \(D_{\rm tot}\) are compatible with exactly the same local causal/quantum data.

### Result 097A — spectator no-go

\[
\boxed{
\text{local causal/quantum observables cannot determine }D_{\rm tot}.
}
\]

This is stronger than a dimensional-analysis argument.

It is an information-theoretic degeneracy.

---

## 5. Required new global axiom

Any theory that claims to derive \(D_{\rm tot}\) must include a principle that forbids or fixes invisible spectator sectors.

Examples of the required kind of statement are:

1. global Hilbert-space completeness;
2. no-spectator principle;
3. every fundamental degree of freedom is represented in the maximal causal algebra;
4. a global topology/state-space construction that fixes \(\mathcal H_{\rm tot}\).

Without such a principle,

\[
D_{\rm tot}
\]

is not an observable of the local LTG theory.

---

## 6. Dimensional-analysis corollary

Even after imposing no spectators, the constants

\[
G,\hbar,c
\]

alone generate only the Planck scale.

They cannot produce

\[
L_*/\ell_P\sim10^{61}
\]

or

\[
\ln D_{\rm tot}\sim10^{122}
\]

without an additional dimensionless hierarchy.

That hierarchy must arise from at least one of:

- a large integer/global count;
- an RG/transmutation mechanism;
- near-critical dynamics;
- a nontrivial microscopic coupling;
- a boundary/topological invariant.

---

## Terminal classification

### Local LTG derivation of \(D_{\rm tot}\)

\[
\boxed{\text{IMPOSSIBLE without extra global structure}.}
\]

### Exact missing ingredient

\[
\boxed{
\text{a global completeness/state-space principle}.
}
\]
