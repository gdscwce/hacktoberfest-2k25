from collections import deque

def deckRevealedIncreasing(deck: list[int]) -> list[int]:
    # 1. Sort the deck in ascending order. 
    # This is the ORDER we want the cards to be REVEALED.
    # We will process them from LARGEST to SMALLEST.
    deck.sort() 
    
    # Use a deque to build the final initial deck arrangement (in reverse).
    # The deque will hold the final arrangement.
    result_deck = deque()

    # Iterate through the sorted cards from LARGEST to SMALLEST.
    # The largest card is the last one in the sorted list.
    for card in reversed(deck):
        
        # Reverse Step 2: Undo the "move to bottom" operation
        if result_deck:
            # Take the card from the back (which was the "next top card")
            last_card = result_deck.pop() 
            # and move it to the front (where it was originally before being moved to bottom).
            result_deck.appendleft(last_card)
        
        # Reverse Step 1: Place the current card (the one that would be revealed)
        # It must be the new top card.
        result_deck.appendleft(card)
        
    # Convert the deque back to a list for the final answer.
    return list(result_deck)

# Example: [17, 13, 11, 2, 3, 5, 7]
# Sorted deck: [2, 3, 5, 7, 11, 13, 17]

# Reverse Process Walkthrough:
# 1. Process 17: result_deck = [17]
# 2. Process 13: 
#    - Move 17 (last) to front: [17] -> [17] 
#    - Add 13 to front: [13, 17]
# 3. Process 11: 
#    - Move 17 (last) to front: [13, 17] -> [17, 13]
#    - Add 11 to front: [11, 17, 13]
# 4. Process 7: 
#    - Move 13 (last) to front: [11, 17, 13] -> [13, 11, 17]
#    - Add 7 to front: [7, 13, 11, 17]
# 5. Process 5: 
#    - Move 17 (last) to front: [7, 13, 11, 17] -> [17, 7, 13, 11]
#    - Add 5 to front: [5, 17, 7, 13, 11]
# 6. Process 3: 
#    - Move 11 (last) to front: [5, 17, 7, 13, 11] -> [11, 5, 17, 7, 13]
#    - Add 3 to front: [3, 11, 5, 17, 7, 13]
# 7. Process 2: 
#    - Move 13 (last) to front: [3, 11, 5, 17, 7, 13] -> [13, 3, 11, 5, 17, 7]
#    - Add 2 to front: [2, 13, 3, 11, 5, 17, 7]

deck = [17, 13, 11, 2, 3, 5, 7]
print(f"Initial Deck: {deck}")
print(f"Required Order: {deckRevealedIncreasing(deck)}")
# Output: [2, 13, 3, 11, 5, 17, 7]
