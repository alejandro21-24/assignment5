# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    # Count how many times each number appears
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    # Start by assuming the first number is the most frequent
    most_common = numbers[0]

    # Check the counts to find the number that appears the most
    for number in counts:
        if counts[number] > counts[most_common]:
            most_common = number

    return most_common


"""
Time and Space Analysis for problem 1:

- Best-case: O(n). Even if the same number appears every time, the
  function still needs to go through the list to count the values.

- Worst-case: O(n) expected time. The function goes through the input
  list and then through the dictionary of counts. Dictionary lookups
  are O(1) on average.

- Average-case: O(n). Each number is processed once while counting,
  and dictionary operations are normally O(1).

- Space complexity: O(n). In the worst case, every number in the list
  is different, so the dictionary could contain n different entries.

- Why this approach?
  I used a dictionary because it lets me keep track of each number
  and how many times it appears. This is more efficient than comparing
  every number to every other number.

- Could it be optimized?
  This solution is already efficient for an unsorted list. Another
  approach would be sorting the list first, but sorting would take
  O(n log n) time. The dictionary uses extra memory, but gives better
  expected time performance.
"""


# Test cases for Problem 1
assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([5, 5, 5]) == 5
assert most_frequent([10]) == 10
assert most_frequent([]) is None


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        # Only add the number if we have not seen it before
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for problem 2:

- Best-case: O(n). The function still needs to check every item in
  the input list.

- Worst-case: O(n) expected time using normal hash-based set behavior.
  Each item is checked and possibly added to the set.

- Average-case: O(n). Looking up and adding an item to a set is O(1)
  on average, and we process n items.

- Space complexity: O(n). The set may store every unique number and
  the result list can also contain up to n values.

- Why this approach?
  I used a set because it is fast for checking whether something has
  already been seen. I also used a result list so the original order
  of the numbers is preserved.

- Could it be optimized?
  I could avoid using a set and check if each number is already in
  the result list. That would use less extra memory, but searching
  the result list repeatedly could make the algorithm O(n^2).
  The set uses more memory but gives much better expected performance.
"""


# Test cases for Problem 2
assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        # Figure out which number would be needed to reach the target
        needed = target - number

        # If we already saw that number, we found a pair
        if needed in seen:
            pairs.append((needed, number))

        seen.add(number)

    return pairs


"""
Time and Space Analysis for problem 3:

- Best-case: O(n). Even if there are no matching pairs, the function
  still goes through the entire list.

- Worst-case: O(n) expected time with normal hash-set behavior because
  each number is processed once and set lookups are O(1) on average.

- Average-case: O(n). Each number is visited once and the set gives
  fast average lookups.

- Space complexity: O(n). The seen set may eventually contain all n
  numbers. The output list also requires space for the pairs found.

- Why this approach?
  I used a set so I do not have to compare every number with every
  other number. For each number, I calculate the number that is needed
  to reach the target and check if I have already seen it.

- Could it be optimized?
  A nested-loop solution could use less extra memory, but it would take
  O(n^2) time. Another option would be sorting the list and using two
  pointers. Sorting would normally make the time O(n log n). I chose
  the set because it gives O(n) expected time while keeping the code
  simple.
"""


# Test cases for Problem 3
assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
assert set(find_pairs([1, 2, 3, 4], 7)) == {(3, 4)}
assert find_pairs([], 5) == []
assert find_pairs([1], 5) == []


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over.
#
# Example:
# add_n_items(6) -> should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    items = [None] * capacity

    for value in range(n):

        # If the list is full, double its capacity
        if size == capacity:
            old_capacity = capacity
            capacity *= 2

            print(f"Resizing from {old_capacity} to {capacity}")

            # Create a larger list
            new_items = [None] * capacity

            # Copy the old values into the new list
            for i in range(size):
                new_items[i] = items[i]

            items = new_items

        # Add the new value
        items[size] = value
        size += 1

    return items[:size]


"""
Time and Space Analysis for problem 4:

- When do resizes happen?
  A resize happens whenever the current number of elements reaches
  the capacity of the list. Starting with capacity 1, the capacities
  grow like 1, 2, 4, 8, 16, 32, and so on.

- What is the worst-case for a single append?
  O(n). Most appends are fast, but when the list is full, a new list
  must be created and all existing elements must be copied.

- What is the amortized time per append overall?
  O(1). Resizing is expensive when it happens, but it does not happen
  for every append. The expensive resize operations are spread across
  many cheap append operations.

- Space complexity:
  O(n). The amount of memory used grows with the number of elements.
  During a resize, both the old list and the new larger list temporarily
  exist.

- Why does doubling reduce the cost overall?
  Doubling gives the list extra empty space for future items. This
  means the program does not need to create a new list every time one
  new element is added. Resizes become less frequent as capacity grows.
"""


# Test cases for Problem 4
assert add_n_items(0) == []
assert add_n_items(1) == [0]
assert add_n_items(6) == [0, 1, 2, 3, 4, 5]


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0

    # Keep the previous total instead of recalculating everything
    for number in nums:
        total += number
        result.append(total)

    return result


"""
Time and Space Analysis for problem 5:

- Best-case: O(n). Each number in the input list is processed once.

- Worst-case: O(n). The function only makes one pass through the list.

- Average-case: O(n). The amount of work grows directly with the
  number of values in the list.

- Space complexity: O(n). The problem requires a new list containing
  the running total for every input value.

- Why this approach?
  I keep one running total and add each new number to it. This means
  I do not have to go back and add the previous numbers again.

- Could it be optimized?
  Yes. A slower original solution could calculate sum(nums[:i + 1])
  for every position. That repeatedly adds numbers that were already
  calculated and would take O(n^2) time.

  I optimized this solution by storing the current total in the
  variable "total". Each number is now processed only once, improving
  the time complexity from O(n^2) to O(n).

- Optimization trade-off:
  Both versions need O(n) space for the output list because the problem
  requires returning a new list. The optimized version is better
  because it avoids repeated calculations without needing meaningful
  additional memory.
"""


# Test cases for Problem 5
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([5]) == [5]
assert running_total([]) == []
assert running_total([2, -1, 4]) == [2, 1, 5]


print("All tests passed!")