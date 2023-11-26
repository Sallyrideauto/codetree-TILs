import sys

def min_wifi_to_cover(n, m, houses):
    wifi_count = 0
    i = 0

    while i < n:
        if houses[i] == 1:
            wifi_pos = i + m
            wifi_count += 1

            i = wifi_pos + m + 1
        else:
            i += 1

    return wifi_count

n, m = map(int, input().split())
houses = list(map(int, sys.stdin.readline().split()))

print(min_wifi_to_cover(n, m, houses))