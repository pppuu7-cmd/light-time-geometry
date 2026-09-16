# EXP-011 — Single-action closure test

## Objective

Test whether the three strongest LTG relations found so far

1. null versus timelike mass shell;
2. mass contribution to the 4D stress-energy trace;
3. geometric/radion response to the massive sector;

can arise from one invariant action rather than being connected by separate phenomenological assumptions.

## 1. Minimal higher-dimensional action

Consider the standard 5D Einstein–Hilbert action plus a massless scalar field:

\[
S_5=\int d^5x\sqrt{-G}\left[
\frac{M_5^3}{2}R_5
-\frac12G^{AB}\partial_A\Phi\partial_B\Phi
\right].
\]

Take

\[
dS_5^2=g_{\mu\nu}(x)dx^\mu dx^\nu+b(x)^2d\psi^2,
\]

with a compact coordinate `psi` of fixed coordinate period `2 pi R0`.

This action contains no explicit 5D matter mass.

## 2. Mode decomposition

Expand the massless 5D field in hidden-direction modes:

\[
\Phi(x,\psi)=\sum_n\phi_n(x)e^{in\psi/R_0}.
\]

Then

\[
\partial_\psi\Phi_n=\frac{in}{R_0}\Phi_n.
\]

The hidden-gradient contribution to the reduced 4D action is proportional to

\[
\frac{n^2}{b^2R_0^2}|\phi_n|^2.
\]

After canonical normalization, and for slowly varying or fixed `b`, the corresponding 4D mass scale is

\[
\boxed{
m_n^2c^2/\hbar^2=\frac{n^2}{b^2R_0^2}
}
\]

or

\[
\boxed{
m_n=\frac{|n|\hbar}{cbR_0}.
}
\]

Thus a **massless higher-dimensional action already contains both 4D sectors**:

\[
n=0\Rightarrow m_0=0,
\]

\[
n\neq0\Rightarrow m_n>0.
\]

No extra mass-generation postulate is required for the KK modes.

## 3. Mass shell from the same action

In the geometric-optics/WKB limit,

\[
\Phi\sim A e^{i\mathcal S/\hbar},
\]

the leading field equation gives the 5D Hamilton–Jacobi/eikonal condition

\[
G^{AB}\partial_A\mathcal S\partial_B\mathcal S=0.
\]

Writing

\[
\partial_\psi\mathcal S=p_\psi,
\]

gives

\[
g^{\mu\nu}p_\mu p_\nu+\frac{p_\psi^2}{b^2}=0.
\]

Therefore

\[
\boxed{
g^{\mu\nu}p_\mu p_\nu=-m_{\rm eff}^2c^2,
\qquad
m_{\rm eff}c=|p_\psi|/b.
}
\]

The null/timelike distinction is therefore encoded in the hidden momentum sector of the same field theory.

## 4. Stress-energy from the same reduced action

The 4D stress tensor is obtained by varying the reduced matter action with respect to `g_{mu nu}`:

\[
T_{\mu\nu}
=-\frac{2}{\sqrt{-g}}
\frac{\delta S_{m,4}}{\delta g^{\mu\nu}}.
\]

The hidden-gradient term that becomes the 4D mass term contributes explicitly to the 4D stress tensor and its trace.

For a relativistic ensemble of massless `n=0` quanta, the perfect-fluid limit has

\[
P=\rho/3,
\qquad T=0.
\]

For a nonrelativistic ensemble of massive `n != 0` modes,

\[
P\ll\rho,
\qquad T\simeq-\rho.
\]

Thus the same hidden momentum that produces the 4D mass shell also produces the standard transition from an approximately trace-free radiation fluid to a traceful massive fluid in the appropriate kinetic limits.

This statement concerns the ensemble/fluid limit; the local trace of a particular scalar-field stress tensor depends on the chosen curvature coupling and improvement term.

## 5. Radion equation from the same action

The compactification factor `b(x)` is part of the 5D metric, so its equation of motion follows by varying the same action with respect to the internal metric component.

The KK mass satisfies

\[
m_n^2\propto b^{-2}.
\]

Therefore the reduced matter action contains a source of the schematic form

\[
\frac{\partial m_n^2}{\partial b}|\phi_n|^2
\propto
-\frac{m_n^2}{b}|\phi_n|^2.
\]

After transformation to a canonically normalized 4D radion `sigma`, this becomes the familiar scalar–tensor structure in which the radion couples to a matter trace/source.

Hence the chain

\[
\boxed{
p_\psi\neq0
\Rightarrow m_{4D}\neq0
\Rightarrow \text{mass contribution to }T
\Rightarrow \text{radion/geometric source}
}
\]

can be derived from **one higher-dimensional action**.

## 6. What this accomplishes

This removes an important weakness in the earlier LTG reasoning: the mass-shell, stress trace, and geometric response no longer need to be joined by verbal analogy. They can all be descendants of one variational principle.

A concise structural chain is

\[
S_5[G,\Phi]
\longrightarrow
\begin{cases}
G^{AB}P_AP_B=0,\\
m_n\sim |p_\psi|/b,\\
T_{\mu\nu}^{(n)},\\
\text{radion equation},\\
G_{\mu\nu}^{(4)}=8\pi G_4T_{\mu\nu}^{\rm eff}.
\end{cases}
\]

## 7. Novelty test

Unfortunately for a novelty claim, the action used above is simply standard higher-dimensional Einstein gravity plus a massless field, and its dimensional reduction is standard Kaluza–Klein/radion physics.

Therefore:

### F-011A

**Yes, one invariant action can generate the entire current LTG chain.**

### F-011B

**No new LTG invariant is required to do so.**

At this stage the strongest coherent formulation of LTG is therefore a unifying interpretation of known higher-dimensional structures, not yet a new theory.

## 8. Where genuine novelty could still enter

A new theory would require a minimal extra invariant not removable by field redefinition or standard dimensional reduction. Candidate classes include:

1. a new constraint coupling hidden momentum to 4D curvature;
2. a nonstandard but covariant kinetic relation between the internal scale `b` and the external expansion scalar;
3. a topological or quantum condition fixing the hidden momentum spectrum from 4D causal geometry;
4. a new dimensionless observable that survives stabilization and frame transformations.

Any candidate must be tested first for equivalence to standard scalar–tensor, Kaluza–Klein, Horndeski/DHOST, induced-matter, and modified-gravity constructions.

## Next experiment

Instead of adding arbitrary terms, derive the **lowest-order generally covariant scalar invariants** capable of coupling hidden momentum/internal geometry to 4D expansion, then classify which are already contained in established effective field theory.

That is the natural EXP-012 novelty search.
