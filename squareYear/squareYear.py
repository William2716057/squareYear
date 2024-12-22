import math

squares = filter(lambda year: math.isqrt(year) ** 2 == year, range(0, 3000))

for year in squares:
    print(year)
