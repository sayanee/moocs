# Applied Cryptography

## 1. Perfect Ciphers

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
