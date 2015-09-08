"""
The problem description is very short:
The equilibrium index of a sequence is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in a sequence A:
A[0]=-7 A[1]=1 A[2]=5 A[3]=2 A[4]=-4 A[5]=3 A[6]=0
3 is an equilibrium index, because:
A[0]+A[1]+A[2]=A[4]+A[5]+A[6]
6 is also an equilibrium index, because:
A[0]+A[1]+A[2]+A[3]+A[4]+A[5]=0
(The sum of zero elements is zero) 7 is not an equilibrium index - because it is not a valid index of sequence A. If you still have doubts, here is a precise definition: The integer k is an equilibrium index of a sequence A[0],A[1]..,A[n-1] if and only if 0<= k and sum(A[0..(k-1)])=sum(A[(k+1)..(n-1)]). Assume the sum of zero elements is equal to zero. 

Write a function
int equi(int A[], int n)
that, given a sequence, returns its equilibrium index (any) or -1 if no equilibrium index exists. Assume that the sequence may be very long.

"""


# def equi(list_of_val,n):
#     if (n==0):
#         return -1
#     sum = 0
#     i = 0
#     final_res = []
#     import pdb; pdb.set_trace()
#     for i in list_of_val:
#         sum += i

#     sum_left = 0
#     for i in range(0,n):
#         print i
#         sum_right = sum - sum_left - list_of_val[i]
#         if (sum_left == sum_right):
#             print "valus is equal"
#             print i, list_of_val[i]
#             final_res.append(i) 

#         sum_left += list_of_val[i]

#     print final_res
#     return -1



def solution(A):
    # write your code in Python 2.7
    import pdb; pdb.set_trace()
    count_dict = {}
    seq = 0
    
    for i in range(0,len(A)):
        if count_dict.has_key(A[i]):
            count_dict[A[i]] += 1
        else:
            count_dict[A[i]] = 1
            seq = i
    print "Result"            
    print seq
    return seq

solution([0,1,2,3,4,0,1,2,3])


#a= [-7,1,5,2,-4,3,0]
#equi(a,len(a))
# for i in range(0,10):
#     print i