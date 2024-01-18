list1 = [9,3,24,33,2]
list2 = [3,37,23,9,2]
list3 = []
for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)

print("Os números iguais das duas listas são:"+str(list3))