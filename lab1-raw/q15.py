import random
import time
from q6 import weighted_sum_2 as weighted_sum_list

random.seed(123)

weights = [random.uniform(0, 1) for _ in range(1000000)]
values = [random.uniform(0, 1) for _ in range(1000000)]

print("Weighted sum lists:", weighted_sum_list(weights, values))


# Todo 1: Perform the weighted average using NumPy

# Todo 2: Measure the time taken to perform the weighted average using NumPy vs list comprehension