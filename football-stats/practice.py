import csv

with open("scores.csv") as file:
    games = list(csv.DictReader(file))

for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])

class TeamStats:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.pointsScored = 0
        self.pointsAllowed = 0
        self.numGames = 0

    def addStatsHome(self, game):
        # Your code goes here !!
        pass

    def addStatsAway(self, game):
        # Your code goes here !!
        pass

    def winPercent(self):
        return round(self.wins / self.numGames, 2)

    def pointsScoredPerGame(self):
        # Your code goes here !!
        pass

    def pointsAllowedPerGame(self):
        # Your code goes here !!
        pass

    def __repr__(self):
        result = ""

        result += f"wins:               {self.wins}\n"
        result += f"losses:             {self.losses}\n"
        result += f"winPercent:         {self.winPercent()}\n"
        result += f"pointsScored:       {self.pointsScored}\n"
        result += f"pointsAllowed:      {self.pointsAllowed}\n"
        result += f"numGames:           {self.numGames}\n"
        result += f"pointsScored/game:  {self.pointsScoredPerGame()}\n"
        result += f"pointsAllowed/game: {self.pointsAllowedPerGame()}\n"

        return result

stats = {}

for game in games:
    stats.setdefault(game["home_team"], TeamStats())
    stats.setdefault(game["away_team"], TeamStats())

for game in games:
    homeStats = stats[game["home_team"]]
    awayStats = stats[game["away_team"]]

    homeStats.addStatsHome(game)
    awayStats.addStatsAway(game)

for team in stats:
    print(team)
    print(stats[team])
