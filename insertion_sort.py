
"""
def insertion_sort(unsorted):
    sorted_list = []
    outer_count = 0
    inner_count = 0
    for un in unsorted:
        outer_count += 1
        posi = 0
        if sorted_list == []:
            sorted_list.append(un)
        else:
            for index, ele in enumerate(sorted_list):
                inner_count += 1
                if un > ele:
                    posi = index+1
                else:
                    break
            sorted_list.insert(posi, un)
            
    print "Sorted list"
    print sorted_list
    print outer_count
    print inner_count
"""
#insertion_sort([12,2,5,3,10,6,9])

"""
def eff_insertion_sort(unsorted):
    import pdb;pdb.set_trace()
    try:
        for index, ele in enumerate(unsorted):
            jvar = index+1
            while jvar > 0:
                if unsorted[jvar] < unsorted[jvar-1]:
                    temp = unsorted[jvar-1]
                    unsorted[jvar-1] = unsorted[jvar]
                    unsorted[jvar] = temp
                    jvar -= 1
                else:
                    jvar -= 1
    except:
        print unsorted
                
    print unsorted
eff_insertion_sort([12,2,5,3,10,6,9])
"""

"""
def insertionsort( aList ):
    import pdb; pdb.set_trace()
    for i in range( 1, len( aList ) ):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
        aList[k] = tmp
        
    print aList
insertionsort([12,2,5,3,10,6,9])

"""

def insertion_sort(A):
    for i in range(1,len(A)):
        j= i
        #val = A[i]
        while j > 0: 
            if A[j-1] > A[j]:
                temp = A[j-1] 
                A[j-1] = A[j]
                A[j] = temp
                
            j = j -1
        #A[j] = val
        
        
A = [13,12,11,10]
#insertion_sort(A)
#print A

def insert_sort1(ele_list):
    chk_val = ele_list[-1]
    
    for i in range(len(ele_list)-2, -1, -1): # this loop max to zero value
        if ele_list[i] > chk_val:
            ele_list[i+1] = ele_list[i]
            if i == 0:
                ele_list[i] = chk_val
            print " ".join(map(str,ele_list))
        elif ele_list[i] < chk_val:
            ele_list[i+1] = chk_val
            print " ".join(map(str,ele_list))
            break
            
a = [2, 4, 6, 8, 3]

a = [1, 3 ,5 ,9 ,13, 22, 27, 35, 46, 51, 55, 83, 87, 23]

print a
insert_sort1(a)
    
    




