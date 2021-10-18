# Flames Calculator
# Sounds lame but okay. I am having fun.

# Calculator Type 1: Where you only remove common letters in each other's names
name1 = input("Enter the first name: ").lower()
name2 = input("Enter the second name: ").lower()

common_letters = []

for a in name1:
    if a in name2:
        common_letters.append(a)

# Now that I have common letters, I will extract the non-common letters from both names

non_common_letters = []

for n in (name1+name2):
    if n not in common_letters:
        non_common_letters.append(n)
    print(non_common_letters)

# Finding the length and selecting the required letter

compatible = 'flames'
useful_length = len(non_common_letters)%len(compatible)

print('\n')
print(common_letters)
print(non_common_letters)
print(compatible[useful_length - 1])

# Idk if I should beautify this or not

# Type 2 would be were any repeated alphabet is completely eliminated
l = {}
for n in name1+name2:
    l[n] = (name1+name2).count(n)

m = []
for k in l:
    if l[k] == 1:
        m.append(k)
        
print(compatible[len(''.join(m)) - 1])        


