
"""
def add_seq(arr,index=None,val=0):
    import pdb; pdb.set_trace()
    if index is None:
        index = -1
        val = 0
        
    index += 1
    if index == len(arr):
        return val
    else:
        val = val + arr[index]
        return add_seq(arr,index,val)
    #return val
    
a = [1,2,3]
ab = add_seq(a)
print ab
"""
"""
memo = {0:0, 1:1}
def fibm(n):
    print "First", n
    if not n in memo:
        print "in if cond", n
        memo[n] = fibm(n-1) + fibm(n-2)
    print memo
    return memo[n]

ab = fibm(5)
print ab

"""


def stairs(n,mem=[]):
    
    if n <0:
        return 0
    elif n == 0:
        return 1
    #elif mem and mem[n] > -1:
    #    return mem[n]
    
    if n <= len(mem):
        return mem[n]
    else:
        mem[n] = stairs(n-1,mem) + stairs(n-2,mem) + stairs(n-3,mem)
    return mem[n]

print stairs(6) 
    
    