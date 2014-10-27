# -*- coding: utf-8 -*-
# python 2



from unicodedata import *

xlist=[]

file_obj = open("unicidetest.txt",'w')
import pdb; pdb.set_trace()
for i in range(945, 969):
    xlist.append(eval('u"\\u%04x"' % i))

import pdb; pdb.set_trace()
for x in xlist:
    if name(x,'-')!='-':
        print x.encode('utf-8'),'|', "%04x"%(ord(x)), '|', name(x,'-')
        abc= x.encode('utf-8')+'|'+ "%04x"%(ord(x))+ '|'+ name(x,'-')
        file_obj.write(abc)




char1 = lookup("GREEK SMALL LETTER ALPHA") # should be UPPER CASE
print char1.encode('utf-8')     # α
print char1.decode('utf-8')



"""
myStr = u'α'

# # Bad. This is a error.
print 'Greek alpha: ', myStr

# Good
print 'Greek alpha: ', myStr.encode('utf-8')
"""
