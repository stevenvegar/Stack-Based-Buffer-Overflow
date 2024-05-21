# Stack-Based-Buffer-Overflow
Some of my fuzzers and exploits for practicing BOFs

## Steps to find and exploit BoFs:
1. Perform a fuzzing process to check if the app would crash at some point
2. Confirm the bytes needed to crash the app with patter_create and pattern_offset
3. Be sure to be able re-write the EIP value
4. Look for badchars
5. Find JMP ESP or CALL ESP memory address
6. Include Nops and Shellcode
