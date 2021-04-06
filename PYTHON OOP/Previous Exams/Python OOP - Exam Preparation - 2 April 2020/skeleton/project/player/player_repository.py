class PlayerRepository:

    def __init__(self):
        self.count: int = 0
        self.players = []

    def add(self, player):
        player_found = [plr for plr in self.players if plr.username == player.username]
        if player_found:
            player = player_found[0]
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        for pl in self.players:
            if pl.username == player:
                self.players.remove(pl)
                self.count -= 1

    def find(self, username: str):
        for pl in self.players:
            if pl.username == username:
                return pl


# from project.player.beginner import Beginner
#
# p = Beginner("test")
# pr = PlayerRepository()
# pr.add(p)
# print(pr.count)
# print(pr.find("test"))
