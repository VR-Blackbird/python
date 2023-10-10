from collections import ChainMap, Counter, OrderedDict, defaultdict


#----------------------ChainMap ------------------------------
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
list1= [1,3,4,5]
list2= [1,7,8,9]
print(list(ChainMap(list1,list2)))   #remove duplicates by maintaining order
chain = ChainMap(baseline,adjustments)
print(chain)
chain["art"] = "play"
chain["opera"] = "xyz"
print(baseline)
print(chain)

#----------------------Counter---------------------------------------
from collections import Counter
c = Counter("abracadabra")
print(c)
print(c.most_common(2))
print(sorted(c.elements()))

l_c = Counter(['eggs', 'ham', 'eggs'])
print(l_c["abc"]) #key is not present then counter return 0

l1= Counter(a=4, b=2, c=0, d=-2)
l2 = Counter(a=1, b=2, c=3, d=4)
print(l1+l2)
# print(l1.subtract(l2))
print(l1)

#---------------------------------------OrderedDict--------------------------------
print(OrderedDict.fromkeys('abcde',0))
o = OrderedDict({"b":1, "a":4, "c":5,"d":2})
print("Ordered_dict")
o.popitem(last = False)
print(o)
o.move_to_end("a", last = False)
print(o)

#------------------------------------defaultDict---------------------------------
s1 = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d1 = defaultdict(list)
for k,v in s1:
    d1[k].append(v)
print(d1)

s2= 'mississippi'
d2 = defaultdict(int)
for i in s2:
    d2[i] +=1
print(d2)

#*d3 = defaultdict(update)
d3 = defaultdict(set)
for k, v in s1:
    d3[k].add(v)
print(d3)


