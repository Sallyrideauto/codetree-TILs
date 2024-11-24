from collections import OrderedDict
import sys

class TreeMap:
    def __init__(self):
        self.map = OrderedDict()

    def add(self, k, v):
        # Add a (k, v) pair to the map, replacing if k already exists.
        self.map[k] = v
        # Keep map sorted by key.
        self.map = OrderedDict(sorted(self.map.items()))

    def remove(self, k):
        # Remove the key k from the map.
        if k in self.map:
            del self.map[k]

    def find(self, k):
        # Find and return the value associated with key k, or None if it doesn't exist.
        return self.map.get(k, None)

    def print_list(self):
        # Print the values of the map in order of their keys.
        if self.map:
            print(" ".join(map(str, self.map.values())))
        else:
            print("None")

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read number of commands
    n = int(data[0])
    
    # Create instance of TreeMap
    treemap = TreeMap()
    
    # Process each command
    for i in range(1, n + 1):
        command = data[i].split()
        if command[0] == "add":
            k, v = int(command[1]), int(command[2])
            treemap.add(k, v)
        elif command[0] == "remove":
            k = int(command[1])
            treemap.remove(k)
        elif command[0] == "find":
            k = int(command[1])
            result = treemap.find(k)
            print(result if result is not None else "None")
        elif command[0] == "print_list":
            treemap.print_list()

if __name__ == "__main__":
    main()