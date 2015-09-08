# def solution(A):
# 2
#      n = len(A)
# 3
#      L = [-1] + A
# 4
#      L.sort()
# 5
#      count = 0
# 6
#      pos = (n + 1) // 2
# 7
#      candidate = L[pos]
# 8
#      for i in xrange(1, n + 1):
# 9
#          if (L[i] == candidate):
# 10
#              count = count + 1
# 11
# -    if (count > pos):
 
# +    if (2*count > n):
# 12
#          return candidate
# 13
#      return -1


# def solution(A):
#     import pdb; pdb.set_trace()
#     n = len(A)
#     L = [-1] + A
#     L.sort()
#     count = 0
#     pos = (n+1) // 2

#     candidate = L[pos]

#     for i in xrange(1, n+1):
#         if (L[i] == candidate):
#             count = count + 1

#     if (count > pos):
#         return candidate

#     return -1

# #print solution([1,1,5,1,1])
# print solution([4,2,2,3,2,4,2,2,6,4])

linked_list = [1,4,-1,3,2]

#linked_list = [6,1,-1,2,3,5,4]

#counter = 0

# def find_length(linked_list, next_index):
#     global counter
#     import pdb;pdb.set_trace()
#     if linked_list[next_index] == -1:
#         return counter + 1
#     else:
#         next_in = linked_list[next_index]
#         counter = counter+1
#         return find_length(linked_list, next_in)

# print find_length(linked_list, 0)



def find_length(linked_list):
    index = 0
    counter = 0
    for i in range(0, len(linked_list)):
        if linked_list[index] == -1:
            counter += 1
            break
        else:
            index = linked_list[index]
            counter = counter+1

    return counter

#print find_length(linked_list)


# A[0] = 4
#   A[1] = 6
#   A[2] = 2
#   A[3] = 2
#   A[4] = 6
#   A[5] = 6
#   A[6] = 1

A = [4,6,2,2,6,6,1]
A = [4,4,2,6,6,4]

# def solution(A):
#     #import pdb; pdb.set_trace()
#     store_dict = {}
#     result = 0

#     for index, value in enumerate(A):
#         if not store_dict.has_key(value):
#             store_dict[value] = {}
#             store_dict[value]["first_index"] = index
#         else:
#             store_dict[value]["latest_index"] = index
#             res = abs(store_dict[value]["first_index"] - store_dict[value]["latest_index"])
#             result = max(result, res)

#     return result

# print solution(A)

# A = [3,5,6,3,3,5]

# A = [2,5,6,2,3,5]
# A = [2,5,6,11,3,10]


# def fact(n):
#     f = 0
#     for x in range(1, n +1):
#         f += x
#     return f


# def solution(A):
#     #import pdb; pdb.set_trace()
#     store_dict = {}
#     pair_counter = 0

#     for index, value in enumerate(A):
#         if not store_dict.has_key(value):
#             store_dict[value] = []
#             store_dict[value].append(index)
#         else:
#             store_dict[value].append(index)
    
#     for key, val in store_dict.iteritems():
#         if len(val) > 0:
#             pair_counter += fact(len(val) - 1)

#     print store_dict
#     print pair_counter

# solution(A)


#print fact(4)



A = [1,2,3,3,1,3,1]

def solution_A(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in xrange(N):
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]

A = [1,3,1,3,2]

A = [4,3,1,3,2,4,4,4,5]


def solution(M, A):
    import pdb; pdb.set_trace()
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in xrange(N):
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp >= maxOccurence:
                maxOccurence = tmp
                index = i

            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1

    print index
    return A[index]

print solution(5, A)























