
class Player:
    def __init__(self, playerName, playerPosition):
        self._playerName = playerName        
        self._playerPosition = playerPosition

   
    def getPlayerName(self):
        return self._playerName

    def getPlayerPosition(self):
        return self._playerPosition


class NFLTeam:
    def __init__(self, teamName, players):
        self._teamName = teamName           
        self._players = players

  
    def displayTeam(self):
        print("Team:", self._teamName)
        print("Players:")
        for player in self._players:
            print(player.getPlayerName(), "-", player.getPlayerPosition())


player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")


playerList = [player1, player2, player3, player4]


team = NFLTeam("Smashmouth Warriors", playerList)

# Display the team
team.displayTeam()

