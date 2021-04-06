from collections import deque

from project.player.beginner import Beginner


class BattleField:

    @staticmethod
    def fight(attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")
        if isinstance(attacker, Beginner):
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30
        if isinstance(enemy, Beginner):
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        attacker_bonus_points = sum([card.health_points for card in attacker.card_repository.cards])
        attacker.health += attacker_bonus_points
        enemy_bonus_points = sum([card.health_points for card in enemy.card_repository.cards])
        enemy.health += enemy_bonus_points

        while not attacker.is_dead and not enemy.is_dead and attacker.card_repository.cards and enemy.card_repository.cards:
            attacker.card_repository.cards = deque(attacker.card_repository.cards)
            attacker_card = attacker.card_repository.cards.popleft()
            enemy.take_damage(attacker_card.damage_points)
            enemy.card_repository.cards = deque(enemy.card_repository.cards)
            enemy_card = enemy.card_repository.cards.popleft()
            attacker.take_damage(enemy_card.damage_points)






