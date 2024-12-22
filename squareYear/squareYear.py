import math

squares = filter(lambda year: math.isqrt(year) ** 2 == year, range(0, 3000))
print(*squares)
#for year in squares:
#    print(year)
