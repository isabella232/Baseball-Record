def checkRecord(n):
    """ O(n) time with O(1) space solution
    """
    
    sh = [1 for _ in range(n+1)]
    Hp, Sp, SSp  = 1, 0, 0
    for i in range(1, n+1):
        SSp = Sp
        Sp  = Hp
        Hp  = sp[i-1]
        sp[i] = (SSp + Sp + Hp) % 1000000007 
    
    return (sp[n] + sum(((sp[i] * sp[n-i-1]) % 1000000007 for i in range(n)))) % 1000000007		
