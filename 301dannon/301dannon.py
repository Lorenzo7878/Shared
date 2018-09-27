#!/usr/bin/env python3
# coding: utf8

from sort import *

count_fusion_sort = 0

def error():
        print("Error with arguments")
        exit(84)

def open_file():
        if (os.path.isfile(sys.argv[1])):
                        file = open(sys.argv[1], "r")
                        content = file.read()
                        return content
        else:
                error()
        return

def count_elem(content):
        x = 0
        a = 1
        
        while (x in range(len(content))):
                if (content[x] == ' '):
                        a+=1
                        x+=1
                else:
                        x+=1
        return a

def convert_string(content):
        i = 0
        tab = [len(content)]
        content = content.split(' ')
        while(i in range(len(content))):
                tab.append(content[i])
                tab[i] = float(content[i])
                i+=1
        del tab[i]
        return tab

def select_sort(tab):
        a = 0
        for i in range(len(tab)):
                min_idx=i
                for j in range(i+1, len(tab)):
                        if (tab[min_idx] > tab[j]):
                                min_idx = j
                        a+=1
                tab[i], tab[min_idx] = tab[min_idx], tab[i]
        return a

def insertion_sort(tab):
        count = 0
        i = 1
        while (i < len(tab)):
                elem = tab[i]
                j = i
                while (j >= 0 and tab[j-1] > elem):
                        tab[j] = tab[j-1]
                        j = j - 1
                        count += 1
                        if (tab[j] == tab[j-1]):
                                count+=2
                tab[j] = elem
                i += 1
        return count

def bubble_sort(tab):
        a = 0
        for i in range (0, len(tab) - 1):
                for j in range(0, len(tab) - 1 - i):
                        if (tab[j] > tab[j+1]):
                                tab[j], tab[j+1] = tab[j+1], tab[j]
                        a+=1
        return a

if (len(sys.argv) == 2):
        if (sys.argv[1] == "-h"):
                print("USAGE\n")
                print("           ./301dannon file\n")
                print("DESCRIPTION")
                print("        file       file that contains the numbers to be sorted, separated by spaces")
        else:
                content = open_file()
                a = count_elem(content)
                print("%d elements"%(a))
                a = select_sort(convert_string(content))
                print("select sort:  %d comparisons"%(a))
                a = insertion_sort(convert_string(content))
                print("insertion sort:  %d comparisons"%(a))
                a = bubble_sort(convert_string(content))
                print("bubble sort:  %d comparisons"%(a))
                b = len(convert_string(content)) - 1
                fusion_sort(convert_string(content))
                print("fusion sort:  %d comparisons"%(temp.cnt))
                a = quick_sort(convert_string(content), 0, b)
                print("quick sort:  %d comparisons"%(a))
                

else:
        error()