import sympy

# Define propositional variables
p = sympy.symbols('p')
q = sympy.symbols('q')
r = sympy.symbols('r')

# Define propositions
prop1 = p
prop2 = sympy.Not(q)
prop3 = sympy.And(p, q)
prop4 = sympy.Or(p, q)
prop5 = sympy.Implies(p, q)
prop6 = sympy.Eq(p, q)

prop7 = sympy.Not(p)
prop8 = sympy.And(p, p)
prop9 = sympy.Or(p, p)
prop10 = sympy.Or(p, sympy.Not(p))
prop11 = sympy.And(p, sympy.Not(p))
prop12 = sympy.Implies(p, q).simplify()

prop15 = sympy.Eq(sympy.Or(p, q), sympy.Or(q, p))
prop16 = sympy.Eq(sympy.And(p, q), sympy.And(q, p))
prop17 = sympy.Eq(sympy.Or(p, sympy.Or(q, r)), sympy.Or(sympy.Or(p, q), r))
prop18 = sympy.Eq(sympy.And(p, sympy.And(q, r)), sympy.And(sympy.And(p, q), r))
prop19 = sympy.Eq(sympy.Or(p, sympy.And(q, r)), sympy.And(sympy.Or(p, q), sympy.Or(p, r)))

# Additional propositions
prop13 = sympy.Or(p, q, r)
prop14 = sympy.And(p, q, r)

# Values
p_value = True
q_value = False

print(f"p = {p_value}, q = {q_value}")
print(f"prop1 (p): {prop1.subs({p: p_value})}")
print(f"prop2 (not q): {prop2.subs({q: q_value})}")
print(f"prop3 (p and q): {prop3.subs({p: p_value, q: q_value})}")
print(f"prop4 (p or q): {prop4.subs({p: p_value, q: q_value})}")
print(f"prop5 (p implies q): {prop5.subs({p: p_value, q: q_value})}")
print(f"prop6 (p equivalent q): {prop6.subs({p: p_value, q: q_value})}")
print(f"prop7 (not p): {prop7.subs({p: p_value})}")
print(f"prop8 (p and p): {prop8.subs({p: p_value})}")
print(f"prop9 (p or p): {prop9.subs({p: p_value})}")
print(f"prop10 (p or not p): {prop10.subs({p: p_value})}")
print(f"prop11 (p and not p): {prop11.subs({p: p_value})}")
print(f"prop12 (Modus Ponens): {prop12.subs({p: p_value, q: q_value})}")

# Validity
def is_valid(proposition):
    return all(proposition.subs({p: p_val, q: q_val}) 
               for p_val in [True, False] 
               for q_val in [True, False])

print(is_valid(prop1))

# Satisfiable
print(sympy.satisfiable(prop1))

# DNF & CNF
print(sympy.to_dnf(prop13))
print(sympy.to_cnf(prop13))