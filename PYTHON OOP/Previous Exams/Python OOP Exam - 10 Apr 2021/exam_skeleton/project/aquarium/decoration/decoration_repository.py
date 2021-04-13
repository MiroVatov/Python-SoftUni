class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        if decoration not in self.decorations:
            self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:   # NOTE check if we have to search the decoration by index or smth else
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        decoration_found = [dec for dec in self.decorations if dec.__class__.__name__ == decoration_type]
        if decoration_found:
            return decoration_found[0]
        return "None"

