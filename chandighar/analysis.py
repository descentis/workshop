#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:01:19 2018

@author: Main
"""


import matplotlib.pyplot as plt
import networkx as nx



def showDegreeSeq(G):
    degree_sequence = [d for n, d in G.in_degree()]
    print("Degree sequence %s" % degree_sequence)
    print("Degree histogram")
    hist = {}
    for d in degree_sequence:
        if d in hist:
            hist[d] += 1
        else:
            hist[d] = 1
    print("degree #nodes")
    for d in hist:
        print('%d %d' % (d, hist[d]))
    
    nx.draw(G)
    plt.show()
    
G = nx.read_graphml('impression.graphml')


def avgInDeg(G):
    degree_sequence = [d for n, d in G.in_degree()]
    sum = 0
    for i in degree_sequence:
        sum+=i
    avg = sum/len(degree_sequence)
    print(avg)
showDegreeSeq(G)