# RSA
This repo is a demonstration of RSA and the simplest breaking attack of factoring the public key.

## rsafullimplementation.py

This file generates a key using the Rabin-Miller test, then uses that key to encrypt and then decrypt the message "HELLO"

## cracker.py

This file imitates what a hacker who is listening in on communications through RSA has access to: the public key and an intercepted message.

The variables p and q are currently filled with strings, but if the primes dividing the public key are substituted in, the message will be revealed
