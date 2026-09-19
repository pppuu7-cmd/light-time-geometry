# EXP-044 terminal result — causal geometry / photon-to-dark-energy transfer

## Authority

Experiment:

- \`experiments/EXP-044-causal-geometry-photon-dark-energy-transfer.md\`
- commit: \`91701f4198f3d64f7d78d7158a710d9b7f508856\`

Deterministic numeric check:

- \`experiments/exp044_numeric_check.py\`
- commit: \`02fa6164cc3f42de9e7522a6384f6a3747c1a2c2\`

EXP-043 equation formatting repair:

- commit: \`4ec466c3187c83eccb645181627c695172d36808\`

## Reproduced numeric output

\`\`\`text
H0_s^-1=2.184285241433e-18
hbar_H0_eV=1.437722663192e-33
mean_CMB_photon_eV=6.343714941687e-04
CMB_to_hbarH_ratio=4.412335636141e+29
required_efolds=68.259371869
asymptotic_deSitter_years=1.196475150778e+12
OmegaLambda_over_OmegaGamma=1.273234200743e+04
Gamma_from_recombination=3.607963951706e-08
temperature_exponent_shift=9.019909879265e-09
\`\`\`

The execution above was reproduced against the deterministic standard-library script. It is a numerical consistency check, not an immutable GitHub Actions artifact.

## Scientific terminal classification

### 044A — minimal Einstein-Maxwell conversion

\[
\boxed{Q^\nu_{\rm geom}=0}
\]

for source-free Maxwell radiation in spatially flat FLRW.

**CLASSIFICATION: ANALYTIC FAIL** for the claim that ordinary expansion by itself converts photon energy into a dark-energy sector.

### 044B — local curvature coupling

A nonzero exchange can be written only after adding a coupling function, scale, field, or higher-dimension coefficient.

**CLASSIFICATION: OPEN BUT NON-UNIQUE / PRIOR-ART MAPPED.**

### 044C — horizon crossing

Dimensional analysis naturally allows

\[
Q_H\sim C_H H\rho_\gamma,
\]

but the coefficient and observer-independent covariant meaning are not fixed by horizon crossing alone.

**CLASSIFICATION: NOT DERIVED.**

### 044D — threshold \(E_*=\hbar H\)

For a typical present CMB photon,

\[
\frac{E_\gamma}{\hbar H_0}
\simeq4.4\times10^{29}.
\]

An asymptotic-de-Sitter estimate gives about 68.3 further e-folds, of order \(1.2\times10^{12}\) years, before such a photon reaches \(E\sim\hbar H\).

**CLASSIFICATION: DISFAVORED AS AN EXPLANATION OF PRESENT DARK ENERGY.**

### 044E — interacting benchmark

For

\[
Q=\Gamma H\rho_\gamma,
\qquad
w_X=-1,
\]

the model can mathematically generate an asymptotically constant \(\rho_X\).

Using recombination as an illustrative start boundary gives

\[
\Gamma\simeq3.61\times10^{-8}.
\]

But the result depends strongly on the arbitrary start scale \(a_i\), and the formal \(a_i\to0\) limit is divergent.

**CLASSIFICATION: MATHEMATICALLY VIABLE BUT UNDERDETERMINED.**

### 044F — global causal / horizon energy

The natural global scaling

\[
\rho_X\sim M_{\rm Pl}^2L^{-2}
\]

maps to holographic dark energy. Hubble-horizon and future-event-horizon choices have established prior art and introduce model choices / dimensionless parameters.

**CLASSIFICATION: PHYSICALLY VIABLE DIRECTION, NOT YET LTG-NOVEL.**

## Updated surviving hypothesis

The original chain

\[
\text{photon redshift}
\to
E=0
\to
E<0
\to
\text{dark energy}
\]

does not survive.

The strongest surviving descendant is

\[
\boxed{
\text{global null/causal geometry}
\stackrel{?}{\Longrightarrow}
\text{an IR/horizon sector}
}
\]

with a required derivation of

\[
\{L,\ c,\ Q^\mu,\ w_X\}
\]

rather than free insertion of those quantities.

The next novelty gate should attempt to derive a unique dimensionless coefficient or boundary condition from null/causal geometry and compare it directly against holographic-dark-energy prior art.
