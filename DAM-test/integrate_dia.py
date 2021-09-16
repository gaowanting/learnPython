def integrated_dia(list1):
    for i in range(1, len(list1)):
        list1[i] = list1[i-1]+"  \t  "+list1[i]
    return list1

