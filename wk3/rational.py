SUPER_NUMS = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
SUB_NUMS = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']


def gcd(a, b):
  """
  Returns the Greatest Common Divisor between `a` and `b`.
  """
  while b:
    a, b = b, a % b
  return a

def simplify(a, b):
  divisor = gcd(a, b)
  return Rational(a//divisor, b//divisor)


class Rational:
  """
  Represents any rational number in fraction form.
  """
  
  def __init__(self, numerator, denominator=1):
    """
    Initialises a rational number with the given numerator and denominator.
    """
    self._numerator = numerator
    self._denominator = denominator
    
  def __eq__(self, other):
    """
    Returns True if the two given Rational numbers are equal.
    """
    simplified_self = simplify(self._numerator, self._denominator)
    simplified_other = simplify(other._numerator, other._denominator)
    if simplified_self._numerator == simplified_other._numerator and simplified_self._denominator == simplified_other._denominator: return True
    return False

  def __str__(self):
    """
    Returns a string representing this Rational number.
    """
    ints = 0
    simplified = simplify(self._numerator, self._denominator)
    if simplified._numerator < 0:
      while -simplified._numerator >= simplified._denominator:
        simplified._numerator += simplified._denominator
        ints -= 1
    else:
      while simplified._numerator >= simplified._denominator:
        simplified._numerator -= simplified._denominator
        ints += 1
    if ints < 0: simplified._numerator*=-1
    numerator = ''.join(SUPER_NUMS[int(i)] if i.isdigit() else i for i in str(simplified._numerator))
    denominator = ''.join(SUB_NUMS[int(i)] if i.isdigit() else i for i in str(simplified._denominator))
    return str(ints) if simplified._numerator==0 else "{}{}/{}".format(str(ints or ''),numerator,denominator)
  
  def __add__(self, other):
    """
    Returns the addition (+) of two Rational numbers.
    """
    return simplify(self._numerator*other._denominator + other._numerator*self._denominator, self._denominator*other._denominator)
  
  def __mul__(self, other):
    """
    Returns the multiplication (*) of two Rational numbers.
    """
    return simplify(self._numerator*other._numerator, self._denominator*other._denominator)

  def __sub__(self, other):
    """
    Returns self minus (-) other of two Rational numbers.
    """
    return simplify(self._numerator*other._denominator - other._numerator*self._denominator, self._denominator*other._denominator)
  
  def __truediv__(self, other):
    """
    Returns self divided by (/) other.
    """
    return simplify(self._numerator*other._denominator, self._denominator*other._numerator)


def test_rational():
  """
  Put your own tests here.
  This function will never be called during marking.
  """