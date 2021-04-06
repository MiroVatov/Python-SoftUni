import unittest
from test_worker.test_worker import Worker


class WorkerTest(unittest.TestCase):

    def setUp(self):
        self.worker = Worker('Ivan Ivanov', 20000, 200)

    def tearDown(self):
        self.worker = None

    def test_is_worker_initialized_with_the_correct_name_salary_and_energy(self):
        # Variant 1 -->>
        # result = self.worker.get_full_info
        # expected_result = 'Ivan Ivanov 20000 200'
        # self.assertEqual(expected_result, result)

        # Variant 2 -->>

        self.assertEqual(self.worker.name, 'Ivan Ivanov')
        self.assertEqual(self.worker.salary, 20000)
        self.assertEqual(self.worker.energy, 200)

    def test_is_workers_energy_decreased_after_rest_method_is_called(self):
        # variant 1 -->
        # self.worker.rest()
        # result = self.worker.energy
        # expected_result = 201
        # self.assertEqual(result, expected_result)

        # Variant 2 -->>

        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)

    def test_is_worker_still_working_after_his_energy_drops_to_0(self):

        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_workers_money_are_increased_by_his_salary_correctly_after_the_work_method_is_called(self):

        # Variant 1 -->>
        # self.worker.work()
        # result = self.worker.money
        # expected_result = 20000
        # self.assertEqual(result, expected_result)

        # Variant 2

        old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - old_money, self.worker.salary)

    def test_workers_energy_is_decreased_after_the_work_method_is_called(self):

        # Variant 1 -->>
        # self.worker.work()
        # result = self.worker.energy
        # expected_result = 199
        # self.assertEqual(result, expected_result)

        # Variant 2 -->>
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy - old_energy, -1)

    def test_if_get_info_method_returns_the_proper_values(self):

        # Variant 1 -->>

        # result = self.worker.get_info()
        # expected_result = 'Ivan Ivanov has saved 0 money.'
        # self.assertEqual(result, expected_result)

        # Variant 2 -- >>
        result = self.worker.get_info()
        self.assertEqual(result, 'Ivan Ivanov has saved 0 money.')


if __name__ == "__main__":
    unittest.main()
