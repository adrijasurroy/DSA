
#Imagine you and your friends are embarking on an exhilarating escape room adventure with a unique twist. In this escape #room challenge, you'll navigate through a series of interconnected chambers, each presenting a distinct puzzle or riddle #that you must solve to proceed to the next chamber. Here's how this escape room puzzle challenge works:


#There are a total of nummPuzzles puzzles you have to solve, labeled from 0 to numPuzzles - 1. You are given an array #puzzle dependencies where prerequisites[i] = [ai, bi] indicates that you must solve puzzle bi first if you want to solve #puzzle ai.

#For example, the pair [0, 1], indicates that to solve puzzle 0 you have to first solve puzzle 1.
# Return true if you can get out of the escape room. Otherwise, return false.

# numOfPuzzles : 5 
# [[3,1], [3,2]]
# [[3,1] [3,2] [2,4] [4,3]]
from collections import defaultdict, deque

def canSolveAllPuzzles(numOfPuzzles, prerequisites):
    # Create an adjacency list and an array to store the in-degrees of nodes
    graph = defaultdict(list)
    in_degree = [0] * numOfPuzzles

    # Fill the adjacency list and in-degrees array
    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    # Create a queue and add all nodes with in-degree 0
    queue = deque([i for i in range(numOfPuzzles) if in_degree[i] == 0])

    # Perform the topological sort
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all nodes have in-degree 0, return True. Otherwise, return False.
    return all(in_degree[i] == 0 for i in range(numOfPuzzles))

# Test the function
print(canSolveAllPuzzles(5, [[3,1], [3,2]]))  # Output: True
print(canSolveAllPuzzles(5, [[3,1], [3,2], [2,4], [4,3]]))  # Output: False
