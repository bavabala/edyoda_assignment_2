length = [(2,5),(1,2),(4,4),(2,3),(2,1)]
# For Loop:
for i in range(len(length)):
    for j in range(len(length)):
#If Condition:
        if length[i][1] < length[j][1]:
            length[i],length[j] = length[j],length[i]
#Print:
print(length)
            
