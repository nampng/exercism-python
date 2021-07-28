class Team:
    def __init__(self, name) -> None:
        self.name = name
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.points = 0

    def AddWin(self):
        self.wins += 1
        self.matches_played += 1
        self.points += 3
    
    def AddDraw(self):
        self.draws += 1
        self.matches_played += 1
        self.points += 1
    
    def AddLoss(self):
        self.losses += 1
        self.matches_played += 1

    def __repr__(self) -> str:
        return f"{self.name}".ljust(31) + f"|  {self.matches_played} |  {self.wins} |  {self.draws} |  {self.losses} |  {self.points}"

def tally(rows):
    output = ["Team                           | MP |  W |  D |  L |  P"]
    teams = {}
    if rows:
        for row in rows:
            data = row.split(';')
            print(f"Team {data[0]} {data[2]} against {data[1]}")
            if data[0] not in teams:
                teams[data[0]] = Team(data[0])
            if data[1] not in teams:
                teams[data[1]] = Team(data[1])

            if data[2] == "win":
                teams[data[0]].AddWin()
                teams[data[1]].AddLoss()
            elif data[2] == "loss":
                teams[data[1]].AddWin()
                teams[data[0]].AddLoss()
            else:
                teams[data[0]].AddDraw()
                teams[data[1]].AddDraw()

    sorted_teams = []
    for team in teams:
        sorted_teams.append( (team, teams[team].points) )

    print(sorted_teams)
    sorted_teams.sort(key = lambda x: x[0])
    sorted_teams.sort(key = lambda x: x[1], reverse=True)
    print(sorted_teams)


    for team in sorted_teams:
        output.append(str(teams[team[0]]))

    # print(output)
    return output
    

