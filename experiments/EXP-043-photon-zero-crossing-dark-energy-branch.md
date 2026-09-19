# EXP-043 — Cosmological photon zero-crossing and dark-energy branch test

## Objective

Test the hypothesis:

> Cosmological expansion stretches a photon until its measured energy reaches zero; continued geometric evolution then drives the photon onto a negative-energy branch, and that branch may behave as dark energy while the photon continues propagating outside our observable region.

The test is split into four gates:

1. Can ordinary FLRW redshift drive a future-directed photon through (E=0)?
2. If a negative photon-energy branch is imposed, does it have the stress-energy of dark energy?
3. Is crossing a cosmological horizon related to an energy-sign flip?
4. Can a consistent radiation-to-vacuum conversion model be written, and what new ingredient does it require?

## 1. Geometric redshift in FLRW

For spatially flat FLRW,

[
ds^2=-dt^2+a(t)^2 dmathbf{x}^2.
]

For a comoving observer (u^mu=(1,0,0,0)), the measured photon energy is

[
E=-p_mu u^mu.
]

Spatial translation symmetry gives a conserved comoving momentum magnitude (q>0). For a future-directed null geodesic,

[
p^mu p_mu=0,
qquad
E(t)=rac{q}{a(t)}.
]

Equivalently,

[
dot E=-HE,
qquad
H=rac{dot a}{a}.
]

Hence

[
E(t)=E(t_i)expleft[-int_{t_i}^{t}H(t'),dt'ight].
]

If (E(t_i)>0), then for every finite real integral,

[
E(t)>0.
]

If (a(t)	oinfty), then (E(t)	o0^+), but ordinary FLRW redshift does not continue the solution to (E<0).

### Result 043A

[
oxed{
	ext{FLRW redshift alone cannot cause }E>0	o0	o E<0.
}
]

The sign of (E) is preserved by the evolution equation.

## 2. Negative photon-energy branch

Assume phenomenologically a photon-like component with negative energy density.

For an isotropic massless ensemble,

[
p_gamma=rac13ho_gamma,
qquad
w_gamma=rac{p_gamma}{ho_gamma}=rac13.
]

If (ho_-<0), then (p_-=ho_-/3<0), but still

[
w_-=rac13.
]

Covariant conservation gives

[
dotho_-+4Hho_-=0,
]

so

[
ho_-(a)=ho_{-,0}a^{-4}.
]

A cosmological constant instead has

[
p_Lambda=-ho_Lambda,
qquad
w_Lambda=-1,
qquad
ho_Lambda=	ext{const}.
]

Therefore a sign-flipped photon fluid is not ordinary vacuum dark energy.

The FLRW acceleration equation is

[
rac{ddot a}{a}
=
-rac{4pi G}{3}
sum_i(ho_i+3p_i).
]

For negative radiation,

[
ho_-+3p_-=2ho_-<0,
]

so its formal contribution is accelerating. However its magnitude decays as (a^{-4}), so it does not provide a persistent late-time vacuum-like component.

### Result 043B

A negative-energy photon-like fluid can formally contribute with the accelerating sign, but

[
w=rac13,
qquad
|ho|propto a^{-4},
]

so it does not reproduce persistent dark energy.

## 3. Horizon crossing

A cosmological horizon is a causal-accessibility boundary.

The local energy measured by an observer is

[
E_{m obs}=-p_mu u^mu.
]

For a future-directed photon and a future-directed local timelike observer,

[
E_{m obs}>0.
]

A photon becoming permanently unobservable to us does not imply that its locally measured energy becomes zero or negative.

Thus

[
oxed{
	ext{cosmological-horizon crossing}

otRightarrow
	ext{photon-energy sign reversal}.
}
]

Negative conserved energies can arise in special stationary geometries such as ergoregions, but that is a different mechanism and not ordinary FLRW redshift.

## 4. Minimal conversion model

A distinct hypothesis can be written as

[
gammalongrightarrow X,
]

where (X) is a new vacuum-like degree of freedom rather than a negative-energy continuation of the same photon.

Use

[
dotho_gamma+4Hho_gamma=-Q,
]

[
dotho_X+3H(1+w_X)ho_X=Q.
]

Total stress-energy remains conserved.

For dark-energy-like behavior require approximately

[
w_Xsimeq-1.
]

As a minimal phenomenological example,

[
Q=Gamma Hho_gamma,
qquad
Gammage0.
]

Then

[
rac{dho_gamma}{dln a}
=-(4+Gamma)ho_gamma,
]

hence

[
ho_gamma(a)
=
ho_{gamma,i}
left(rac{a}{a_i}ight)^{-(4+Gamma)}.
]

For (w_X=-1),

[
rac{dho_X}{dln a}
=
Gammaho_gamma,
]

which gives

[
ho_X(a)
=
ho_{X,i}
+
rac{Gamma}{4+Gamma}ho_{gamma,i}
left[
1-
left(rac{a}{a_i}ight)^{-(4+Gamma)}
ight].
]

Thus a radiation reservoir can mathematically feed a component that asymptotes to a constant energy density.

But this requires three genuinely new ingredients:

1. a nonzero interaction (Q);
2. a distinct component (X);
3. an equation of state (w_Xsimeq-1).

This does not follow from ordinary redshift (dot E=-HE).

### Result 043C

[
oxed{
	ext{radiation}	o	ext{vacuum-like energy}
}
]

is mathematically consistent as an interacting-fluid model, but it is not equivalent to

[
E_gamma>0	o0	o E_gamma<0.
]

## 5. Why ordinary redshift loss is not automatically a source term

For standard radiation,

[
dotho_gamma+4Hho_gamma=0.
]

The (4H) term already follows from covariant stress-energy conservation:

- (3H) from dilution in physical volume;
- (H) from redshift of each photon's energy.

There is no additional local source term in standard GR.

Therefore the redshift of photon energy in a comoving volume is not by itself evidence that a dark-energy component has been created.

## 6. Terminal classification

### Strict zero-crossing hypothesis

[
oxed{
	ext{geometry stretches an ordinary photon through }E=0	ext{ into }E<0
}
]

**ANALYTIC FAIL in standard FLRW null-geodesic dynamics.**

Reason:

[
E(t)=E_i e^{-int Hdt}
]

preserves sign.

### Negative-photon-dark-energy hypothesis

[
oxed{
E_gamma<0
Rightarrow
	ext{ordinary dark energy}
}
]

**FAIL as stated.**

A photon-like branch retains (w=1/3) and redshifts as (a^{-4}), rather than behaving as (wsimeq-1).

### Conversion hypothesis

[
oxed{
gamma
stackrel{Q[g,	ext{global causal data}]}{longrightarrow}
X,
qquad
w_Xsimeq-1
}
]

**MATHEMATICALLY OPEN.**

This requires new dynamics and is the viable descendant of the original intuition.

## 7. Next discriminating gate

The next useful LTG question is:

[
oxed{
	ext{Can global null/causal geometry derive a non-arbitrary }Q^mu
	ext{ that transfers stress-energy from radiation to a vacuum-like sector?}
}
]

A successful model must:

1. preserve total covariant conservation,
   [
   
abla_mu(T_gamma^{mu
u}+T_X^{mu
u})=0;
   ]
2. derive the sign and scale of (Q^mu) from geometry rather than fit them freely;
3. generate (w_X<-1/3), ideally (w_Xsimeq-1);
4. preserve or predict controlled deviations from the observed CMB spectrum and temperature-redshift law;
5. satisfy photon-number / distance-duality constraints;
6. produce at least one dimensionless observable not already present in generic interacting-dark-energy models.
