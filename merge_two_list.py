def merging(S, S1,S2):
    i = 0
    j = 0
    S = [None] * (len(S1)+len(S2))
    
    while (i+j < len(S)):
        if (j == len(S2)) or (i < len(S1) and S1[i] < S2[j]):
            if not S1[i] in S:
                S[i+j] = S1[i]
            i += 1
        else:
            if not S2[j] in S:
                S[i+j] = S2[j]
            j += 1
    print S

S1 = [1,2,3,4]
S2 = [4,6,7,8]
merging([],S1,S2)



        