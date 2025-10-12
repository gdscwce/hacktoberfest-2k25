def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    """
    Determines if 'n' new flowers can be planted in the flowerbed 
    such that no two flowers are planted in adjacent plots.
    """
    if n == 0:
        return True

    count = 0
    # Pad the flowerbed with zeros at both ends to simplify the logic 
    # for the first and last elements.
    # [0] + flowerbed + [0]
    padded_flowerbed = [0] + flowerbed + [0]
    
    # Iterate from the second element (index 1) up to the second-to-last 
    # element of the padded array. This corresponds to the original flowerbed.
    for i in range(1, len(padded_flowerbed) - 1):
        
        # Check if the current plot and its neighbors are empty.
        # padded_flowerbed[i-1] is the left neighbor (or the added '0' before the start).
        # padded_flowerbed[i] is the current plot.
        # padded_flowerbed[i+1] is the right neighbor (or the added '0' after the end).
        if (padded_flowerbed[i-1] == 0 and 
            padded_flowerbed[i] == 0 and 
            padded_flowerbed[i+1] == 0):
            
            # If all three are 0, we can plant a flower here.
            padded_flowerbed[i] = 1
            count += 1
            
            # If we've planted enough flowers, we can stop and return True.
            if count >= n:
                return True
                
    return count >= n

# --- Example Usage ---
# Example 1: flowerbed = [1,0,0,0,1], n = 1 -> True
print(f"Example 1: {canPlaceFlowers([1,0,0,0,1], 1)}") 
# Example 2: flowerbed = [1,0,0,0,1], n = 2 -> False
print(f"Example 2: {canPlaceFlowers([1,0,0,0,1], 2)}") 
# Example 3: flowerbed = [0,0,1,0,0], n = 2 -> True
print(f"Example 3: {canPlaceFlowers([0,0,1,0,0], 2)}") 
# Example 4: flowerbed = [0,0,0,0,0], n = 3 -> True
print(f"Example 4: {canPlaceFlowers([0,0,0,0,0], 3)}")
# Example 5: flowerbed = [1,0,1,0,1], n = 0 -> True
print(f"Example 5: {canPlaceFlowers([1,0,1,0,1], 0)}")
