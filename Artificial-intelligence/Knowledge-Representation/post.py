from ai_pkg.utils import Expr

def is_prop_symbol(s):
    
    return isinstance(s, str) and s[:1].isalpha() and s[0].isupper()

def is_true(exp, model={}):
    
    if exp in (True, False):
        return exp

    op, args = exp.op, exp.args

    if is_prop_symbol(op):
        return model.get(exp)

    elif op == '~':  # Negasi
        p = is_true(args[0], model)
        if p is None:
            return None
        else:
            return not p

    elif op == '|':  # Disjungsi (OR)
        result = False
        for arg in args:
            p = is_true(arg, model)
            if p is True:
                return True
            if p is None:
                result = None
        return result

    elif op == '&':  # Konjungsi (AND)
        result = True
        for arg in args:
            p = is_true(arg, model)
            if p is False:
                return False
            if p is None:
                result = None
        return result

    p, q = args

    if op == '>>':  # Implikasi
        return is_true(~p | q, model)
        # T F : F

    elif op == '<<':  # Implikasi terbalik
        return is_true(p | ~q, model)

    pt = is_true(p, model)
    if pt is None:
        return None

    qt = is_true(q, model)
    if qt is None:
        return None

    if op == '**':  # Biimplikasi (ekuivalensi)
        return pt == qt

    elif op == '^':  # XOR (eksklusif OR)
        return pt != qt

    else:
        raise ValueError("Illegal operator: " + str(exp))

# A: Server aktif               : True
# B: Website dapat diakses      : False
# C: Jaringan stabil            : True
# D: Ada gangguan listrik       : False
# E: Database berjalan normal   : True
# F: API merespon dengan baik   : False

if __name__ == '__main__':
    A, B, C, D, E, F = map(Expr, 'ABCDEF')
    model = {A: True, B: False, C: True, D: False, E: True, F: False}
    query = ( ((((A & E) >> B) & (C >> (F | ~D))) ** ((A & F) & (~B >> (~E | ~F)))) >> C )
    print(query, ' : ', is_true(query, model))