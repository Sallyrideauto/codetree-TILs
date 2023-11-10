N = int(input())
seats = input().strip()

distances = []

for i in range(1, len(seats)):
    if seats[i - 1] == '1' and seats[i] == '0':
        dist = 0
        j = i
        while j < len(seats) and seats[j] == '0':
            dist += 1
            j += 1
        distances.append(dist)

updated_distances = [x - 1 for x in distances]
print(max(updated_distances))