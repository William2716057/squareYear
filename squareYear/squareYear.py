import math

squares = filter(lambda year: math.isqrt(year) ** 2 == year, range(0, 3000))

for year in squares:
    print(year)

#for year in range(0, 3000):
#    result = math.isqrt(year)

#    if result * result == year:
#        print(year)
