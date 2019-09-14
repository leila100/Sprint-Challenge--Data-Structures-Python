import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Complexity: O(n^2) - double for loops going through all the elements - 8.6 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Runtime complexity: O(n) - only one for loop going through all the elements
# Getting key from dict is O(1) 
# 0.007 seconds
# name_dict = {name:1 for name in names_2}
# for name_1 in names_1:
#     if name_1 in name_dict:
#         duplicates.append(name_1)

# Stretch solution
# sorting the major array is O(nlog(n))
# The for loop will be O(n)
# This solution will then be O(nlog(n)) - slower than the solution using a dictionary
# 1.35 seconds
names1 = []
names2 = []
# Remove duplicates in names_1 and names_2
for i in range(len(names_1)):
    if names_1[i] not in names1:
        names1.append(names_1[i])
for i in range(len(names_2)):
    if names_2[i] not in names2:
        names2.append(names_2[i])

names = names1 + names2
names.sort()
for i in range(len(names)-1):
    if names[i] == names[i+1] and names[i] not in duplicates:
        duplicates.append(names[i])
        i += 1

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

