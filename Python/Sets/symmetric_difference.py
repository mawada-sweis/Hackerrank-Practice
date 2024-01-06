M = int(input())
M_List = set(map(int, input().split()))

N = int(input())
N_List = set(map(int, input().split()))

diff = sorted(M_List.symmetric_difference(N_List))

for i in diff:
    print(i)