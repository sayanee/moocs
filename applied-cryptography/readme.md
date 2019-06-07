<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Applied Cryptography](#applied-cryptography)
  - [1. Symmetric ciphers](#1-symmetric-ciphers)
  - [2. Application of symmetric ciphers](#2-application-of-symmetric-ciphers)

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
