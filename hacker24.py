from itertools import combinations
string, num = input().split()
string = sorted(string)
for i in range(1,int(num)+1):
    for j in list(combinations(string, i)):
        print("".join(j))
