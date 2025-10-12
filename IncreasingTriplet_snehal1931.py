import math

def increasingTriplet(nums: list[int]) -> bool:
    """
    Checks if there exists an increasing subsequence of length 3 
    (i.e., nums[i] < nums[j] < nums[k] where i < j < k).
    The solution is O(n) time and O(1) space.
    """
    
    # We maintain two variables to track the smallest and second smallest 
    # numbers encountered so far. We initialize them to positive infinity 
    # to ensure any number in the array will be smaller than them initially.
    # first: Stores the smallest number found so far.
    # second: Stores the second smallest number found so far (which is > first).
    first = math.inf
    second = math.inf
    
    for n in nums:
        # Case 1: n is smaller than or equal to the smallest number found.
        # This is the best candidate for the start of a new triplet.
        if n <= first:
            first = n
            
        # Case 2: n is greater than 'first' but smaller than or equal to 'second'.
        # This number extends our potential pair (first, second) and is a 
        # better candidate for the middle of a triplet.
        elif n <= second:
            second = n
            
        # Case 3: n is greater than 'second'.
        # Since first < second, and second < n, we have found a triplet: 
        # (first, second, n). We can immediately return True.
        else: # n > second
            return True
            
    # If we iterate through the entire array without finding Case 3, 
    # no increasing triplet exists.
    return False

# --- Example Usage ---
print(f"Input: [1, 2, 3, 4, 5] -> Output: {increasingTriplet([1, 2, 3, 4, 5])}")
print(f"Input: [5, 4, 3, 2, 1] -> Output: {increasingTriplet([5, 4, 3, 2, 1])}")
print(f"Input: [2, 1, 5, 0, 4, 6] -> Output: {increasingTriplet([2, 1, 5, 0, 4, 6])}") # True (0, 4, 6 or 1, 4, 6)
print(f"Input: [20, 100, 10, 101] -> Output: {increasingTriplet([20, 100, 10, 101])}") # True (20, 100, 101)
