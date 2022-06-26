n, m = map(int, input().split())
card = []
sum = []
tmp_card = input()

tmp_string = ""
for i in range(len(tmp_card)):
    if (tmp_card[i] == ' ' or tmp_card[i] == '\n') and tmp_string != '':
        card.append(int(tmp_string))
        tmp_string = ""
    if tmp_card[i] != ' ':
        tmp_string += tmp_card[i]
    if i == len(tmp_card) - 1:
        card.append(int(tmp_string))
for i in range(n):
    for j in range(n):
        for k in range(n):
            if card[i] + card[j] + card[k] <= m and not (i >= j or i >= k or j >= k):
                sum.append(card[i] + card[j] + card[k])
print(max(sum))