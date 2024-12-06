import csv

with open("scores.csv") as file:
    games = list(csv.DictReader(file))

for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])

wins = {}
losses = {}

for game in games:
    homeTeam = game["home_team"]
    homeScore = game["home_score"]

    awayTeam = game["away_team"]
    awayScore = game["away_score"]

    wins.setdefault(homeTeam, 0)
    wins.setdefault(awayTeam, 0)

    losses.setdefault(homeTeam, 0)
    losses.setdefault(awayTeam, 0)

    # Your code goes here !!

for team in wins:
    print(team, wins[team], losses[team])
