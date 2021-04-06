class CardRepository:

    def __init__(self):
        self.count: int = 0
        self.cards = []

    # TODO create method to check the cards by name  -->> IF NEEDED !!!

    def add(self, card):
        card_found = [ca for ca in self.cards if ca.name == card.name]
        if card_found:
            card = card_found[0]
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")

        for c in self.cards:
            if c.name == card:
                self.cards.remove(c)
                self.count -= 1

    def find(self, name: str):
        for c in self.cards:
            if c.name == name:
                return c


# from project.card.magic_card import MagicCard
#
# c = MagicCard("magic")
# cr = CardRepository()
# cr.add(c)
# cr.add(c)
# print(cr.count)
# print(cr.cards)
# print(cr.remove("magic"))
# print(cr.cards)
# print(cr.count)