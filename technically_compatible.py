
"""
def append_five(list=[]):
    list.append(5)
    return list


for i in range(5):
    first_list = append_five()
    second_list = append_five([])

print first_list
print second_list

dna = "ATTGC"
abc = {"A":"T",
        "T":"A",
        "C":"G",
        "G":"C"}

print "".join([abc[letter] for letter in dna])

"""


"""
def append_four():
    import pdb; pdb.set_trace()
    list_val.append(4)

list_val = [1]
list_val += [2]
list_val.append(3)
append_four()
print(list_val)
"""

"""

class Employee(object):
    def __init__(self, name):
        self.name = name

    def pay_cheque(self):
        return self.monthly_amount()

class Salaried(Employee):
    def __init__(self, name, salary):
        import pdb; pdb.set_trace()
        super(Salaried, self).__init__(name)
        self.salary = salary

    def monthly_amount(self):
        return self.salary / 12


class Hourly(Salaried):
    def __init__(self, name, rate):
        import pdb; pdb.set_trace()
        super(Hourly, self).__init__(name)
        self.rate = rate

    def monthly_amount(self):
        return self.hours_worked_this_month * self.rate


andy = Hourly("andy", 16.75)
andy.hours_worked_this_month = 160

antony = Salaried("antony",125720)

print(andy.pay_cheque())
print(antony.pay_cheque())
"""

"""
class Person():
    def __init__(self,date_of_birth):
        self._date_of_birth = date_of_birth

    @property
    def date_of_birth(self):
        return self._date_of_birth
"""
"""
class Person():
    def __init__(self,date_of_birth):
        self._date_of_birth = date_of_birth

    @readonly
    def date_of_birth(self):
        return self._date_of_birth
"""

"""
class Person():
    def __init__(self,date_of_birth):
        self._date_of_birth = date_of_birth

    @property
    date_of_birth
class Person(object):
    def __init__(self,date_of_birth):
        self._date_of_birth = date_of_birth

    @property
    def date_of_birth(self):
        return self._date_of_birth




obj = Person("21-05-1986")
print obj.date_of_birth
obj.date_of_birth = "22-05-1986"
print obj.date_of_birth


"""

"""
class Duplication(Exception):
    pass


def stop_on_duplicate(text):

    last = None
    result = []

    try:
        for letter in text:
            if letter == last:
                raise Duplication()
            last = letter
            result.append(letter)
        return result
    except Duplication:
        return result
    finally:
        result.append("STOP")

print(stop_on_duplicate("hello"))
"""

"""
def primes(up_to):
    result = []
    for no in range(2, up_to):
        for x in range(2,no):
            import pdb; pdb.set_trace()
            if no % x == 0:
                break
        else:
            result.append(no)
    return result

print(primes(10))
"""

"""
def logging(fn):
    def _log(self):
        print "Entering '%s' " % (fn.__name__)
        result = fn(self)
        print "Exiting '%s' . result '%s'" % (fn.__name__, result)
        return result 
    return _log

def logging(self):
    def _log(fn):
        print "Entering '%s' " % (fn.__name__)
        result = fn(self)
        print "Exiting '%s' . result '%s'" % (fn.__name__, result)
        return result 
    return _log


class RangeFinder:

    @logging
    def a(self):
        print "Inside method a"
        return range(5)

obj = RangeFinder()
obj.a()
"""

"""
import weakref
import gc

class Foo:
    def __init__(self, name):
        self.name = name
        print "%s created" % name

    def __del__(self):
        print "%s detroyed" % self.name

    def store(self, obj):
        self.obj = obj

import pdb; pdb.set_trace()
one = Foo("one")
two = Foo("two")

one.store(weakref.ref(two))

two.store(one)

one = None
two = None

gc.collect()
"""

"""

class Person(object):

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, studied_course):
        super(Student, self).__init__(name)
        self.studied_course = studied_course
        #self.name = name


stu = Student("sathish", "mca")
print stu.name
"""




"""
def logging(fn):
    def _log(self):
        print "Entering '%s' " % (fn.__name__)
        result = fn(self)
        print "Exiting '%s' . result '%s'" % (fn.__name__, result)
        return result 
    return _log

def logging(self):
    def _log(fn):
        print "Entering '%s' " % (fn.__name__)
        result = fn(self)
        print "Exiting '%s' . result '%s'" % (fn.__name__, result)
        return result 
    return _log
"""

# def logging(prefix):
#     def _log(fn):
#         def _log_with_prefix(self):
#             print "%s : Entering '%s' " % (prefix, fn.__name__)
#             return fn(self)
#         return _log_with_prefix 
#     return _log

# def logging(fn):
#     def _log(prefix):
#         def _log_with_prefix(self):
#             print "%s : Entering '%s' " % (prefix, fn.__name__)
#             return fn(self)
#         return _log_with_prefix 
#     return _log

# def logging(fn, prefix):

#     def _log_with_prefix(self):
#         print "%s : Entering '%s' " % (prefix, fn.__name__)
#         return fn(self)
#     return _log_with_prefix 




# class RangeFinder:

#     @logging(prefix = "EXPERT")
#     def a(self):
#         print "Inside method a"
#         return range(5)

# obj = RangeFinder()
# obj.a()

"""

def lazy_property(fn):
    attr_name = '_lazy_' + '_' + fn.__name__

    @property # (A)
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    # (B)
    # @_lazy_property.setter
    # def _lazy_property(self, value):
    #     setattr(self, attr_name, value)

    return _lazy_property

class Sloth:
    @lazy_property   # (C)
    def a(self):
        print('fetching expensive data inside property "a"')
        return "Data from a REALLY expensive database call"

    # (D)    
    @a.lazy_setter
    def a(self, value):
        setattr(self, "a", value)

x = Sloth()
x.a = "Data provided by an external service"
print(x.a) # Expecting this to SKIP the expensive call

y = Sloth()
print(y.a) # Expecting this to make the expensive call

"""

class Duplication(Exception):
    pass

def stop_on_duplicate(text):

    last = None
    result = []

    try:
        for letter in text:
            if letter == last:
                raise Duplication()
            last = letter
            result.append(letter)
        
    except Duplication:
        pass
    else:
        result.append("OK")
    finally:
        result.append("STOP")
    return result
print(stop_on_duplicate("ready"))