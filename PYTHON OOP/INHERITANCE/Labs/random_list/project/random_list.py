import random


class RandomList(list):
    def get_random_element(self):

        element_to_remove = random.choice(self)
        self.remove(element_to_remove)
        return element_to_remove



