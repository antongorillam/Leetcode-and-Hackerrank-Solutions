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


### 021. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

**Idea**: Use a dummy node.

**Personal Note**: Had quite a hard time with this one, but when I got the idea to create a dummy node, then its quite straight forward.Furthermore, there's quite many edge cases if porly designed

**Improvements**: Perhaps rewrite loop so that last if statements would  be needed.

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

### 142. [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

**Idea**:

- Hash every node.
- If we have seen a node before, it is a loop, return it.

**Time Complexity**: $\mathcal{O}(n)$

**Space Complexity**: $\mathcal{O}(n)$

**Improvement**: We can get it the space complexity to $\mathcal{O}(1)$ if we use 2 pointers, a *slow*- and a *fast* pointer. It is a but theoretical though.

### 205. [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

**Idea**: We can transform a string to a list, eg. f("*egg*") = "011". The number in the string is arbitrary, as long as it preserves the its structure. The function can be implemented with a hashfunction and works basically like this:
    - Loop through the string.
    - If the character haven't been seen previously (eg. not in hashmap), add it, with a arbitrary number.
    - If the character exist, assign the number its corresponding to it.

With this algorithm, f("*egg*") = f("*add*") = "011"

**Time Complexity**: $\mathcal{O}(n)$

**Space Complexity**: $\mathcal{O}(n)$

### 206. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

**Idea**: Loop through LL and direct pointer to the previous node.

Hardest part is the order:

1. Save the coming node
2. Redirect the current node pointer to the previous node
3. Move previous node to the current node
4. Move current node to the next node

If done right, no edge cases need to be added.

### 409. [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

**Idea**:

Understand a couple of things:
- If a character occurs an even number of time -> we can always build a palidrome
- There can only be one oddly numbered characters in a palidrome. If     there's more we have to remove a character to make it even.
- The length of longest palidrome is the length of the string, subtracting the number of characters from the oddly numbered characters to make a palidrome, eg. *len(s) - oddly_numbered_char + 1*

**Time-complexity**: $\mathcal{O}(n)$

**Space-complexity**: $\mathcal{O}(n)$

### 876. [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

**Idea**: This one was quite simple, just loop through list and use counter, then go to the middle

**Time-complexity**: $\mathcal{O}(n)$

**Space-complexity**: $\mathcal{O}(1)$

## Hackerrank solutions
