# Coverage — check_symbolic.py (final)

Runs: round 1, run 3 (PYTHONHASHSEED=0,1,2,3, byte-identical) -> check_symbolic.round1.out; round 2 (seeds 0-3, byte-identical, and identical to round 1) -> check_symbolic.round2.out. The single FAIL line is S7a, the faulty sympy series method, kept on purpose.

The text below is quoted from the solver's own coverage notes (answers/answer-2.md §4.3 unless stated). /log adds nothing to them. Where the answer gives no 'would not catch' half, that absence is recorded rather than filled in.

S1 (marginal). Tests (5)–(6) against the definition (3), in one dimension, symbolically. Inputs: $\rho_0$ from the prompt, and the claimed formula. Would catch a wrong mean or variance, for example $Du(\tau-u)/\tau$ in place of $2Du(\tau-u)/\tau$. Would not catch anything about $d>1$ (factorization is argued in the text), nor whether (3) is the intended bridge ([A6]).

S2 (Chapman–Kolmogorov (7)). Would catch normalization errors in the bead measure. Would not catch anything beyond a Gaussian integral.

S3 (covariance (8), two-time means). Inputs: the kernel product (definition) and the claimed covariance. Would catch a missing $1/\tau$ or the wrong $\min/\max$ structure. Would not catch errors in laws at three or more times; those are Gaussian and fixed by (8).

S4 (covariance integrals $I_1$–$I_5$). Inputs: the claimed $C(u,v)$, checked in S3. Would catch arithmetic errors in $1/6$, $1/360$, $2/45$, $1/15$ and in the vanishing odd moment. Would not catch an error in which integrals are the right ones, i.e. in the Isserlis bookkeeping of §3.5.4; S7, S8, N4b, N5b, N8 and S9 address that independently. The integral $\int_0^1(t-\frac12)^2t(1-t)dt=1/120$ is not in S4; N8 and S9 test the term it produces.

S5 ((12) and the endpoint limits). Computes $\langle V\rangle_u$ for the oscillator from the definition (4) by symbolic integration, then integrates over $u$. Would catch errors in (12) and in the trapezium endpoint values. Would not catch anything about non-quadratic $V$ (see N1).

S6 (Mehler). Would catch a misremembered oscillator kernel. Would not catch failures of uniqueness: I take PDE plus initial condition plus positivity as determining the kernel (`[R]`, standard).

S7a/S7b/S7c ((30) against exact). Inputs: Mehler (S6) and (12) (S5); both are independent of the variance computation that produced (30). Would catch a wrong leading coefficient, or wrong $\Delta^2$ or $\tau^4$ coefficients for quadratic $V$. Would not catch the $\nabla^3V$ terms, which vanish for the oscillator, nor anything about non-quadratic $V$. S7a is the method that failed (R1); S7c is the 40-digit arbiter that decides between S7a and S7b.

S8 (linear potential). Would catch a wrong coefficient in (26); the $1/24$ alternative is shown to leave a residual. Would not catch Hessian or third-derivative terms (absent for linear $V$).
