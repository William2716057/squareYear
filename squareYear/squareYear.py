import math

for year in range(0, 3000):
    result = math.isqrt(year)

    if result * result == year:
        print(year)
