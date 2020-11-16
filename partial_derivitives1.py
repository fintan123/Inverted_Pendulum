import sympy as sym

m, ell, x3, x4, M, g, F, m = sym.symbols('m, ell, x3, x4, M, g, F, m')

# φ(F, x3, x4)
phi = 4*m*ell*x4**2*sym.sin(x3) + 4*F - 3*m*g*sym.sin(x3)*sym.cos(x3)
phi /= 4*(M+m) - 3*m*sym.cos(x3)**2

# z(F, x3, x4)
z = -3*m*ell*x4**2 * sym.sin(x3)* sym.cos(x3) + F* sym.cos(x3) - (M + m)* g * sym.sin(x3)
z /= (4 * (M + m) - 3*m * sym.cos(x3)**2)* ell

dphi_x3 = phi.diff(x3)
dphi_x4 = phi.diff(x4)
dphi_F = phi.diff(F)

dz_x3 = z.diff(x3)
dz_x4 = z.diff(x4)
dz_F = z.diff(F)


def evaluate_at_eq(f):
    return f.subs([(F, 0),(x3, 0),(x4, 0)])

dphi_F_eq = evaluate_at_eq(dphi_F)
dphi_x3_eq = evaluate_at_eq(dphi_x3)
dphi_x4_eq = evaluate_at_eq(dphi_x4)

dz_F_eq = evaluate_at_eq(dz_F)
dz_x3_eq = evaluate_at_eq(dz_x3)
dz_x4_eq = evaluate_at_eq(dz_x4)

print("Equation 1")
sym.pprint(dphi_F_eq)
sym.pprint(dphi_x3_eq)
sym.pprint(dphi_x4_eq)
print("Equation 2")
sym.pprint(dz_F_eq)
sym.pprint(dz_x3_eq)
sym.pprint(dz_x4_eq)
