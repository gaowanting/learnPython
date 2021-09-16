import numpy as np
import matplotlib.pyplot as plt


def sample():
    lottery_list = []
    for i in range(0, 11):
        lottery_list.append(list((np.random.randint(10, size=3))))
    return lottery_list


def count_win():
    win = [0, 3]
    count = 0
    for i in sample():
        if i[-1] in win:
            count += 1
    return count


def simulation():
    dic = {}
    for right_num in range(12):
        p = 0
        for i in range(10000):
            if count_win() == right_num:
                p += 1
            p /= 10000
        dic[right_num] = p
    return dic


print(simulation())



