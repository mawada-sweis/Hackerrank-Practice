A = set(map(int, input().split()))
N = int(input())
flag = True
for _ in range(N):
    B = set(map(int, input().split()))
    
    if len(B.intersection(A)) != len(B):
        flag = False

print(flag)