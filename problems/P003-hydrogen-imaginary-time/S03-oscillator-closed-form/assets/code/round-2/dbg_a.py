# dbg_a.py -- round-1 diagnostic, re-run in round 2 against check_a_run1.py
# (round 1 read 'check_a.py', which at that time was the run-1 version; that filename is the only change)
import sys; sys.argv=['x']
exec(open('check_a_run1.py').read().split("wrong = {")[0])
x,xp,tau=mp.mpf(2),mp.mpf(-2),mp.mpf('0.001')
r=rho0(x,xp,tau)
for fr in ['1e-14','1e-11','1e-9','1e-8','1e-7','1e-5','1e-3','0.3']:
    u=tau*mp.mpf(fr)
    val=inner(x,xp,tau,u)/r
    yb=((tau-u)*x+u*xp)/tau; s2=u*(tau-u)/tau
    print(fr, mp.nstr(val,15), mp.nstr((yb**2+s2)/2,15))
