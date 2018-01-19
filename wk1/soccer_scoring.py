teams = {}
for line in open("commentary.txt"):
    splitted = line.split()
    if 'versus' in splitted:
        teams[splitted[0]] = 0
        teams[splitted[2]] = 0
    else:
        teams[splitted[0]] += 1
printed = 0
for points in sorted(teams.values(), reverse=True):
    for team, score in teams.items():
        if score == points and printed < 2:
            print(team, score)
            printed += 1