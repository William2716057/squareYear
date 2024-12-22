import math

squares = filter(lambda year: math.isqrt(year) ** 2 == year, range(0, 3000))
print("Years that are square numbers: ")
print(*squares)