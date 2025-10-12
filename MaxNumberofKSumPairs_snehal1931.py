from collections import Counter
from typing import List

def maxOperations_Counter(nums: List[int], k: int) -> int:
    counts = Counter(nums)
    operations = 0
    
    # Iterate over a copy of the keys to safely modify the counts
    for num in list(counts.keys()):
        # The number needed to sum to k
        complement = k - num
        
        if complement in counts:
            if num == complement:
                # If num == complement (e.g., k=6, num=3), the number of pairs is count[num] // 2
                operations += counts[num] // 2
                # Mark as used to prevent double counting
                counts[num] = 0
            else:
                # If num != complement, number of pairs is the minimum of their counts
                pairs = min(counts[num], counts[complement])
                operations += pairs
                
                # Mark as used to prevent double counting (e.g., when k-num is encountered later)
                counts[num] -= pairs
                counts[complement] -= pairs

    return operations

# A more concise version (without modifying the Counter) is often used:
def maxOperations_Concise(nums: List[int], k: int) -> int:
    counts = Counter(nums)
    total_pairs = 0
    
    for num in counts:
        complement = k - num
        
        if complement in counts:
            if num == complement:
                # For num=complement, we count pairs as count[num] // 2
                total_pairs += counts[num] // 2
            elif num < complement:
                # For num < complement, we count min(count[num], count[complement])
                # and only count once (e.g., when num=1, complement=4, we skip when num=4)
                total_pairs += min(counts[num], counts[complement])
                
    return total_pairs
