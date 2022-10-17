# Leetcode-and-Hackerrank-Solutions

## Leetcode Solutions Notes

### 001. [Two Sum](https://leetcode.com/problems/two-sum/)

**Idea**: It is easy to bruteforce $\mathcal{O}(n^2)$, but using hashtables can reduce it to $\mathcal{O}(n)$, while it might increase memory complexity a bit.

1. Loop over nums and save the results in a hashtable with value as key (I choosed to save the residual from the target, but does not matter)
2. Loop over nums once again, but this time we use to hashtable to check if the corresponding answer exist, which is $\mathcal{O}(1)$.

### 013. [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

**Idea**: For every roman symbol, if the symbol left of it is smaller than the one, add the roman symbol to the total sum, else subtract is:

Furthermore will use hashtable linking each roman symbol to its value to make the code shorter.

### 020. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

**Idea**: Beacause we need to preserve the order, a stack should be used.As soon as I realized that, the task becomes easy. There are x cases where it should fail:

- The closing bracket and the last element does not match.
- The stack is empty when encountering a opening bracket.
- The stack is not empty when we reach the end of the string.

**Personal Note**: The performance should in theory improve (a tiny bit) if we instead use *hashmaps* to check for the bracket. Try if you want!

**Time Complexity**: $\mathcal{O}(n)$

### 024. [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

**Idea**: Always look at 2 node at a time.

**Personal Note**: Problem gets quite easy once I realized that I only need to look at 2 node each time (think of a sliding window of 2)

### 066. [Plus One](https://leetcode.com/problems/plus-one/)

Idea: While looping throught the list from reverse, there are only 3 cases:

- Case 1: We are on the "last" digit (eg. index=0) and its a 9. We therefore need to extend the list with 1 more position.
- Case 2: The digit is a 9, thus we need a carry over (eg. the loops continues).
- Case 3: If the number is not a 9, then just add 1 and break the loop.

**Personal Note**: Good to always remember that the way to loop through a list in reverse in python (with indexing) is:

```python
for i in range(len(list)-1, -1, -1):
    pass
```

**Time Complexity**: $\mathcal{O}(n)$

### 101 Symmetric Tree

### 104. [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

**Idea**: Regular DFS. Call the function recusively for each child, and return the max height.

### 111. [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

**Idea**: Since we want to find the shortest height, *bfs* (breath-first-search) makes most sense, since it will check each "level" at a time.

1. Create a queue and proceed with a normal bfs, with only difference is that we track which heigh each node is on.
2. As soon as booth we find a leaf node (both children are `None`) then we know we have found the lowest height.

**Time Complexity**: $\mathcal{O}(|V|)$

### 206. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

**Idea**: Loop through LL and direct pointer to the previous node.

Hardest part is the order:

1. Save the coming node
2. Redirect the current node pointer to the previous node
3. Move previous node to the current node
4. Move current node to the next node

If done right, no edge cases need to be added.

## Hackerrank solutions
