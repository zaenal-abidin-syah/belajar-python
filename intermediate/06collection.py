# collection: Counter, namedtuple, ordereddict,defaultdict, deque


#  Counter

# from collections import Counter

# # a="aaaaaaabbbbbccccccc" # a=7 c=7 b=5 , urut
# a="aaacbbaaaabaabcacbccccbbccbccabbaccc"
# mycounter=Counter(a)
# print(mycounter)
# print(mycounter.items())
# print(mycounter.keys())
# print(mycounter.values())
# print(mycounter.most_common()) # descending nilai
# print(mycounter.most_common(2)) # 2 nilai terbanyak
# print(mycounter.most_common(2)[0][1])
# print(list(mycounter.elements())) # mengambil huruf perhuruf





# from collections import namedtuple

# Point = namedtuple('Point', 'x,y')
# pt=Point(1, -4)
# print(pt)
# print(pt.x, pt.y)



# Ordered Dict
# from collections import OrderedDict


# ordered_dict = OrderedDict()
# # ordered_dict = {}

# ordered_dict['b']= 2
# ordered_dict['c']= 3
# ordered_dict['d']= 4
# ordered_dict['a']= 1

# print(ordered_dict)






#  default dict 

# from collections import defaultdict


# d = defaultdict(int)
# d['a']=1
# d['b']=2
# print(d['a']) # selain a dan b default value adalah 0
# print(d['c'])

# d = defaultdict(float)
# d['a']=1.232
# d['b']=2.6326
# print(d['a']) # selain a dan b default value adalah 0,0
# print(d['c'])


# d = defaultdict(list)
# d['a']=1
# d['b']=2
# print(d['a']) # selain a dan b default value adalah []
# print(d['c'])

# default list=[], 




# deque

# from collections import deque

# d=deque()
# d.append(1)
# d.append(2) # end

# d.appendleft(3) #start
# print(d)

# d.pop()#end
# print(d)

# d.popleft()#start
# print(d)

# # d.clear()# hapus seluruh elemen
# # d.extend([4,5,6]) # menambahkan banyak elemen end
# d.extendleft([4,5,6]) # menambahkan banyak elemen start
# print(d)

# d.rotate(1) # to end
# print(d)