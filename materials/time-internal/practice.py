class Time:
    def __init__(self, hours, minutes, ampm):
        # Add code to track time internally using totalMinutes
        self.totalMinutes = 0

    def __repr__(self):
        # Add code to calculate hours, minutes, and ampm from internal rep
        # and create string representation for Time
        return f"12:00am"

    def __add__(self, minutes):
        # Implement method
        return Time(0, 0, "am")

    def __sub__(self, minutes):
        # Implement method
        return Time(0, 0, "am")

    def __eq__(self, other):
        # Implement method
        return False

    def __lt__(self, other):
        # Implement method
        return False

    def __le__(self, other):
        # Implement method
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
