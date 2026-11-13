import sympy as sp
D, kap = sp.symbols('D kappa', positive=True)
X = sp.symbols('X', real=True)
e, dd = sp.symbols('e d', positive=True)
om = sp.sqrt(2*D*kap); Mw = om/(2*D)
taue = e**2
xs, xps = X - dd*e/2, X + dd*e/2
# log of Mehler written as a sum of logs by hand (no algebra beyond log(AB)=logA+logB)
logK = sp.Rational(1,2)*sp.log(Mw/(2*sp.pi)) - sp.Rational(1,2)*sp.log(sp.sinh(om*taue)) \
       - Mw*((xs**2+xps**2)*sp.cosh(om*taue) - 2*xs*xps)/(2*sp.sinh(om*taue))
logR = -sp.Rational(1,2)*sp.log(4*sp.pi*D*taue) - (xs-xps)**2/(4*D*taue) \
       - (kap*taue/6*(xs**2+xs*xps+xps**2) + kap*D*taue**2/6)
f = sp.expand(logK - logR)
ser = sp.series(f, e, 0, 11).removeO()
print(sp.collect(sp.expand(sp.simplify(ser)), e))
# independent numeric spot check of the same difference at small tau
vals = {D: sp.Rational(1,2), kap: 1, X: sp.Rational(7,10), dd: sp.Rational(13,10)}
for ee in [sp.Rational(1,5), sp.Rational(1,10)]:
    num = sp.N((logK-logR).subs(vals).subs(e, ee), 40)
    pr = sp.N((ser).subs(vals).subs(e, ee), 40)
    print(float(ee**2), num, pr)
