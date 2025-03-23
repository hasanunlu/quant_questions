import random

N = 1000000  # Number of simulated games
X = 40       # Payment cost to open each box
total = 0    # Running total of net earnings

for i in range(N):
    # Randomly determine the winning box (one of 0, 1, 2, or 3)
    winning_box = random.randint(0, 3)

    # Initialize a list representing the four boxes
    boxes = [0, 1, 2, 3]

    # First attempt: randomly choose one box
    first_attempt = random.choice(boxes)

    if first_attempt == winning_box:
        # If the first attempt is correct, net gain is prize (100) minus cost of one box (X)
        total += 100 - X
    else:
        # Remove the first (wrong) attempt and proceed to a second attempt
        boxes.remove(first_attempt)
        second_attempt = random.choice(boxes)

        if second_attempt == winning_box:
            # If the second attempt is correct, net gain is prize minus cost of two boxes (2 * X)
            total += 100 - 2 * X
        else:
            # Remove the second (wrong) attempt and proceed to a third attempt
            boxes.remove(second_attempt)
            third_attempt = random.choice(boxes)

            if third_attempt == winning_box:
                # If the third attempt is correct, net gain is prize minus cost of three boxes (3 * X)
                total += 100 - 3 * X
            else:
                # If the first three attempts are wrong, the last remaining box must be the winning box.
                # Net gain is prize minus cost of all four boxes (4 * X)
                total += 100 - 4 * X

# Compute the expected net earnings per game.
# This represents the prize (100) minus the total cost for the boxes opened.
# In a fair game, the expected net earnings should be close to zero.
print('Expected net earnings per game:', total / N)
