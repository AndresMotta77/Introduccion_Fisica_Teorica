"""LaTeX source of every equation image in the Phase 1 deck, in slide order.

Keys are the image ids used while building the deck. render.py turns each entry into
png/<id>.png. The slide number and slide id are given in the comment above each entry.
"""

EQ = {
    # slide 2, feynman
    'e_S': r"""S\approx\sum_{n=0}^{N-1}\Big[\frac{m\,(x_{n+1}-x_n)^2}{2\varepsilon}-\varepsilon\,V(x_n)\Big],\qquad \varepsilon=\frac{t_b-t_a}{N}""",
    # slide 2, feynman
    'f_phi': r"""\phi_j=A\,e^{iS_j/\hbar},\qquad \phi=\sum_j\phi_j""",
    # slide 2, feynman
    'f_K': r"""K(b,a)=A\int_{-\infty}^{\infty}\!dx_1\cdots\int_{-\infty}^{\infty}\!dx_{N-1}\;\exp\Big\{\frac{i}{\hbar}\sum_{n=0}^{N-1}\Big[\frac{m(x_{n+1}-x_n)^2}{2\varepsilon}-\varepsilon V(x_n)\Big]\Big\}=\int\mathcal{D}x\;e^{iS/\hbar}""",
    # slide 3, gauss
    'g_diag': r"""\int_{-\infty}^{\infty}\!dy_1\cdots\int_{-\infty}^{\infty}\!dy_{N-1}\;e^{-b(a_1y_1^2+\dots+a_{N-1}y_{N-1}^2)}=\sqrt{\frac{\pi^{N-1}}{b^{N-1}a_1a_2\cdots a_{N-1}}}""",
    # slide 3, gauss
    'g_ex': r"""z_1^2+(z_2-z_1)^2+z_2^2=\mathbf z^{\mathsf T}\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\mathbf z=3y_1^2+y_2^2""",
    # slide 3, gauss
    'g_gen': r"""\int d^{N-1}z\;e^{-b\,\mathbf z^{\mathsf T}M\mathbf z}=\sqrt{\frac{\pi^{N-1}}{b^{N-1}\det M}}""",
    # slide 3, gauss
    'g_free': r"""\int d^{N-1}z\;e^{-b\,[z_1^2+(z_2-z_1)^2+\dots+(z_{N-1}-z_{N-2})^2+z_{N-1}^2]}=\sqrt{\frac{\pi^{N-1}}{b^{N-1}N}}""",
    # slide 4, free
    'h_exp': r"""S[x+z]\simeq S^{\mathrm{cl}}+\int_{t_a}^{t_b}\Big(\tfrac12 m\dot z^2-\tfrac12V''(x)\,z^2\Big)dt,\qquad z(t_a)=z(t_b)=0""",
    # slide 4, free
    'h_Kz': r"""K(b,a)=A\,e^{iS^{\mathrm{cl}}/\hbar}\int d^{N-1}z\;\exp\Big(-\frac{m}{2i\hbar\varepsilon}\big[z_1^2+(z_2-z_1)^2+\dots+z_{N-1}^2\big]\Big)=A\,e^{iS^{\mathrm{cl}}/\hbar}\sqrt{\Big(\frac{2\pi i\hbar\varepsilon}{m}\Big)^{N-1}\frac{1}{N}}""",
    # slide 4, free
    'h_cl': r"""S^{\mathrm{cl}}=\frac{m}{2}\,\frac{(x_b-x_a)^2}{t_b-t_a}""",
    # slide 4, free
    'h_C': r"""A=\frac{1}{C^N},\qquad C=\sqrt{\frac{2\pi i\hbar\varepsilon}{m}}""",
    # slide 4, free
    'e_K0': r"""K_0(x_b,t_b;x_a,t_a)=\sqrt{\frac{m}{2\pi i\hbar\,(t_b-t_a)}}\;\exp\Big[\frac{i\,m\,(x_b-x_a)^2}{2\hbar\,(t_b-t_a)}\Big]""",
    # slide 5, plan
    'e_wick': r"""t=-i\tau:\qquad e^{-iHt/\hbar}\ \longrightarrow\ e^{-\tau H/\hbar}\equiv e^{-\beta H},\qquad \beta=\tau/\hbar""",
    # slide 5, plan
    'k_Z': r"""Z(\beta)=\operatorname{Tr}e^{-\beta\hat H}=\sum_n\langle n|e^{-\beta\hat H}|n\rangle=\sum_n e^{-\beta E_n}\ \simeq\ e^{-\beta E_0}""",
    # slide 5, plan
    'k_E0': r"""E_0\approx-\frac{\ln Z(\beta)}{\beta}""",
    # slide 5, plan
    'k_tr': r"""Z(\beta)=\int dx\,\langle x|e^{-\beta\hat H}|x\rangle,\qquad x(\beta)=x(0)""",
    # slide 6, imaginary
    'l_nc': r"""[\hat K,\hat V]\neq0\ \ \Longrightarrow\ \ e^{-\beta(\hat K+\hat V)}\neq e^{-\beta\hat K}e^{-\beta\hat V}""",
    # slide 6, imaginary
    'l_tay': r"""e^{\Delta t A}e^{\Delta t B}\approx(I+\Delta t A)(I+\Delta t B)=I+\Delta t(A+B)+\dots\approx e^{\Delta t(A+B)}""",
    # slide 6, imaginary
    'l_U': r"""e^{-\Delta\beta(\hat K+\hat V)}\approx e^{-\Delta\beta\hat K}e^{-\Delta\beta\hat V}\equiv\hat U,\qquad\Delta\beta=\frac{\beta}{m}""",
    # slide 6, imaginary
    'l_ZU': r"""Z(\beta)\approx\int dx_1\,\langle x_1|\,\underbrace{\hat U\hat U\cdots\hat U}_{m}\,|x_1\rangle""",
    # slide 7, beads
    'm_Z3': r"""Z_3=\int dx_1\,dx_2\,dx_3\;\langle x_1|\hat U|x_3\rangle\langle x_3|\hat U|x_2\rangle\langle x_2|\hat U|x_1\rangle""",
    # slide 7, beads
    'm_Zm': r"""Z_m=\int dx_1\cdots dx_m\prod_{j=1}^{m}\langle x_{j+1}|\hat U|x_j\rangle,\qquad x_{m+1}=x_1""",
    # slide 7, beads
    'm_U': r"""\langle x_{j+1}|\hat U|x_j\rangle=e^{-\Delta\beta V(x_j)}\,\langle x_{j+1}|e^{-\Delta\beta\hat K}|x_j\rangle=\sqrt{\frac{\mu}{2\pi\hbar^2\Delta\beta}}\;\exp\Big[-\frac{\mu(x_{j+1}-x_j)^2}{2\hbar^2\Delta\beta}-\Delta\beta V(x_j)\Big]""",
    # slide 7, beads
    'm_Zf': r"""Z_m=\Big(\frac{\mu}{2\pi\hbar^2\Delta\beta}\Big)^{m/2}\int dx_1\cdots dx_m\;\exp\Big(-\sum_{j=1}^{m}\Big[\frac{\mu(x_{j+1}-x_j)^2}{2\hbar^2\Delta\beta}+\Delta\beta V(x_j)\Big]\Big)""",
    # slide 8, action
    'n_Sm': r"""S_m=\sum_{j=1}^{m}\Big[\frac{\mu(x_{j+1}-x_j)^2}{2\Delta\tau}+\Delta\tau\,V(x_j)\Big],\qquad\Delta\tau=\hbar\Delta\beta""",
    # slide 8, action
    'n_Zm': r"""Z_m=\Big(\frac{\mu}{2\pi\hbar^2\Delta\beta}\Big)^{m/2}\int dx_1\cdots dx_m\;e^{-S_m/\hbar}""",
    # slide 8, action
    'n_H': r"""\hat H=\frac{\hat{\mathbf p}^2}{2\mu}-\frac{k}{r},\qquad k=\frac{e^2}{4\pi\varepsilon_0}""",
    # slide 8, action
    'n_SE': r"""S=\int dt\Big[\frac{\mu}{2}\Big|\frac{d\mathbf r}{dt}\Big|^2+\frac{k}{r}\Big]\ \xrightarrow{\ t=-i\tau\ }\ i\int d\tau\Big[\frac{\mu}{2}\Big|\frac{d\mathbf r}{d\tau}\Big|^2-\frac{k}{r}\Big]\equiv iS_E""",
    # slide 8, action
    'n_KE': r"""\int\mathcal D\mathbf r\;e^{iS/\hbar}\ \longrightarrow\ \int\mathcal D\mathbf r(\tau)\;e^{-S_E/\hbar}""",
    # slide 9, weight
    'o_SEm': r"""S_{E,m}=\sum_{j=1}^{m}\Big[\frac{\mu\,|\mathbf r_{j+1}-\mathbf r_j|^2}{2\Delta\tau}-\frac{\Delta\tau\,k}{r_j}\Big],\qquad\Delta\tau=\frac{\tau_f-\tau_i}{m}""",
    # slide 9, weight
    'o_w': r"""w_{\mathrm{pot}}(r)=e^{-\Delta\tau V(r)/\hbar}=e^{\Delta\tau k/\hbar r}\ \xrightarrow{\ r\to0^{+}\ }\ +\infty""",
    # slide 9, weight
    'o_I': r"""I(\varepsilon)=\int e^{\Delta\tau k/\hbar r}\,dV=4\pi\int_0^{\varepsilon}r^2e^{\Delta\tau k/\hbar r}\,dr=+\infty""",
    # slide 10, onebead
    'e_bound': r"""e^{x}\ge\frac{x^3}{6}\quad(x\ge0)\qquad\Longrightarrow\qquad r^2\,e^{a/r}\ \ge\ \frac{a^3}{6\,r}""",
    # slide 10, onebead
    'e_log': r"""4\pi\!\int_\eta^{\varepsilon}r^2e^{a/r}\,dr\ \ge\ \frac{2\pi a^3}{3}\,\ln\frac{\varepsilon}{\eta}\ \xrightarrow{\ \eta\to0\ }\ \infty""",
    # slide 10, onebead
    'e_growth': r"""4\pi\!\int_\eta^{\varepsilon}r^2e^{a/r}\,dr\ \simeq\ \frac{4\pi\,\eta^4\,e^{a/\eta}}{a}\Big(1+\frac{4\eta}{a}+\dots\Big)""",
    # slide 11, springs
    'e_sprb': r"""|\mathbf r_k|<1\ \text{for all }k\ \ \Longrightarrow\ \ e^{-|\mathbf r_{k+1}-\mathbf r_k|^2/2\Delta\tau}\ \ge\ e^{-2/\Delta\tau}""",
    # slide 11, springs
    'r_ZNb': r"""Z_m\ \ge\ (2\pi\Delta\tau)^{-3m/2}\,e^{-2m/\Delta\tau}\Big(\frac{4\pi}{3}\Big)^{m-1}\int_{|\mathbf r_1|<\varepsilon}e^{\Delta\tau/r_1}\,d^3r_1=+\infty""",
    # slide 11, springs
    'r_Npow': r"""Z_m(\eta)\ \simeq\ (2\pi\Delta\tau)^{-3m/2}\Big(\frac{4\pi\,\eta^4\,e^{\Delta\tau/\eta}}{\Delta\tau}\Big)^{m}""",
    # slide 12, continuum
    'e_kato': r"""\sup_{\mathbf x}\int_{|\mathbf x-\mathbf y|<\delta}\frac{d^3y}{|\mathbf y|\,|\mathbf x-\mathbf y|}\ \le\ 4\pi\delta\ \xrightarrow{\ \delta\to0\ }\ 0""",
    # slide 12, continuum
    'e_K00': r"""\langle\mathbf 0|e^{-\tau H}|\mathbf 0\rangle=\sum_{n\ge1}\frac{e^{\tau/2n^2}}{\pi n^3}+\frac{1}{\pi}\int_0^\infty\frac{k\,e^{-\tau k^2/2}}{1-e^{-2\pi/k}}\,dk""",
    # slide 12, continuum
    'e_trinf': r"""\operatorname{Tr}e^{-\beta H}\ \ge\ \sum_{n\ge1}n^2\,e^{\beta/2n^2}=\infty""",
    # slide 13, trotter
    'e_trrt': r"""e^{-it(A+B)}=\operatorname*{s-lim}_{n\to\infty}\big(e^{-itA/n}\,e^{-itB/n}\big)^{n}""",
    # slide 13, trotter
    'e_trit': r"""e^{-t(A+B)}=\operatorname*{s-lim}_{n\to\infty}\big(e^{-tA/n}\,e^{-tB/n}\big)^{n},\quad t\ge0""",
}
