import random
from datetime import datetime

class Robot:
    def __init__(self):
        self.name = self.createName()

    def reset(self):
        random.seed(datetime.utcnow().timestamp())
        self.name = self.createName()

    def createName(self):
        name = chr(random.randint(97, 97 + 26)) + chr(random.randint(97, 97 + 26)) + str(random.randint(100, 1000))
        return name.upper()

