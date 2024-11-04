class Player:
    def __init__(self, name):
        self.name = name
        self.baskets = 0
        self.shots = 0

    def __repr__(self):
        return f"{self.name} {self.baskets}/{self.shots}"

class Team:
    def __init__(self):
        self.players = {} # Dictionary of player objects, starts empty

    # Make a new player with the given name and add to team
    def addPlayer(self, name):
        pass

    # Find the player matching name and update basket and shot count
    def addBasket(self, name):
        pass

    # Find the player matching name and update shot count
    def addMiss(self, name):
        pass

    def __repr__(self):
        return str(self.players)

team = Team()

team.addPlayer("alex")
team.addPlayer("marcus")

team.addBasket("marcus")
team.addBasket("marcus")

team.addMiss("marcus")
team.addMiss("alex")

print(team)
