import math_utils as m
import string_utils as s
import shop_package.discount as disc
from shop_package.billing import calculate_total
print(m.add(2,3))
print(m.subtract(10,3))
print(m.square(5))
print(s.capitalise_text("Hello"))
print(s.reverse_text("Hello"))
print(s.word_count("Hello this is 5 words"))
print(disc.apply_discount(1000, 10))
print(calculate_total([100, 200, 300]))
