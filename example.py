def abc(file):
    o = open(file,'r')
    for i in o.readlines():
        print i
    
if __name__ == '__main__':
    import sys
    print sys.argv[1]
    import pdb; pdb.set_trace()
    #print args[1]
    abc(sys.argv[1])
    