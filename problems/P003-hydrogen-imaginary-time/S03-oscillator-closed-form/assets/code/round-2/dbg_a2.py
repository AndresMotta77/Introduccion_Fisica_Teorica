# dbg_a2.py -- round-1 diagnostic, re-run in round 2 against check_a_run1.py
# (round 1 read 'check_a.py', which at that time was the run-1 version; that filename is the only change)
exec(open('check_a_run1.py').read().split("wrong = {")[0])
x,xp,tau=mp.mpf(2),mp.mpf(-2),mp.mpf('0.001')
for fr in ['1e-9','1e-3','0.3']:
    u=tau*mp.mpf(fr)
    g = lambda yy: -(yy - x)**2/(2*u) - (yy - xp)**2/(2*(tau - u))
    dg = lambda yy: mp.diff(g, yy)
    ystar = mp.findroot(dg, (x, xp + mp.mpf('1e-3')), solver='secant', verify=False)
    curv = -mp.diff(g, ystar, 2); s=1/mp.sqrt(curv)
    yb=((tau-u)*x+u*xp)/tau; s2=u*(tau-u)/tau
    f = lambda yy: rho0(x, yy, u)*V(yy)*rho0(yy, xp, tau - u)
    pts = [-mp.inf] + [ystar + k*s for k in (-40, -12, -5, -2, 0, 2, 5, 12, 40)] + [mp.inf]
    v,err=mp.quad(f, pts, error=True)
    v2=mp.quad(f, [-mp.inf]+[yb+k*mp.sqrt(s2) for k in range(-40,41,2)]+[mp.inf])
    print(fr, mp.nstr(ystar-yb,5), mp.nstr(s/mp.sqrt(s2),10), mp.nstr(v/rho0(x,xp,tau),15), mp.nstr(err/v,3), mp.nstr(v2/rho0(x,xp,tau),15))
