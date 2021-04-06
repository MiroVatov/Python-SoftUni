class Robot:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def get_count(self):
        pass


class Android(Robot):

    def get_count(self):
        return 4


class Chappie(Robot):
    def get_count(self):
        return 6


def count_robot_senzors(robots: list):
    for robot in robots:
        print(robot.get_count())


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)
