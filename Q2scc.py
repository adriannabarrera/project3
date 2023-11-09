#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 13:42:21 2023

@author: adriannabarrera
"""

import networkx as nx
#import matplotlin.pyplot as plt
import sys
import time
import heapq
#import resource
from itertools import groupby
from collections import defaultdict



class Tracker(object):
    """Keeps track of the current time, current source, component leader,
    finish time of each node and the explored nodes.
    
    'self.leader' is informs of {node: leader, ...}."""

    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()


def dfs(graph_dict, node, tracker):
    """Inner loop explores all nodes in a SCC. Graph represented as a dict,
    {tail: [head_list], ...}. Depth first search runs recursively and keeps
    track of the parameters"""

    tracker.explored.add(node)
    tracker.leader[node] = tracker.current_source
    for head in graph_dict[node]:
        if head not in tracker.explored:
            dfs(graph_dict, head, tracker)
    tracker.current_time += 1
    tracker.finish_time[node] = tracker.current_time


def dfs_loop(graph_dict, nodes, tracker):
    """Outer loop checks out all SCCs. Current source node changes when one
    SCC inner loop finishes."""

    for node in nodes:
        if node not in tracker.explored:
            tracker.current_source = node
            dfs(graph_dict, node, tracker)


def graph_reverse(graph):
    """Given a directed graph in forms of {tail:[head_list], ...}, compute
    a reversed directed graph, in which every edge changes direction."""

    reversed_graph = defaultdict(list)
    for tail, head_list in graph.items():
        for head in head_list:
            reversed_graph[head].append(tail)
    return reversed_graph


def scc(graph):
    """First runs dfs_loop on reversed graph with nodes in decreasing order,
    then runs dfs_loop on original graph with nodes in decreasing finish
    time order(obtained from first run). Return a dict of {leader: SCC}."""

    out = defaultdict(list)
    tracker1 = Tracker()
    tracker2 = Tracker()
    nodes = set()
    reversed_graph = graph_reverse(graph)
    for tail, head_list in graph.items():
        nodes |= set(head_list)
        nodes.add(tail)
    nodes = sorted(list(nodes), reverse=True)
    dfs_loop(reversed_graph, nodes, tracker1)
    sorted_nodes = sorted(tracker1.finish_time,
                          key=tracker1.finish_time.get, reverse=True)
    dfs_loop(graph, sorted_nodes, tracker2)
    for lead, vertex in groupby(sorted(tracker2.leader, key=tracker2.leader.get),
                                key=tracker2.leader.get):
        out[lead] = list(vertex)
    return out

def main():
    # Your code for processing the graph and calculating SCCs
    t1 = time.time() - start
    print(t1)
    groups = scc(graph)
    t2 = time.time() - start
    print(round(t2, 4))
    top_5 = heapq.nlargest(5, groups, key=lambda x: len(groups[x]))

    result = []
    for i in range(5):
        try:
            result.append(len(groups[top_5[i]]))
        except:
            result.append(0)

    return result, groups

if __name__ == '__main__':
    start = time.time()
    graph = {
        4: {1, 2, 12},
        1: {3},
        3: {2, 5},
        2: {1},
        12: set(),
        5: {8, 6},
        11: {12},
        9: {11, 5},
        10: {11, 9},
        8: {9, 10},
        6: {7, 8, 10},
        7: {10}
    }

    result, components = main()

    print('Strongly connected components are:')
    for key, value in components.items():
        print(value)