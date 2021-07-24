class Clock:
    def __init__(self, hour, minute):
        carry, self.minutes = divmod(minute, 60)
        self.hour_sum = hour + carry

        self.RollOver()

    # __repr__ returns a representation of the object.
    def __repr__(self):
        return self.time

    # __eq__ is used to compare two objects
    def __eq__(self, other):
        return self.time == other.time

    # __add__ handles the + operator
    def __add__(self, minutes):
        carry, added_minutes = divmod(minutes, 60)

        self.hour_sum += carry
        self.minutes += added_minutes

        self.RollOver()

        return self.time

    # __sub__ handles the - operator
    def __sub__(self, minutes):
        carry, subbed_minutes = divmod(minutes, 60)
        self.hour_sum -= carry
        self.minutes -= subbed_minutes

        self.RollOver()

        return self.time

    def RollOver(self):
        while self.minutes < 0:
            self.hour_sum -= 1
            self.minutes += 60

        while self.minutes > 60:
            self.hour_sum += 1
            self.minutes -= 60

        while self.hour_sum < 0:
            self.hour_sum += 24
        
        while self.hour_sum >= 24:
            self.hour_sum -= 24

        self.time = f"{str(self.hour_sum).zfill(2)}:{str(self.minutes).zfill(2)}"