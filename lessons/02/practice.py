# A class representing a time with some number of hours and minutes

class Time:
    def __init__(self, hours, minutes):
        # Add code to add hours and minutes fields to Time
        # Make sure to adjust hours and minutes
        # when minutes > 60
        pass

    def __repr__(self):
        # Add code to print out a Time in "hours:minutes" format
        return f"Time"

    def addHours(self, hours):
        # Add code to make a new Time object with additional hours
        return Time(0, 0)

    def addMinutes(self, minutes):
        # Add code to make a new Time object with additional minutes
        return Time(0, 0)

print(Time(10, 15).hours == 10)

print(Time(10, 15).minutes == 15)

print(str(Time(10, 15)) == "10:15")

print(str(Time(10, 5)) == "10:05")

print(str(Time(12, 0)) == "12:00")

print(str(Time(1, 0)) == "1:00")

print(Time(1, 15).addHours(4).hours == 5)

print(Time(1, 15).addMinutes(5).minutes == 20)

print(Time(1, 15).addMinutes(65).minutes == 20)

print(Time(1, 15).addMinutes(65).hours == 2)
