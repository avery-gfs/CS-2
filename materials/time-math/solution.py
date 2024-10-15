# def swapAmPm(ampm):
#     if ampm == "am":
#         return "pm"
#     return "am"

def swapAmPm(ampm):
    return "pm" if ampm == "am" else "am"

class Time:
    def __init__(self, hours, minutes, ampm):
        # Add code to normalize hours, minutes, and ampm
        while minutes < 0:
            minutes += 60
            hours -= 1

        while minutes >= 60:
            minutes -= 60
            hours += 1

        while hours < 0:
            hours += 12
            ampm = swapAmPm(ampm)

        while hours >= 12:
            hours -= 12
            ampm = swapAmPm(ampm)

        self.hours = hours
        self.minutes = minutes
        self.ampm = ampm

    def __repr__(self):
        # Add code to account for when minutes < 10
        # Add code to account for when hours == 0

        # if self.hours == 0:
        #     hoursStr = "12"
        # else:
        #     hoursStr = str(self.hours)

        # if self.minutes < 10:
        #     minutesStr = "0" + str(self.minutes)
        # else:
        #     minutesStr = str(self.minutes)

        hoursStr = "12" if self.hours == 0 else str(self.hours)
        minutesStr = "0" + str(self.minutes) if self.minutes < 10 else str(self.minutes)

        return f"{hoursStr}:{minutesStr}{self.ampm}"

    def totalMinutes(self):
        # Add code to calculate the total numbers of minutes since midnight
        total = self.hours * 60 + self.minutes
        if self.ampm == "pm":
            total += 12 * 60 # minutes in 12 hours
        return total

    def __add__(self, minutes):
        # Add code to make a new Time object with additional minutes
        return Time(self.hours, self.minutes + minutes, self.ampm)

    def __sub__(self, minutes):
        # Add code to make a new Time object with decreased minutes
        return Time(self.hours, self.minutes - minutes, self.ampm)

    def __eq__(self, other):
        # Add code to compare two times (use totalMinutes)
        return self.totalMinutes() == other.totalMinutes()

    def __lt__(self, other):
        # Add code to compare two times (use totalMinutes)
        return self.totalMinutes() < other.totalMinutes()

    def __le__(self, other):
        # Add code to compare two times (use totalMinutes)
        return self.totalMinutes() <= other.totalMinutes()

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
