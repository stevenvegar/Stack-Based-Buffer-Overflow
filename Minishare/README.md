# Minishare 1.4.1

These are the steps to reproduce a Stack-Based Buffer Overflow that allows Remote Command Execution using a shellcode on **Windows XP SP3 English**.

### 1. Check how many bytes the application needs to receive in order to crash the memory stack.

Using the script [fuzzer1.py](/Minishare/fuzzer1.py) we can send many dummy bytes, in this case, the letter "A" (x\41), and wait until the application crashes. With approximately 1772 bytes, the application stops and shows the current memory offset where it fails.
<img src="/Minishare/images/image1.png">

### 2. Confirm the bytes needed to crash the app with patter_create and pattern_offset

In the script [fuzzer2.py](/Minishare/fuzzer2.py), we use a tool to create a specific pattern of bytes to send to the application, which will show us the current offset where the application crashed. Using that address, we can determine exactly how many bytes are required to overwirte the EIP register.
<img src="/Minishare/images/image2.png">

### 3. Ensure the ability to overwrite the EIP value

One we have the exact size of the buffer, we can perform a little check to ensure we can overwirte EIP register using 4 "B"s (\x42\x42\x42\x42) in the script [fuzzer3.py](/Minishare/fuzzer3.py). As we can see, at this time we receive the offset address where the application crashed, matching the 4 "B"s, meaning we have successfully filled the buffer and overflowed it.
<img src="/Minishare/images/image3.png">

### 4. Look for bad characters

With the script [badchars.py](/Minishare/badchars.py), we send an ordered pattern of bytes to examine the memory for any issues with other data. We need to keep removing "badchars" or "badbytes" until we get the same exact pattern from the script in the application's memory. In this case, the only 2 "badchars" we need to avoid on our shellcode are "\x00\x0d" .
<img src="/Minishare/images/image4.png">

### 5. Find JMP ESP or CALL ESP memory address

Since Windows XP does not have any protection against Buffer Overflows, such as ASLR or DEP, it is easy to persist the exploit code on every reboot. However, the ESP address can change with each OS installation.\
Using Immunity Debugger, once the process is attached, we can review the loaded OS modules to look for the "JMP ESP" or "CALL ESP" function that will trigger the shellcode.\
In this case, we can use either user32.dll, shell32.dll or comctl32.dll, which have the necessary instruction.

### 6. Include NOPs and Shellcode

The final step to create our exploit is to add a shellcode that will execute the commands we want on the victim machine. In the script [exploit.py](/Minishare/exploit.py), there are 2 different types of shellcode. The first generates a reverse shell that will connect back to our attacking machine.  The second shellcode is not harmful at all, it just open the calculator for demonstration purposes.\
It is important to include some "NOPs" or "no operation bytes" to provide some space where the shellcode will be stored and match the ESP address.
<img src="/Minishare/images/image5.png">
