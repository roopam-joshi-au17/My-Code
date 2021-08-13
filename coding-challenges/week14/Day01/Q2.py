'''
Q-2) Find the Town Judge (5 marks)
https://leetcode.com/problems/find-the-town-judge/
(Easy)
In a town, there are n people labelled from 1 to n. There is a rumor that one of
these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person
labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.
Otherwise, return -1.
Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
'''


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if N == 0: return -1
        
        graph = {}
        for i in range(1,N+1):
            graph[i] = set()
        
        for e in trust:
            graph[e[0]].add(e[1])
        
        # if someone in graph has no edges, they are candidate
        candidates = [i for i,v in graph.items() if len(v) == 0]
        if len(candidates) == 0: return -1
        candidate = candidates[0]   # theoretically should have only 1
        
        # go through edges and see if everybody trusts candidate
        for i,v in graph.items():
            if candidate == i: continue
            if candidate not in graph[i]:
                return -1
        
        return candidate