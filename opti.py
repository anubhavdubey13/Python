# Optimization Problem
# Start by solving basics 
# Solve for minimization with less than equal to constraints
# Then introduce greater than equal to constraint
# Then generalize

# Problem 1
# MIN Z = 5x1 + 10x2
# subject to
# 3x1 + 5x2 >= 60
# 4x1 + 4x2 >= 72
# and x1,x2 >= 0
#=====================================
# Manual solution
# constraint 1: 3x1 + 5x2 - s1 + a1 = 60
cf1 = [3, 5]
cf1.append(-1)
cf1.append(1)
# constraint 2: 4x1 + 4x2 -s2 + a2 = 72
cf2 = [4, 4]
cf2.append(-1)
cf2.append(1)
# I feel dict would be better

# So what I am doing: Putting coeff against variables in dict. Then converting it to equality
d1 = {'x1':3, 'x2':5}
d1['s1'] = -1
d1['a1'] = 1
d2 = {'x1':4, 'x2':4}
d2['s2'] = -1
d2['a2'] = 1

# To get it to a form where both of them have all the variables
for i in d1.keys() | d2.keys():
    if i not in d1.keys():
        d1[i] = 0
    if i not in d2.keys():
        d2[i] = 0
        
print(d1,'\n', d2)
    
# Now dictionary of coeffs of the optimization func
m1, m2 = 100,100 # not the right way. will figure about representative multiplication
cj = {'x1':5, 'x2':10, 's1':0, 's2':0, 'a1':m1, 'a2':m2}


# the rhs of constraints
xb = [60, 72]

# initializing cb
cb = {'1':cj['a1'], '2':cj['a2']}

# working with zj
zj = {}

for i in cj:
    zj[i] = d1[i]*cb['1'] + d2[i]*cb['2']

# extracting candidate
candidate = [n for n, v in zj.items() if v == max(zj.values())]

# finding which one is replaced from cb
# CONTINUE



#======================================
# Check constraint type - this is unnecessary right now - let's deal with solving first
def identify(equation):
    if '>=' in equation:
        return 'greater'
    elif '<=' in equation:
        return 'lesser'
    else:
        return 'Constraint should contain <= or >='
    
identify('3x1+5x2>=0')

# Might have to use regex
# But let's prioritise solving the main problem. Regex would be helpful when I want someone 
# else to interact with it

# List of 