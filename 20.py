from math import *
from constants import MIN, MAX, NUMBERS

numbers = [None] * 20 # 20 numbers
couples_thresholds = [None] * 20 # 20 couples
threshold_multiplier = 0
min = 0
for i in range(NUMBERS):
    couples_thresholds[i] = [min, floor(MAX / 20) * (threshold_multiplier + 1) + i]
    min = ceil(MAX / 20) * (threshold_multiplier + 1) 
    threshold_multiplier += 1
    
print(couples_thresholds)




