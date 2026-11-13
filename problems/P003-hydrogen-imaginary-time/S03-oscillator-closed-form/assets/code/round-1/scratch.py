import sympy as sp
t,n=sp.symbols('tau n',positive=True)
k=sp.sqrt(1+t**2/12)
E_n = t/12 + sp.log(k+t/2)/t + n/t*sp.log((k+t/2)/(k-t/2))
print(sp.series(E_n-(n+sp.Rational(1,2)),t,0,7).removeO().expand().collect(t))
kp=sp.sqrt(1+t**2/4)
EP=(n+sp.Rational(1,2))*2/t*sp.asinh(t/2)
print(sp.series(EP-(n+sp.Rational(1,2)),t,0,7).removeO().expand().collect(t))
