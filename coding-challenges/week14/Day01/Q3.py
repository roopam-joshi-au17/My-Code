'''
Q-3) Find Center of Star Graph (5 marks)
https://leetcode.com/problems/find-center-of-star-graph/
(Easy)
There is an undirected star graph consisting of n nodes labeled from 1 to n. A
star graph is a graph where there is one center node and exactly n - 1 edges that
connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
that there is an edge between the nodes ui and vi. Return the center of the given
star graph.
'''
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = {}
        for i in edges:
            dic[i[0]] = dic.get(i[0],0) + 1
            dic[i[1]] = dic.get(i[1],0) + 1
        n = len(dic.keys())
        for i in dic.keys():
            if dic[i] == n-1:
                return i