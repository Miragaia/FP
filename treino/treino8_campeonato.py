def setTeams():
    print('Digite uma equipa')
    teams=[]
    while True:
        team = input()
        if team =='':
            break
        else:
            teams.append(team)
    return teams


def allmatches(teams):
    matches=[]
    for team1 in teams:
        for team2 in teams:
            if team1 != team2:
                matches.append((team1,team2))
    print(matches)
    return matches

def results(matches):
    results={}
    for n in matches:
        print(n)
        r=[]
        r1= input('Qual o resultado do encontro? ')
        r.append((r1))
        r2= input('Qual o resultado do encontro? ')
        r.append((r2))
        results[n]= r

    return results

def tabela(eq, ma, res):
    pontos = [0] * len(eq)
    x = 0
    for e in eq:
        for m in ma:
            if (e == ma[0] and res[m][0] > res[m][1]) or (e == ma[1] and res[m][1] > res[m][0]):
                pontos[x] += 3
            elif (e == ma[0] and res[m][0] == res[m][1]) or (e == ma[1] and res[m][0] == res[m][1]):
                pontos[x] += 1
          
            
                

def main():
    T=setTeams()
    M=allmatches(T)
    R=results(M)
    print(R)

main()
