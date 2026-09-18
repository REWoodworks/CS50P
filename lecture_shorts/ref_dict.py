## Dictionary examples
## example function with code
def main():
    scores = {}

    # Add key-value pairs
    scores["Alice"] = 95
    scores["Bob"] = 87

    # Reference a value using its key
    print(scores["Alice"])       # 95

    # Safely reference a possibly missing key
    print(scores.get("Charlie"))     # None
    print(scores.get("Charlie", 0))  # 0

    # Check whether a key exists
    if "Bob" in scores:
        print(scores["Bob"])

    # Change an existing value
    scores["Alice"] = 98

    # Loop through the dictionary
    for name, score in scores.items():
        print(name, score)


main()

## example functionality

scores ["Alice"] = 95
#       key       value

scores = {}                    # Create an empty dictionary

scores["Alice"] = 95           # Add or change an entry

scores["Alice"]                # Retrieve a value
scores.get("Alice")            # Retrieve safely

"Alice" in scores              # Check whether a key exists

scores.keys()                  # Access all keys
scores.values()                # Access all values
scores.items()                 # Access key-value pairs

del scores["Alice"]            # Delete an entry
scores.pop("Alice", None)      # Delete safely

len(scores)                    # Count the entries


