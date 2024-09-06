n = int(input())
words = []

for _ in range(n):
    s = input()
    words.append(s)

hashmap = {}

for word in words:
    hashmap[word] = hashmap.get(word, 0) + 1
    
all_values = hashmap.values()
max_value = max(all_values)

print(max_value)