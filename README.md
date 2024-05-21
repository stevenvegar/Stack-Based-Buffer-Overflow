# Stack-Based-Buffer-Overflow
Some of my fuzzers and exploits for practicing BOFs

## Steps to find and exploit BoFs:
1. Perform a fuzzing process to check if the app would crash at some point
2. Confirm the bytes needed to crash the app with patter_create and pattern_offset
3. Ensure the ability to overwrite the EIP value
4. Look for bad characters
5. Find JMP ESP or CALL ESP memory address
6. Include NOPs and Shellcode

## Exploits
- [Minishare 1.4.1](/Minishare)\
  Remote Buffer Overflow written on Python3, tested on Windows XP SP3 English.

