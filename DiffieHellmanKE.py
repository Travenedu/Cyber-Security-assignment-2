import random

#Write a program by implementing Diffie–Hellman key exchange and show that the algorithm generates a same key/result at both ends.

def main(P, G, a, b):
    
    #Public key computation and exhange 
    person1_public_values = ((G ** b)  % P)
    person2_public_values = ((G ** a)  % P)

    #symmetric keys computation
    person1_sym_values = ((person1_public_values ** a) % P)
    person2_sym_values = ((person2_public_values ** b) % P)

    #Check that algorithm generates a same key/result at both ends
    if person1_sym_values == person2_sym_values:
        return person1_sym_values, "is the secret key"

print(main(43,5,6,90))