

# (7) Use the decorator measure_time to calculate how long the above
#     function calculating population growth takes when it loops
#     1 million iterations.
import math
def population_growth_loop(initial, rate, time):
    def exponential_growth():
        return initial * math.exp(rate * time)

    for _ in range(1000000):          # 1 million iterations
        result = exponential_growth()
    print("Population after", time, "is:", round(result))

population_growth_loop(100, 0.05, 10)