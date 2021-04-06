import unittest
from project.rooms.room import Room
# from project.rooms.alone_old import AloneOld
# from project.rooms.young_couple import YoungCouple
# from project.rooms.alone_young import AloneYoung
# from project.rooms.old_couple import OldCouple
# from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.people.child import Child
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Vatovi", 2000, 2)

    def test_room_init(self):
        self.assertEqual(self.room.family_name, "Vatovi")
        self.assertEqual(self.room.budget, 2000)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def test_if_setter_set_the_expenses(self):
        self.room.expenses = 20
        self.assertEqual(self.room.expenses, 20)

    def test_room_setter_raises_exception(self):
        with self.assertRaises(ValueError, msg="Expenses cannot be negative") as context:
            self.room.expenses = -20
        self.assertEqual(context.msg, "Expenses cannot be negative")

    def test_room_calculate_expenses(self):
        appliances = [TV(), Laptop(), Fridge()] * self.room.members_count
        child1 = Child(5, 2, 3, 1)
        children = [child1]
        self.room.calculate_expenses(appliances, children)
        self.assertEqual(self.room.expenses, 552)

    # def test_alone_old_init(self):
    #     self.alone_old_room = AloneOld("Frederikson", 500)
    #     self.assertEqual(self.alone_old_room.family_name, "Frederikson")
    #     self.assertEqual(self.alone_old_room.room_cost, 10)
    #     self.assertEqual(self.alone_old_room.budget, 500)
    #     self.assertEqual(self.alone_old_room.members_count, 1)
    #
    # def test_expenses_property_alone_old(self):
    #     self.alone_old_room = AloneOld("Frederikson", 500)
    #     self.assertEqual(self.alone_old_room.expenses, 0)
    #
    # def test_alone_young_init(self):
    #     self.alone_young = AloneYoung("Bonderik", 850)
    #     self.assertEqual(self.alone_young.family_name, "Bonderik")
    #     self.assertEqual(self.alone_young.room_cost, 10)
    #     self.assertEqual(self.alone_young.budget, 850)
    #     self.assertEqual(self.alone_young.members_count, 1)
    #
    # def test_expenses_property_alone_young(self):
    #     self.alone_young = AloneYoung("Bonderik", 850)
    #     self.assertEqual(self.alone_young.expenses, 45)
    #
    # def test_old_couple_init(self):
    #     self.old_couple = OldCouple("Lindenberg", 500, 650)
    #     self.assertEqual(self.old_couple.family_name, "Lindenberg")
    #     self.assertEqual(self.old_couple.room_cost, 15)
    #     self.assertEqual(self.old_couple.budget, 1150)
    #     self.assertEqual(self.old_couple.members_count, 2)
    #
    # def test_expenses_property_old_couple(self):
    #     self.old_couple = OldCouple("Lindenberg", 500, 650)
    #     self.assertEqual(self.old_couple.expenses, 204)
    #
    # def test_young_couple_with_children_init(self):
    #     child1 = Child(5, 2, 3, 1)
    #     self.young_couple_with_children = YoungCoupleWithChildren("Bonus Family", 1500, 2500, child1)
    #     self.assertEqual(self.young_couple_with_children.family_name, "Bonus Family")
    #     self.assertEqual(self.young_couple_with_children.budget, 4000)
    #     self.assertEqual(self.young_couple_with_children.members_count, 3)
    #     self.assertEqual(self.young_couple_with_children.room_cost, 30)
    #
    # def test_expenses_property_young_couple_with_children(self):
    #     child1 = Child(5, 2, 3, 1)
    #     self.young_couple_with_children = YoungCoupleWithChildren("Bonus Family", 1500, 2500, child1)
    #     self.assertEqual(self.young_couple_with_children.expenses, 663)
    #
    # def test_young_couple_init(self):
    #     self.young_couple = YoungCouple("Sopolevi", 2000, 2300)
    #     self.assertEqual(self.young_couple.family_name, "Sopolevi")
    #     self.assertEqual(self.young_couple.budget, 4300)
    #     self.assertEqual(self.young_couple.members_count, 2)
    #     self.assertEqual(self.young_couple.room_cost, 20)
    #
    # def test_expenses_property_young_couple(self):
    #     self.young_couple = YoungCouple("Sopolevi", 2000, 2300)
    #     self.assertEqual(self.young_couple.expenses, 222)


if __name__ == "__main__":
    unittest.main()