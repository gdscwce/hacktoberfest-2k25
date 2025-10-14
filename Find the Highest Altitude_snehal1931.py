def find_highest_altitude(gain: list[int]) -> int:
    """
    Calculates the highest altitude reached on a road trip.

    Args:
        gain: A list of integers where gain[i] is the net change 
              in altitude between point i and point i + 1.

    Returns:
        The highest altitude reached during the entire trip.
    """
    
    # The highest altitude reached so far (starts at the initial altitude)
    highest_altitude = 0 
    
    # The altitude at the current point (starts at point 0)
    current_altitude = 0 

    for net_gain in gain:
        # Update the current altitude by adding the net gain
        current_altitude += net_gain
        
        # Check if the new current altitude is the highest reached so far
        highest_altitude = max(highest_altitude, current_altitude)

    return highest_altitude

# Example 1:
gain1 = [-5, 1, 5, 0, -7]
# Altitudes: [0, -5, -4, 1, 1, -6]. Highest is 1.
print(f"Example 1 Highest Altitude: {find_highest_altitude(gain1)}")

# Example 2:
gain2 = [-4, 2, 6, 1, -6]
# Altitudes: [0, -4, -2, 4, 5, -1]. Highest is 5.
print(f"Example 2 Highest Altitude: {find_highest_altitude(gain2)}")
