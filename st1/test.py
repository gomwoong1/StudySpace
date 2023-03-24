val = list(map(int, input().split()))
max = 0
min = 9999

for i in val:
    if i > max:
        max = i
    if i < min:
        min = i

print("최대값:", max)
print("최소값", min)