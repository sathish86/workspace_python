def good_fib(no):
    import pdb; pdb.set_trace()
    if no <= 1:
        return (no,0)
    else:
        (a,b) = good_fib(no-1)
        return (a+b,a)
    
print good_fib(6)


