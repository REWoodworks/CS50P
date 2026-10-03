# CS50P Week 2 Short: Lists
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - results.py
# Race results in a list: append adds one item, extend adds each item from
# another list, remove deletes by value, insert adds at a position, index finds
# a position, and reverse flips the order.

results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

print(results)

results.append(["Bowser", "Donkey Kong Jr."])
results.remove(["Bowser", "Donkey Kong Jr."])
results.extend(["Bowser", "Donkey Kong Jr."])

print(results)

results.remove("Bowser")

print(results)

results.insert(0, "Bowser")

print(results)

print(results.index("Mario"))

results.reverse()

print(results)
