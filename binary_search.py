
"""
count = 0
def binary_search(low,high,target,data=[]):
    #import pdb; pdb.set_trace()
    global count
    count += 1
    print "no of calls: {0}".format(count)
    
    if low > high:
        return False
    
    medium = len(data)/2
    
    if target == data[medium]:
        return "Got the targeted value: {0}".format(target)
    
    if target < data[medium]:
        return binary_search(low,medium-1,target,data[low:medium-1])
    
    if target > data[medium]:
        return binary_search(medium+1,high,target,data[medium+1:high])
        
        
data = [1,2,4,5,7,8,9,10,13,15,16,18,20]
print binary_search(0,len(data),16,data)

"""

A = [1,2,3,4,5,6,7,8,9,10]

def binary_search(A,min,max,find_val):
    if len(A) == 0:
        print "Nothing to search"
    import pdb; pdb.set_trace()
    mid = (min+max)/2
    
    if min > max:
        return "Could not Found"
    
    if find_val == A[mid]:
        print "found", A[mid]
        return A[mid]
    
    elif find_val < A[mid]:
        return binary_search(A,min,mid-1,find_val)
    else:
        return binary_search(A,mid+1,max,find_val)

print binary_search(A,0,len(A)-1,11)




























