# The idea is to make a key exchange method where two or more parties can create a secret key without any public sharing of this key 

# So in this example we will have the users, Adam and Bob
# There will be a public number that everyone will know, and there will also be another public prime number
# Both Adam and Bob will also have a private number 


from random import randint

public_number = randint(1, 10000)
public_prime_number = (2 ** 5) - 1 

adam_private_number = randint(1, public_prime_number)
bob_private_number = randint(1, public_prime_number)

adam_g = (public_number ** adam_private_number) % public_prime_number
bob_g = (public_number ** bob_private_number) % public_prime_number

secret_KEY_bob = (adam_g ** bob_private_number) % public_prime_number
secret_KEY_adam = (bob_g ** adam_private_number) % public_prime_number

print(secret_KEY_adam)
print(secret_KEY_bob)