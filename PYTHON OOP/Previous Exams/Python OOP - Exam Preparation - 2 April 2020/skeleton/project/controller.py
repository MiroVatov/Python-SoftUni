from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        player = ''
        if type == "Beginner":
            player = Beginner(username)
        elif type == "Advanced":
            player = Advanced(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        card = ''
        if type == "Magic":
            card = MagicCard(name)
        elif type == "Trap":
            card = TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = [pl for pl in self.player_repository.players if pl.username == username]
        card = [ca for ca in self.card_repository.cards if ca.name == card_name]
        if player and card:
            player = player[0]
            card = card[0]
            player.card_repository.add(card)
            return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = [attack for attack in self.player_repository.players if attack.username == attack_name]
        enemy = [enemy for enemy in self.player_repository.players if enemy.username == enemy_name]
        if attacker and enemy:
            attacker = attacker[0]
            enemy = enemy[0]
            battlefield = BattleField()  # TODO  check if Battlefield should be instantiated  !!!
            battlefield.fight(attacker, enemy)
            return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        data = ''
        for user in self.player_repository.players:
            data += f"Username: {user.username} - Health: {user.health} - Cards {user.card_repository.count}" + '\n'
            for card in user.card_repository.cards:
                data += f"### Card: {card.name} - Damage: {card.damage_points}" + '\n'
        return data


# controller = Controller()
# controller.add_card()