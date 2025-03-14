a, b = map(int, input().strip().split(' '))

row= ""
for i in range(a):
    row+="*"

for i in range(b):
    print(row)
