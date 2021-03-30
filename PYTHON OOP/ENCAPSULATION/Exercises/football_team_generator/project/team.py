class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @property
    def players(self):
        return self.__players

    @name.setter
    def name(self, value):
        self.__name = value

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player):
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str):
        try:
            player_in_the_team = [p for p in self.__players if p.name == player_name][0]
            self.__players.remove(player_in_the_team[0])
            return player_in_the_team[0]

        except IndexError:
            return f"Player {player_name} not found"


