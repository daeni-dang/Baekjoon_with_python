import sys

N, M = map(int, input().split())

pokemon = {}
pokemon_rev = {}

for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    pokemon[i + 1] = tmp
    pokemon_rev[tmp] = i + 1

for i in range(M):
    query = sys.stdin.readline().rstrip()
    if '0' <= query[0] <= '9':
        if 1 <= int(query) <= N:
            sys.stdout.write(pokemon[int(query)] + '\n')
    else:
        sys.stdout.write(str(pokemon_rev[query]) + '\n')
