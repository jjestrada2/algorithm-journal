"""
Title     : Fruit Into Baskets
Difficulty: Medium

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.
 
Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

 
Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""

# Your solution below:
Due to the nature of the problem, a sliding window technique is suitable for the solution. 

In this scenario, with the sliding window technique, we maintain a window with at most two distinct fruit types. 

Here's how it works:

1. We'll start from the leftmost tree and try to extend the range to the right as far as possible, until we encounter a third type of fruit.

2. When the third type of fruit is encountered, we need to move the left boundary of our window until there are only two unique types within our window.

3. All the while we're doing this, we'll keep updating our max fruits count.

Here's the Python code implementing this logic:

```python
def totalFruit(fruits):
    basket = {}  # To keep track of the current fruits in the basket
    left, max_fruits = 0, 0
    
    # Iterate over fruits
    for right in range(len(fruits)):
        # If the fruit is not in the basket, add to the basket
        if fruits[right] not in basket:
            basket[fruits[right]] = 0
        # Increment the count of current fruit
        basket[fruits[right]] += 1
        
        # If the basket size is greater than 2
        if len(basket) > 2:
            # Decrease the count of the left-most fruit in the basket
            basket[fruits[left]] -= 1
            # If no more of that fruit remains in the basket, remove it
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            # Move the left pointer
            left += 1
        
        # Keep updating max_fruits
        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits
```

This solution has a linear time complexity O(n) where n is the length of the fruits list as we traverse the list once.

Note: To better understand this approach, it can be helpful to look at a few examples and write them out step by step, or to run the code with some print statements to get an idea of what is happening at each step.
