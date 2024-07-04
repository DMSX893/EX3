import random

results = []
heads = 0
tails = 0

print("Tossing a coin...")

for round in range(1, 4):
    result = random.choice(["Heads", "Tails"])
    print(f"Round {round}: {result}")
    results.append(result)
    if result == "Heads":
        heads += 1
    else:
        tails += 1

print(f"Heads: {heads}, Tails: {tails}")




