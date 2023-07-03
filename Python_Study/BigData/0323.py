
result = 0

# i = 1
# while i <= 1000:
#   if i % 3 == 0:
#     result += i
#   i += 1

for i in range(1, 1001):
    if i % 3 == 0:
        result += i

print(result)
