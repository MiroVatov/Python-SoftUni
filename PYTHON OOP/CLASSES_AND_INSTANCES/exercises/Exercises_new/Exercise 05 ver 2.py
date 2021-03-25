class Time:

    hours: int
    minutes: int
    seconds: int

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    def next_second(self) -> str:
        self.seconds = (self.seconds + 1) % 60
        self.minutes = (self.minutes + int(self.seconds == 0)) % 60
        self.hours = (self.hours + int(self.minutes == 0 and self.seconds == 0)) % 24
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())

time = Time(00, 00, 00)
print(time.next_second())