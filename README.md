# Leetcode-and-Hackerrank-Solutions

## Leetcode solutions

### 001 Two Sum

[Problem link](https://leetcode.com/problems/two-sum/)

Idea: It is easy to bruteforce $\mathcal{O}(n^2)$, but using hashtables can reduce it to $\mathcal{O}(n)$, while it might increase memory complexity a bit.

1. Loop over nums and save the results in a hashtable with value as key (I choosed to save the residual from the target, but does not matter)
2. Loop over nums once again, but this time we use to hashtable to check if the corresponding answer exist, which is $\mathcal{O}(1)$.

### 013 Roman to Integer

[Problem link](https://leetcode.com/problems/roman-to-integer/)

Idea: For every roman symbol, if the symbol left of it is smaller than the one, add the roman symbol to the total sum, else subtract is:

Furthermore will use hashtable linking each roman symbol to its value to make the code shorter.

### 101 Symmetric Tree

### 104 Maximum Depth of Binary Tree

[Problem link](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Idea: Regular DFS. Call the function recusively for each child, and return the max height.

### 111 Minimum Depth of Binary Tree

[Problem link](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

Idea: Since we want to find the shortest height, *bfs* (breath-first-search) makes most sense, since it will check each "level" at a time.

1. Create a queue and proceed with a normal bfs, with only difference is that we track which heigh each node is on.
2. As soon as booth we find a leaf node (both children are `None`) then we know we have found the lowest height.

Time complexity: $\mathcal{O}(|V|)$


## Hackerrank solutions
