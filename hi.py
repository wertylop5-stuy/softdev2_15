def valid_password(p):
    lo = [ 0100*c.islower() for c in p ]
    up = [ 0010*c.isupper() for c in p ]
    no = [ 0001*c.isdigit() for c in p ]
    
    res = 0
    for x in range(len(p)):
        res = res | (lo[x] | up[x] | no[x])
    
    return res == 0111

def test_password(p):
    other_chars = ".?!&#,;:-_*"
    
    #how much to increase strength by
    factor = .2
    other_factor = 0.5

    strength = 1
    
    lo = [ factor*c.islower() for c in p ]
    up = [ factor*c.isupper() for c in p ]
    ot = [ other_factor for c in p if c in other_chars ]

    if len(lo) > 1: strength += reduce(lambda x, y: x+y, lo)
    if len(up) > 1: strength += reduce(lambda x, y: x+y, up)
    if len(ot) > 1: strength += reduce(lambda x, y: x+y, ot)
    
    return 10 if strength >= 10 else strength



