<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Applied Cryptography](#applied-cryptography)
  - [1. Symmetric ciphers](#1-symmetric-ciphers)
  - [2. Application of symmetric ciphers](#2-application-of-symmetric-ciphers)
  - [3. Asymmetric ciphers](#3-asymmetric-ciphers)
  - [4. Asymmetric Cryptosystems](#4-asymmetric-cryptosystems)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Applied Cryptography

## 1. Symmetric ciphers

- Crypto: Secret
- Graphy: Writing

**Don't implement your own crypto**

Message + Key --> Encryption --> Cypher text

Example:

Plaintext --> Encryption --> Cypher text  ===== insecure channel ===== Cypher text --> Decryption --> Plain text

```
E: µ -> C
D: C -> µ
```

- Need same key for encryption and decryption
- Keys must be kept secret
- Encryption and decryption algorithms can be open
- Cypher text can be open
- If the keys are exposed, just generate a new one!

Ideal: Cipher text reveals nothing about the Key or the Message

| A | B | XOR |
| ------ | ------ | ------ |
| 0 | 0 | 0
| 0 | 1 | 1
| 1 | 0 | 1
| 1 | 1 | 0

- A xor B xor A == B
- A xor A == 0

Proving security:

1. There is a mathematical proof that shows that cipher is secure (best reason)
    - E.g. Claude Shannon proved that one-time-pad is secure
1. Why breaking the cipher is at least as hard as some problem we believe is hard
1. Many smart, very motivated people tried to break it, but couldn't
1. Lots of possible keys are available (worst reason)

Probability:

- Set of all possible outcomes
- each outcome is equally likely
- complementary event probability
- conditional probability = `P(A∩B) / P(A)`

Perfect cipher:

- The cipher text provides an attacker with no additional information about the plain text
- Given any message and cipher text, there is only 1 key
- Example One-Time Pad

Problems with One-Time Pad:

- Malleable cipher text in channel
- Impractical keys as long as messages
- You cannot re-use the keys

Shanon'e Theorem: if a cipher is perfect, it must be impractical!

Lorenz cipher machine:

- `C` = `M xor K`
- `C'` = `M' xor K`
- `C xor C'` =` M xor K xor M' xor K` = `M xor M'`

Modern crytoanalysis:

- Goal of Cipher: Hide statistical properties of message and key `|k| < |M|`
- Goal of analyst: Find statistical properties in cipher text to break key / message
- Mechanical / Mathematical weakness
- Lots of hard work
- Motivation helps!

Modern symmetric ciphers:

- stream cipher (1 byte) vs block cipher (64 bits to 128-256 bits)
- Example of block cipher: **Advanced Encryption Standard** (AES)
- `Security = Actual number of rounds / Maximum number of "breakable"`
- Speed - implementing in hardware and software
- Simplicity
- Expected cost of brute of attack: 2^127
- Developed by 2 Belgian crytographers in 1997 during an [open AES selection process](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

Advanced Encryption Standard (AES) Rijndael:

- round key xor
- shifts
- s-boxes / non-linearity
- takes advantage of modern computing power

## 2. Application of symmetric ciphers

- Encrypt: message to cipher
- Decrypt: cipher to message
- Select a random key

What is randomness?

- Measure complexity of a sequence `s`
- where Kolmogorov Complexity `k(s)` is the length of the shortest possible description of `s`
- Randomness: `s` is random if `k(s) = |s| + C`
- For a given sequence `s`, is there a way to compute `k(s)`? NO
- Berry Paradox

Unpredictability:

- Statistical test can only show something is non-random
- How the sequence is generated
- Physically random events:
    - Quantum mechanics
    - Thermal noise
    - Key presses / mouse moves - takes time!
- physical randomness --> pseudo random number generator --> long sequence of random bits

Cipher block chaining:

- `m0` -> AES -> `c0` xor `m1` -> AES -> `c1` xor `m2` -> AES -> `c2` ...

CTR (counter) Mode vs CBC Mode

- CBC con: Always need the previous cipher block
- CTR pro: Uses a nonce

Security Protocol:

- Involves 2 or more parties
- Precisely defined sequences of steps
- Steps are computation and communication
- Procedure with 2 or more participants
- Involves secrets

Birthday paradox:

- weak collision resistance
- strong collision resistance

Hash functions need large outputs:

- `SHA-1`: 160 bits
- `SHA-2`: 256 or 512 bits

Storing password the WRONG WAYS:

- Storing passwords in clear text that is recoverable
- Reveals the length of password
- Reveals if 2 users have the same password
- If the key is compromised, it reveals all passwords!

Making dictionary attacks harder:

- Train / coerce users to use better passwords
- Protect encrypted passwords better
- Add salt

Hash chain

- Server stores no secrets!
- Server only stores last key in the hash chain `H^100(s)`
- S/Key: Server generates hash chain
- Needs Alice to print out each unique password

Modes of operation:

- CBC
- CTR
- CFB

## 3. Asymmetric ciphers

Impractical to use a symmetric key:

- Share the key physically
- Keep the key safely
- Destroy the key when required
- Create a huge number of pairwise unique shared keys
- Use a trusted third party
- Possibility of using Merkel's puzzle (impractical also!)

Merkel's puzzle:

- Agree on encryption function, security parameters
- Alice will create many puzzles
- Bob will randomly choose 1 puzzle to solve
- Eve will have to solve all the puzzles
- Will need to have a large number of puzzles

Diffie-Hellman Key Exchange

- Shared: large number `q` and a primitive root of `q`
- Alice and Bob will obtain the same key
- Secure against a passive eavesdropper

Finding large primes:

- `q` is a large prime number which is not secret, but different
- Euclid proved that there are infinite number of primes
- Probability that a number is prime is `1/ln x`

Tests:

- Fermat's Little Theorum
- Rabin-Miller Test  

## 4. Asymmetric Cryptosystems

- Symmetric encryption: Key used for encryption and decryption are **same**
- Asymmetric encryptionL Keys used for encryption and decryption are **different**

Trap door / One-way function:

- easy to compute in one direction
- difficult to computer in another direction

Totient Function is the number of positive integers less than `n` that are relatively prime to `n`. 
