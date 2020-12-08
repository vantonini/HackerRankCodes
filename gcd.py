## An example of a code that finds the GCD of an array of numbers

# helpers 
def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

def power_times(num, prime_array):
  prime_power_array = []
  for prime in prime_array:
    count = 0;
    while ((num % prime) == 0):
      count+=1
      num = num/prime
    prime_power_array.append(count)
  return prime_power_array  

# finds the shortest array and transverse it find what is the smaller common pair of all numbers
def calculate_gcd(final_array):
  shorter_power_array_index = list(map(len, final_array)).index(min(list(map(len, final_array))))
  gcd = 1;
  for idx, value in enumerate(final_array[shorter_power_array_index]):
    gcd *= (min(final_array[0][idx], final_array[1][idx], final_array[2][idx])[0] ** min(final_array[0][idx], final_array[1][idx], final_array[2][idx])[1])
  return gcd

# program 

numbers = [24, 36, 48]
prime_arrays = []
final_array = []
power_array = []

# first we find all numbers that are prime between 0 and that number
# then we factored that number, 
for idx, number in enumerate(numbers):
  prime_arrays.append(list(filter(is_prime, range(number+1))))
  power_array.append(power_times(number, prime_arrays[idx]))
  final_array.append(list(zip(prime_arrays[idx],power_array[idx])))

# find the smaller array
print(calculate_gcd(final_array))