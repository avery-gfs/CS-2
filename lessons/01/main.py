class Fraction:
	def __init__(self, num, denom):
		# add num and denom as fields
		pass

	def __repr__(self):
		# update to include num and denom in string representation
		return f"Fraction"

	def value(self):
		# calculate num / denom
		return None

	def multiply(self, n):
		# return a new Fraction with the value
		# of the old fraction multiplied by n
		return None

	def simplified(self):
		# return a new Fraction with simplified
		# numerator and denominator
		return None

f = Fraction(4, 10)

print("Test __repr__ method:")
print(f)

print("-" * 10)

print("Test value method:")
print(f.value())

print("-" * 10)

print("Test multiply method:")
print(f.multiply(5))

print("-" * 10)

print("Test simplified method:")
print(f.simplified())
