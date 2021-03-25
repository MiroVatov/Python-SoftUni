class Smartphone:

    apps = []
    is_on: bool = False

    def __init__(self, memory: int):
        self.memory = memory

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if (self.memory - app_memory) >= 0 and self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif (self.memory - app_memory) >= 0 and not self.is_on:
            return f"Turn on your phone to install {app}"

        else:
            return f"Not enough memory to install {app}"

    def status(self):
        memory_left = self.memory
        return f"Total apps: {len(self.apps)}. Memory left: {memory_left}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
