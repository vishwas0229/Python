n = int(input("Enter n : "))
def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_first_n_primes(n):
    sum, count, current = 0, 0, 2
    while count < n:
        if prime(current):
            sum += current
            count += 1
        current += 1
    return sum


print(f"The sum of the first {n} prime numbers is: {sum_first_n_primes(n)}")
