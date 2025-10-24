# 문제 풀이 1
def tournamentWinner(competitions, results):
    team_dict = {team: 0 for match in competitions for team in match}
    for i, match in enumerate(competitions):
        if results[i] == 1:
            team_dict[match[0]] += 3
        else:
            team_dict[match[1]] += 3
    return max(team_dict, key=lambda x: team_dict[x])

    # dict comprehension
    # key function


# 문제 풀이 2
from collections import Counter

def tournamentWinner(competitions, results):
    winners = (home if r == 1 else away for (home, away), r in zip(competitions, results))
    return Counter(winners).most_common(1)[0][0]

    # zip, generator
    # Counter().most_common
