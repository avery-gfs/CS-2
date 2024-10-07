class Time:
    def __init__(self, hours, minutes, ampm):
        # Add code to normalize hours, minutes, and ampm
        self.hours = hours
        self.minutes = minutes
        self.ampm = ampm

    def __repr__(self):
        # Add code to account for when minutes < 10
        # Add code to account for when hours == 0
        return f"{self.hours}:{self.minutes}{self.ampm}"

    def totalMinutes(self):
        # Add code to calculate the total numbers of minutes since midnight
        return 0

    def __add__(self, minutes):
        # Add code to make a new Time object with additional minutes
        return self

    def __sub__(self, minutes):
        # Add code to make a new Time object with decreased minutes
        return self

    def __eq__(self, other):
        # Add code to compare two times (use totalMinutes)
        return False

    def __lt__(self, other):
        # Add code to compare two times (use totalMinutes)
        return False

    def __le__(self, other):
        # Add code to compare two times (use totalMinutes)
        return False

t = Time(10, 15, "am")

print(str(t + 20) == "10:35am")
print(str(t + 45) == "11:00am")
print(str(t - 15) == "10:00am")
print(str(t - 20) == "9:55am")
print(str(t + 720) == "10:15pm")
print(str(t + 1440) == "10:15am")
print(str(t - 1440) == "10:15am")
print(str(t - 600) == "12:15am")
print(t == Time(10, 15, "am"))
print(t != Time(10, 15, "pm"))
print(t > Time(9, 20, "am"))
print(t < Time(11, 4, "am"))
print(t >= Time(10, 15, "am"))
print(t <= Time(10, 0, "pm"))
print(t >= Time(12, 15, "am"))
print(t <= Time(12, 15, "pm"))
