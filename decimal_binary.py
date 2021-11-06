# Converting Decimal to Binary
# Final Function

def dec_to_bin(d):
    r = []
    while d != 0:
        r.append(str(d%2))
        d = d//2
    r.reverse()
    b = ''.join(r)
    return b

dec_to_bin(2936)
bin(2936)[2:]


#================ROUGH WORK=========================
# Stop when q = 0

d = 123
q = d//2
r = d%2

d1 = q
q1 = d1//2
r1 = d1%2

d2 = q1
q2 = d2//2
r2 = d2%2

d3 = q2
q3 = d3//2
r3 = d3%2

d4 = q3
q4 = d4//2
r4 = d4%2

d5 = q4
q5 = d5//2
r5 = d5%2

d6 = q5
q6 = d6//2
r6 = d6%2

# d = 123 so b = 1111011 all remainders arranged from last to first
b = bin(d)
print(b)

# Iter 1
d = 145
r = []
while d != 0:
    r.append(str(d%2))
    d = d//2
    #print(d,'\n',r)
r.reverse()
''.join(r)


