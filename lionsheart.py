

A = [0,1,3,-2,0,1,0,-3,2,3]
# A[0] =  0
# A[1] =  1
# A[2] =  3
# A[3] = -2
# A[4] =  0
# A[5] =  1
# A[6] =  0
# A[7] = -3
# A[8] =  2
# A[9] =  3

def solution(A):
    import pdb;pdb.set_trace()
    def find_min(p,q,r):
        return min((p-q), (r-q))

    p_val = 0
    q_val = 0 
    r_val = 0

    depth = []
    curr = None
    prev = None
    pqr = {"p":False,
            "q":False,
            "r":False}

    for i in A:
        if curr == None and prev == None:
            p_val, prev = i, i
            pqr["p"] = True
            continue
        
        if pqr["q"] == False and prev < i :
            if r_val > i:
                continue
            p_val = i
            pqr["p"] = True
            continue

        if prev > i:
            prev, q_val = i, i
            pqr["q"] = True

        if pqr["q"] == True and prev < i:
            prev, r_val = i, i
            pqr["r"] = True

        if pqr["p"] and pqr["q"] and pqr["r"]:
            import pdb; pdb.set_trace()
            depth.append(find_min(p_val,q_val,r_val))
            pqr["p"] = False
            pqr["q"] = False
            pqr["r"] = False

    import pdb; pdb.set_trace()
    return max(depth)

print solution(A)