def checkRecord(n):
    """ O(n) 
    """
    
    lp = [1 for _ in range(n+1)]
    Pp, Lp, LLp  = 1, 0, 0
    for i in range(1, n+1):
        LLp = Lp
        Lp  = Pp
        Pp  = lp[i-1]
        lp[i] = (LLp + Lp + Pp) % 1000000007 
    
    return (lp[n] + sum(((lp[i] * lp[n-i-1]) % 1000000007 for i in range(n)))) % 1000000007		
