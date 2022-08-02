# The idea is to make a key exchange method where two or more parties can create a secret key without any public sharing of this key 

# So in this example we will have the users, Adam and Bob
# There will be a public number that everyone will know, and there will also be another public prime number
# Both Adam and Bob will also have a private number 


from random import randint

public_number = randint(1, 10000)
public_prime_number = (2 ** 5) - 1

# These public numbers will be known, in truth, these numbers should be bigger

adam_private_number = randint(1, public_prime_number) 
bob_private_number = randint(1, public_prime_number)

# These private numbers will not be known at all and stored with Adam and Bob

adam_g = (public_number ** adam_private_number) % public_prime_number
bob_g = (public_number ** bob_private_number) % public_prime_number

# Here we are raising the public number everyone knows to the private numbers and then finding the modulus of the result with the prime number
# This allows us to get a number that will not be able to be reversable to find the private numbers

secret_KEY_bob = (adam_g ** bob_private_number) % public_prime_number
secret_KEY_adam = (bob_g ** adam_private_number) % public_prime_number

# Now if we raise that to the alternative private numbers and again find the modulus of it with the public prime number we will get a number that is
# the public number raised to both the secret keys this method allows both parties to make the same key without the need of sharing the other number

print(secret_KEY_adam)
print(secret_KEY_bob)