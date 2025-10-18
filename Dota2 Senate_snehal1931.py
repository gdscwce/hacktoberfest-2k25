from collections import deque

def predictPartyVictory(senate: str) -> str:
    n = len(senate)
    qR = deque()
    qD = deque()

    # 1. Initialize queues with the original indices
    for i, char in enumerate(senate):
        if char == 'R':
            qR.append(i)
        else:
            qD.append(i)

    # 2. Simulate the round-based elimination process
    while qR and qD:
        # Get the next senator from each party
        r_idx = qR.popleft()
        d_idx = qD.popleft()

        # The senator with the smaller index acts first and bans the other.
        # The winner is re-queued with a new index (current index + N) 
        # to ensure they are considered in the next round.
        if r_idx < d_idx:
            # Radiant acts first, bans Dire's senator.
            # Radiant survives and is re-queued for the next round.
            qR.append(r_idx + n)
        else:
            # Dire acts first, bans Radiant's senator.
            # Dire survives and is re-queued for the next round.
            qD.append(d_idx + n)

    # 3. Determine the winner: The party with remaining senators wins.
    return "Radiant" if qR else "Dire"

# Example 1: R D
# qR = [0], qD = [1]
# R(0) < D(1) -> R wins, re-queue R: qR = [0+2], qD = []
# Loop ends. Winner: Radiant
print(f"RD -> {predictPartyVictory('RD')}") 

# Example 2: R D D
# Round 1:
# R(0) < D(1) -> R wins, re-queue R: qR = [0+3], qD = [2]
# D(2) < R(3) -> D wins, re-queue D: qD = [3+3], qR = [] (The R(3) was banned)
# Loop ends. Winner: Dire
print(f"RDD -> {predictPartyVictory('RDD')}")
