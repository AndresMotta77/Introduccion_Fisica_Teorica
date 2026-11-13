# reconstruct_superseded.py -- rebuild the round-1 superseded versions of check_c.py (runs 0
# and 1) and check_b.py (run 1), which were edited in place in round 1 and not kept, by
# reverse-applying the exact round-1 edits to the final scripts. Every replacement is
# asserted to occur exactly once. The reconstructions are validated by re-running them and
# diffing against the outputs recorded in round 1.
import pathlib

def rev(text, new, old):
    assert text.count(new) == 1, new[:70]
    return text.replace(new, old)

c = pathlib.Path('check_c.py').read_text()

# ---- final -> run 1 (undo round-1 edit 2) ----
c1 = rev(c, '''# ----- C5: small-tau coefficients from GRID eigenvalues -----
# REVISION NOTE (run 2): in run 1 (out_c_run1_C5FAILED.txt) the predictions stopped at
# O(tau^3) in R_n and O(tau^2) in P_n, and the primitive case failed the 5e-6 tolerance at
# tau=0.4, n=2,3 (d = 7.4e-6, 1.0e-5), the omitted remainder scaling as tau^4 (1.0e-5 -> 6.6e-7
# -> 4.3e-8). I changed the CHECK, not the derivation: the next two analytic series terms of
# the closed form (sympy, see check_algebra-style series) were added to the predictions; the
# tolerance was kept at 5e-6. The leading coefficients under test are unchanged.''',
'''# ----- C5: small-tau coefficients from GRID eigenvalues -----''')
c1 = rev(c1, '''        pred = (-1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296 + 103*(2*nn + 1)*t**3/387072
                - t**4/10368 + 187*(2*nn + 1)*t**5/5308416)''',
'''        pred = -1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296 + 103*(2*nn + 1)*t**3/387072''')
c1 = rev(c1, '''        predP = 3*(2*nn + 1)/1280 - 5*(2*nn + 1)*t*t/14336 + 35*(2*nn + 1)*t**4/589824''',
'''        predP = 3*(2*nn + 1)/1280 - 5*(2*nn + 1)*t*t/14336''')
c1 = rev(c1, '''"-1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 - tau^4/10368 + 187(2n+1)tau^5/5308416 + O(tau^6));")''',
'''"-1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 + O(tau^4));")''')
c1 = rev(c1, '''"   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 - 5(2n+1)tau^2/14336 + 35(2n+1)tau^4/589824 + O(tau^6))")''',
'''"   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 - 5(2n+1)tau^2/14336 + O(tau^4))")''')
pathlib.Path('check_c_run1.py').write_text(c1)

# ---- run 1 -> run 0 (undo round-1 edit 1) ----
new_hdr = '''print("C5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted "
      "-1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 + O(tau^4));")
print("   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 - 5(2n+1)tau^2/14336 + O(tau^4))")
print("   failure if |R_n - pred| or |P_n - pred| > 5e-6 at any tau <= 0.4, n <= 3")'''
old_hdr = '''print("C5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted "
      "-1/144 + 3(2n+1)tau/1280 - tau^2/1296 + O(tau^3));")
print("   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 + O(tau^2))")'''
c0 = rev(c1, new_hdr, old_hdr)
c0 = rev(c0, '''        pred = -1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296 + 103*(2*nn + 1)*t**3/387072
        rowb.append(f"n={nn}: R={R:+.7f} d={R - pred:+.1e}")
        EnP = -np.log(evp[nn])/t
        P = (EnP - (nn + 0.5) + (2*nn + 1)*t*t/48)/t**4
        predP = 3*(2*nn + 1)/1280 - 5*(2*nn + 1)*t*t/14336
        rowp.append(f"n={nn}: P={P:.7f} d={P - predP:+.1e}")
        bad = (abs(R - pred) > 5e-6) or (abs(P - predP) > 5e-6) or not np.isfinite(R + P)
        nfail += bad''',
'''        pred = -1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296
        rowb.append(f"n={nn}: R={R:+.6f} pred={pred:+.6f}")
        EnP = -np.log(evp[nn])/t
        P = (EnP - (nn + 0.5) + (2*nn + 1)*t*t/48)/t**4
        rowp.append(f"n={nn}: P={P:.6f} pred={3*(2*nn + 1)/1280:.6f}")''')
pathlib.Path('check_c_run0.py').write_text(c0)

# ---- check_b final -> run 1 ----
b = pathlib.Path('check_b.py').read_text()
b1 = rev(b, '''        X = E + E[i]                              # rows: e_j + e_i
        X[i] = E[i]                               # row i would be 2 e_i; it is not used (diagonal
                                                  # set below) and for tau=0.002 it underflows w
                                                  # to 0 (run 1 printed a log(0) warning here)
        Sij, dSij = S_and_dS(X)''',
'''        Sij, dSij = S_and_dS(E + E[i])            # rows: e_j + e_i''')
pathlib.Path('check_b_run1.py').write_text(b1)
print("reconstructed: check_c_run0.py, check_c_run1.py, check_b_run1.py")
