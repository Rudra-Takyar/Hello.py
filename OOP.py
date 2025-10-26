# Define the Player class
class Player:
    def __init__(self, playerName, playerPosition):
        self._playerName = playerName        # underscore indicates internal/private
        self._playerPosition = playerPosition

    # Getter methods to access the attributes
    def getPlayerName(self):
        return self._playerName

    def getPlayerPosition(self):
        return self._playerPosition

# Define the NFLTeam class
class NFLTeam:
    def __init__(self, teamName, players):
        self._teamName = teamName            # underscore for internal/private
        self._players = players

    # Method to display team info
    def displayTeam(self):
        print("Team:", self._teamName)
        print("Players:")
        for player in self._players:
            print(player.getPlayerName(), "-", player.getPlayerPosition())

# Create player objects
player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

# Add players to a list
playerList = [player1, player2, player3, player4]

# Create a team object
team = NFLTeam("Smashmouth Warriors", playerList)

# Display the team
team.displayTeam()
