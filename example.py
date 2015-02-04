def zip(xs,ys):
    assert isinstance(xs, list) and isinstance(ys,list)
    if xs == [] or ys ==[]:
        value = []
    else:
        value = [(xs[0],ys[0])]
        if len(xs) != 1 and len(ys) != 1:
            value.append(zip(xs[1:],ys[1:]))
    return value

#print(zip([1,2,3], [5,6]))


def abc(a,**kwargs):
    for key, value in iter(kwargs):
        print key, value


abc('sa',{'name':'sathish','score':100})
        