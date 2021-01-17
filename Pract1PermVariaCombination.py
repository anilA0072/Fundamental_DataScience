#!/usr/bin/env python
# coding: utf-8

# # Combinatorics: Permutations, Variations & Combinations
# 
# Consider the following example. We have a box with some balls inside (each with a different color) and we want to compute the number of ways we can arrange those balls. We can do so with two different approaches: with repetition (each ball is reinserted into the box after it is picked) or without repetition.
# 
# # With Repetition
# The idea is that, after each ball extracted, we can pick it again as many times as we want. Let’s have an easy start and consider the box={g,b}, where g=’green ball’ and b=’blue ball’: well, in that case, the possible ways we can arrange those balls are ‘gg’, ‘bg’, ‘gb’, ‘bb’. We can also compute it with Python:
# 
# If we want to generalize, when we have n objects and we want to see in how many ways we can arrange them, we have:
# 
# n*n*n*.............*n= n^n
# 

# In[1]:


import itertools
from itertools import product
box_1=['g','b']
perm=[]
for p in itertools.product(box_1, repeat=2):
     perm.append(p)

perm


# 
# Let’s do the same with 3 balls instead:

# In[2]:


box_2 = ['g','b','y']
perm=[]
for p in itertools.product(box_2, repeat=3):
     perm.append(p)

perm


# 
# # Without repetition
# In this case, once you picked one ball, it cannot be used anymore. So each arrangement of balls will have unique values. In that case, coming back to our box={g,b}, the two possible permutations are ‘gb’ and ‘bg’:
# 
# In that case, we have to consider, after each extraction, that the number of available elements is one less. So, if we have n elements in our set, the permutations will be:
# 
#     1*2*3*...........*n=n!
#     

# In[4]:


import itertools 
  
box_1 = ['g','b']
perm = itertools.permutations(box_1) 
  
for i in list(perm): 
    print(i)
    


# 
# Again, let’s consider a bigger box ={g,b,y}, where y=’yellow ball’:
# 

# In[6]:


box_2 = ['g','b','y']
perm = itertools.permutations(box_2) 

for i in list(perm): 
    print(i)


# 
# # Variation
# Variations are nothing but permutations where the number of objects we want to pick is less than the total number of objects n. Let’s simply retrieve the example above and let’s say that, out of three balls, we want to arrange only the first and second positions. Let’s use the box={g,b,y} and let’s start with the case of repetition:
# 
# # With repetition
# We want to choose two balls (k=2) out of three (n=3) and compute the number of possible permutations: which can be calculated as:
# 
#    V(n,k) =  n*n*........(k times) = n^k

# In[7]:


box_2 = ['g','b','y']
perm=[]
for p in itertools.product(box_2, repeat=2):
     perm.append(p)

perm


# 
# # Without repetition
# The same reasoning holds if there are no repetitions.
# Indeed: In that case, we have:
#      V(n,k) = n!/(n-k)!

# In[8]:


box_2 = ['g','b','y']
perm = itertools.permutations(box_2,2) 
  
for i in list(perm): 
    print(i)


# 
# # Combinations
# 
# Combinations are variations (or permutations, if k=n) where the order does not matter. Basically, we use combinations whenever we want to compute in how many ways, from n objects, we can extract k of them, regardless of the order with which those are picked.
# 
# Namely, if you recall the permutation without repetition we examined at the very beginning, whose outputs were ‘gb’ and ‘bg’, the equivalent combination would be only ‘gb’ (or only ‘bg’), since the order does not matter, hence they represent the same object.
# 
# Let’s see it with python, always examining separately the two cases of repetition and no repetition:
# 
# # With repetition
# 
# The number of possible combinations (with repetition) is given by:
# 
#     C(n,k) = (n+k-1)!/k!(n-1)!

# In[9]:


from itertools import combinations_with_replacement 

box_1=['g','b']
comb = combinations_with_replacement(box_1, 2) 
  

for i in list(comb): 
    print(i)


# 
# The same holds with 3 balls (let’s combine only two of them):

# In[10]:


from itertools import combinations_with_replacement 

box_2=['g','b','y']
comb = combinations_with_replacement(box_2, 2) 
  

for i in list(comb): 
    print(i)


# 
# # Without repetition
# 
# The number of possible combinations (without repetition) is given by:
# 
#     C(n,k) = n!/k!(n-k)!

# In[11]:


from itertools import combinations 

comb = combinations(box_1, 2) 
   
for i in list(comb): 
    print(i) 


# 
# And with three balls:

# In[12]:


from itertools import combinations 

comb = combinations(box_2, 2) 
   
for i in list(comb): 
    print(i) 


# In[ ]:




