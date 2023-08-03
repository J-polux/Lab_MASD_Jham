# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 07:19:02 2023

@author: prestamour
"""

"""
Lab MASD Jham Pool Murillo 
"""
from statistics import mean  #used in the point 1.7 for calculed average
import statistics as st #used in the point 1.11 for calcules the mediam
import random #used in the point 1.12 for random list 


""" 2 Data Structures """
""" 1 """
fruit = ["Mango", "Watermelon", "Coconout", "Apple"]


""" 2 """
fruit.append("carombolo") 


""" 3 """
fruit.pop(1)
print(fruit)

""" 4 """
valor = 1
for i in fruit:
    
    if i == "banana":
        valor = 1
    else:
        valor = 0
if valor == 1:
    print("banana yes it's on the list")
else:
    print("banana don´t it's on the list")

""" 5 """
for i in fruit:
    print(i)
    
""" 6 """
numbers = []
print ("enter 5 integers to the list")
for i in range(5):
    one = int(input("enter:"))
    numbers.append(one)

print(mean(numbers))

""" 7 """ 
lista = ["Mango", "Watermelon", "Coconout", "Apple", "Mango", "Apple"]
unique = []
for element in lista:
  if element not in unique:
    unique.append(element)

print(unique)

""" 8 """
names = ["Jham", "Pool", "Juan", "Camilo", "Ana"]
names.sort()
print(names)

""" 9 """
many_num = [2,3,4,5,6,7,8,9]
mayor = max(many_num)
many_num.remove(mayor)
max_num = max(many_num)
print(max_num)


""" 10 """
['juan', 'mango'] 
['Juan', 'Mango']

""" 11 """

list = [1,2,3,4,5,15]
median = st.median(list)
print(median)

""" 12 """
countries = ["China", "USA", "UK", "France"]
random.shuffle(countries)
print(countries)

""" 13 """
lengt = ['dddd','a','bb','ccc']
lengt.sort(key=len)
print(lengt)
