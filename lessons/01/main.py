def gcd(a, b):
  div = min(a, b)

  while a % div != 0 or b % div != 0
    div -= 1

  return div

class Fraction:
  def __init__(self, num, denom):
    # add num and denom as fields
    pass

  def value(self):
    # calculate num / denom
    return None

  def simplify(self):
    # return a new Fraction with simplified
    # numerator and denominator
    return None

  def multiply(self, n):
    # return a new Fraction that stores the value
    # of the old fraction multiplied by n
    return None

  def __repr__(self):
    # update to give a good representation of Fraction
    return f"Fraction"
