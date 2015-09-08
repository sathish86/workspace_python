a = [1,2,3]
b = [2,3]

# def index(subseq, seq):
#     """Return an index of `subseq`uence in the `seq`uence.

#     Or `-1` if `subseq` is not a subsequence of the `seq`.

#     The time complexity of the algorithm is O(n*m), where

#         n, m = len(seq), len(subseq)

#     >>> index([1,2], range(5))
#     1
#     >>> index(range(1, 6), range(5))
#     -1
#     >>> index(range(5), range(5))
#     0
#     >>> index([1,2], [0, 1, 0, 1, 2])
#     3
#     """
#     i, n, m = -1, len(seq), len(subseq)
#     try:
#         while True:
#             i = seq.index(subseq[0], i + 1, n - m + 1)
#             if subseq == seq[i:i + m]:
#                return i
#     except ValueError:
#         return -1

#     start = -1
#     seq_len = len(seq)

#     sub_seq_len = len(subseq)

#     try:
#         while True:
#             start = seq.index(subseq[0], start+1, seq_len - sub_seq_len + 1)
#             if subseq == seq[start:start + sub_seq_len]:
#                 return start
#     except ValueError:
#         return -1

#     pos = main_list.index(first, pos) + 1
#     if not sub_seq_len or main_list[pos:pos+len(sub_seq_len)] == sub_seq_len:
#         return pos

# #print index([1,2], [0, 1, 0, 1, 2])

# if not bigger:
#         return -1
#     if not sub:
#         return 0
#     first, rest = sub[0], sub[1:]
#     pos = 0
#     try:
#         while True:
#             pos = bigger.index(first, pos) + 1
#             if not rest or bigger[pos:pos+len(rest)] == rest:
#                 return pos
#     except ValueError:
#         return -1


def solution(val):
    list_of_data = map(int, list(str(val)))
    val_dict = {}
    result = ""
    import pdb; pdb.set_trace() 
    
    for index , value in enumerate(list_of_data):
        if val_dict.has_key(value):
            val_dict[value] += 1
            
        else:
            val_dict[value] = 1
        #try:
        if len(list_of_data) > 1:
            if index != 0:
                if abs(list_of_data[index] - list_of_data[index - 1]) != 0:
                    for key, val in val_dict.iteritems():
                        if value != val: 
                            result = result + str(val) + str(key)
                    val_dict = {}
        else:
            return int('1' + str(value))

    for key, val in val_dict.iteritems():
        result = result + str(val) + str(key)

    return int(result)

print solution(1211)


