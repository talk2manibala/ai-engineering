prime_numbers=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#extract the middle five elements
middle_five=prime_numbers[2:7]
print("Middle five prime numbers:", middle_five)
#get every second prime number
every_second=prime_numbers[::2]
print("Every second prime number:", every_second)
#use negative indexing to get the last three prime numbers
last_three=prime_numbers[-3:]
print("Last three prime numbers:", last_three)
#reverse the list of prime numbers
reversed_primes=prime_numbers[::-1]
print("Reversed list of prime numbers:", reversed_primes)
#descending order
sorted_primes=sorted(prime_numbers, reverse=True)
print("Prime numbers in descending order:", sorted_primes)