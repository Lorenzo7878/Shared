import sys
import os.path
import random
from math import *

class temp:
        a = 0
        cnt = 0

def quick_sort(tab, first, last):
        i = j = 0
        if (first < last):
                pivot = first
                i = first
                j = last
                while (i < j):
                        while ((tab[i] <= tab[pivot]) & (i < last)):
                                i+=1
                                temp.a+=1
                        while (tab[j] > tab[pivot]):
                                j-=1
                                temp.a+=1
                        if (i < j):
                                tab[i], tab[j] = tab[j], tab[i]
                tab[pivot], tab[j] = tab[j], tab[pivot]
                quick_sort(tab, first, j-1)
                quick_sort(tab, j+1, last)
        return temp.a - 1

def fusion_sort(x):
        result = []
        if len(x) < 2:
                return x
        mid = int(len(x)/2)
        y = fusion_sort(x[:mid])
        z = fusion_sort(x[mid:])
        while (len(y) > 0) or (len(z) > 0):
                if len(y) > 0 and len(z) > 0:
                        if y[0] > z[0]:
                                result.append(z[0])
                                z.pop(0)
                                temp.cnt+=1
                        else:
                                result.append(y[0])
                                y.pop(0)
                                temp.cnt+=1
                elif len(z) > 0:
                        for i in z:
                                result.append(i)
                                z.pop(0)
                else:
                        for i in y:
                                result.append(i)
                                y.pop(0)
        return result
        