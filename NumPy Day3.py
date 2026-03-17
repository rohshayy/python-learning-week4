
import numpy as np

'''
array = np.array([[1,2,3,4,5],
                   [6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
'''

ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]])

teenagers = ages[ages < 19]
adults = ages[(ages >= 20) & (ages <= 65)]
adults2 = ages[(ages > 18) | (ages <= 100)]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

adults3 = np.where(ages >= 20, adults, 0)

print(adults3)

rng=np.random.default_rng()
print(rng.integers(0,100,(3,2)))

