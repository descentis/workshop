#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:05:34 2018

@author: descentis
"""
import networkx as nx

def create_graph():
        
    G=nx.read_adjlist("edge_list.adjlist",create_using=nx.DiGraph())
    f = open('edge_list.csv','w')
    f.write("Source,Target\n")
    for line in nx.generate_edgelist(G,data=False):
        f.write(line[0])
        f.write(',')
        f.write(line[2])    
        f.write('\n')
    
    f.close()

file = open('Impression network (Responses).csv')

data_list = []
for i in file:
    a = i.split(',')
    last_ind = 0
    for j in range(len(a)):
        if(a[j]==''):
            last_ind = j
            break
    
    a = a[:last_ind]
    data_list.append(a)

file.close()


f = open('node_list.csv','w')
f.write("Id,Label\n")
for i in data_list:
    f.write(i[1])
    f.write(',')
    f.write('"'+i[0]+'"')
    f.write('\n')

f.close()


f = open('edge_list.adjlist','w')
for i in data_list:
    for j in range(1,len(i)):
        f.write(i[j])
        if(j!=len(i)-1):
            f.write(' ')
        else:
            f.write('\n')

f.close()

create_graph()      
    