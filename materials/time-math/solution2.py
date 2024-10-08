class Time:
    def __init__(self, hours, minutes, ampm):
        if hours == 12:
            hours = 0

        self.totalMinutes = hours * 60 + minutes

        if ampm == "pm":
            self.totalMinutes += 12 * 60 # minutes in 12 hours

        self.totalMinutes %= (24 * 60) # minutes in a day

    def __repr__(self):
        minutes = self.totalMinutes % 60
        hours = (self.totalMinutes // 60) % 12
        ampm = "pm" if self.totalMinutes > 12 * 60 else "am"

        hoursStr = "12" if hours == 0 else str(hours)
        minutesStr = "0" + str(minutes) if minutes < 10 else str(minutes)

        return f"{hoursStr}:{minutesStr}{ampm}"

    def __add__(self, minutes):
        return Time(0, self.totalMinutes + minutes, "am")

    def __sub__(self, minutes):
        return Time(0, self.totalMinutes - minutes, "am")

    def __eq__(self, other):
        return self.totalMinutes == other.totalMinutes

    def __lt__(self, other):
        return self.totalMinutes < other.totalMinutes

    def __le__(self, other):
        return self.totalMinutes <= other.totalMinutes

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
