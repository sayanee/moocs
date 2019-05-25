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
