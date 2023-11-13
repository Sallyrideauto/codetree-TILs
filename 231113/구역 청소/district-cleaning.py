a, b = map(int, input().split())
c, d = map(int, input().split())

# 청소된 구역의 시작과 끝 계산
start = min(a, c)
end = max(b, d)

# 청소된 구역의 수 출력
print(end - start)