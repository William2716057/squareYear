import math

year1, year2 = 0, 3000
squares = filter(lambda year: math.isqrt(year) ** 2 == year, range(year1, year2))
print(f"Years that are square numbers between: {year1} and {year2}")
print(*squares)