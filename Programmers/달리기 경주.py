def solution(players, callings):
    answer = []
    rankDict = {}
    playerDict = {}
    for idx, player in enumerate(players):
        rankDict[idx + 1] = player
        playerDict[player] = idx + 1
    
    for call in callings:
        curRank = playerDict[call]
        # call player의 등수 1 감소
        prevPlayer = rankDict[curRank - 1]
        rankDict[curRank - 1] = call
        playerDict[call] -= 1
        # 1 감소된 등수였던 player 등수 1 증가
        rankDict[curRank] = prevPlayer
        playerDict[prevPlayer] += 1
    answer = list(rankDict.values())
    return answer