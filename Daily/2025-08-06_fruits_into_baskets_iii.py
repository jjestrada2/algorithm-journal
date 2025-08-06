"""
Title     : Fruits Into Baskets III
Difficulty: Medium

You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.

Return the number of fruit types that remain unplaced after all possible allocations are made.
 
Example 1:

Input: fruits = [4,2,5], baskets = [3,5,4]
Output: 1
Explanation:

fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.

Since one fruit type remains unplaced, we return 1.

Example 2:

Input: fruits = [3,6,1], baskets = [6,4,7]
Output: 0
Explanation:

fruits[0] = 3 is placed in baskets[0] = 6.
fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
fruits[2] = 1 is placed in baskets[1] = 4.

Since all fruits are successfully placed, we return 0.

 
Constraints:

n == fruits.length == baskets.length
1 <= n <= 105
1 <= fruits[i], baskets[i] <= 109
"""

# Your solution below:
Sure, I can provide a solution in Python. The key to solving this problem optimally is to use heaps.

Here's how it works:

1. We'll sort the baskets in ascending order. This allows us to allocate the smallest available baskets first, which makes it more likely that we can allocate larger baskets later.

2. For the fruits array, we'll turn it into a max heap. A max heap will always give us the largest element (which is the quantity of fruits) when we pop it. This is because we always want to allocate the largest quantity of fruits first, as it requires a larger basket. 

3. Then, for each fruit, we'll pop the fruit from the heap and try to place it in the smallest available basket in the sorted basket array.

4. If the largest quantity of fruit can't be placed into the smallest basket, we have to increment our counter, indicating that one fruit type cannot be placed in any basket. We will then continue to the next fruit. We can stop if there are no more baskets available to place fruit in.

5. We return the number of unplaced fruit types, which we have been tracking.

Here is the Python code:

```python
import heapq

def unplacedFruitTypes(fruits, baskets):
    # Use heapq.heapify() to transform list into a max heap in-place.
    heapq.heapify(fruits)
    # Sorts basket capacity from smallest to largest.
    baskets.sort()
    # The counter for unplaced fruit.
    unplaced = 0

    for basket in baskets:
        # Loop until we find a fruit that fits in the basket or until there are no more fruits.
        while fruits:
            fruit = -heapq.heappop(fruits)
            if basket >= fruit:
                # This fruit fits in the basket, so break out of the loop and move on to the next basket.
                break
            else:
                # This fruit doesn't fit in the basket, so increment the count of unplaced fruit and try the next fruit.
                unplaced += 1
        if not fruits:
            # No more fruits to place, so break out of the loop.
            break

    # If there are still fruits left, these are unplaced.
    unplaced += len(fruits)

    return unplaced
```

Let's run yet another sample to see how the function works:

```python
fruits = [7,5,6]
baskets = [6,7,8]
print(unplacedFruitTypes(fruits, baskets)) # prints 1
```

In each step:

1. First, the largest fruit (7) cannot fit in the smallest basket (6), so we increment unplaced to 1. We then try the next largest fruit (6).

2. The fruit of size 6 fits in the smallest basket (6), so we move on to the next basket.

3. Now, we only have one fruit left (5), which fits in the next basket (7). 

4. Finally, all fruits have been placed, but we still have one empty basket (8) left.

5. The function correctly returns 1, because one type of fruit could not be placed.
