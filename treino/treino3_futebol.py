def allmatches(teams):
    matches=[]
    for team1 in teams:
        for team2 in teams:
            if team1 != team2:
                matches.append((team1,team2))
    return matches


teams=['CAF','SLB','FPF']
print(allmatches(teams))