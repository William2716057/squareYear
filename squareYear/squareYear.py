import math

year1 = 0
year2 = 3000
squares = filter(lambda year: math.isqrt(year) ** 2 == year, range(year1, year2))
print("Years that are square numbers: ")
print(*squares)